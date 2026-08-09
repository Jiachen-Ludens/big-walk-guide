# Big Walk Guide SEO Setup

目标：让 Google 收录 https://jiachen-ludens.github.io/big-walk-guide/ 并接入统计与广告。

## 1. Google Search Console

1. 打开 https://search.google.com/search-console ，添加资源：
   - 属性类型选 "网址前缀"。
   - 输入 `https://jiachen-ludens.github.io/big-walk-guide/`。
2. 验证方式选 "HTML 文件" 或 "HTML 标签"：
   - 把 Google 给的文件放到仓库根目录并 push；或把 meta 标签加入每个页面的 `<head>`。
3. 提交 Sitemap：
   - 在项目根目录创建 `sitemap.xml`，列出全部 15 个页面 URL，push 后到 GSC 提交。
4. 请求索引：在 GSC "网址检查" 输入首页和主要内页，点 "请求编入索引"。

## 2. Google Analytics (GA4)

1. 打开 https://analytics.google.com ，创建 GA4 媒体资源。
2. 数据流选 "Web"，URL 填线上地址，生成测量 ID（格式 `G-XXXXXXX`）。
3. 把 GA4 脚本（含测量 ID）插入每个页面的 `</head>` 前，然后 push。
4. 用 GA4 的 Realtime 报告验证访问。

## 3. Adsterra / AdSense

1. 注册 Adsterra 或 Google AdSense（需可访问站点、有内容、遵守平台政策）。
2. 拿到广告位代码后，放到页面布局中（建议不遮挡正文）。
3. 不要在站点上线早期就放置大量广告；先验证收录与流量。

> 本文件只提供步骤，不代注册任何账号。GA/广告代码请在上线后按需接入。
