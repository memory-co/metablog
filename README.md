# metablog

> 存元认知的地方，主形态是博客。

metablog 有三层内容，全部住在一个**分层 git 仓库**里，没有数据库、没有索引：

- **origin** —— 素材。外部来的、原样的：对话记录、读书摘录、随手笔记。不带后缀的文件都是它，只读。
- **post** —— 博文，主形态。`<标题>.post/` 一个目录：`readme.md`（frontmatter + 正文）、`assets/`、`afterwords/`（回看时追加的后记，只增不改）。
- **insight** —— 元认知条目。`<条目>.insight/readme.md`，从几篇博文里提炼出来，像维基词条，可改可删。

目录树按主题组织，目录就是博客的分类 / 系列；三层的对象并排放。设计见 [`docs/designs/v1/`](docs/designs/v1/README.md)；数据结构 [`docs/structure/v1/`](docs/structure/v1/README.md)；HTTP API [`docs/api/v1/`](docs/api/v1/README.md)；CLI [`docs/cli/v1/`](docs/cli/v1/README.md)。

## 安装

```bash
pip install metablog
metablog server start             # 本地 API：http://127.0.0.1:8100/docs
```

需要 `git`。

## 用起来

```bash
metablog origin add 学习/2026-10-03\ 读《思考，快与慢》第3章摘录.md --file ./摘录.md
metablog post new 学习/我为什么总是高估自己读懂了 --kind 复盘 --tag 阅读 \
    --source '学习/2026-10-03 读《思考，快与慢》第3章摘录.md'
metablog post afterword 学习/我为什么总是高估自己读懂了          # 过段时间回看，追加一篇后记
metablog insight write 学习/流畅感不等于理解 --post 学习/我为什么总是高估自己读懂了
metablog publish                                                 # 导出静态站到 ~/.metablog/site/
```

## 存储

```
~/.metablog/
├── metas/      分层 git 仓库：layer/origin、layer/post、layer/insight(+ 用户层)、stack
├── layers/     用户自定义层：<名>.yaml
└── site/       metablog publish 的产物（静态 HTML + feed.xml），不进 git
```

全部环境变量见 [`docs/structure/v1/filesystem.md`](docs/structure/v1/filesystem.md)。

## 开发

```bash
pip install -e ".[dev]"
pytest
cd metablog/frontend && npm ci && npm run dev
```

## 布局

```
metablog/                ← Python 包（pip: metablog；命令 metablog）
├── cli/                 ← 命令行（本地 API 的客户端）：server / origin / post / insight / meta / search / publish
├── backend/             ← 服务：main.py config.py
│   ├── models/ services/ controllers/     ← 三层
│   └── providers/       ← 存储介质：本地文件系统 + git
└── frontend/            ← Vite + React（读、写、条目浏览）
tests/                   ← 按场景组织
docs/                    ← designs / structure / api / cli
examples/metas/          ← 一份示例内容，看三层长什么样
```
