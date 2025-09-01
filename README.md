# CUMCM-AI-Usage-Report

全国大学生数学建模竞赛AI工具使用详情 LaTeX 模板

## 项目简介

本项目是一个 LaTeX 模板，旨在帮助参加全国大学生数学建模竞赛的队伍规范、清晰地记录和展示其在研究过程中使用 AI 工具的详细情况。模板预设了多种交互场景，支持长内容自动分页，并可轻松定制，以满足竞赛报告的排版要求。

## 主要特点

- **可定制的AI模型环境**：在 `texfile/模型定义.tex` 中可轻松添加或修改AI模型及其图标、颜色、版本信息。
- **多种交互示例**：覆盖了从“简单问答”、“多轮追问”到“结构化长问答”等多种典型使用场景。
- **自动分页的长内容支持**：核心交互环境基于 `tcolorbox` 构建，并启用了 `breakable` 特性，确保提问或回答内容过长时能够优雅地跨页显示，而不会造成页面空白。
- **全局样式配置**：通过 `\tcbset` 在主文件 `AI工具使用详情.tex` 中统一设置对话框样式，便于一键更换整体风格。
- **清晰的结构**：将模型定义、各个使用说明模块化为独立文件，便于团队协作与内容管理。

## 主要内容结构

- `AI工具使用详情.tex`：主文档，负责整合所有模块并定义全局样式。
- `md_to_latex.py`：一个Python GUI工具，用于将Markdown格式的文本转换为LaTeX代码。
- `texfile/模型定义.tex`：参赛作品所用AI工具列表及对应的 `tcolorbox` 环境定义。
- `texfile/使用说明1.tex`：AI工具使用示例（简单问答）。
- `texfile/使用说明2.tex`：AI工具使用示例（包含追问的多轮交互）。
- `texfile/使用说明3.tex`：AI工具使用示例（结构化的长篇幅问答）。
- `icons/`：存放各AI工具的图标文件。

## Markdown to LaTeX 转换工具

为了方便将从AI工具复制的 Markdown 格式内容转换为 LaTeX，项目提供了一个基于 Python 的 GUI 工具 `md_to_latex.py`。

### 功能

- **图形化界面**：提供用户友好的窗口，包含 Markdown 输入和 LaTeX 输出区域。
- **文件导入**：支持打开 `.md` 文件并将其内容加载到输入区。
- **实时转换**：将输入的 Markdown 文本转换为 LaTeX 代码并实时显示。
- **代码导出**：可以将转换后的 LaTeX 代码保存为 `.tex` 文件。

### 使用方法

1.  **安装依赖**:
    -   **Pandoc**: 转换的核心工具。
        -   macOS (使用 Homebrew): `brew install pandoc`
        -   其他系统请参考 [pandoc 官网](https://pandoc.org/installing.html)。
    -   **pypandoc**: Python 对 pandoc 的封装。
        ```bash
        pip install pypandoc
        ```

2.  **运行工具**:
    ```bash
    python md_to_latex.py
    ```

## 参赛作品使用的AI工具列表

- ChatGPT (OpenAI)
- Kimi (月之暗面)
- DeepSeek (深度求索)
- Github Copilot (GitHub)
- Qwen (阿里巴巴通义千问)
- Claude (Anthropic)
- Gemini (Google DeepMind)

## 文档编译说明

- **编译器**：推荐使用 `XeLaTeX` 进行编译，以确保中文和图标的正确显示。
- **主要依赖包**：`xeCJK`、`graphicx`、`tcolorbox` (需 `breakable` 和 `skins` 库)、`amsthm`、`amsmath`、`amssymb` 等。
- **图片路径**：已通过 `\graphicspath` 设置，图标文件应放置在 `icons/` 目录下。

## 使用示例

文档中每个AI工具的使用场景均包含三个核心部分：

1. **用户提问**：使用带颜色的 `tcolorbox` 清晰展示用户向 AI 提出的问题。
2. **AI 回答**：在带有模型图标、名称和版本信息的 `tcolorbox` 中展示 AI 生成的回答。
3. **采纳和人工修改情况**：在另一个 `tcolorbox` 中总结回答的采纳程度以及进行了哪些人工修改或补充。

## 许可证

本项目采用 MIT License。
