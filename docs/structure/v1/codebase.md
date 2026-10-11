# Codebase (v1)

代码仓库的布局：每个目录放什么。参考 [memory-co/memory.talk](https://github.com/memory-co/memory.talk) 的布局（2026-10-11 读的 main 分支）。内容数据放哪见 [filesystem.md](filesystem.md)，层和对象见 [metas.md](metas.md)。

> 目录骨架已经搭好，2026-10-11 起暂停，先做设计。

## 0. 从 memory.talk 借了什么、没借什么

| memory.talk 的做法 | metablog 怎么用 |
|---|---|
| 一个 Python 包装三样：`cli/`（只是本地 API 的客户端）、`backend/`（models / services / controllers 三层 + providers）、`frontend/`（Vite + React，build 产物随包分发） | **照搬**。包名 `metablog`，命令 `metablog` |
| 认知层是**分层 git 仓库**：每层一条 `layer/<名>` 分支，`stack` 是合并视图；没有数据库、没有索引，git 里每个字节都是 canonical | **照搬**，作为博客的存储 |
| 层 = 一份 YAML 协议；对象 = 带后缀的目录（`.issue/`、`.card/`）；不带后缀的文件就是 origin（原文） | **照搬机制，换层**：`origin` / `post` / `insight` |
| 目录树按主题组织，原文和各层对象并排 | **照搬**：主题目录 = 博客的分类 / 系列 |
| 一个动作一个 commit，subject 以 `[层名]` 开头；历史 / 检索 / 旧版本都靠 git | **照搬**：博文的修订史就是 git log，不另存版本 |
| `tests/` 按场景组织，每个目录 `README.md`（测什么 / 不测什么 / fixture）+ `test.py` | **照搬** |
| `docs/` 分 `designs/`（为什么）、`structure/`（是什么）、`api/`、`cli/`，各自按 `v<N>/` 分版本 | **照搬**；`api/` `cli/` 等设计定稿、接口确定后再加 |
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
└── docs/                         ← 见 docs/README.md
    ├── designs/v1/               ← 为什么
    └── structure/v1/             ← 是什么
```
