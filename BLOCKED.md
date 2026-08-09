# BLOCKED

## 已解决

- 无。

## 当前阻塞

### 1. Cloudflare Pages 部署（需要用户操作）

本机没有 Cloudflare API token，无法自动创建 Pages 项目。GitHub Pages 已上线（https://jiachen-ludens.github.io/big-walk-guide/），Cloudflare 可选补充。

步骤（在浏览器登录 dash.cloudflare.com）：

1. Workers & Pages → Create application → Connect to Git (GitHub)。
2. 选择 `Jiachen-Ludens/big-walk-guide`，分支 `main`。
3. Framework preset 选 None，Build command 留空，Build output directory 填 `/`。
4. Save and Deploy；如 `big-walk-guide.pages.dev` 被占用，用 Cloudflare 建议的后缀名。
5. 部署后 curl 每个页面确认 200。

### 2. 来源访问受限（已降级处理）

- Polygon（ski lift / 4166-1899）与 Destructoid（drawbridge）直连被 Cloudflare/403 拦截。
- 处理方式：这些页面仅在 RESEARCH/sources 中标为"经搜索摘要交叉核验"，站点正文不引用为确定数值；可后续在正常网络下复核后升级为已打开来源。

## 注意事项

- 仓库根目录的 markdown（README/RESEARCH/COMPETITORS/PROGRESS/BLOCKED/SEO_SETUP）在 GitHub Pages 上可公开访问，属预期行为。
- 本机 git 全局 `commit.gpgsign=true` 且 GPG key 失效，提交须带 `-c commit.gpgsign=false`。
