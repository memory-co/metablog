# metablog —— Python 包

pip 包 `metablog`，命令 `metablog`（也可 `python -m metablog`）。

| 目录 / 文件 | 是什么 |
|---|---|
| [`backend/`](backend/README.md) | FastAPI 服务：models / services / controllers 三层 + providers；`metablog server start` 起的就是它 |
| [`cli/`](cli/README.md) | 命令行：本地 API 的客户端，不含业务逻辑 |
| [`frontend/`](frontend/README.md) | React 前端；`npm run build` 出的 `dist/` 随包分发，由后端在 `/` 托管 |
| `__init__.py` | `__version__` |
| `__main__.py` | `python -m metablog` → `cli.main()` |
