# metablog/cli —— 命令行

本地 API 的客户端，**不含业务逻辑**：解析参数、发 HTTP、打印结果。一个子命令一个文件。

| 文件 | 子命令 |
|---|---|
| `server.py` | `metablog server start / stop / status` |
| `origin.py` | `metablog origin add`：收一份原始素材 |
| `post.py` | `metablog post new / edit / afterword / list / show` |
| `insight.py` | `metablog insight write / list / show` |
| `meta.py` | 通用的分层仓库操作：`tree` / `log` / `show` |
| `search.py` | `metablog search <词>`：`git grep` stack |
| `publish.py` | `metablog publish`：导出静态站 + RSS |
| `_common.py` | 服务地址、HTTP 客户端、`--json` 输出 |

命令手册等接口定下来再写；使用流程见 [`docs/designs/v1/workflows.md`](../../docs/designs/v1/workflows.md)。
