# insights/backlinks —— 条目反查到引用它的博文

## 这个场景在测什么
条目的 `posts[]` 列了两篇博文；读条目时两篇都在反查结果里；删掉一篇后读时容忍悬挂。

## 不在这测什么
- 条目字段校验 → 和 `posts/write` 同一套协议机制

## fixture 来源
`client` / `svc`。
