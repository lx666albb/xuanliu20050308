# -*- coding: utf-8 -*-
"""
习题 6.1—6.3：用 Python 复现图 6.7、6.8、6.9。

运行：
    python plot_ex6.py

依赖：numpy、matplotlib
输出：fig6_7.png、fig6_8.png、fig6_9.png（300 dpi）
      以及同名 PDF 文件。
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # 无界面运行，直接保存图片

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import (
    LogFormatterMathtext,
    LogLocator,
    NullFormatter,
)

BASE_DIR = Path(__file__).resolve().parent


# ---------------------------------------------------------------------------
# 全局样式
# ---------------------------------------------------------------------------
def pick_chinese_font() -> str:
    """返回当前系统可用的中文字体名。"""
    candidates = [
        "SimSun",              # Windows 宋体
        "Songti SC",           # macOS 宋体
        "Noto Sans CJK SC",    # Linux
        "Microsoft YaHei",     # Windows 微软雅黑
    ]
    for name in candidates:
        try:
            font_manager.findfont(name, fallback_to_default=False)
            return name
        except ValueError:
            continue
    return "DejaVu Sans"


CN_FONT = pick_chinese_font()

plt.rcParams.update(
    {
        "font.family": CN_FONT,
        "font.size": 12,
        "axes.unicode_minus": False,
        "mathtext.fontset": "stix",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "savefig.dpi": 300,
        "axes.linewidth": 0.9,
    }
)

try:
    font_manager.findfont("Times New Roman", fallback_to_default=False)
    LATIN = FontProperties(family="Times New Roman", size=11)
except ValueError:
    LATIN = FontProperties(family=CN_FONT, size=11)


def style_axes(ax, log_axis: bool = False) -> None:
    """统一的坐标轴风格：四边刻度朝内、细边框。"""
    ax.tick_params(
        axis="both",
        which="major",
        direction="in",
        top=True,
        right=True,
        length=5,
        width=0.8,
        labelsize=11,
    )
    ax.tick_params(
        axis="both",
        which="minor",
        direction="in",
        top=True,
        right=True,
        length=2.8,
        width=0.7,
    )
    for spine in ax.spines.values():
        spine.set_linewidth(0.9)

    if log_axis:
        ax.xaxis.set_major_locator(LogLocator(base=10.0, numticks=5))
        ax.yaxis.set_major_locator(LogLocator(base=10.0, numticks=6))
        ax.xaxis.set_major_formatter(LogFormatterMathtext(base=10.0))
        ax.yaxis.set_major_formatter(LogFormatterMathtext(base=10.0))
        ax.xaxis.set_minor_locator(
            LogLocator(base=10.0, subs=np.arange(2, 10) * 0.1, numticks=15)
        )
        ax.yaxis.set_minor_locator(
            LogLocator(base=10.0, subs=np.arange(2, 10) * 0.1, numticks=15)
        )
        ax.xaxis.set_minor_formatter(NullFormatter())
        ax.yaxis.set_minor_formatter(NullFormatter())


def style_legend(ax):
    leg = ax.legend(
        loc="upper right",
        frameon=True,
        fancybox=False,
        framealpha=1.0,
        edgecolor="black",
        borderpad=0.45,
        handlelength=2.6,
        handletextpad=0.6,
        labelspacing=0.35,
        prop=LATIN,
    )
    leg.get_frame().set_linewidth(0.8)
    return leg


def save(fig, stem: str) -> None:
    fig.savefig(BASE_DIR / f"{stem}.png", dpi=300, bbox_inches="tight")
    fig.savefig(BASE_DIR / f"{stem}.pdf", bbox_inches="tight")
    plt.close(fig)
    print(f"已生成 {stem}.png / {stem}.pdf")


# ---------------------------------------------------------------------------
# 图 6.7
# ---------------------------------------------------------------------------
def fig6_7() -> None:
    N = np.array([20, 50, 100, 200, 500], dtype=float)
    T_URW = np.array([2.4, 6.8, 23, 60, 130], dtype=float)
    T_NRRW = np.array([2.3, 6.5, 21, 56, 122], dtype=float)
    T_SARW = np.array([2.2, 6.0, 18, 48, 108], dtype=float)

    fig, ax = plt.subplots(figsize=(6.4, 4.8))

    common = dict(
        color="black",
        linewidth=1.1,
        markersize=6.5,
        markerfacecolor="white",
        markeredgecolor="black",
        markeredgewidth=0.9,
    )
    ax.loglog(N, T_URW, marker="s", label="URW", **common)
    ax.loglog(N, T_NRRW, marker="^", label="NRRW", **common)
    ax.loglog(N, T_SARW, marker="o", label="SARW", **common)

    ax.set_xlim(10, 1000)
    ax.set_ylim(1, 1000)
    style_axes(ax, log_axis=True)

    ax.set_xlabel(r"网络规模 $N$", fontsize=14, labelpad=6)
    ax.set_ylabel(r"平均搜索次数 $T$", fontsize=14, labelpad=6)
    ax.set_title(r"$k=5,\ p=0.2$", fontsize=13, pad=8)

    style_legend(ax)
    fig.subplots_adjust(left=0.14, right=0.96, bottom=0.15, top=0.90)
    save(fig, "fig6_7")


# ---------------------------------------------------------------------------
# 图 6.8
# ---------------------------------------------------------------------------
def fig6_8() -> None:
    p = np.array(
        [0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7],
        dtype=float,
    )

    T_URW_200 = np.array([2200, 1350, 950, 760, 600, 500, 330, 160, 90, 78, 72], dtype=float)
    T_NRRW_200 = np.array([1250, 800, 580, 450, 350, 280, 200, 100, 68, 60, 55], dtype=float)
    T_SARW_200 = np.array([550, 430, 340, 250, 200, 170, 100, 55, 40, 35, 32], dtype=float)

    T_URW_100 = np.array([600, 520, 400, 300, 220, 150, 120, 80, 45, 30, 28], dtype=float)
    T_NRRW_100 = np.array([330, 280, 220, 170, 120, 90, 70, 50, 32, 25, 23], dtype=float)
    T_SARW_100 = np.array([130, 115, 95, 80, 65, 50, 40, 28, 20, 17, 16], dtype=float)

    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.6))
    common = dict(
        color="black",
        linewidth=1.1,
        markersize=6.2,
        markerfacecolor="white",
        markeredgecolor="black",
        markeredgewidth=0.9,
    )

    for ax, n_label, urw, nrrw, sarw in [
        (axes[0], "200", T_URW_200, T_NRRW_200, T_SARW_200),
        (axes[1], "100", T_URW_100, T_NRRW_100, T_SARW_100),
    ]:
        ax.loglog(p, urw, marker="s", label="URW", **common)
        ax.loglog(p, nrrw, marker="^", label="NRRW", **common)
        ax.loglog(p, sarw, marker="o", label="SARW", **common)

        ax.set_xlim(1e-3, 1)
        ax.set_ylim(10, 1e4)
        style_axes(ax, log_axis=True)

        ax.set_xlabel(r"重连概率 $p$", fontsize=13, labelpad=5)
        ax.set_ylabel(r"平均搜索步数 $T$", fontsize=13, labelpad=6)
        ax.set_title(rf"网络规模 $N={n_label}$", fontsize=13, pad=6)
        style_legend(ax)

    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.88, wspace=0.27)
    save(fig, "fig6_8")


# ---------------------------------------------------------------------------
# 图 6.9
# ---------------------------------------------------------------------------
def fig6_9() -> None:
    N = np.array([20, 50, 80, 100, 150, 200, 300, 500], dtype=float)

    T_k1 = np.array([22, 48, 72, 90, 125, 210, 280, 525], dtype=float)
    T_k2 = np.array([16, 38, 55, 68, 82, 110, 130, 270], dtype=float)
    T_k4 = np.array([11, 23, 30, 38, 47, 58, 72, 128], dtype=float)
    T_k8 = np.array([7, 14, 20, 25, 32, 38, 48, 75], dtype=float)

    fig, ax = plt.subplots(figsize=(6.8, 5.2))
    common = dict(
        color="black",
        linewidth=1.1,
        markerfacecolor="white",
        markeredgecolor="black",
        markeredgewidth=0.9,
    )

    ax.plot(N, T_k1, marker="s", markersize=6.5, label="k=1", **common)
    ax.plot(N, T_k2, marker="^", markersize=6.5, label="k=2", **common)
    ax.plot(N, T_k4, marker="o", markersize=6.5, label="k=4", **common)
    ax.plot(N, T_k8, marker="*", markersize=10, label="k=8", **common)

    ax.set_xlim(0, 600)
    ax.set_ylim(0, 800)
    ax.set_xticks(np.arange(0, 601, 100))
    ax.set_yticks(np.arange(0, 801, 100))
    style_axes(ax, log_axis=False)

    ax.set_xlabel(r"网络规模 $N$", fontsize=14, labelpad=6)
    ax.set_ylabel(r"平均搜索步数 $T$", fontsize=14, labelpad=6)

    style_legend(ax)
    fig.subplots_adjust(left=0.14, right=0.96, bottom=0.14, top=0.96)
    save(fig, "fig6_9")


def main() -> None:
    print(f"使用中文字体：{CN_FONT}")
    fig6_7()
    fig6_8()
    fig6_9()
    print("全部完成。")


if __name__ == "__main__":
    main()
