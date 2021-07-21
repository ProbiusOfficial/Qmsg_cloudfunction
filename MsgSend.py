import requests
# qmsg get the key
host="https://qmsg.zendee.cn/send/Your_Key"
#Module of push，need the QQ Num and The message you need push
def postData(qq,msg):
    data={
        'qq':"{}".format(qq),
        'msg':"{}".format(msg)
    }
    r = requests.post(host, data=data)
    return r
