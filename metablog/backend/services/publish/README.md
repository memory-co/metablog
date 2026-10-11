# services/publish

把 stack 里的 post / insight 渲染成静态站，写到 `~/.metablog/site/`（不进 git，可随时重建）。origin 默认不发布。

| 文件 | 是什么 |
|---|---|
| `service.py` | `PublishService` |
| `render.py` | Markdown → HTML |
| `feed.py` | RSS / Atom |
| `templates/` | 页面模板：首页、单篇、系列、标签、条目 |
