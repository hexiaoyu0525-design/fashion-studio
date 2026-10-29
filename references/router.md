# Fashion Studio 路由表

本文件是 fashion-studio 的**完整任务分类路由**，由 SKILL.md「任务路由」一节指向。**每次任务开始，先按下方「任务分类路由表」判断任务类型，命中即进入对应文件，再执行具体操作。**

> 文件路径约定：下列引用均相对**技能根目录**（与 SKILL.md 同级）；本文件位于 `references/` 下。

## 任务分类路由表

按顺序判，命中即进入对应参考文件：

| 任务 | 进入 |
|---|---|
| **① 开工 / 素材接入** | |
| 项目文件夹放了参考图/视频，或想从中间阶段开始（已有灵感/部分要素/已有效果图） | SKILL.md「怎么开工：素材接入 + 任意阶段进入」 |
| 要自动抓品牌官网/秀场参考图（给品牌名或 URL，收集图片 + 设计理念文字） | **独立技能 `fashion-web-scraper`**（https://github.com/hexiaoyu0525-design/fashion-web-scraper，另行安装；三通道按环境选：① 本地 Playwright 批量 / ② Agent 内置浏览器自动化零部署少量 / ③ 手动放图或直接发参考图——零门槛，人人可用） |
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

## 全流程怎么走

**全流程怎么走（编号 ≠ 创作先后）**：调研→灵感→服装三要素（款式·廓形/色彩/面料并行）→纹样/工艺花型→**效果图（先）定款→款式图（后）**→配饰（选做）→摄影大片/细节特写→工程（要生产时）→提交。做设计先走 `references/design-ideation.md`（把设计做出来），前期板走 `references/design-boards.md`（含三要素与顺序），设计图走 `references/fashion-illustration-spec.md`，**定稿后出商品图全程受 `references/image-quality-sop.md` 四步管线调度**，大片走 `references/image-editorial.md`，要生产走 `references/technical-production-spec.md`，提交/商业走 `references/portfolio-board.md`；企业语境归 `references/enterprise-proposal.md`，赛事语境归 `references/aigc-competition.md`，文字归 `references/text-content.md`，版权归 `references/copyright-compliance.md`。

## 混合任务

**混合任务**（企划里既有图又有片）：先走 `references/enterprise-proposal.md` 定总方案与交付物矩阵，再分别进入图/视频模块。

## 文件地图（29 个参考 + assets 模板，按域分组；"什么任务进哪个文件"以上方路由表为准）

- **开工 / 协作**：`references/project-workflow.md`（三模式·画布·交付打包）、`references/tool-adapter.md`（换平台 / Agent）、`references/quick-reference.md`（硬数值速查卡）、`references/delivery-checkpoints.md`（全流程验收速查卡）、`references/worked-examples.md`（全流程范例）
- **企业 / 赛事**：`references/enterprise-proposal.md`（三企划·趋势节奏·波段·封样·评审）、`references/aigc-competition.md`（三层分类·读题·获奖案例·交付）
- **设计与前期**：`references/design-ideation.md`（从零做设计·分寸尺·白模自举）、`references/design-language-dictionary.md`（感性词→设计变量 + 人话⇄术语对照）、`references/design-boards.md`（全局板面底座 + 01–06、10 板）、`references/material-lab.md`（造料：面料再造 / AI 创意面料 / 可持续）、`assets/prompt-samples.md`（示例锚点包：已翻好术语的完整提示词模板）
- **出图**：`references/image-quality-sop.md`（总调度·四步管线）、`references/image-garment.md`（无模特服装图）、`references/image-editorial.md`（大片 / lookbook）、`references/image-detail-fabric.md`（细节微距）、`references/fashion-illustration-spec.md`（07–09、11 图与人体比例）、`references/ai-model-muse.md`（固定 AI 模特）、`references/muse-asset-library.md`（Muse 资产库运营：归档/版本/索引/云盘）、`references/asset-delivery.md`（AI 资产双通道交付与归档）、`references/category-guide.md`（全品类全风格）、`references/fabric-guide.md`（识料 / 面料知识）、`references/consistency-lock.md`（返工诊断）
- **工程 / 提交**：`references/technical-production-spec.md`（12–16 白坯到 3D）、`references/portfolio-board.md`（17–21 作品集到 AI 成片）
- **视频**：`references/video-film-types.md`（九种影片类型）、`references/video-brief.md`（导演流水线·四段式·对标拆解·声音与包装）
- **文字 / 合规 / 库**：`references/text-content.md`（随件说明与文案）、`references/copyright-compliance.md`（版权底线与自查报告）、`references/asset-library-schema.md`（素材库蓝图·**四级投喂权限唯一定义**）
