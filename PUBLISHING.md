# 发布说明

这个仓库更适合公开“方法”和 “skill”，不适合公开你的个人求职资料。

## 建议公开

- `project-skill/`
- `README.md`
- `PUBLISHING.md`
- `LICENSE`
- 脱敏后的示例

## 不建议公开

- `profile/`
- `output/`
- 原始抓取数据
- 简历 PDF
- 私人 Excel
- 个人分析报告

## 推送前检查

先运行：

```powershell
git status --short
```

确认没有这些内容：

- 登录态
- 原始数据
- 简历
- 私人表格

## 最推荐的结构

- `公开仓库`
  - 放 skill、文档、示例
- `私有仓库或本地项目`
  - 放实际运行数据、登录态、个人材料
