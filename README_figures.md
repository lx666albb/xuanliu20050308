# 图 6.7 / 6.8 / 6.9 的 Python 复现

用 Matplotlib 复现教材第 107 页附近的三幅搜索效率图：

| 图号 | 内容 | 输出文件 |
| --- | --- | --- |
| 图 6.7 | 网络规模 \(N\) 与平均搜索步数 \(T\) 的关系（\(k=5,\ p=0.2\)） | `figures/fig6_7_N_vs_T.png` |
| 图 6.8 | 平均搜索步数 \(T\) 与重连概率 \(p\) 的关系（\(N=200\)、\(N=100\)） | `figures/fig6_8_T_vs_p.png` |
| 图 6.9 | \(k\) 遍历器搜索效率比较（\(k=1,2,4,8\)） | `figures/fig6_9_k_walker.png` |

## 运行

```bash
python -m pip install matplotlib numpy
python generate_figures.py
```

脚本会在当前目录下创建 `figures/`，并生成三张 300 dpi 的 PNG。

## 数据说明

教材只给了曲线图，没有附原始数据表。`generate_figures.py` 中 `DATA` 的数组是**按原图标记点估读**的，用于复现曲线形态：

- 图 6.7：\(N=20,50,100,200,300,500\)，三条曲线分别为 URW / NRRW / SARW；
- 图 6.8：左图 \(N=200\)、右图 \(N=100\)，横坐标为 \(p\)；
- 图 6.9：\(N=50,70,80,100,120,150,200,300,500\)，四条曲线对应 \(k=1,2,4,8\)。

如果已有仿真数据，直接替换 `DATA` 中对应列表即可，绘图与排版代码不需要改动。

## 实现要点

- 图 6.7、6.8 使用双对数坐标，图 6.9 使用线性坐标；
- 四边刻度朝内，并打开对数坐标的次刻度；
- 黑色实线 + 空心标记，图例带方框；
- 中文使用宋体（Windows 的 `SimSun`，macOS 的 `Songti SC` 等），公式使用 Computer Modern；
- 自定义了 \(10^n\) 刻度格式器，避免宋体缺少 Unicode 负号（U+2212）时出现方框；
- 每幅图底部带教材风格的图题，如不需要可删除对应的 `add_caption(...)` 调用。

## 字体

脚本会自动从系统字体中选择：

`SimSun` → `Songti SC` → `STSong` → `Source Han Serif SC` → `Noto Serif CJK SC` → `SimHei` → `Microsoft YaHei` → `Noto Sans CJK SC` → `WenQuanYi Zen Hei`

如果系统没有中文字体，脚本会打印警告；此时中文可能显示为方框，安装任一中文字体后重新运行即可。
