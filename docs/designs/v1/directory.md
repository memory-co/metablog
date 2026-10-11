# metablog 目录结构设计（v1 草案）

> 存元认知的地方，主形态是博客。参考 [memory-co/memory.talk](https://github.com/memory-co/memory.talk) 的目录结构（2026-10-11 读的 main 分支）。

## 0. 从 memory.talk 借了什么、没借什么

| memory.talk 的做法 | metablog 怎么用 |
|---|---|
| 一个 Python 包装三样：`cli/`（只是本地 API 的客户端）、`backend/`（models / services / controllers 三层 + providers）、`frontend/`（Vite + React，build 产物随包分发） | **照搬**。包名 `metablog`，命令 `metablog` |
| 认知层是**分层 git 仓库**：每层一条 `layer/<名>` 分支，`stack` 是合并视图；没有数据库、没有索引，git 里每个字节都是 canonical | **照搬**，作为博客的存储 |
| 层 = 一份 YAML 协议；对象 = 带后缀的目录（`.issue/`、`.card/`）；不带后缀的文件就是 origin（原文） | **照搬机制，换层**：`origin` / `post` / `insight` |
| 目录树按主题组织，原文和各层对象并排 | **照搬**：主题目录 = 博客的分类 / 系列 |
| 一个动作一个 commit，subject 以 `[层名]` 开头；历史 / 检索 / 旧版本都靠 git | **照搬**：博文的修订史就是 git log，不另存版本 |
| `tests/` 按场景组织，每个目录 `README.md`（测什么 / 不测什么 / fixture）+ `test.py` | **照搬** |
| `docs/` 分 `designs/`（为什么）、`structure/`（是什么）、`api/`、`cli/`，各自按 `v<N>/` 分版本 | **照搬** |
| 每个代码目录都有一份 `README.md` 说明它是什么 | **照搬** |
| work / worklet / tmux / node / trace（跑 agent 的工作台） | **不要**。metablog 不跑 agent |
| user / auth / JWT（团队多人） | **v1 不要**，单人使用；作者取 git author。以后要多人再加 |

## 1. 代码仓库布局

```
metablog/                         ← 仓库根
├── README.md                     ← 一句话定位、安装、用起来、存储、开发、布局
├── LICENSE
├── pyproject.toml                ← pip 包 metablog，命令 metablog
├── .github/workflows/test.yml    ← pytest + 前端 build
│
├── metablog/                     ← Python 包
│   ├── README.md                 ← 包里有哪几样
│   ├── __init__.py               ← __version__
│   ├── __main__.py               ← python -m metablog → cli.main()
│   │
│   ├── cli/                      ← 命令行：本地 API 的客户端，不含业务逻辑；一个子命令一个文件
│   │   ├── README.md
│   │   ├── _common.py
│   │   ├── server.py             ← metablog server start
│   │   ├── origin.py             ← metablog origin add（收原始素材）
│   │   ├── post.py               ← metablog post new / edit / afterword / list
│   │   ├── insight.py            ← metablog insight write / list
│   │   ├── meta.py               ← 通用的分层仓库操作：tree / log / show
│   │   ├── search.py             ← git grep 包一层
│   │   └── publish.py            ← metablog publish（导出静态站 + RSS）
│   │
│   ├── backend/                  ← FastAPI 服务
│   │   ├── README.md
│   │   ├── main.py  config.py  serve.py
│   │   ├── models/               ← 请求 / 响应模型：metas.py posts.py insights.py search.py result.py
│   │   ├── services/
│   │   │   ├── metas/            ← 分层 git 引擎（几乎可以从 memory.talk 原样拿来）
│   │   │   │   ├── repo.py  git.py  manager.py
│   │   │   │   └── layers/       ← 内置层协议：origin.yaml / post.yaml / insight.yaml + protocol.py
│   │   │   ├── posts/            ← 博客视角的读：时间线（按 date 排）、系列（按目录）、标签聚合、后记
│   │   │   ├── insights/         ← 元认知条目：从博文提炼、反查引用它的博文
│   │   │   ├── search/
│   │   │   └── publish/          ← 渲染静态站：模板、RSS / Atom、站点地图
│   │   ├── controllers/          ← HTTP 路由：metas.py posts.py insights.py search.py publish.py system.py
│   │   └── providers/            ← 存储介质：fs.py（v1 只有本地文件系统 + git）
│   │
│   └── frontend/                 ← Vite + React
│       ├── README.md
│       └── src/
│           ├── shell/            ← 外壳、导航、全局搜索
│           ├── reader/           ← 读：时间线、系列、标签、单篇（含后记）
│           ├── editor/           ← 写：Markdown 编辑器、frontmatter 表单、引用 origin
│           ├── insights/         ← 元认知条目浏览：条目页 + 「出自哪些博文」
│           ├── components/  hooks/  lib/
│           └── assets/
│
├── tests/                        ← 按场景组织，每个目录 README.md + test.py
│   ├── README.md  conftest.py  _util.py
│   ├── metas/
│   │   ├── basic/                ← 三层各放一个对象，stack 看到全部
│   │   ├── layer_guard/          ← [post] 提交碰不到 .insight/ 里的东西
│   │   └── user_layer/           ← 自定义层能载入
│   ├── posts/
│   │   ├── write/                ← 新建博文，frontmatter 不合协议整批拒
│   │   ├── afterword_append_only/← 后记只增不改
│   │   ├── timeline/             ← 按 date 排序、按系列 / 标签过滤
│   │   └── assets/               ← 博文图片随对象目录走
│   ├── insights/
│   │   └── backlinks/            ← 条目反查到引用它的博文
│   ├── publish/
│   │   └── static_site/          ← 导出的 HTML / RSS 里有该有的东西
│   └── cli/
│       └── end_to_end/
│
└── docs/
    ├── designs/v1/               ← 为什么：README.md、metas/{README,layer,post,insight}.md、publish.md
    ├── structure/v1/             ← 是什么：README.md（对象清单）、filesystem.md、metas.md
    ├── api/v1/                   ← HTTP 契约
    └── cli/v1/                   ← 命令手册
```

## 2. 数据目录（内容存哪）

```
~/.metablog/                      ← METABLOG_HOME
├── metas/                        ← 分层 git 仓库，内容的唯一真身
│   ├── .git/                     ←   refs/heads/layer/{origin,post,insight,…}、refs/heads/stack；HEAD → stack
│   ├── metas.json                ←   始祖提交里唯一的文件：layers[]（最底在前）
│   └── <按主题组织的目录树>/      ←   原文、.post/、.insight/ 并排；目录 = 博客的分类 / 系列
├── layers/                       ← 用户自定义层：<名>.yaml，启动时载入
└── site/                         ← metablog publish 的产物（静态 HTML + feed.xml），不进 git，可随时重建
```

### 一个真实的样子

```
metas/
├── metas.json
├── 学习/
│   ├── 2026-10-03 读《思考，快与慢》第3章摘录.md        ← origin：原样的素材，不带后缀，只读
│   ├── 我为什么总是高估自己读懂了.post/                  ← post：一篇博文
│   │   ├── readme.md                                     ←   frontmatter + 正文
│   │   ├── assets/曲线.png                               ←   本篇图片
│   │   └── afterwords/
│   │       ├── 2026-10-20.md                             ←   后记：过段时间回看，只增不改
│   │       └── 2027-01-05.md
│   └── 流畅感不等于理解.insight/                         ← insight：提炼出的元认知条目
│       └── readme.md
└── 写代码/
    ├── 2026-09-28 和 Claude 的调试对话.md               ← origin
    └── 一次三小时的方向性错误.post/
        └── readme.md
```

## 3. 三个内置层

| 层 | 层序 | 形态 | 能不能改 | 对应 memory.talk |
|---|---|---|---|---|
| `origin` | 0（最底） | 任何不带后缀的文件：对话记录、读书摘录、随手笔记、外链存档 | 只读（原样保存） | origin |
| `post` | 1 | `<标题>.post/` 目录 | 正文可改（修订史在 git）；`afterwords/` 只增 | issue 的位置，但换成博客形态 |
| `insight` | 2 | `<条目>.insight/readme.md` | 可改、可删，像维基词条 | card |

**post 是主形态**：大部分元认知直接以博文存在，insight 只在一个想法被多篇博文反复印证、值得单独成条时才写。

### post 层：`<标题>.post/`

```markdown
---
date: 2026-10-05
kind: 复盘            # 复盘 / 方法 / 觉察 / 提问
tags: [阅读, 理解]
summary: 读得顺不代表读懂了，检验办法是合上书讲一遍
sources: [学习/2026-10-03 读《思考，快与慢》第3章摘录.md]
links: [写代码/一次三小时的方向性错误]
---

## 发生了什么
## 我当时怎么想的
## 现在怎么看
## 下次怎么做
```

| 字段 | 类型 | 说明 |
|---|---|---|
| `date` | date | 发表日；时间线按它排 |
| `kind` | enum | 复盘 / 方法 / 觉察 / 提问；给元认知分个类型 |
| `tags[]` | list of string | 横向聚合 |
| `summary` | string | 一句话，列表页和 RSS 用 |
| `sources[]` | list of ref origin | 这篇基于哪些原始素材 |
| `links[]` | list of ref post | 相关博文 |

没有 `title`（目录名就是）、没有 `series`（所在目录就是）、没有 `status`（删就是删，草稿可以用一个 `草稿/` 目录或用户层表达）。正文的四段是模板，不强制。

`afterwords/<YYYY-MM-DD>.md`：回看时追加的后记，**只增不改**（对应 memory.talk 里立场的「只增」约定）。元认知最有价值的往往是「三个月后我怎么看当时的自己」，单独成文件让它在时间线和 git log 里都清楚可见。

### insight 层：`<条目>.insight/readme.md`

```markdown
---
context: 读技术书 / 读论文时
posts: [学习/我为什么总是高估自己读懂了, 写代码/一次三小时的方向性错误]
links: [学习/先输出再输入]
---

读起来流畅，只说明文字好懂，不说明我能用。检验：合上书，能不能给别人讲出来、举出书上没有的例子。
```

| 字段 | 类型 | 说明 |
|---|---|---|
| `context` | string | 在什么情境下成立 |
| `posts[]` | list of ref post | 出自哪些博文（条目记博文，博文不记条目，和 card 记 issue 同理） |
| `links[]` | list of ref insight | 相关条目 |

## 4. 几个我替你定的默认（可改）

1. **metablog 是工具仓库 + 内容数据目录分离**，和 memory.talk 一样：代码在仓库里，内容在 `~/.metablog/metas/`（本身是 git，可以单独推到一个私有仓库备份）。如果你更想要「内容就放在仓库里、像 Hexo / Hugo 那样」，把 `metas/` 挪进仓库根即可，层机制不变。
2. **v1 去掉 work / user / auth**：单人博客用不上；作者取 git author。
3. **三层 origin / post / insight**，post 为主。如果只要纯博客，insight 层可以先不实现，目录结构不受影响。
4. **发布是静态导出**（`site/`），不做在线评论；读者交互以后再说。
