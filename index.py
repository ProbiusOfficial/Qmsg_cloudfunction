
# coding=utf-8

import io
import sys
import time
import datetime
import requests
import MsgSend
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

name = "Your_Name"
mail_port = 465

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

def getWeather():
    r = requests.get(
        'http://wthrcdn.etouch.cn/weather_mini?city=YourCity')
    if 'OK' in r.text:
        r = r.json()['data']
        tip = r['ganmao']
        temperature = r['wendu']
        weather = r['forecast'][0]['type']
        return f'天气：{weather} 当前温度：{temperature}\n{tip} '
    return '获取天气失败:('


def getTime():
    today = datetime.datetime.now()+datetime.timedelta(hours=+8)
    t = today.timetuple()
    return f'今天是{t.tm_year}年{t.tm_mon}月{t.tm_mday}日 星期{t.tm_wday+1} '

def getmorning():
    url='http://api.tianapi.com/txapi/zaoan/index?key=YourKey'
    r = requests.get(url)
    result=r.json()
    results=result['newslist']
    data1=results[0]
    content=data1['content']
    return content

  def getevening():
    url='http://api.tianapi.com/txapi/wanan/index?key=YourKey'
    r = requests.get(url)
    result=r.json()
    results=result['newslist']
    data1=results[0]
    content=data1['content']
    return content

def pom():
    url='https://v1.hitokoto.cn/?c=i'
    r = requests.get(url)
    result=r.json()
    results=result
    data1=results
    stttt=data1['hitokoto']
    from1=data1['from']
    str1=stttt+'\n'+"————"+from1
    return str1


def morning():
    return '\n'.join([f'嘿，{name}，早上好啊~！',getTime(),getWeather(),getmorning(),f'今日古诗：',pom(),f'今天也是充满希望的一天呢~~'])


def night():
    return '\n'.join([f'嘿，{name}，晚上好！',getevening(), f'(要早点睡哟~ヾ(✿ﾟ▽ﾟ)ノ)'])


def getTimeX():
    t = int(time.strftime("%H", time.localtime()))+8
    if t > 24:
        t = t-24
    return 'morning' if t < 11 else ('noon' if t < 20 else 'afterNoon')

def main_handler(event, context):
    content = night() if getTimeX() == 'afterNoon' else morning()
    try:
        sendSMS.postData("2293808331",content)
        logger.info("send message success")
    except:
        logger.info("Error: send message fail")
    logger.info(content)
    return content
