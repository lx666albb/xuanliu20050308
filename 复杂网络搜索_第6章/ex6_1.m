function ex6_1
%EX6_1  习题 6.1：绘制图 6.7
%   网络规模 N 与平均搜索步数 T 的关系（K=5, p=0.2）。
%   三条曲线分别对应 URW、NRRW、SARW 三种随机游走搜索策略。
%
%   运行环境：MATLAB R2016b 或更高版本。
%   输出：fig6_7.png（300 dpi）和 fig6_7.fig。

% ---------- 1. 数据 ----------
% 数据点按教材图 6.7 中的标记读取（双对数坐标）。
N      = [20,   50,   100,  200,  500];
T_URW  = [2.4,  6.8,  23,   60,   130];
T_NRRW = [2.3,  6.5,  21,   56,   122];
T_SARW = [2.2,  6.0,  18,   48,   108];

% ---------- 2. 画图 ----------
fig = figure('Color', 'w', 'Position', [100, 100, 720, 540]);
ax  = axes('Parent', fig);
hold(ax, 'on');
box(ax, 'on');

h1 = loglog(ax, N, T_URW,  '-s', 'Color', 'k', 'LineWidth', 1.2, ...
    'MarkerSize', 7, 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'w');
h2 = loglog(ax, N, T_NRRW, '-^', 'Color', 'k', 'LineWidth', 1.2, ...
    'MarkerSize', 7, 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'w');
h3 = loglog(ax, N, T_SARW, '-o', 'Color', 'k', 'LineWidth', 1.2, ...
    'MarkerSize', 7, 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'w');

% ---------- 3. 坐标轴与标注 ----------
set(ax, 'XScale', 'log', 'YScale', 'log', ...
    'XLim', [10, 1000], 'YLim', [1, 1000], ...
    'XTick', [10, 100, 1000], 'YTick', [1, 10, 100, 1000], ...
    'XMinorTick', 'on', 'YMinorTick', 'on', ...
    'TickDir', 'in', 'TickLength', [0.015, 0.015], ...
    'LineWidth', 1, 'FontName', 'Times New Roman', 'FontSize', 12);

cnFont = cn_font();
xlabel(ax, '网络规模 N', 'FontName', cnFont, 'FontSize', 14);
ylabel(ax, '平均搜索次数 T', 'FontName', cnFont, 'FontSize', 14);
title(ax, 'k=5, p=0.2', 'FontName', 'Times New Roman', ...
    'FontSize', 14, 'FontWeight', 'normal');

lgd = legend([h1, h2, h3], {'URW', 'NRRW', 'SARW'}, ...
    'Location', 'northeast');
set(lgd, 'FontName', 'Times New Roman', 'FontSize', 12, 'Box', 'on');

% ---------- 4. 导出 ----------
set(fig, 'PaperPositionMode', 'auto');
print(fig, 'fig6_7.png', '-dpng', '-r300');
savefig(fig, 'fig6_7.fig');

end
