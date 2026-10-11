# posts/write —— 新建 / 修改博文；frontmatter 不合协议整批拒

## 这个场景在测什么
缺 `date` → 422；`kind` 不在枚举里 → 422；`sources` 指向不存在的 origin → 422；合法的写成一个 `[post]` 提交。

## 不在这测什么
- 后记 → `afterword_append_only`

## fixture 来源
`client` / `svc`。
