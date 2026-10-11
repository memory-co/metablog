# Filesystem (v1)

```
~/.metablog/                      ← METABLOG_HOME
├── metas/                        ← 分层 git 仓库
│   ├── .git/                     ←   refs/heads/layer/{origin,post,insight,…}、refs/heads/stack；HEAD → stack
│   ├── metas.json                ←   始祖提交里唯一的文件：layers[]（最底在前）
│   └── <按主题组织的目录树>/      ←   原文、.post/、.insight/ 并排
├── layers/                       ← 用户自定义层：<名>.yaml
└── site/                         ← metablog publish 的产物，不进 git
```

## 环境变量

| 变量 | 默认 | 说明 |
|---|---|---|
| `METABLOG_HOME` | `~/.metablog` | 数据根 |
| `METABLOG_AUTHOR` / `METABLOG_EMAIL` | `metablog` / `metablog@localhost` | 提交的 author |
| `METABLOG_URL` | `http://127.0.0.1:8100` | CLI 连哪个服务 |
