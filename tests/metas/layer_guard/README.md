# metas/layer_guard —— 守卫：路径归哪层由后缀决定，跨层写被拒

## 这个场景在测什么
`[post]` 提交写 `x.insight/readme.md` 被拒；`[insight]` 提交改 `.post/` 里的文件被拒；任何层改 origin 已有的路径被拒。

## 不在这测什么
- 字段校验 → `posts/write`

## fixture 来源
`client` / `svc`。
