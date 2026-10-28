# fashion-studio · 时尚行业 AIGC 内容生产技能

> 一套面向**服装 / 服饰品牌、设计师、教师、参赛学生**的完整方法论：把"企业给了什么"一路做到"最终交付什么"——覆盖 **企业企划、生图、视频、AIGC 赛事** 四条线，并贯穿设计全流程 **21 项交付物规范**。

License: **CC BY-NC 4.0**（使用须署名、禁止商用）· 版本 1.4.0 · 作者：hexiaoyu0525-design

---

## 这是什么

`fashion-studio` 是一个 **Agent Skill（智能体技能）**：一个 `SKILL.md` + 一组 `references/` 方法论文档 + 三个 `assets/` 模板文件（项目画布、素材库 CSV、提示词示例锚点包）。任何支持 SKILL.md 的 Agent 读到它，就会按这套规范帮你做服装企划、出图、出片、打比赛。

它是**方法论、检查清单、提示词骨架、行业标准**，不是一个连了某个平台的插件，也不包含可执行代码。

### 四条主线

1. **企业企划**：接活六问、商品/设计/营销三企划、主题色彩面料系列、波段、概念方案五板、系列化五要素、评审会验收、数字→实物保真。
2. **生图**：lookbook、服装大片、模特图、款式/平铺/挂拍/人台、细节与面料微距、灵感/色彩/面料/纹样/廓形/配饰板；固定 AI 模特（Muse）；全品类、全风格、面料全库。
3. **视频**：品牌宣传片、时装电影、秀场、宣发、BTS、webisode、moodfilm、techfilm、AR/虚拟时装短片；图生视频四段式备料 + 声音与后期包装。
4. **AIGC 赛事**：国内外大赛选赛、读题、从零到交付（灵感→三要素→效果图/款式图→数字成衣→虚拟走秀→设计说明与 AI 披露），三层分类（纯图 / 图+视频 / 图+3D）。

并覆盖：设计灵感与原创方法论、参考分寸（怎么借鉴服饰史/大师而不抄袭）、四步保图管线、版权合规、素材库蓝图、项目运行与协作层（项目画布、三模式、审美基准板、出图工单、成本档、交付打包）。

### 特点

- **纯 Markdown、零代码、零专有 API**：不依赖任何平台的连接器，也不依赖本地算力。
- **工具中立**：默认用即梦 Seedream / Seedance（作者实测），但同一套方法可迁到任何生图 / 视频平台，详见 `references/tool-adapter.md`。
- **"Agent 备料，你按生成"**：即使 Agent 没有图像工具，也能把素材、提示词、四段式备齐，你在任意平台手动粘贴生成。
- **可移植**：无写死的本地路径、无私有链接；素材库给空 CSV，可导入 Airtable / Notion / Excel。

---

## 明确不做什么（边界）

- **不做本地节点工作流（如 ComfyUI）**：面向即梦等线上云模型，批量提效交云平台。
- **不生成 3D 工程文件**：可编辑的 `.zprj/.clo3d/.sproj/.fbx/.glb` 必须用 Style3D / CLO / Marvelous Designer 等专业软件；本技能负责交给 3D 前的全部图与视频，并**出超真实 3D 渲染图可交付看效果**（提案/赛事/数字走秀）。
- **不冒充生产文件**：纸样、Tech Pack、BOM、精确珠绣制版（.DST）必须由专业软件/人工完成，AI 图不冒充；AI 出**超真实展示图**（含款式图约束直出、工艺单插图、材料创意展示）可直接交付提案，生产数据与合规判定仍走人工/专业路径。
- **不做虚拟试穿（把任意衣服临时穿到模特身上）/数字人主播/直播带货**：Muse 解决"固定同一人"，**换装/改款属已固定 Muse 的全套重出**（`ai-model-muse.md` 五·5），不临时试穿、不口播。

---

## 安装

### 方式一：skills 安装器（推荐）

在支持 skills 的 Agent 环境中：

```bash
npx skills add <你的GitHub用户名>/fashion-studio
```

### 方式二：手动安装

1. 下载或 clone 本仓库；
2. 把整个 `fashion-studio` 文件夹放进该 Agent 的 skills 目录，例如：
   - Claude Code：`~/.claude/skills/`
   - WorkBuddy：`~/.workbuddy/skills/`
   - 豆包：用户级 skills 目录（`.user_skills/`）
   - Codex / 其他：按其官方 skills / 配置入口放入同一份 `SKILL.md`
3. 重开一个新会话，Agent 即会加载。

### 不支持 SKILL.md 的 Agent / 网页对话

把 `SKILL.md` 与 `references/` 当作"手册 / 提示词包"：让它读取该目录，或把 `SKILL.md` 贴进系统提示 / 项目说明，让它按任务路由表引用对应文件。方法依然有效，只是不会自动触发。

---

## 可选配套：fashion-web-scraper（自动素材采集）

`fashion-studio` 核心是**零依赖的纯方法论**，本身不要求任何浏览器或采集能力。路由表里有一项"自动抓品牌官网 / 秀场参考图"，由**可选旁挂 skill `fashion-web-scraper`** 提供；它和本技能**同一作者、同一许可（CC BY-NC 4.0）**发布。

- **安装**（需要自动采集时）：
  ```bash
  npx skills add <你的GitHub用户名>/fashion-web-scraper
  ```
  或手动把 `fashion-web-scraper` 文件夹放进该 Agent 的 skills 目录（路径同上方"方式二"）。
- **不装也完全可用**：采集有三条通道——① 本地 Playwright 批量抓取、② Agent 内置浏览器自动化零部署少量抓取、③ **手动放图 / 直接发参考图**（零门槛、人人可用、永远可用）。不装 scraper 时，直接用通道③即可，本技能"怎么开工"一节照常运转，全流程不受影响。
- 抓取的素材会按 `asset-library-schema.md` 的字段与版权分级落盘登记（**秀场图默认 🟢 全绿**：可看/学/拆/垫、可作长期参考；**拿秀场款当改造基底是行业常态**——改结构/面料/色彩即改造；红线只剩 🔴 老花/Logo 慎喂、交付不复现），可直接进调研板 / 灵感板 / 素材库。
- **纯文字描述也可**：没有 URL / 图时，只给风格、主题、品牌的文字描述，Agent 会整理成设计调研要点落盘（权限 ⚪ 知识 / 🟢 主题概念），同样走素材库登记。
- **换新电脑 / 首次使用**：环境初始化（检查 Node、验证 playwright-cli、按需安装浏览器内核）见 scraper 技能内「新环境初始化」节，含一键脚本 `setup.ps1`（该脚本位于 scraper 技能目录内，不在本技能库）；内核装不上不影响使用——自动落回通道②/③。

---

## 可选配套：video-remix-studio（爆款视频复刻 / 改编）

`fashion-studio` 负责**时尚美学、人物比例与服装大片/时装电影**的方法论——视频环节自带一条完整导演流水线（定类型→五问定片→视觉系统分层→风格档/导演声音→镜头表→四段式备料→生成与锚点→声音后期→验收，见 `video-brief.md`「导演流水线总览」）；当任务变成"拿一条爆款参考视频做**克隆 / 复刻 / 翻拍 / 改编**成自己的版本（口播、盘点排行、短剧、街头采访、双人播客、讲解演示、旁白带货等），换人、换脸、换产品、换品牌、换行业、换语言、换场景"，由**可选协作 skill `video-remix-studio`** 承接：它是一条六阶段导演流水线（立项 → 拆参考 → 改编导演案 → 脚本与时间 → 素材生产 → 合成与审片），方法论与生成平台解耦，素材生成与合成按当前环境适配层执行（豆包环境 = 即梦 Seedream/Seedance + 语音合成 + mediakit/剪映，其他 Agent / 平台可换适配层复用）。

- **安装**（需要复刻爆款视频时）：与 `fashion-studio` 同目录安装即可（`npx skills add <你的GitHub用户名>/video-remix-studio`，或手动把 `video-remix-studio` 文件夹放进该 Agent 的 skills 目录，路径同上方"方式二"）。
- **不装也完全可用**：不涉及爆款复刻时无需安装；本技能核心流程零依赖照常运转。
- **分工边界**：本技能的视频环节只覆盖**用户自建 / 原创**的时装片（导演流水线见 `video-brief.md`）；`video-remix-studio` 只覆盖**复刻 / 改编他人爆款视频**。两者是独立方法论，任务归属哪边就走哪边，不混合、不互相承接。
- **合规提醒**：含**真人脸**的参考视频做"换脸 / 克隆真人主持"，多数视频模型在网关侧会拒绝且有合规风险；默认改用 AI 数字人 / 自建模特，或仅在持有明确授权时尝试并如实报告失败。AI 自建模特（非真人）不受此限，且仍按本技能的 Muse 流程锁人。

---

## 快速开始

直接对 Agent 说一句话即可：

- 「帮我做今年秋冬企业季度企划」
- 「参赛-<赛名>，从头带我做」
- 「做个新系列，4 套高定礼服」
- 「我只有一张参考图，帮我出效果图」
- 「继续这个项目」（会读取项目根目录的 `00_项目画布`，从断点续做）

开工可在项目文件夹放 `服装/ 模特/ 面料/ 场景/ 纹样/ 参考视频/ 灵感/` 等素材，Agent 会先做素材登记；**也可以从任意阶段中途开始**（已有灵感/部分三要素/已有效果图都能接）。

---

## 目录结构

```
fashion-studio/
├─ SKILL.md                     # 入口：任务路由、开工方式、基本原则、工具入口、总检
├─ README.md                    # 本文件（给人看）
├─ LICENSE                      # CC BY-NC 4.0
├─ references/                  # 29 篇方法论（Agent 按需加载）
│  ├─ project-workflow.md       # 项目运行与协作层（模式/画布/工单/成本/交付）
│  ├─ enterprise-proposal.md    # 企业企划
│  ├─ aigc-competition.md       # 赛事三条线与案例
│  ├─ design-ideation.md        # 设计灵感、参考分寸、原创方法论
│  ├─ image-quality-sop.md      # 生图总调度：四步管线/验收门
│  ├─ design-boards.md          # 前期板 + 板面规范
│  ├─ fashion-illustration-spec.md / technical-production-spec.md / portfolio-board.md
│  ├─ category-guide.md / fabric-guide.md / material-lab.md   # 全品类 / 面料全库 / 面料实验室
│  ├─ ai-model-muse.md          # 固定 AI 模特（标准 6 件模卡资产包/复用/换装）
│  ├─ muse-asset-library.md     # Muse 资产库运营（结构/索引/版本/备份）
│  ├─ asset-delivery.md         # AI 资产双通道交付与归档（全部出图通用）
│  ├─ image-garment.md / image-editorial.md / image-detail-fabric.md
│  ├─ video-film-types.md / video-brief.md      # 影片类型 / 四段式
│  ├─ copyright-compliance.md / text-content.md / consistency-lock.md
│  ├─ asset-library-schema.md / tool-adapter.md / quick-reference.md / delivery-checkpoints.md / worked-examples.md
│  └─ design-language-dictionary.md
└─ assets/
   ├─ project-template.md        # 可复制的项目画布
   ├─ asset-library-template.csv # 素材库空模板
   └─ prompt-samples.md          # 已翻好术语的完整提示词模板（新手/零术语直接套用）
```

---

## 生成平台与适配

- **默认**：生图用即梦 **Seedream 5.0 Pro**（大片/高定/campaign 等成品档默认 Pro；Pro 不可用时降级 5.0 Flash/标准版；文生图/图生图/多图参考），视频用即梦 **Seedance 2.5**（统一默认；2.0 仅在不支持 2.5 的环境降级；全能参考/首尾帧）。
- **可换**：可灵 / Runway / Pika / MiniMax H3 / Sora / Veo 等视频，或 Midjourney / Flux / Stable Diffusion / 其他出图。能力清单、术语映射、降级做法、跨 Agent 说明见 **`references/tool-adapter.md`**。
- 各文件里标注的"参考图上限、时长、有无负向字段"等是**默认平台口径**，换平台以官方为准；设计流程、锚点、比例、国标等**方法常数不变**。

## 素材库

仓库只给**蓝图 + 空 CSV 模板**，不绑定任何表格工具。可在飞书多维表格、Airtable、Notion、Excel 自建，字段与投喂权限见 `references/asset-library-schema.md`；个人素材库与技能本体分离，可移植。

---

## 许可证

本作品采用 **[Creative Commons 署名—非商业性使用 4.0 国际许可协议（CC BY-NC 4.0）](https://creativecommons.org/licenses/by-nc/4.0/)** 授权。

- 你可以共享、改编，但**必须署名原作者**（hexiaoyu0525-design，并注明作品名 fashion-studio）、**不得商用**、不得追加限制。
- 完整法律文本见 [`LICENSE`](LICENSE)。

**使用边界**：本仓库公开，欢迎学习与借鉴方法论（设计思路、流程组织、检查清单均可参考）。但**禁止整包复制 / 改名换名后重新发布**，**禁止商用**（含以此接单、卖课、收费服务）；引用本作品内容请注明出处。

© 2026 hexiaoyu0525-design　·　仓库：<https://github.com/hexiaoyu0525-design/fashion-studio>

> 免责声明：本作品为方法论与提示词模板，以"现状"提供；涉及品牌名仅用于行业示例，不构成侵权指引；商用请遵循各生成平台条款与所在国法规。
