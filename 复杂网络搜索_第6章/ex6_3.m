function ex6_3
%EX6_3  习题 6.3：绘制图 6.9
%   k 遍历器（k 个并行随机游走者）搜索效率比较。
%   横轴为网络规模 N，纵轴为平均搜索步数 T；k = 1, 2, 4, 8。
%
%   运行环境：MATLAB R2016b 或更高版本。
%   输出：fig6_9.png（300 dpi）和 fig6_9.fig。

% ---------- 1. 数据 ----------
N  = [20, 50, 80, 100, 150, 200, 300, 500];

T_k1 = [ 22,  48,  72,  90, 125, 210, 280, 525];
T_k2 = [ 16,  38,  55,  68,  82, 110, 130, 270];
T_k4 = [ 11,  23,  30,  38,  47,  58,  72, 128];
T_k8 = [  7,  14,  20,  25,  32,  38,  48,  75];

% ---------- 2. 画图 ----------
fig = figure('Color', 'w', 'Position', [100, 100, 760, 560]);
ax  = axes('Parent', fig);
hold(ax, 'on');
box(ax, 'on');

h1 = plot(ax, N, T_k1, '-s', 'Color', 'k', 'LineWidth', 1.2, ...
    'MarkerSize', 7, 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'w');
h2 = plot(ax, N, T_k2, '-^', 'Color', 'k', 'LineWidth', 1.2, ...
    'MarkerSize', 7, 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'w');
h3 = plot(ax, N, T_k4, '-o', 'Color', 'k', 'LineWidth', 1.2, ...
    'MarkerSize', 7, 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'w');
h4 = plot(ax, N, T_k8, '-p', 'Color', 'k', 'LineWidth', 1.2, ...
    'MarkerSize', 9, 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'w');

% ---------- 3. 坐标轴与标注 ----------
set(ax, 'XLim', [0, 600], 'YLim', [0, 800], ...
    'XTick', 0:100:600, 'YTick', 0:100:800, ...
    'TickDir', 'in', 'TickLength', [0.015, 0.015], ...
    'LineWidth', 1, 'FontName', 'Times New Roman', 'FontSize', 12);

cnFont = cn_font();
xlabel(ax, '网络规模 N', 'FontName', cnFont, 'FontSize', 14);
ylabel(ax, '平均搜索步数 T', 'FontName', cnFont, 'FontSize', 14);

lgd = legend([h1, h2, h3, h4], {'k=1', 'k=2', 'k=4', 'k=8'}, ...
    'Location', 'northeast');
set(lgd, 'FontName', 'Times New Roman', 'FontSize', 12, 'Box', 'on');

% ---------- 4. 导出 ----------
set(fig, 'PaperPositionMode', 'auto');
print(fig, 'fig6_9.png', '-dpng', '-r300');
savefig(fig, 'fig6_9.fig');

end
