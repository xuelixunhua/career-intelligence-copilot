# Career Intelligence Copilot

一个用于 `岗位抓取 + 市场分析 + 简历反推 + 企业筛选` 的 Codex 项目级 skill。

这个仓库不是传统的固定脚本爬虫，而是把求职研究做成一条可复用的工作流。

## 适合做什么

- 抓取真实岗位并维护主数据集
- 每周持续更新市场变化
- 只基于真实岗位样本分析市场
- 反推简历怎么改、该补什么项目经验
- 对企业做结构化排序，而不是拍脑袋选公司

## 核心特点

- `浏览器优先`
  - 适合需要登录、动态渲染、反爬较强的招聘网站
- `真实岗位优先`
  - 简历建议和企业排序尽量来自真实样本，而不是泛泛建议
- `可持续更新`
  - 适合按周增量维护，而不是一次性跑完
- `可迁移`
  - 电力交易只是示例，也可以迁移到别的岗位方向

## 仓库结构

```text
career-intelligence-copilot/
├── README.md
├── PUBLISHING.md
├── LICENSE
├── .gitignore
├── examples/
│   └── power-trading-case.md
└── project-skill/
    └── career-intelligence-copilot/
        ├── README.md
        ├── SKILL.md
        └── references/
```

## 怎么用

把 `project-skill/career-intelligence-copilot/` 放进你的项目里，然后在 Codex 中直接提出类似任务：

```text
请用 career-intelligence-copilot 这个 skill，
更新最新岗位数据，并同步刷新市场分析和企业排序。
```

```text
请基于最新真实岗位样本，反推我的简历应该怎么改，
以及下一阶段最该补什么经验。
```

## 当前示例

仓库里带了一个电力交易方向的示例：

- Boss / 猎聘岗位抓取
- 主数据集去重
- 市场分析
- 企业排序
- 简历反推

示例见 `examples/power-trading-case.md`。

## 公开仓库建议

建议公开：

- skill 本体
- 规则文档
- 示例说明

不建议公开：

- 浏览器登录态
- 原始抓取数据
- 个人简历
- 私人 Excel / 报告

更详细的发布建议见 `PUBLISHING.md`。
