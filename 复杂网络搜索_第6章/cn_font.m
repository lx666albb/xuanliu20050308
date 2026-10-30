function f = cn_font()
%CN_FONT  返回当前系统可用的中文字体名。
%   用于坐标轴标签，避免中文显示为方框。

if ispc
    f = 'SimSun';          % 宋体，Windows 默认自带
elseif ismac
    f = 'Songti SC';       % macOS 宋体
else
    f = 'Noto Sans CJK SC'; % Linux 常见中文字体
end

end
