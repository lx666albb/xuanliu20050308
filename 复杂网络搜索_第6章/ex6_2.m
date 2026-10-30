function ex6_2
%EX6_2  习题 6.2：绘制图 6.8
%   平均搜索步数 T 与重连概率 p 的关系（双对数坐标）。
%   左图 N=200，右图 N=100；每种网络规模下比较 URW、NRRW、SARW。
%
%   运行环境：MATLAB R2016b 或更高版本。
%   输出：fig6_8.png（300 dpi）和 fig6_8.fig。

% ---------- 1. 数据 ----------
p = [0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7];

% 网络规模 N = 200
T_URW_200  = [2200, 1350, 950, 760, 600, 500, 330, 160, 90, 78, 72];
T_NRRW_200 = [1250,  800, 580, 450, 350, 280, 200, 100, 68, 60, 55];
T_SARW_200 = [ 550,  430, 340, 250, 200, 170, 100,  55, 40, 35, 32];

% 网络规模 N = 100
T_URW_100  = [600, 520, 400, 300, 220, 150, 120, 80, 45, 30, 28];
T_NRRW_100 = [330, 280, 220, 170, 120,  90,  70, 50, 32, 25, 23];
T_SARW_100 = [130, 115,  95,  80,  65,  50,  40, 28, 20, 17, 16];

cnFont = cn_font();

% ---------- 2. 左图：N = 200 ----------
fig = figure('Color', 'w', 'Position', [80, 80, 1120, 460]);

ax1 = subplot(1, 2, 1);
hold(ax1, 'on');
box(ax1, 'on');

h1 = loglog(ax1, p, T_URW_200,  '-s', 'Color', 'k', 'LineWidth', 1.2, ...
    'MarkerSize', 7, 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'w');
h2 = loglog(ax1, p, T_NRRW_200, '-^', 'Color', 'k', 'LineWidth', 1.2, ...
    'MarkerSize', 7, 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'w');
h3 = loglog(ax1, p, T_SARW_200, '-o', 'Color', 'k', 'LineWidth', 1.2, ...
    'MarkerSize', 7, 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'w');

set(ax1, 'XScale', 'log', 'YScale', 'log', ...
    'XLim', [1e-3, 1], 'YLim', [10, 1e4], ...
    'XTick', [1e-3, 1e-2, 1e-1, 1], 'YTick', [10, 100, 1000, 10000], ...
    'XMinorTick', 'on', 'YMinorTick', 'on', ...
    'TickDir', 'in', 'TickLength', [0.015, 0.015], ...
    'LineWidth', 1, 'FontName', 'Times New Roman', 'FontSize', 11);

xlabel(ax1, '重连概率 p', 'FontName', cnFont, 'FontSize', 13);
ylabel(ax1, '平均搜索步数 T', 'FontName', cnFont, 'FontSize', 13);
title(ax1, '网络规模 N=200', 'FontName', cnFont, 'FontSize', 13, ...
    'FontWeight', 'normal');

lgd1 = legend([h1, h2, h3], {'URW', 'NRRW', 'SARW'}, ...
    'Location', 'northeast');
set(lgd1, 'FontName', 'Times New Roman', 'FontSize', 11, 'Box', 'on');

% ---------- 3. 右图：N = 100 ----------
ax2 = subplot(1, 2, 2);
hold(ax2, 'on');
box(ax2, 'on');

h4 = loglog(ax2, p, T_URW_100,  '-s', 'Color', 'k', 'LineWidth', 1.2, ...
    'MarkerSize', 7, 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'w');
h5 = loglog(ax2, p, T_NRRW_100, '-^', 'Color', 'k', 'LineWidth', 1.2, ...
    'MarkerSize', 7, 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'w');
h6 = loglog(ax2, p, T_SARW_100, '-o', 'Color', 'k', 'LineWidth', 1.2, ...
    'MarkerSize', 7, 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'w');

set(ax2, 'XScale', 'log', 'YScale', 'log', ...
    'XLim', [1e-3, 1], 'YLim', [10, 1e4], ...
    'XTick', [1e-3, 1e-2, 1e-1, 1], 'YTick', [10, 100, 1000, 10000], ...
    'XMinorTick', 'on', 'YMinorTick', 'on', ...
    'TickDir', 'in', 'TickLength', [0.015, 0.015], ...
    'LineWidth', 1, 'FontName', 'Times New Roman', 'FontSize', 11);

xlabel(ax2, '重连概率 p', 'FontName', cnFont, 'FontSize', 13);
ylabel(ax2, '平均搜索步数 T', 'FontName', cnFont, 'FontSize', 13);
title(ax2, '网络规模 N=100', 'FontName', cnFont, 'FontSize', 13, ...
    'FontWeight', 'normal');

lgd2 = legend([h4, h5, h6], {'URW', 'NRRW', 'SARW'}, ...
    'Location', 'northeast');
set(lgd2, 'FontName', 'Times New Roman', 'FontSize', 11, 'Box', 'on');

% 两个子图留出合适边距
set(ax1, 'Position', [0.07, 0.15, 0.38, 0.72]);
set(ax2, 'Position', [0.56, 0.15, 0.38, 0.72]);

% ---------- 4. 导出 ----------
set(fig, 'PaperPositionMode', 'auto');
print(fig, 'fig6_8.png', '-dpng', '-r300');
savefig(fig, 'fig6_8.fig');

end
