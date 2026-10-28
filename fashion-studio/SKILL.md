---
name: fashion-studio
description: 时尚行业 AIGC 内容生产技能，覆盖企业企划、生图、视频、赛事四线全流程：从"企业给了什么"一路做到"最终交付什么"，贯穿 21 项交付物规范与版权合规。提及服装企划、出图、出片、参赛，或"灵感板/款式图/lookbook/大片/走秀视频"时使用；结果不对时用于定位改哪句。
license: CC-BY-NC-4.0
metadata:
  author: "hexiaoyu0525-design"
  version: "1.4.0"
  license-name: "Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)"
  repository: "https://github.com/hexiaoyu0525-design/fashion-studio"
  copyright: "Copyright © 2026 hexiaoyu0525-design"
---

# 时尚工作室

> **fashion-studio**　© 2026 hexiaoyu0525-design　|　版本 1.4.0　|　许可 [CC BY-NC 4.0](LICENSE)（使用须署名、禁商用）　|　仓库：https://github.com/hexiaoyu0525-design/fashion-studio

把服装/服饰品牌的任务，从"企业给了什么"一路做到"最终交付什么"。四类任务：**企业企划、生图、视频、赛事**，并贯穿一条版权合规底线。

## 怎么开工：素材接入 + 任意阶段进入

### A. 素材接入：参考图 / 视频，怎么用

在对话框绑定项目文件夹，把素材按用途放进去（`服装/`、`模特/`、`面料/`、`场景/`、`纹样/`、`参考视频/`、`灵感/`、`草图/`）；也可以让我用浏览器自动采集官网/秀场素材（可选旁挂 `fashion-web-scraper`）。**你的草图/线稿是最佳输入**，可直接垫图当锚点（详见 `design-ideation.md`）。

**素材登记与投喂分级**：开工先扫描文件夹、逐件登记（能控制什么、投喂权限 🟢/🟡/🔴/⚪），原则是**参考全绿、交付分级**——🟢 可作终稿锚点；🟡（真人脸/当代品牌/在世设计师）公开交付须实质转化；🔴（品牌 Logo/老花/注册印花）看学无限制、慎喂垫图。完整规则见 `asset-library-schema.md`。

- 生成时把素材作为"图1/图2/图3、@视频/@音频"上传（连接器没开则由你手动传，我给清单顺序）；图片直接读，视频走抽帧解析。
- 素材不会自动监听：中途新增时说一句"新加了什么"，或让我重新扫描。
- 图1/图2/图3 缺件（如缺背面/面料特写）时，我先明确要补哪张，不硬出。

### B. 从任意阶段中途开始（warm start）

分阶段、带验收门的流水线：**已有什么就锁定什么，从第一个"没验收过"的阶段继续**。开工先做现状盘点（已锁✅/待补❌/存疑⚠️），存疑的退回确认，不擅自重做。

| 你的起点 | 从哪接 |
|---|---|
| 只有灵感/主题/参考图 | 三要素（廓形/色彩/面料）→ 纹样/工艺 → 效果图 → 款式图 → 配饰版（选做）→ 摄影大片 |
| 已有色彩/面料，缺款式 | 补廓形/款式 → 效果图 |
| **已有效果图，没款式图** | 直接做款式图（07章节）→ 配饰版（选做）→ 摄影大片 |
| **已有款式图，要做宣传** | 配饰版（选做）→ 摄影大片（image-editorial.md） |
| **已有纯白底图（6套定稿）** | 配饰版（选做）→ 摄影大片 |
| **已有摄影大片参考图，只换服装** | 直接走"复刻参考"流程（image-editorial.md 场景2） |
| 已有款式图/成衣图/实物 | 直接走 `image-quality-sop.md` 四步管线：锁样衣→成衣→上模特→补镜头 |
| 有图有想法、只要出片 | `video-film-types.md` 定类型 → `video-brief.md` 导演流水线 → 四段式 |
| **有其他系列的部分内容，要接着做** | 先盘点已有什么、缺什么，从第一个缺的阶段继续 |

> 已锁定的上游要素（给定色/面料/廓形/效果图/款式图/纯白底图）按约束处理，不擅自改；若彼此冲突或不足以支撑下一步，我先指出并给选项，再继续。

## 先做任务分类

按顺序判，命中即进入对应参考文件：

| 任务 | 进入 |
|---|---|
| **① 开工 / 素材接入** | |
| 项目文件夹放了参考图/视频，或想从中间阶段开始（已有灵感/部分要素/已有效果图） | 本文档「怎么开工：素材接入 + 任意阶段进入」 |
| 要自动抓品牌官网/秀场参考图（给品牌名或 URL，收集图片 + 设计理念文字） | **可选旁挂 skill `fashion-web-scraper`**（三通道按环境选：① 本地 Playwright 批量 / ② Agent 内置浏览器自动化零部署少量 / ③ 手动放图或直接发参考图——零门槛，人人可用） |
| 怎么开工/配合/续接：工作模式（快速/协作/评审）、项目画布、审美基准板、出图前工单、成本档、项目目录、交付打包 | `references/project-workflow.md` |
| 开工/立项要模板：项目画布空表、素材库空 CSV（字段与投喂权限列头已就绪） | `assets/project-template.md`（可复制项目画布）、`assets/asset-library-template.csv`（素材库空模板，字段见 `references/asset-library-schema.md`） |
| 查硬数值/规格/术语/尺寸/标准号（开工前或交付前对一遍） | `references/quick-reference.md` |
| 换生图/视频平台、换 Agent（Codex / WorkBuddy / Claude Code 等）：能力清单、术语映射、降级做法 | `references/tool-adapter.md` |
| 交付前全流程验收速查 / 阶段流转检查（21 项逐项打勾） | `references/delivery-checkpoints.md` |
| 想要可照抄的完整流程范例（企业任务/生图/视频/高定系列/参赛、强写法↔弱写法） | `references/worked-examples.md` |
| **② 企业 / 赛事** | |
| 企业给了完整任务 / 要季度企划 / 要一套完整方案 | `references/enterprise-proposal.md` |
| 参加 AIGC / 数字时装 / 服装设计比赛：选赛、读题、从零到交付 | `references/aigc-competition.md` |
| **③ 设计与前期（含语言字典）** | |
| 从零做设计：没想法、给了参考图/纯文字、要好看且原创、灵感转译、参考分寸 | `references/design-ideation.md` |
| **点名品牌/设计师做参照或灵感**（"想要 Margiela 那种感觉 / 对标 XX 品牌"）→ 先翻译成锚点语言再设计 | `references/design-ideation.md` 3·7/3·8 + `references/design-language-dictionary.md` 六·5/六·6 |
| 感性词/风格词说不清（显瘦、高级、复古、老钱、甜酷、年代、品类、面料）→ 翻译成设计变量 | `references/design-language-dictionary.md` |
| 你完全不懂服装术语（说不出面料/廓形/工艺叫什么），只会说感受、打比方或给图 | `references/design-language-dictionary.md` 第七节「人话⇄术语对照」+ `references/project-workflow.md`「零术语适配·新手模式」+ `assets/prompt-samples.md`（已翻好术语的完整提示词模板，只改 2–3 处占位） |
| 前期企划板：调研（01 含自主趋势研判四步）/灵感/服装三要素（款式·廓形/色彩/面料）/纹样·工艺花型（含刺绣）；另含 **02-附 主题板/概念板**（可作灵感板替代或追加） | `references/design-boards.md` |
| 配饰造型板（10）：可以在前期企划阶段定方向，也可以在款式图之后、摄影大片之前做完整搭配方案，选做环节 | `references/design-boards.md` |
| 面料再造 / 材料实验 / AI 创意面料·虚拟材质 / 可持续·未来材料（"造料"，不是选料） | `references/material-lab.md` |
| **④ 出图（含返工）** | |
| **出图统一交付规则（fs 全部 AI 生图/编辑产物通用）：每张出图须"持久归档 + 直接展示"双通道闭环，豆包办公即"画布写入 + 本地归档 + 对话框展示"** | `references/asset-delivery.md` |
| 出任何服装/系列图：四步管线、验收门、走哪条路径、人体比例统一口径（**生图总入口**） | `references/image-quality-sop.md` |
| 设计表达：平面款式图/时装效果图/系列 Line-up/细节图、时装人体比例（07–09、11） | `references/fashion-illustration-spec.md` |
| 只要图 · 服装本体（无模特）：款式、平铺、挂拍、人台、幽灵模特、技术款式图 | `references/image-garment.md` |
| 只要图 · 模特穿上：lookbook、服装大片、上身、系列图 | `references/image-editorial.md` |
| 建立/复用一个固定 AI 模特（专属模特，跨图/跨系列锁同一人；含真人照片/参考图建模的起点三问、比例口径与身形分离法） | `references/ai-model-muse.md` |
| Muse 资产库运营：整库结构/身份卡与索引一致性/版本迭代/头身比实测/云盘备份与增量同步 | `references/muse-asset-library.md` |
| 出图对品类没把握（针织/牛仔/男装/童装/内衣泳装/羽绒/婚纱高定/皮革等）查品类结构·工艺·翻车点 | `references/category-guide.md` |
| 查某面料是什么、怎么渲染/打光/写动态（面料全品类知识） | `references/fabric-guide.md` |
| 只要图 · 局部特写：细节、工艺、面料、辅料、微距 | `references/image-detail-fabric.md` |
| 图或视频结果不对、要返工 | `references/consistency-lock.md` |
| **⑤ 工程 / 提交** | |
| 版型工程：白坯/立裁/纸样/工艺单 Tech Pack/BOM 尺寸推档/3D 虚拟成衣（12–16） | `references/technical-production-spec.md` |
| 提交落地：作品集展板/Line Sheet/吊牌洗唛/甘特/AI 成片衔接、赛事提交速查（17–21） | `references/portfolio-board.md` |
| **⑥ 视频** | |
| 只要视频 · 先定影片类型 | `references/video-film-types.md` |
| 已定类型 · 写投喂 Seedance 的四段式备料包；**导演流水线**（定类型→五问定片→视觉系统分层→风格档/导演声音→镜头表→四段式→生成锚点→声音后期→验收）；文生/图生视频生成前的导演逻辑（五问定片、出现形态、锚点链）；有参考时尚片想对标重做 | `references/video-brief.md` |
| 参考片是短视频爆款/带货玩法，要复刻换人换产品（口播/盘点/街采/播客等） | 可选协作 `video-remix-studio`（爆款复刻六阶段导演流水线，README「可选配套」有安装与分工说明）；时尚美学/人物比例仍以本技能为准 |
| **⑦ 文字 / 合规 / 库** | |
| 要写文字：品牌故事、主题概念、三级随件说明、汇报发言稿、营销文案、designer statement、AI 创作说明 | `references/text-content.md` |
| 版权合规：AI 素材来源、可商用判定、风险评级、原创证明、版权自查报告 | `references/copyright-compliance.md` |
| 建/用 AIGC 素材库：模特、服装、面料、姿态、动态、文化参考的分类、投喂权限与字段规范 | `references/asset-library-schema.md` |

**全流程怎么走（编号 ≠ 创作先后）**：调研→灵感→服装三要素（款式·廓形/色彩/面料并行）→纹样/工艺花型→**效果图（先）定款→款式图（后）**→配饰（选做）→摄影大片/细节特写→工程（要生产时）→提交。做设计先走 `design-ideation.md`（把设计做出来），前期板走 `design-boards.md`（含三要素与顺序），设计图走 `fashion-illustration-spec.md`，**定稿后出商品图全程受 `image-quality-sop.md` 四步管线调度**，大片走 `image-editorial.md`，要生产走 `technical-production-spec.md`，提交/商业走 `portfolio-board.md`；企业语境归 `enterprise-proposal.md`，赛事语境归 `aigc-competition.md`，文字归 `text-content.md`，版权归 `copyright-compliance.md`。

**混合任务**（企划里既有图又有片）：先走 `enterprise-proposal.md` 定总方案与交付物矩阵，再分别进入图/视频模块。

## 三档分工

> 完整协作协议（快速/协作/评审三模式、四类决策、审美分叉走对比图、问题按需即时问、输出详细度）见 `project-workflow.md` 第二、四节；下表是简化版。

| 谁定 | 内容 |
|---|---|
| 我直接定 | 光线方向、运镜可行性、参数、焦段、镜头数、时间轴密度、提示词写法 |
| 我出选项你选 | 场景、动作链、运镜风格、影片类型、风格档 |
| 只能你定 | 主推点、品牌调性、目标受众、预算、上线时间 |

缺了"只能你定"的信息，我用选项来问，不替你决定。

## 三条基本原则

1. **锚点不可动。** 服装锚点（结构、版型、颜色及色位、长度、闭合件、图案位置尺度、配饰鞋履、面料质地反光）+ 模特锚点（五官、发型、身形比例、妆容标志特征）只随动作、场景、光源变化；变形就是废片（完整锚点清单与禁区句式见 `references/consistency-lock.md`）。
2. **素材各司其职。** 一件素材只控制它该控制的；图生图提示词必须点名 `图1/图2/图3` 各自管什么。
3. **白话与抽象词，我先共鸣再翻译。** 你不知道服装术语完全没关系——说人话、说感受、打比方、给图，都是**合法输入**（**新手模式默认开**）。**先共鸣后翻译，不直接查字典猜方向**：一个感性词有多个方向（"高级"有极简/繁复/暗黑/静奢/先锋五种），先用一句话回显你给的感觉、给 2–3 个意象方向选项（画面感而非风格名），你拍板后再翻译。我自动：① 查 `design-language-dictionary.md` 第七节「人话⇄术语对照」，把"滑滑的/硬邦邦/闪亮像水"翻成可执行的专业词；② 说不出就出**向导选择题**（每项带"我推荐+理由"，先走"感觉五步收拢"：回显→意象选项→翻锚点→对比小图→进宪法，见 `project-workflow.md`「零术语适配」）；③ 连感觉都说不清就引导你**发图**（参考图/垫图/灵感图，图代词是零术语主通道）。翻译后交给你看的提示词必须具体可执行、不含模糊词，并附"你说的原话 → 我用的专业词"对照，让你边用边积累。

## 生成工具与入口（默认平台，可替换）

> 本技能的方法论**工具中立**；下列平台是**作者实测的默认实现**，不是唯一选择。换生图/视频平台、换 Agent（Codex / WorkBuddy / Claude Code 等）的能力清单、术语映射与降级做法，见 `tool-adapter.md`。

- **生图（默认）**：**Seedream 5.0 Pro**（即梦；**大片/高定/campaign 等成品档统一默认 Pro**，编辑一致性更强、防漂移；Pro 不可用时降级 5.0 Flash/标准版）。
- **视频（默认）**：即梦 **Seedance 2.5**（统一默认 2.5；只有「全能参考」和「首尾帧」两个入口能命中 2.0/2.5；2.0 仅在不支持 2.5 的环境降级）。
- 本技能**不绑定本地节点工作流、不依赖本地算力**；批量提效（批量换色/换装/换场景、批量出图）交给云平台的批量能力。
- 我负责把料备齐、把提示词写准；**最终"生成"由你按下**。连接器没开时流程照走，只是不由我直接调用——正因如此，这套方法在任何 Agent、任何平台上都能用。

## 文件地图（29 个参考 + assets 模板，按域分组；"什么任务进哪个文件"以上方路由表为准）

- **开工 / 协作**：`project-workflow.md`（三模式·画布·交付打包）、`tool-adapter.md`（换平台 / Agent）、`quick-reference.md`（硬数值速查卡）、`delivery-checkpoints.md`（全流程验收速查卡）、`worked-examples.md`（全流程范例）
- **企业 / 赛事**：`enterprise-proposal.md`（三企划·趋势节奏·波段·封样·评审）、`aigc-competition.md`（三层分类·读题·获奖案例·交付）
- **设计与前期**：`design-ideation.md`（从零做设计·分寸尺·白模自举）、`design-language-dictionary.md`（感性词→设计变量 + 人话⇄术语对照）、`design-boards.md`（全局板面底座 + 01–06、10 板）、`material-lab.md`（造料：面料再造 / AI 创意面料 / 可持续）、`assets/prompt-samples.md`（示例锚点包：已翻好术语的完整提示词模板）
- **出图**：`image-quality-sop.md`（总调度·四步管线）、`image-garment.md`（无模特服装图）、`image-editorial.md`（大片 / lookbook）、`image-detail-fabric.md`（细节微距）、`fashion-illustration-spec.md`（07–09、11 图与人体比例）、`ai-model-muse.md`（固定 AI 模特）、`muse-asset-library.md`（Muse 资产库运营：归档/版本/索引/云盘）、`asset-delivery.md`（AI 资产双通道交付与归档）、`category-guide.md`（全品类全风格）、`fabric-guide.md`（识料 / 面料知识）、`consistency-lock.md`（返工诊断）
- **工程 / 提交**：`technical-production-spec.md`（12–16 白坯到 3D）、`portfolio-board.md`（17–21 作品集到 AI 成片）
- **视频**：`video-film-types.md`（九种影片类型）、`video-brief.md`（导演流水线·四段式·对标拆解·声音与包装）
- **文字 / 合规 / 库**：`text-content.md`（随件说明与文案）、`copyright-compliance.md`（版权底线与自查报告）、`asset-library-schema.md`（素材库蓝图·**四级投喂权限唯一定义**）

## 交付前总检（任何任务交付前过一遍）

交付前逐项核对，任一项不过先修：

- **任务归位**：企业/赛事/图/视频分类正确；混合任务已按总方案拆到对应模块。
- **设计站得住**：母题/记忆点说得清；有参考的过了分寸尺 L2–L4、改动 ≥3 层、交付三问能答；纯文字已把感性词翻成变量并走白模骨架。
- **出图顺序对**：四步管线没有跳级；每步过了验收门；人体比例统一口径（无母版直出写实/照片向 **1:9 + 裆 55%**、有 Muse 继承母版、插画档 9–10 头，未混用）；**成片人体锚 = Muse 写实母版、效果图只供服装（母版锚定法，见 `image-editorial.md` 场景3），且成片提示词默认不写头身比数字**；图1/图2/图3 各管一个变量。
- **视频先导后生**：五问定片能答、服装出现形态全覆盖、锚点依赖链浅；有参考时只继承功能关系、不抄秒数（`video-brief.md`）。
- **规格合规**：尺寸/dpi/出血/色彩模式（印 300 CMYK、屏 150 RGB）按 `quick-reference.md` 对过；色号 Pantone/hex、面料、工艺、公差不缺。
- **AI 边界守好**：精确取色、款式图矢量、无缝分色、纸样/Tech Pack/BOM/3D 工程没有拿 AI 图冒充；工艺核验件为实拍/矢量；电商主图为实物、AI 合成真人已披露。
- **企业保真**：企业件有色卡/面料封样、PP/TOP 链路；AI 图只用于提案与营销，未冒充实物。
- **赛事**：匿名、尺寸/页数/dpi、原创与 AI 流程披露、3D 边界都按当年章程。
- **版权**：每图/每板有来源与授权标注；投喂权限 🟢/🟡/🔴/⚪ 正确（参考层无红线）；**公开交付**（参赛/商用/公开发布）成片无可识别真人、无品牌老花/Logo、🟡 已转化；自查报告齐备（`copyright-compliance.md`）。
- **文字**：每张图/每组图有专业随件说明；图与说明一致、不夸大（`text-content.md`）。
- **项目留痕**：项目画布已更新到最新（进度看板/设计宪法/素材/提示词与版权日志，见 `project-workflow.md`）；给领导/买手/评委附一页纸摘要；版权报告可一键汇总。
- **产物闭环**：**fs 全部出图/出片**已逐项"持久归档 + 直接展示"（豆包办公=画布写入+对话框展示，见 `asset-delivery.md`），无静默跳过、无只给路径不展示。
- **命名与交付**：按 `季节码_系列_板名_版本_日期` 命名；PDF 可打印、可编辑母版留存。
