#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import wifi
import mytime
import mysocket
import getlp
import getlum
import time
from machine import unique_id
host = '123.206.37.27'
port = 9000
wifi.do_connect()
socket = mysocket.MySocket(host, port)
time_stamp = mytime.MyTime().time_stamp
lum = getlum.GetLum().get_value
lp = getlp.GetLp().get_value
id = unique_id()

def send_message():
    i = 0
    while True:
        i += 1
        data = {
            'Lp': lp(),
            'lum': lum(),
            'time': time_stamp()
        }
        if data['Lp'] is False or data['lum'] is False:
            time.sleep(1)
            continue
        print('检测时间：')
        print('第'+ str(i) +'次测量, 噪声为' + str(data['Lp']) + 'dB, 光照为' + str(data['lum']) + 'lx')
        time.sleep(1)
