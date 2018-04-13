import requests,urllib.parse
import re,json,time
import ssl,urllib.request
#ssl用来处理ssl连接问题的
# ssl._create_default_https_context = ssl._create_stdlib_context
source_url = 'https://tieba.baidu.com/index.html'
#添加headers，模拟登录效果
headers ={
    'Cookie':'BIDUPSID=379083FF488A6A35EAF292E8E9133BB3; PSTM=1482216697; TIEBA_USERTYPE=edaa8f2916c1036781e780ca; bdshare_firstime=1489480235692; FP_LASTTIME=1509676133813; BAIDUID=90FD4ABF076D1EDBEE96935D72ED9845:FG=1; MCITY=-179%3A; TIEBAUID=d8c56c89f3e58a1581484795; 959457984_FRSVideoUploadTip=1; FP_UID=0feb862f27308a1dae42bac369304d08; BDUSS=TlsYnlVQThXRkxLVVF6UEhzNjRHOWJkVzVLQVZiQm9HYWlzVEItcG9uS1N5fmRhQVFBQUFBJCQAAAAAAAAAAAEAAADAKjA5TWVyZFJlYWQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJI-0FqSPtBaV; STOKEN=e194337ef92d493e996c5f973e2d973dcaac2a74781e64c9b3e2cb234e7d62f2; showCardBeforeSign=1; rpln_guide=1; BDRCVFR[BkUmQAfVpsD]=mk3SLVN4HKm; PSINO=5; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; wise_device=0; Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1523586334,1523590544,1523590844,1523602586; Hm_lpvt_287705c8d9e2073d13275b18dbd746dc=1523602586; BDRCVFR[KKxQ_aGZ5eD]=yiTPYW-i3eTXZFWmv68mvqV; H_PS_PSSID=; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1523597175,1523600384,1523602585,1523602615; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1523602617',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

#签到函数,签到时，都会提交到一组数据到sign_url上，现在只需将数据中所需要的参数替换成我们要签到的参数即可
def signAdd(kw,tbs_data):
    sign_url = 'url =http://tieba.baidu.com/sign/add'
    post_data = {
        "ie": "utf-8",
        "kw": kw,
        "tbs": tbs_data,
    }
    data = urllib.parse.urlencode(post_data).encode('utf-8')
    post_req = requests.get(sign_url, data=data, headers=headers)
    try:
        return [kw,json.loads(post_req.text)['data']['errmsg']]
    except:
        return (kw,'faild')

#获取页面源码，获取贴吧id和名称，并将数据进行解析，模拟post提交
r = requests.get(source_url,headers=headers)
infolist = re.findall('"forum_id":(.*?),"forum_name":"(.*?)"',r.text)
for info in infolist:
    kw=info[1].encode('utf-8').decode('unicode_escape')
    forum_url = 'http://tieba.baidu.com/f?kw='+urllib.parse.quote(kw)
    time.sleep(2)
    tie = requests.get(forum_url)
    tbs_data = re.findall('\'tbs\': "(.*?)"',tie.text)[0]
    time.sleep(2)
    print('-'.join(signAdd(kw,tbs_data)))




