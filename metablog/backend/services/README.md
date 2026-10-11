# backend/services —— 业务

| 子包 | 入口 | 管什么 | 设计 |
|---|---|---|---|
| [`metas/`](metas/README.md) | `MetasService` | 分层 git 引擎：层协议、守卫、提交、读树 / 历史 | [designs storage.md](../../../docs/designs/v1/storage.md) |
| [`posts/`](posts/README.md) | `PostService` | 博客视角的读写：时间线、系列、标签、后记 | [designs content.md](../../../docs/designs/v1/content.md) |
| [`insights/`](insights/README.md) | `InsightService` | 元认知条目；反查引用它的博文 | [designs content.md](../../../docs/designs/v1/content.md) |
| [`search/`](search/README.md) | `SearchService` | `git grep` stack | — |
| [`publish/`](publish/README.md) | `PublishService` | 导出静态站、RSS / Atom、站点地图 | [designs publish.md](../../../docs/designs/v1/publish.md) |

posts / insights 只是 metas 之上的视角：写都落成 metas 的一次层提交，读都是读 stack 的树再按博客的需要排序 / 聚合。
