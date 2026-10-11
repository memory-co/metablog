# docs

| 目录 | 讲什么 | 什么时候看 |
|---|---|---|
| [`designs/v1/`](designs/v1/README.md) | **为什么**：产品定位、内容模型、存储、使用流程、发布，以及还没定的事 | 想知道 metablog 是什么、为什么这么做 |
| [`structure/v1/`](structure/v1/README.md) | **是什么**：对象清单、字段、磁盘布局、代码仓库布局 | 写代码、写内容时查 |

## 阅读顺序

1. [designs/v1/product.md](designs/v1/product.md) —— metablog 解决什么问题、不解决什么
2. [designs/v1/content.md](designs/v1/content.md) —— origin / post / insight 三层为什么这么分
3. [designs/v1/workflows.md](designs/v1/workflows.md) —— 一条元认知从记下到发出去的完整路径
4. [designs/v1/storage.md](designs/v1/storage.md) —— 为什么用分层 git、不用数据库
5. [designs/v1/publish.md](designs/v1/publish.md) —— 发什么、不发什么
6. [designs/v1/open-questions.md](designs/v1/open-questions.md) —— 待你拍板的问题

## 约定

- **一件事只在一处写**。designs 讲理由，引用 structure 里的定义，不重抄字段表和目录树；structure 讲定义，不讲理由。
- **字段以层协议 YAML 为准**：[`metablog/backend/services/metas/layers/*.yaml`](../metablog/backend/services/metas/layers/README.md)。structure 里的字段表跟着它改。
- **版本**：每个目录下按 `v<N>/` 分版本。v1 定稿前直接改，定稿后不兼容的改动开 v2。
- **没有占位文件**。还没设计的东西不建空文件，记在 [open-questions.md](designs/v1/open-questions.md)。HTTP API（`api/`）和命令手册（`cli/`）等接口定下来再加。
