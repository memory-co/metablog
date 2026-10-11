# services/posts

博客视角：时间线（按 `date` 降序）、系列（= 所在目录）、标签聚合、后记追加。写落成 `[post]` 提交。

| 文件 | 是什么 |
|---|---|
| `service.py` | `PostService` |
| `timeline.py` | 扫 stack 树里的 `.post/`，读 frontmatter，排序 / 过滤 |
| `afterword.py` | 追加后记；同一天已有则拒（只增不改） |
