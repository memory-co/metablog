# tests

**场景化**：每个目录一个场景，自带 `README.md`（在测什么 / 不在这测什么 / fixture 来源）和 `test.py`；test.py 里每个函数只断言一件事，函数名就是结论。

```
pip install -e ".[dev]" && pytest     # 全部
pytest tests/metas/layer_guard        # 单个场景
```

| 目录 | 场景 |
|---|---|
| `metas/` | 分层 git 的地基：`basic`、`layer_guard`、`user_layer` |
| `posts/` | 博文：`write`、`afterword_append_only`、`timeline`、`assets` |
| `insights/` | 条目：`backlinks` |
| `publish/` | 静态导出：`static_site` |
| `cli/` | `end_to_end` |
| `system/` | `boot` |

公共 fixture（`conftest.py`）：`home`（临时 `METABLOG_HOME`）、`client`（直连 ASGI 的 TestClient）、`svc`（`client.app.state`）。
