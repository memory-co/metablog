# metablog/backend —— 服务层

metablog 的 FastAPI 服务。`cli/` 和 `frontend/` 都是它的客户端。

## 分层

```
controllers/   HTTP 面：路由、参数、响应信封；不含业务        → controllers/README.md
services/      业务：每个子包对应一篇设计，入口是 XxxService   → services/README.md
models/        数据形状：请求 / 响应体                         → models/README.md
providers/     存储介质原语：本地文件系统 + git                → providers/README.md
```

依赖只往下走：controllers → services → providers；models 谁都能用。service 之间不互相 import 内部模块，只通过构造函数注入。

## 装配

`main.py` 的 `create_app(config)`；`config.py` 的 `Config` 全部来自环境变量（`METABLOG_HOME`、git author），没有配置文件。v1 单人使用，没有登录。
