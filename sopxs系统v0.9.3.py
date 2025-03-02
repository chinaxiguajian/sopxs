#sopxs系统
#初始化
from selenium import webdriver
from random import randint
import time
import subprocess
import pygame
sop_a = bool(False);
sop_b = bool(False);
sop_c = bool(False);
def stop(a_a_a):
    print('关机中……23%');
    time.sleep(a_a_a);
    print('关机中……59%');
    time.sleep(0.5)
    print('关机中……99%');
    time.sleep(2);
    print('已关机');
    input('点击回车键继续……');
#初始化、开机BL
sf_kj = bool(False);
kj_bl = bool(False);
#软件脚本BL
rjbl_suijishu = bool(False);
rjbl_time = bool(False);
rjbl_wj_a = bool(False);
rjbl_wj_b = bool(False);
rjbl_wj_c = bool(False);
rjbl_wj_d = bool(False);
rjbl_wj_e = bool(False);
sopxs_Help = ['刷新','联网','选择/打开','关机'];
HelP_2 = ['刷新系统','连接网络（不是真正的联网）','打开文件或软件','关闭系统,更多命令请打开“sopxs(v0.9.5.0) command copy UI.py”'];
#bq a mm
asx_a = input('密码？：');
if asx_a == 'wgh1wangguanghua1234wgh246t2736427463723':
    pass;
else:
    while asx_a != 'wgh1wangguanghua1234wgh246t2736427463723':
        print('密码不对，请重新输入');
        asx_a = input('密码？：');

print('密码正确！');
sf_kj = bool(True);
i_a = input('是否开机？：');
if i_a == '是':
    kj_bl = bool(True);
if kj_bl == True:
    #开机代码
    for i in range(101):
        print('开机中',i,'%');
        time.sleep(0.03);
    for ia in range(101):
        print('系统初始化中……',ia,'%');
        time.sleep(0.09);
    print('欢迎来到sopxs系统!');
    for i in range(5):
        print('');
    while True:
        w_sp = input();
        if w_sp == '刷新':
            print('系统已刷新');
        elif w_sp == '联网':
            print('联网中 23 %');
            time.sleep(0.7);
            print('联网中 89 %');
            print('已联网');
        elif w_sp == '选择/打开':
            i_b = input('选择：C/:zmSOPXS/;')
            if i_b == '随机数':
                rjbl_suijishu = bool(True);
                print('已打开',i_b);
            if i_b == '闹钟':
                i_c = input('时间(s):');
                for i in range(int(i_c)):
                    time.sleep(1);
                    print('')
                print('时间到了。');
            if i_b == '年':
                time_a = time.time();
                time_a = time_a / (600*6*24*365);
                time_a = time_a - 30;
                print('20' , time_a , '年');
            if i_b == '浏览器':
                print('常用网址：');
                print('1.https://www.baidu.com 百度');
                print('2.https://www.taobao.com/ 淘宝');
                print('3.https://www.jd.com/ 京东');
                print('4.https://www.bilibili.com/ b站');
                print('5.https://github.com/ Github(非国内网站)');
                https_wz = input('网址(请加上"https://")：')
                driver = webdriver.Chrome();
                driver.get(https_wz);
                print('网站已打开');
            if i_b == '资源管理器':
                i_d = input('选择：(盘)/：');
                if i_d == 'C':
                    i_d_a = input('选择：C/:');
                    if i_d_a == 'SOPXS':
                        print('你没有此权限！');
                    elif i_d_a == 'Help' or i_d_a == '帮助':
                        print('请联系开发者');
                    elif i_d_a == 'help.txt':
                        for ax in range(4):
                            print(sopxs_Help[ax],HelP_2[ax]);
                        print('>>>');
                    elif w_sp == '关机':
            break
        elif w_sp == '系统命令帮助':
            for ax in range(4):
                print(sopxs_Help[ax],HelP_2[ax]);
        elif w_sp == '安装扩展插件应用sopXseerror_exe_eerror.exe':
            inp_a = input('该应用存在风险，是否安装？：')
            if inp_a == '是' or inp_a == 'yes':
                print('安装中50%');
                time.sleep(2);
                print('安装成功！');
                print('运行中');
                print('eerror!');
                time.sleep(1);
                for i in range(66):
                    commands = "color 4"
                    subprocess.Popen(f'start cmd /k {commands}', shell=True)
            else:
                print('取消成功！');
        else:
            print('指令错误');
        if rjbl_suijishu == True:
            rg_sjs_a = int(input('数量：'));
            rg_sjs_b = int(input('范围（最小）：'));
            rg_sjs_c = int(input('范围（最大）：'));
            for i in range(rg_sjs_a):
                rg_sjs_d = randint(rg_sjs_b,rg_sjs_c);
                print(rg_sjs_d);
            rjbl_suijishu = bool(False);
stop(0.6);
