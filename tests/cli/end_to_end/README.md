# cli/end_to_end —— CLI 端到端：从收素材到发布

## 这个场景在测什么
`origin add` → `post new` → `post afterword` → `insight write` → `publish`，每步的输出和仓库状态正确。

## 不在这测什么
- 各命令的边界情况 → 对应服务层场景

## fixture 来源
`client` / `svc`。
