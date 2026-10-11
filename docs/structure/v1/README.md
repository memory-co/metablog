# Structure (v1)

v1 的数据模型：对象 schema、字段语义、磁盘布局。**是什么**；为什么见 [`../../designs/v1/`](../../designs/v1/README.md)。

## 对象清单

| 对象 | 形态 | 存哪 | 文档 |
|---|---|---|---|
| origin | 不带后缀的任何文件，原文 | `metas/` 任意路径 | [metas.md](metas.md) |
| post | `<标题>.post/`：`readme.md`（字段 date / kind / tags / summary / sources / links + 正文）、`assets/`、`afterwords/<日期>.md` | `metas/` | [metas.md](metas.md) |
| insight | `<条目>.insight/readme.md`（字段 context / posts / links + 正文） | `metas/` | [metas.md](metas.md) |

## ID

全部是**仓库内相对路径**（不含后缀），目录即分类，像维基的词条名：`学习/我为什么总是高估自己读懂了`。

## 互相引用

```
post    ──(sources)──▶ origin
post    ──(links)────▶ post
insight ──(posts)────▶ post        ← 条目记博文；博文不记条目
insight ──(links)────▶ insight
```

全部是裸 path 引用，读时容忍悬挂。

## 不变性

| 对象 | 能不能改 | 历史在哪 |
|---|---|---|
| origin | 只增（原样保存） | git log |
| post 正文 / 字段 | 能改、能删 | git log |
| post 后记 | **只增不改不删** | git log |
| insight | 能改、能删 | git log |
