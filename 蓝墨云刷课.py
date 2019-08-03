import requests
import re
def login():
    url1="https://www.mosoteach.cn/web/index.php?c=passport&m=account_login"#登陆的链接
    head1={#这个是数据头
        "Host":"www.mosoteach.cn",
        "Content-Length":"60",
        "Connection": "keep-alive",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Origin": "https://www.mosoteach.cn",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://www.mosoteach.cn/web/index.php?c=passport",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
}
    username=input("请输入账号：")
    password=input("请输入密码：")
    body="account_name={0}&user_pwd={1}&remember_me=N".format(username,password)#数据包
    result1=requests.post(url1,headers=head1,data=body)#发送请求，并将结果赋给result1
    cookie=result1.headers["Set-Cookie"]#提取cookie，在下一次发送请求的时候带上这个cookie，服务器才会认识你
#除了上面这个，还要提取aliyungf_tc，teachweb，SERVERID，不要问我为什么提取，他返回给你的数据肯定是有用的，提取保存就行，提取用到了正则表达式
    print("获取如下参数")
    aliyungf_tc=re.findall(r"aliyungf_tc=(.*?);",cookie)
    aliyungf_tc=aliyungf_tc[0]
    print("aliyungf_tc=%s"%aliyungf_tc)
    teachweb=re.findall(r"teachweb=(.*?);",cookie)
    teachweb=teachweb[0]
    print("teachweb=%s"%teachweb)
    Ser=re.findall(r"SERVERID=(.*?);",cookie)
    Ser=Ser[0]
    print("serverid=%s"%Ser)
    url2 = "https://www.mosoteach.cn/web/index.php?c=clazzcourse&m=index"
    head2 = {
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Origin": "https://www.mosoteach.cn",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Referer": "https://www.mosoteach.cn/web/index.php?c=passport",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cookie": "aliyungf_tc={};teachweb={};SERVERID={}".format(aliyungf_tc, teachweb, Ser)
    }
    result2 = requests.post(url=url2, headers=head2)
    classid = re.findall("data-id=\"(.*)\"", result2.text)
    print("成功获取科目ID：%s" % classid)
    classid = input("请输入你要刷的科目ID：")
    head3 = {
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Origin": "https://www.mosoteach.cn",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cookie": "aliyungf_tc={0};teachweb={1};SERVERID={2}".format(aliyungf_tc, teachweb, Ser),
        "Refere": "https://www.mosoteach.cn/web/index.php?c=interaction&m=index&clazz_course_id={}".format(classid)
    }

    url3 = "https://www.mosoteach.cn/web/index.php?c=res&m=index&clazz_course_id={}".format(classid.replace("'", ""))
    result3 = requests.get(url3, headers=head3)
    viedoid = re.findall("data-value=\"(.*)\"", result3.text)  # 这是用正则表达式提取资源id
    url4 = "https://www.mosoteach.cn/web/index.php?c=res&m=save_watch_to"
    i = list(range(1, len(viedoid), 1))
    # print(i)
    for k in i:
        if len(viedoid[k]) == len(viedoid[1]):  # 检测所提取的视频id长度是不是等于第一个视频的id长度，因为在提取的过程中后面有几个不是视频id，得把它去掉
            head4 = {
                "Connection": "close",
                "Content-Length": "141",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Referer": "https://www.mosoteach.cn/web/index.php?c=res&m=index&clazz_course_id={}".format(classid),
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Origin": "https://www.mosoteach.cn",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Cookie": "aliyungf_tc={0};teachweb={1};SERVERID={2}".format(aliyungf_tc, teachweb, Ser)
            }
            data4 = "clazz_course_id={}&res_id={}&watch_to=1200&duration=1200¤t_watch_to=0".format(classid, viedoid[
                k])  # 这里的watch_to和duration要设置的大一些，如果设置小了，有些视频长度大于这个数值，你就会看不完
            result4 = requests.post(url4, headers=head4, data=data4).json()
            print("视频%s的结果为:%s" % (viedoid[k], result4))
        else:
            pass


login()