clc
tic
% FileChange.py后的数字表示时间步增量，
% 请根据ProCAST时间步的长短自己输入一个正整数。
! python FileChange.py 3
! python ReadElem.py
disp("文件转换文成！")
toc
! python Add2Inp.py
disp("inp文件写入完成!")
disp("开始ABAQUS仿真!")
! abaqus job=job
