# publish/static_site —— 导出的静态站里有该有的东西

## 这个场景在测什么
`metablog publish` 后 `site/` 有首页、每篇博文页（含后记）、系列页、标签页、条目页和 `feed.xml`；origin 不出现。

## 不在这测什么
- 前端交互 → 不在 pytest

## fixture 来源
`client` / `svc`。
