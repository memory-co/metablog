# Metas (v1)

层、对象、字段的完整定义。字段以 [`metablog/backend/services/metas/layers/*.yaml`](../../../metablog/backend/services/metas/layers/README.md) 为准，这里跟着它改；示例见 [`examples/metas/`](../../../examples/metas/)。整体定位见 [designs/v1/main.md](../../designs/v1/main.md)；这里还是三层旧模型，等定位定下来再对齐。

## 层

| 层 | 层序 | 对象形态 |
|---|---|---|
| `origin` | 0（最底） | 任何不带层后缀的文件 |
| `post` | 1 | `<标题>.post/` 目录 |
| `insight` | 2 | `<条目>.insight/` 目录 |

层序记在仓库根的 `metas.json`：`{"version": 1, "layers": [{"name": "origin", "builtin": true}, …]}`，最底在前。用户层追加在后面。

## origin

任何不带层后缀的文件，任意格式，原样保存。没有字段。

## post：`<标题>.post/`

| 文件 | 必须 | 说明 |
|---|---|---|
| `readme.md` | 是 | frontmatter + Markdown 正文 |
| `assets/<文件名>` | 否 | 本篇的图片等附件，二进制 |
| `afterwords/<YYYY-MM-DD>.md` | 否 | 后记，Markdown 正文，**只增** |

`readme.md` 的字段：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `date` | date | 是 | 发表日；时间线按它排 |
| `kind` | enum：复盘 / 方法 / 觉察 / 提问 | 否 | 元认知的类型 |
| `tags` | list of string | 否 | 横向聚合 |
| `summary` | string | 否 | 一句话；列表页和 RSS 用 |
| `sources` | list of ref origin | 否 | 基于哪些素材 |
| `links` | list of ref post | 否 | 相关博文 |

新建时的正文模板：

```markdown
## 发生了什么

## 我当时怎么想的

## 现在怎么看

## 下次怎么做
```

## insight：`<条目>.insight/`

| 文件 | 必须 | 说明 |
|---|---|---|
| `readme.md` | 是 | frontmatter + Markdown 正文 |

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `context` | string | 否 | 在什么情境下成立 |
| `posts` | list of ref post | 否 | 出自哪些博文 |
| `links` | list of ref insight | 否 | 相关条目 |

## 引用的写法

引用是仓库内相对路径，**不带层后缀**：`学习/我为什么总是高估自己读懂了` 指 `学习/我为什么总是高估自己读懂了.post/`。origin 没有后缀，所以写完整文件名：`学习/2026-10-03 读《思考，快与慢》第3章摘录.md`。读时容忍悬挂。
