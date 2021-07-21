import requests
# qmsg get the key
host="https://qmsg.zendee.cn/send/24130fa4e009ee90f6bb4895c5357ab5"
#Module of push，need the QQ Num and The message you need push
def postData(qq,msg):
    data={
        'qq':"{}".format(qq),
        'msg':"{}".format(msg)
    }
    r = requests.post(host, data=data)
    return r
