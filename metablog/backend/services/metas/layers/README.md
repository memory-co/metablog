# metas/layers —— 内置层协议

一层一份 YAML：对象目录名的正则、目录里每种文件的正则、字段（类型 / 枚举 / 引用 / 必填）和正文。用户层写在 `~/.metablog/layers/<名>.yaml`，格式完全一样。

| 层 | 层序 | 对象 |
|---|---|---|
| `origin` | 0 | 不带后缀的任何文件 |
| `post` | 1 | `<标题>.post/`：`readme.md` + `assets/*` + `afterwords/<YYYY-MM-DD>.md` |
| `insight` | 2 | `<条目>.insight/readme.md` |
