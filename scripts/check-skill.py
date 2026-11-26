#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""技能结构自检（fashion-studio 与 pattern-texture-skill 共用同一份）。

结构检查（逐项如下）：
1. 指针缺失：文中出现的 `xxx.md` 若指向本技能 references/ 下的文件却不存在 → FAIL；
   若该行明确写了本技能名或 references/ 前缀、或文件名不像外部技能的文件 → 也按缺失计。
   纯外部技能文件名（如 fashion-studio 的 tool-adapter.md）只报 WARN 供人核对。
2. 无孤儿：references/ 下每个文件至少被 SKILL.md 或其它文件引用一次 → FAIL。
3. 行数上限：SKILL.md ≤ 500 行；每个 reference ≤ 500 行（超出只报 WARN，不阻断）。
4. 章节锚点：`xxx.md §1.5` / `第 1.5 节` / `§六` 这类引用，目标文件必须有对应编号标题 → FAIL。
   支持区间写法（第 2.2–2.5 节 = 两端都要有）。
5. 标题编号重复：同一文件里同一编号出现两次（拆分/合并残留）→ WARN。
6. 路径前缀：`assets/xxx` 与 `references/xxx` 必须落在对应目录（双向）→ FAIL。
6c. 跨技能引用：一行里提到别的技能（或写了 `references/xxx` 且提到兄弟技能），
    但兄弟技能里并没有这个同名文件 → WARN（拆/改名后留下的悬空引用）。
7. 自指锚点：`本文第 12 节` / `§六` / 不带文件名的 `第 5 节`，本文必须有该编号标题 → FAIL。
   [4] 只管「文件名紧跟节号」，本项管同一句话里文件名离得远、或干脆没写文件名的自指。
8. frontmatter：`name` 必须等于技能目录名；缺 `description` → FAIL；description 超过 450 字 → WARN。
9. 版本一致：frontmatter 的 `version` 必须出现在 README 里，README 不得残留别的版本号 → FAIL / WARN。
10. 同名标题：同一父级标题下、同一层级的标题文字完全重复 → WARN。
11. README 树 vs 磁盘：树里写了但磁盘没有 → FAIL；references/ 里有但树里没登记 → WARN。
12. 目录过期：`## 目录`（或「本篇目录」）里的条目必须能在本文标题里找到，改了标题没改目录 → FAIL。

用法：python scripts/check-skill.py [skill_dir]
退出码：0 = 全过；1 = 有指针缺失 / 孤儿 / 锚点失效 / 前缀错配 / 自指失效 / frontmatter 不合规 / 版本不一致 / 树与磁盘不符 / 目录过期
"""
import os
import re
import sys

CITE = re.compile(r'([A-Za-z0-9_\-\u4e00-\u9fa5]+\.md)')
HEAD_ARABIC = re.compile(r'^#{2,6}\s*([0-9]+(?:\.[0-9]+)?)\s*[、.]?\s')
HEAD_CN = re.compile(r'^#{2,6}\s*([一二三四五六七八九十]+)\s*(?:、|[\.\s])')
LIMIT_SKILL = 500   # 官方规范：SKILL.md 正文 ≤500 行
LIMIT_REF = 800     # references 提示线（官方未设限，取经验值）

# 带目录前缀的引用：assets/xxx 与 references/xxx 必须各自落在对应目录
PREFIX = re.compile(r'(assets|references)/([A-Za-z0-9_\-\u4e00-\u9fa5]+\.(?:md|csv))')
SIBLING_HINT = ("pattern-texture-skill", "PTS", "fashion-studio",
                "video-remix-studio", "fashion-web-scraper", "兄弟技能", "跨技能")

# xxx.md + 章节号；支持 §1.5 / §六 / 第 1.5 节 / 第 2.2–2.5 节
ANCHOR = re.compile(
    r'([A-Za-z0-9_\-\u4e00-\u9fa5]+\.md)`?\s*'
    r'(?:'
    r'§\s*([0-9]+(?:\.[0-9]+)?)'
    r'|§\s*([一二三四五六七八九十]+)'
    r'|第\s*([0-9]+(?:\.[0-9]+)?)'
    r'(?:\s*[–—~\-]\s*([0-9]+(?:\.[0-9]+)?))?'
    r'\s*节'
    r'|第\s*([一二三四五六七八九十]+)\s*节'
    r')'
)

# 本技能以外的常见文件名，只 WARN
EXTERNAL_HINTS = (
    "fashion-studio", "pattern-texture-skill", "video-remix-studio",
    "fashion-web-scraper", "SKILL.md",
)

# [7] 自指锚点：本文/本节，或不带文件名的节号
SELF_SEC = re.compile(
    r'(?:§\s*([0-9]+(?:\.[0-9]+)?|[一二三四五六七八九十]+(?:\.[0-9]+)?)'
    r'|第\s*([0-9]+(?:\.[0-9]+)?|[一二三四五六七八九十]+(?:\.[0-9]+)?)'
    r'(?:\s*[–—~\-]\s*([0-9]+(?:\.[0-9]+)?))?\s*节)')
FNAME = re.compile(r'[A-Za-z0-9_\-\u4e00-\u9fa5]+\.md')
CN2NUM = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
          "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}
HEAD_A2 = re.compile(r'^#{2,6}\s*([0-9]+)(?:[·.]([0-9]+))?\s*(?:[、.．]|\s|$)')
HEAD_C2 = re.compile(r'^#{2,6}\s*([一二三四五六七八九十]+)(?:[·.]([0-9]+))?\s*(?:[、.．]|\s|$)')


def norm_num(s):
    """把 六 / 十二 / 6 统一成 '6'；带小节的按 '6.5' 处理"""
    if re.match(r'^[0-9]', s):
        return s
    if '十' in s:
        a, _, b = s.partition('十')
        return str((CN2NUM.get(a, 1) if a else 1) * 10 + (CN2NUM.get(b, 0) if b else 0))
    return str(CN2NUM.get(s, s))


def heads_norm(path):
    """归一化后的标题编号集合（中文数字与阿拉伯数字都折成阿拉伯）"""
    out = set()
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        m = HEAD_A2.match(line)
        if m:
            out.add(m.group(1) + (("." + m.group(2)) if m.group(2) else ""))
            continue
        m = HEAD_C2.match(line)
        if m:
            out.add(norm_num(m.group(1)) + (("." + m.group(2)) if m.group(2) else ""))
    return out


FM_NAME = re.compile(r'^(name|description):\s*(.+)$')
FM_VER = re.compile(r'^\s+version:\s*(.+)$')
VER = re.compile(r'\b\d+\.\d+\.\d+\b')


def front_matter(path):
    t = open(path, encoding="utf-8").read()
    if not t.startswith("---"):
        return None
    end = t.find("\n---", 3)
    if end < 0:
        return None
    out = {}
    for line in t[3:end].split("\n"):
        m = FM_NAME.match(line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
            continue
        m = FM_VER.match(line)
        if m and "version" not in out:
            out["version"] = m.group(1).strip().strip('"').strip("'")
    return out


TOC_HEAD = re.compile(r'^#{2,3}\s*(?:本篇)?目录(?:\s*（[^）]*）)?\s*$')
TREE_NAME = re.compile(r'([A-Za-z0-9_\-.]+\.(?:md|csv|py|json|ya?ml|txt))')


def strip_num(s):
    s = re.sub(r'^[0-9]+(?:\.[0-9]+)*\s*[、.．]?\s*', '', s.strip())
    s = re.sub(r'^[一二三四五六七八九十]+(?:[·.]\d+)?\s*[、.．]?\s*', '', s)
    return re.sub(r'\s+', '', s.replace('`', ''))


def toc_stale(path):
    """目录块里的条目，必须能在本文标题里找到对应（过期条目=改了标题没改目录）"""
    lines = open(path, encoding="utf-8").read().split("\n")
    heads = {strip_num(m.group(1)) for m in
             (re.match(r'^#{2,6}\s*(.+)$', l) for l in lines) if m}
    for i, l in enumerate(lines):
        if not TOC_HEAD.match(l):
            continue
        entries = []
        for l2 in lines[i + 1:]:
            if l2.startswith("#"):
                break
            s = l2.strip()
            if s.startswith("- "):
                entries.append(s[2:].strip())
        bad = []
        for e in entries:
            en = strip_num(e)
            if not en:
                continue
            if any(en == h for h in heads):
                continue
            bad.append(e)
        return bad
    return []


def dup_head_text(path):
    cnt, stack = {}, []   # stack: [(level, text)]
    for line in open(path, encoding="utf-8"):
        raw = line.rstrip("\n")
        m = re.match(r'^(#{2,6})\s*(.*)$', raw)
        if not m:
            continue
        level = len(m.group(1))
        while stack and stack[-1][0] >= level:
            stack.pop()
        parent = stack[-1][1] if stack else ""
        txt = re.sub(r'^[0-9]+(?:\.[0-9]+)?\s*[、.]?\s*', '', m.group(2))
        txt = re.sub(r'^[一二三四五六七八九十]+(?:[·.]\d+)?\s*[、.]?\s*', '', txt).strip()
        if level >= 3 and len(txt) >= 4:
            key = (parent, level, txt)
            cnt[key] = cnt.get(key, 0) + 1
        stack.append((level, m.group(2).strip()))
    return [(p, t) for (p, _, t), v in cnt.items() if v > 1]


def collect(path, root):
    """返回 (arity 标题编号集合, 中文标题编号集合, 重复编号列表)"""
    text = open(path, encoding="utf-8").read()
    arabic, cn, dup = set(), set(), []
    for line in text.split("\n"):
        m = HEAD_ARABIC.match(line)
        if m:
            num = m.group(1).rstrip(".")
            if num in arabic:
                dup.append(num)
            arabic.add(num)
            continue
        m = HEAD_CN.match(line)
        if m:
            ch = m.group(1)
            if ch in cn:
                dup.append(ch)
            cn.add(ch)
    return arabic, cn, dup


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(here)
    refs_dir = os.path.join(root, "references")

    # references/ 索引（用于孤儿检查）
    index = {}
    for dirpath, _, files in os.walk(refs_dir):
        for f in files:
            if f.endswith(".md"):
                index.setdefault(f, []).append(os.path.join(dirpath, f))
    # 兄弟技能 md 索引（跨技能引用不算缺失）
    siblings = {}
    sib_root = os.path.dirname(root)
    if os.path.isdir(sib_root):
        for dirpath2, _, files2 in os.walk(sib_root):
            if os.path.abspath(dirpath2).startswith(os.path.abspath(root) + os.sep):
                continue
            for f in files2:
                if f.endswith(".md"):
                    siblings.setdefault(f, os.path.join(dirpath2, f))
    # 全技能 md 索引（用于指针与锚点：tests/ 下的评测集也算可解析目标）
    allmd = {}
    for dirpath, _, files in os.walk(root):
        for f in files:
            if f.endswith(".md") and f != "SKILL.md":
                allmd.setdefault(f, os.path.join(dirpath, f))

    md_files = []
    for dirpath, _, files in os.walk(root):
        for f in files:
            if f.endswith(".md"):
                md_files.append(os.path.join(dirpath, f))

    anchors = {}
    for name, paths in index.items():
        anchors[name] = collect(paths[0], root)

    missing, external, cited, anchor_broken, dup_head = [], [], set(), [], []
    ext_unverified = []
    warn = []

    for path in md_files:
        rel = path.replace(root + os.sep, "")
        text = open(path, encoding="utf-8").read()
        for lineno, line in enumerate(text.split("\n"), 1):
            # 1. 指针
            for name in CITE.findall(line):
                if name == "SKILL.md":
                    continue
                # 交付物文件名（身份卡/总览索引/项目画布）不是技能文件，跳过
                if re.search(r'(身份卡|总览索引|项目画布|画布_)', name):
                    continue
                if name in index:
                    cited.add(name)
                if name in allmd:
                    continue
                # 兄弟技能里有同名文件 → 外部引用；否则才算缺失
                if name in siblings:
                    external.append(f"{rel}:{lineno} {name}（兄弟技能文件）")
                    continue
                # 同一行点了别的技能：兄弟技能确有同名文件才算外部引用，否则记为待核
                if any(h in line for h in ("fashion-studio", "video-remix-studio",
                                           "fashion-web-scraper", "pattern-texture-skill", "PTS")):
                    if name in siblings:
                        external.append(f"{rel}:{lineno} {name}（外部技能文件）")
                    else:
                        ext_unverified.append(f"{rel}:{lineno} {name}（提到外部技能，但兄弟技能里无此文件）")
                else:
                    missing.append(f"{rel}:{lineno} 引用了不存在的文件 {name}")
            # 2. 锚点
            for m in ANCHOR.finditer(line):
                target = m.group(1)
                if target in anchors:
                    arabic, cn, _ = anchors[target]
                elif target in allmd:
                    arabic, cn, _ = collect(allmd[target], root)
                else:
                    continue
                ref = m.group(0).strip()
                nums = [g for g in (m.group(2), m.group(4), m.group(5)) if g]
                chs = [g for g in (m.group(3), m.group(6)) if g]
                bad = [n for n in nums if n not in arabic]
                bad += [c for c in chs if c not in cn]
                if bad:
                    anchor_broken.append(
                        f"{rel}:{lineno} {ref} → {target} 缺少章节 {', '.join(bad)}")

    # 7. 自指锚点（本文/本节，或不带文件名的节号）
    self_broken = []
    for path in md_files:
        rel = path.replace(root + os.sep, "")
        hs = heads_norm(path)
        for lineno, line in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
            names = [m.start() for m in FNAME.finditer(line)]
            for m in SELF_SEC.finditer(line):
                pre = line[max(0, m.start() - 4):m.start()]
                is_self = ("本文" in pre or "本节" in pre
                           or not [p for p in names if p < m.start()])
                if not is_self:
                    continue   # 带文件名的交给 [4]
                nums = [norm_num(g) for g in (m.group(1), m.group(2), m.group(3)) if g]
                if any(n not in hs for n in nums):
                    self_broken.append(
                        f"{rel}:{lineno} 自指 {m.group(0).strip()}，本文无该节")

    # 8/9. frontmatter 与版本一致
    fm_bad, fm_warn, ver_bad, ver_warn = [], [], [], []
    skill_path = os.path.join(root, "SKILL.md")
    if os.path.exists(skill_path):
        fm = front_matter(skill_path) or {}
        dirname = os.path.basename(os.path.abspath(root))
        if fm.get("name") != dirname:
            fm_bad.append(f"SKILL.md name={fm.get('name')!r} ≠ 目录名 {dirname!r}")
        if not fm.get("description"):
            fm_bad.append("SKILL.md 缺 description（这是唯一的触发机制）")
        elif len(fm["description"]) > 450:
            fm_warn.append(f"description {len(fm['description'])} 字（预算约 100 词 / 450 字内）")
        ver = fm.get("version", "")
        readme = os.path.join(root, "README.md")
        if ver and os.path.exists(readme):
            vers = set(VER.findall(open(readme, encoding="utf-8").read()))
            if ver not in vers:
                ver_bad.append(f"README 里找不到当前版本 {ver}")
            others = sorted(v for v in vers if v != ver)
            if others:
                ver_warn.append("README 残留其它版本号：" + ", ".join(others))
        elif not ver:
            fm_bad.append("SKILL.md 缺 metadata.version")

    # 10. 同一父级下的同名标题
    same_head = []
    for path in md_files:
        rel = path.replace(root + os.sep, "")
        for parent, t in dup_head_text(path):
            same_head.append(f"{rel}「{parent}」下重复标题「{t}」")

    # 11. README 目录树 vs 磁盘
    tree_missing, tree_uncovered = [], []
    readme = os.path.join(root, "README.md")
    disk = {}
    for dirpath, _, files in os.walk(root):
        if ".git" in dirpath:
            continue
        for f in files:
            disk.setdefault(f, []).append(os.path.join(dirpath, f).replace(root + os.sep, ""))
    if os.path.exists(readme):
        tree_names = []
        for line in open(readme, encoding="utf-8").read().split("\n"):
            if "├" in line or "└" in line:
                tree_names += TREE_NAME.findall(line)
        for n in tree_names:
            if n not in disk:
                tree_missing.append(f"README 树里的 {n} 在磁盘上不存在")
        refs_md = [os.path.basename(p) for p in
                   [os.path.join(dp, f) for dp, _, fs in os.walk(refs_dir) for f in fs if f.endswith(".md")]]
        for n in refs_md:
            if n not in tree_names:
                tree_uncovered.append(f"{n} 在 references/ 里，但 README 树没列（新增文件忘了登记）")
    else:
        tree_missing.append("缺 README.md")

    # 12. 目录条目过期
    toc_bad = []
    for path in md_files:
        rel = path.replace(root + os.sep, "")
        for e in toc_stale(path):
            toc_bad.append(f"{rel} 目录条目「{e}」在本文找不到对应标题")

    # 5.5 路径前缀（双向：assets→references 与 references→assets 都要查）
    assets_dir = os.path.join(root, "assets")
    assets_index = set(os.listdir(assets_dir)) if os.path.isdir(assets_dir) else set()
    prefix_bad, prefix_ext = [], []
    for path in md_files:
        rel = path.replace(root + os.sep, "")
        for lineno, line in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
            for m in PREFIX.finditer(line):
                kind, name = m.group(1), m.group(2)
                if name in (assets_index if kind == "assets" else index):
                    continue
                if kind == "assets" and name in index:
                    prefix_bad.append(f"{rel}:{lineno} {m.group(0)}（文件在 references/，前缀写成 assets/）")
                elif kind == "references" and name in assets_index:
                    prefix_bad.append(f"{rel}:{lineno} {m.group(0)}（文件在 assets/，前缀写成 references/）")
                elif any(h in line for h in SIBLING_HINT):
                    prefix_ext.append(f"{rel}:{lineno} {m.group(0)}（兄弟技能文件）")
                    if name not in siblings:
                        ext_unverified.append(f"{rel}:{lineno} {m.group(0)}（提到外部技能，但兄弟技能里无此文件）")
                else:
                    prefix_bad.append(f"{rel}:{lineno} {m.group(0)}（该目录下没有这个文件）")

    for name, paths in index.items():
        if name not in cited:
            warn.append("ORPHAN " + paths[0].replace(root + os.sep, ""))

    for name, (_, _, dup) in anchors.items():
        for d in dup:
            dup_head.append(f"{name} 编号 {d} 出现两次以上")

    for path in md_files:
        n = len(open(path, encoding="utf-8").read().split("\n"))
        rel = path.replace(root + os.sep, "")
        is_skill = rel.lower().endswith("skill.md")
        lim = LIMIT_SKILL if is_skill else LIMIT_REF
        if n > lim:
            kind = "SKILL.md 硬线" if is_skill else "references 提示线"
            warn.append(f"{rel}: {n} 行（上限 {lim}，{kind}）")

    print("== 结构自检 ==")
    print(f"md 文件 {len(md_files)} 个；references 下 {len(index)} 个不同文件名")
    print(f"[1] 指针缺失：{len(missing)}")
    for m in missing:
        print("    MISS", m)
    print(f"[2] 孤儿文件：{len([w for w in warn if w.startswith('ORPHAN')])}")
    for w in [w for w in warn if w.startswith("ORPHAN")]:
        print("    ", w)
    print(f"[3] 行数超限（WARN）：{len([w for w in warn if isinstance(w, str) and '行（上限' in w])}")
    for w in [w for w in warn if isinstance(w, str) and "行（上限" in w]:
        print("    WARN", w)
    print(f"[4] 章节锚点失效：{len(anchor_broken)}")
    for a in anchor_broken:
        print("    ANCHOR", a)
    print(f"[5] 标题编号重复（信息项，多为按组编号，人工核对）：{len(dup_head)}")
    for d in dup_head[:5]:
        print("    INFO", d)
    if len(dup_head) > 5:
        print(f"    … 其余 {len(dup_head)-5} 条略")
    print(f"[6] 路径前缀错配：{len(prefix_bad)}")
    for b in prefix_bad:
        print("    BAD", b)
    if prefix_ext:
        print(f"[6b] 兄弟技能引用（前缀写法仅提示）：{len(prefix_ext)}")
    print(f"[7] 自指锚点失效：{len(self_broken)}")
    for s in self_broken:
        print("    SELF", s)
    print(f"[8] frontmatter 不合规：{len(fm_bad)}")
    for f in fm_bad:
        print("    FM", f)
    for f in fm_warn:
        print("    FM-WARN", f)
    print(f"[9] 版本不一致：{len(ver_bad)}")
    for v in ver_bad:
        print("    VER", v)
    for v in ver_warn:
        print("    VER-WARN", v)
    print(f"[10] 同名标题（WARN，锚点歧义）：{len(same_head)}")
    for s in same_head[:8]:
        print("    HEAD", s)
    if len(same_head) > 8:
        print(f"    … 其余 {len(same_head)-8} 条略")
    print(f"[11] README 树 vs 磁盘不符：{len(tree_missing)}")
    for m in tree_missing:
        print("    TREE", m)
    for u in tree_uncovered:
        print("    TREE-WARN", u)
    print(f"[12] 目录条目过期：{len(toc_bad)}")
    for t in toc_bad:
        print("    TOC", t)

    # 同一行的 "name" 与 "references/name" 会重复命中，按 (文件, 行号, 文件名) 去重
    dedup, seen = [], set()
    for e in ext_unverified:
        m = re.match(r'(.+?):(\d+) (\S+?)（', e)
        key = (m.group(1), m.group(2), re.sub(r'^(references|assets)/', '', m.group(3))) if m else e
        if key in seen:
            continue
        seen.add(key)
        dedup.append(e)
    ext_unverified = dedup

    if ext_unverified:
        print(f"[6c] 跨技能引用未验证（WARN）：{len(ext_unverified)}")
        for e in ext_unverified[:10]:
            print("    EXT?", e)
        if len(ext_unverified) > 10:
            print(f"    … 其余 {len(ext_unverified)-10} 条略")

    if external:
        print(f"[附] 外部文件引用（人工核对）：{len(external)}")
        for e in external[:12]:
            print("    EXT", e)

    ok = (not missing and not anchor_broken and not prefix_bad and not self_broken
          and not fm_bad and not ver_bad and not tree_missing and not toc_bad
          and not [w for w in warn if w.startswith("ORPHAN")])
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
