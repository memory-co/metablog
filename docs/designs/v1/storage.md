# 存储

磁盘布局见 [structure/v1/filesystem.md](../../structure/v1/filesystem.md)。机制沿用 memory.talk 的 metas。

## 为什么用分层 git、没有数据库

- **内容就是文件**。Markdown + frontmatter，任何编辑器都能打开，不依赖 metablog 也能读。
- **历史免费**。博文的修订史、后记什么时候加的，全在 git log 里，不另存版本表。
- **备份免费**。`~/.metablog/metas/` 本身是 git 仓库，推到一个私有远端就是备份。
- **没有第二份真相**。没有数据库就没有「数据库和文件不一致」的问题。规模是一个人一辈子写的博客，几千篇，`git grep` 足够。

## 为什么分层

三层的规则不同（素材只读、后记只增、条目可删），混在一个分支上很难守住。分层后：

- 每层一条权威分支 `layer/<名>`，线性，只放这一层的文件。
- `stack` 分支是合并视图，每次层提交后一个 merge 节点，HEAD 指向它。读的时候只看 stack。
- 一层的提交碰不到别的层的文件（**层守卫**）：路径按后缀该归哪层，和声明的层不符即拒；路径已在别的层的树里即拒。

## 一个动作一个提交

每个写操作（加一份素材、改一篇博文、追加一篇后记、写一条条目）是一个提交，subject 以 `[层名]` 开头。这样 git log 本身就是一份可读的活动记录，「最近一次回看」之类的信息直接从 log 里算。

## 层协议

一层一份 YAML：对象目录名的正则、目录里每种文件的正则、字段（类型 / 枚举 / 引用 / 必填）、正文格式、模板、只增标记。内置层在 [`metablog/backend/services/metas/layers/`](../../../metablog/backend/services/metas/layers/README.md)，用户层写在 `~/.metablog/layers/<名>.yaml`，格式完全一样，启动时载入。

写入时按协议整批校验，不合协议整批拒，不会写进一半。

## 唯一写者

服务进程是仓库的唯一写者，CLI 和前端都通过本地 API 写。用户直接在 `metas/` 里手改文件会怎样，见 [open-questions.md](open-questions.md)。
