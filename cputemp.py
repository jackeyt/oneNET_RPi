# -*- coding:utf-8 -*-
# File: cputemp.py
#��ƽ̨�Ѿ��������������������ݵ�
import urllib2
import json
import time
import datetime

APIKEY = 'xxxxxxxxxxx'  #�ĳ����APIKEY

def get_temp():
        # ���ļ� 
        file = open("/sys/class/thermal/thermal_zone0/temp") 
        # ��ȡ�������ת��Ϊ������ 
        temp = float(file.read()) / 1000 
        # �ر��ļ� 
        file.close() 
        # �����̨��ӡ��� 
        print "CPU���¶�ֵΪ: %.3f" %temp 
        # �����¶�ֵ
        return temp
        
        
def http_put():
    temperature = get_temp() #��ȡCPU�¶Ȳ��ϴ�
    CurTime = datetime.datetime.now()
    url='http://api.heclouds.com/devices/5494280/datapoints'
    values={'datastreams':[{"id":"temp","datapoints":[{"at":CurTime.isoformat(),"value":temperature}]}]}

    print "��ǰ��ISOʱ��Ϊ�� %s" %CurTime.isoformat()
    print "�ϴ����¶�ֵΪ: %.3f" %temperature

    jdata = json.dumps(values)                  # �����ݽ���JSON��ʽ������
    #��ӡjson����
    print jdata
    request = urllib2.Request(url, jdata)
    request.add_header('api-key', APIKEY)
    request.get_method = lambda:'POST'          # ����HTTP�ķ��ʷ�ʽ
    request = urllib2.urlopen(request)
    return request.read()

while True:
        time.sleep(5)
        resp = http_put()
        print "OneNET������:\n %s" %resp
        time.sleep(5)
