# 发布

## 形态

`metablog publish` 把选中的内容渲染成静态 HTML + RSS / Atom + 站点地图，输出到 `~/.metablog/site/`。产物不进 git，随时可以删掉重建。放到哪托管（GitHub Pages、自己的服务器）是用户的事。

## 默认不公开

元认知很私人：写「我哪里想错了」时，如果心里想着读者，就会不自觉地往好看了写。所以：

- **默认什么都不发**。
- 逐篇选择公开。表达方式见 [open-questions.md](open-questions.md)（建议在博文上加一个 `publish` 字段）。

## 发什么、不发什么

| 内容 | 发不发 | 理由 |
|---|---|---|
| 选中公开的博文正文 | 发 | |
| 这些博文的后记 | 发，附在文末，带日期 | 看法的变化是博文的一部分 |
| 这些博文的 `assets/` | 发 | |
| 素材（origin） | **不发** | 原样的对话、摘录，可能涉及别人或版权 |
| 博文里指向素材的 `sources` | 不发链接 | 同上 |
| 指向未公开博文的 `links` | 去掉链接，保留文字 | 不泄露未公开博文的存在 |
| 条目（insight） | 待定 | 见 [open-questions.md](open-questions.md) |

## 不做什么

在线评论、访问统计、多主题市场。模板在 [`metablog/backend/services/publish/templates/`](../../../metablog/backend/services/publish/README.md)，先只有一套。
