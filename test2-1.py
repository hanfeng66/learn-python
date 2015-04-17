# -*- coding:utf-8 -*-
#########学生基本信息############
#姓名:韩峰
#学号:1403050210
#班级：通风14-2班
###############题目###############
#物理题12.2 已知容器内P有某种理想气体，气温都和压强分别为 T=273K,P=1.0*10e2atm,密度rou=1.24*10e—2kg/m3.该气体的摩尔质量。
#解： p=ntk    （1）
#	 p=nm      （2）
#     M=mN4       (3)   由=以上二式联立得：
#	 M=PKT/NA=1.24*10e-2*1.38*10e-23*273/1.0*10e2*1.013*10e3*6.022*10e23=0,028kg/mol
	 
T=89
P=1.0e2
k=1.38e-23
rho=1.24e-2
N=1.0e2
A=6022e23
M=p*k*T/N*A
print 'M=PKT/NA=', M
