# 复杂网络搜索与随机过程学习记录

本仓库收录两部分内容：

1. **《复杂网络搜索》第 6 章习题**（图 6.7 / 6.8 / 6.9）的 MATLAB 与 Python 复现代码；
2. **《应用随机过程》** 的备考计划、知识清单与每日学习记录（Markdown / LaTeX 源文件及排版好的 PDF）。

## 目录结构

```
├── generate_figures.py            # 图 6.7/6.8/6.9 的 Python 复现（输出到 figures/）
├── README_figures.md              # 上述脚本的说明
├── figures/                       # 脚本生成的 300 dpi PNG
├── 复杂网络搜索_第6章/             # MATLAB 版本：ex6_1.m / ex6_2.m / ex6_3.m
├── 复杂网络搜索_第6章_python/       # Python 版本：plot_ex6.py 及其输出
├── 应用随机过程/                   # 备考计划、知识清单、每日学习（D001、D002…）
└── 习题6_MATLAB程序.zip            # 原始习题打包
```

## 环境要求

- Python 3.9 及以上，依赖见 `requirements.txt`：

```bash
python -m pip install -r requirements.txt
```

- 运行 MATLAB 部分需要 MATLAB R2016b 或更高版本（使用了 `string` 与隐式扩展）。
- 绘图需要系统中文字体（Windows 的 SimSun、macOS 的 Songti SC 等），否则中文会显示为方框。

## 运行方式

```bash
# Python：在仓库根目录运行，结果输出到 figures/
python generate_figures.py

# Python 习题版：结果输出到该目录
cd 复杂网络搜索_第6章_python
python plot_ex6.py
```

MATLAB：在 `复杂网络搜索_第6章` 目录下执行 `run_all`，或单独运行 `ex6_1` / `ex6_2` / `ex6_3`。

## 数据说明

教材只给出曲线图，未附原始数据表。脚本中的数组是按原图标记点**估读**的，目的是复现曲线形态；
若有仿真数据，替换源码中对应的数据列表即可，绘图代码无需改动。

## 关于 PDF

`应用随机过程/` 下的 PDF 是由同目录的 `.tex` / `.md` 源文件排版生成的成果物；
`复杂网络搜索_第6章_python/` 下的 PNG / PDF 是 `plot_ex6.py` 的输出。
修改源文件后重新运行或重新排版即可覆盖更新。
