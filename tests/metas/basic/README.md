# metas/basic —— 分层 git 的最小闭环：三层各放一个对象，stack 看到全部

## 这个场景在测什么
origin 提交一份素材、post 提交一篇博文、insight 提交一个条目；`stack` 的树里三个都在，各层分支只有自己的那个。别的场景都建立在它成立之上。

## 不在这测什么
- 后缀规则 / 归属守卫 → `layer_guard`
- 博客视角的读 → `posts/`

## fixture 来源
`client` / `svc`。
