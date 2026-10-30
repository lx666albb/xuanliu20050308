# -*- coding: utf-8 -*-
"""
复现教材中的三幅搜索效率图：

    图 6.7  网络规模 N 与平均搜索步数 T 的关系图（k=5, p=0.2）
    图 6.8  平均搜索步数 T 对应于重新连接概率 p 的关系图（N=200 / N=100）
    图 6.9  k 遍历器搜索效率比较

说明
----
1. 图中的数据点是根据原始照片估读的，用于复现曲线形态；
   如果你有实验数据，直接替换下面 DATA 中对应的列表即可。
2. 运行脚本后，会在当前目录下的 figures/ 中生成三张 300 dpi 的 PNG。
3. 依赖：matplotlib、numpy。
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")           # 无显示器环境也能保存图片
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.ticker import FuncFormatter, LogLocator, MultipleLocator

BASE_DIR = Path(__file__).resolve().parent
OUT_DIR = BASE_DIR / "figures"

# ---------------------------------------------------------------------------
# 全局绘图风格
# ---------------------------------------------------------------------------
def setup_style() -> str:
    """选择可用的中文字体，并设置论文/教材风格的全局参数。"""
    candidates = [
        "SimSun",                 # Windows 宋体（最接近教材排版）
        "Songti SC",              # macOS 宋体
        "STSong",
        "Source Han Serif SC",
        "Noto Serif CJK SC",
        "SimHei",
        "Microsoft YaHei",
        "Noto Sans CJK SC",
        "WenQuanYi Zen Hei",
    ]
    available = {f.name for f in font_manager.fontManager.ttflist}
    chosen = next((name for name in candidates if name in available), "DejaVu Sans")
    if chosen == "DejaVu Sans":
        print("[WARN] 未找到中文字体，中文可能显示为方框；请安装 SimSun/Noto CJK 等字体。")

    plt.rcParams.update({
        "font.family": chosen,
        # 原书公式是 Times 风格的斜体；Computer Modern 与中文宋体搭配较协调
        "mathtext.fontset": "cm",
        "axes.unicode_minus": False,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.edgecolor": "black",
        "axes.linewidth": 1.2,
        "text.color": "black",
        "xtick.color": "black",
        "ytick.color": "black",
        "legend.edgecolor": "black",
        "savefig.facecolor": "white",
    })
    return chosen


def decade_formatter(value, _pos=None):
    """把 10^n 写成 $10^{n}$，避免 \\mathdefault 在宋体中缺负号。"""
    if value <= 0:
        return ""
    exponent = int(round(np.log10(value)))
    if np.isclose(value, 10.0 ** exponent, rtol=1e-8):
        return r"$10^{%d}$" % exponent
    return ""


def style_log_axes(ax, xlim, ylim):
    """统一设置双对数坐标轴的刻度、边框和刻度线方向。"""
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    for axis in (ax.xaxis, ax.yaxis):
        axis.set_major_locator(LogLocator(base=10, numticks=12))
        axis.set_minor_locator(
            LogLocator(base=10, subs=np.arange(2, 10) * 0.1, numticks=120)
        )
        axis.set_major_formatter(FuncFormatter(decade_formatter))

    ax.tick_params(which="major", direction="in", top=True, right=True,
                   length=6, width=1.0, labelsize=12.5, pad=6)
    ax.tick_params(which="minor", direction="in", top=True, right=True,
                   length=3, width=0.8)
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)


def style_linear_axes(ax, xlim, ylim, step=100):
    """图 6.9 使用的线性坐标轴。"""
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.xaxis.set_major_locator(MultipleLocator(step))
    ax.yaxis.set_major_locator(MultipleLocator(step))
    ax.tick_params(which="major", direction="in", top=True, right=True,
                   length=6, width=1.0, labelsize=12.5, pad=6)
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)


def add_legend(ax, loc="upper right"):
    leg = ax.legend(
        loc=loc,
        frameon=True,
        fancybox=False,
        framealpha=1.0,
        edgecolor="black",
        fontsize=12.5,
        handlelength=2.6,
        handletextpad=0.5,
        borderpad=0.55,
        labelspacing=0.35,
    )
    leg.get_frame().set_linewidth(1.0)
    return leg


def add_caption(fig, text, y=0.035):
    fig.text(0.5, y, text, ha="center", va="center", fontsize=12.5)


# ---------------------------------------------------------------------------
# 数据（按原图估读）
# ---------------------------------------------------------------------------
DATA = {
    # 图 6.7：N = 20, 50, 100, 200, 300, 500
    "6.7": {
        "N": [20, 50, 100, 200, 300, 500],
        "URW":  [2.4, 8.0, 21, 40, 70, 129],
        "NRRW": [2.2, 7.0, 18, 35, 62, 115],
        "SARW": [2.0, 5.8, 14, 28, 49, 88],
    },
    # 图 6.8 左：N = 200
    "6.8_left": {
        "p":    [0.001, 0.005, 0.01, 0.02, 0.03, 0.05,
                 0.1, 0.2, 0.3, 0.5, 0.7, 1.0],
        "URW":  [2500, 1250, 950, 600, 570, 330,
                 200, 130, 95, 85, 80, 78],
        "NRRW": [1300, 850, 520, 400, 380, 230,
                 150, 105, 70, 60, 58, 55],
        "SARW": [600, 430, 330, 240, 230, 140,
                 95, 60, 45, 40, 38, 38],
    },
    # 图 6.8 右：N = 100
    "6.8_right": {
        "p":    [0.001, 0.005, 0.01, 0.02, 0.03, 0.05,
                 0.1, 0.2, 0.3, 0.4, 0.5],
        "URW":  [600, 500, 300, 250, 130, 145,
                 80, 50, 43, 39, 37],
        "NRRW": [330, 280, 190, 180, 90, 95,
                 60, 40, 26, 24, 23],
        "SARW": [130, 100, 80, 75, 45, 47,
                 32, 22, 18, 17, 17],
    },
    # 图 6.9
    "6.9": {
        "N":  [50, 70, 80, 100, 120, 150, 200, 300, 500],
        "k=1": [38, 60, 75, 95, 108, 130, 205, 275, 525],
        "k=2": [22, 32, 38, 45, 48, 65, 100, 135, 265],
        "k=4": [12, 17, 20, 24, 27, 32, 55, 72, 130],
        "k=8": [8, 11, 13, 15, 18, 22, 26, 38, 72],
    },
}

METHOD_STYLES = {
    "URW":  {"marker": "s", "label": "URW"},
    "NRRW": {"marker": "^", "label": "NRRW"},
    "SARW": {"marker": "o", "label": "SARW"},
}


# ---------------------------------------------------------------------------
# 图 6.7
# ---------------------------------------------------------------------------
def make_fig_6_7():
    d = DATA["6.7"]
    fig = plt.figure(figsize=(6.7, 5.8))
    ax = fig.add_axes([0.155, 0.205, 0.79, 0.68])

    style_log_axes(ax, xlim=(1e1, 1e3), ylim=(1e0, 3e3))
    for method, cfg in METHOD_STYLES.items():
        ax.plot(d["N"], d[method], color="black", lw=1.4,
                marker=cfg["marker"], markersize=8.0,
                markerfacecolor="none", markeredgecolor="black",
                markeredgewidth=1.4, label=cfg["label"], clip_on=False)

    ax.set_xlabel(r"网络规模 $N$", fontsize=15, labelpad=6)
    ax.set_ylabel(r"平均搜索次数 $T$", fontsize=15, labelpad=8)
    ax.set_title(r"$k=5,\ p=0.2$", fontsize=14, pad=14)
    add_legend(ax, "upper right")

    add_caption(
        fig,
        r"图 6.7  网络规模 $N$ 与平均搜索步数 $T$ 的关系图（$k=5,\ p=0.2$）",
        y=0.045,
    )
    out = OUT_DIR / "fig6_7_N_vs_T.png"
    fig.savefig(out, dpi=300)
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
# 图 6.8
# ---------------------------------------------------------------------------
def make_fig_6_8():
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 6.4))
    fig.subplots_adjust(left=0.07, right=0.985, top=0.875, bottom=0.19,
                        wspace=0.26)

    panels = [
        (axes[0], DATA["6.8_left"], 200),
        (axes[1], DATA["6.8_right"], 100),
    ]
    for ax, d, n in panels:
        style_log_axes(ax, xlim=(1e-3, 1e0), ylim=(1e1, 1e4))
        for method, cfg in METHOD_STYLES.items():
            ax.plot(d["p"], d[method], color="black", lw=1.4,
                    marker=cfg["marker"], markersize=7.5,
                    markerfacecolor="none", markeredgecolor="black",
                    markeredgewidth=1.4, label=cfg["label"], clip_on=False)

        ax.set_xlabel(r"重连概率 $p$", fontsize=14.5, labelpad=6)
        ax.set_ylabel(r"平均搜索步数 $T$", fontsize=14.5, labelpad=8)
        ax.set_title(rf"网络规模 $N={n}$", fontsize=14, pad=10)
        add_legend(ax, "upper right")

    add_caption(
        fig,
        r"图 6.8  平均搜索步数 $T$ 对应于重新连接概率 $p$ 的关系图",
        y=0.045,
    )
    out = OUT_DIR / "fig6_8_T_vs_p.png"
    fig.savefig(out, dpi=300)
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
# 图 6.9
# ---------------------------------------------------------------------------
def make_fig_6_9():
    d = DATA["6.9"]
    fig = plt.figure(figsize=(6.5, 6.1))
    ax = fig.add_axes([0.16, 0.20, 0.79, 0.74])

    style_linear_axes(ax, xlim=(0, 600), ylim=(0, 800), step=100)
    series = [
        ("k=1", "s", r"$k$=1"),
        ("k=2", "^", r"$k$=2"),
        ("k=4", "o", r"$k$=4"),
        ("k=8", "*", r"$k$=8"),
    ]
    for key, marker, label in series:
        ax.plot(d["N"], d[key], color="black", lw=1.4,
                marker=marker, markersize=9 if marker == "*" else 8,
                markerfacecolor="none", markeredgecolor="black",
                markeredgewidth=1.3, label=label, clip_on=False)

    ax.set_xlabel(r"网络规模 $N$", fontsize=15, labelpad=6)
    ax.set_ylabel(r"平均搜索步数 $T$", fontsize=15, labelpad=8)
    add_legend(ax, "upper right")

    add_caption(fig, r"图 6.9  $k$ 遍历器搜索效率比较", y=0.045)
    out = OUT_DIR / "fig6_9_k_walker.png"
    fig.savefig(out, dpi=300)
    plt.close(fig)
    return out


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    font = setup_style()
    print(f"[OK] font: {font}")
    outputs = [make_fig_6_7(), make_fig_6_8(), make_fig_6_9()]
    for path in outputs:
        print(f"[OK] saved: {path}")


if __name__ == "__main__":
    main()
