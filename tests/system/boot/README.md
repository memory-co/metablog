# system/boot —— 服务能起来，配置从环境变量来

## 这个场景在测什么
`create_app` 能装起一个 FastAPI 应用；`METABLOG_HOME` 决定数据根，`metas/` `layers/` `site/` 都在它下面。骨架阶段唯一真正跑的场景，保证 CI 至少收集到测试。

## 不在这测什么
- 分层 git → `metas/`
- 具体接口 → 各自场景

## fixture 来源
`home` / `client`。
