# CUMCM-AI-Usage-Report
全国大学生数学建模竞赛AI工具使用详情

## 项目简介
本项目用于展示全国大学生数学建模竞赛中参赛作品所用的AI工具及其具体使用过程，包含详细的工具列表、使用场景、采纳与人工修改情况等。

## 主要内容结构
- `AI工具使用详情.tex`：主文档，包含AI工具列表与详细使用说明。
- `texfile/模型定义.tex`：参赛作品所用AI工具列表及环境定义。
- `texfile/使用说明1.tex`：AI工具在基础数学问题中的使用示例（实数加法）。
- `texfile/使用说明2.tex`：AI工具在基础数学问题中的使用示例（虚数加法）。
- `icons/`：各AI工具图标文件。

## 参赛作品使用的AI工具列表
- ChatGPT（OpenAI）
- Kimi（月之暗面）
- DeepSeek（深度求索）
- Github Copilot（GitHub）
- Qwen
- Claude（Anthropic）
- Gemini（Google DeepMind）

## 文档编译说明
- 推荐使用 XeLaTeX 编译器进行编译，确保中文和图标正常显示。
- 主要依赖包：`xeCJK`、`graphicx`、`tcolorbox`、`amsthm`、`amsmath`、`amssymb` 等。
- 图片路径已设置为 `icons/`，无需额外配置。

## 使用示例
文档中每个AI工具的使用均包含：
- 用户提问
- AI工具自动生成的解答（带图标和模型信息）
- 采纳与人工修改情况说明

## 许可证
本项目采用 MIT License。
