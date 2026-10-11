# posts/assets —— 图片跟着博文目录走

## 这个场景在测什么
`assets/` 下的二进制文件随 `[post]` 提交；博文改名（目录移动）后图片跟着走。

## 不在这测什么
- 渲染时的图片路径 → `publish/static_site`

## fixture 来源
`client` / `svc`。
