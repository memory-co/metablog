# posts/afterword_append_only —— 后记只增不改

## 这个场景在测什么
追加 `afterwords/<日期>.md` 成功；再改它或删它被拒；同一天第二篇被拒。

## 不在这测什么
- 正文修改 → `write`

## fixture 来源
`client` / `svc`。
