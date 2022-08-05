

import requests
import re
from bs4 import BeautifulSoup

txtfile = open('111.txt')
for line in txtfile:
    url = "http://wy.zone.ci/bug_detail.php?wybug_id="+line.replace('\n','')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36'}
    req = requests.get(url, headers=headers)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    reqqq = soup.get_text()
    jg = re.findall(r"(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]",reqqq)
    # print(jg)
    # [{"md5mix":"c4ca4238a0b923820dcc509a6f75849b","passwd":"1"}]
    logwt = open('漏洞url.txt', 'a', encoding='utf8')
    for jjjggg in jg:
        logwt.write(str(jjjggg) + '\n')
    print("写入成功"+line)
logwt.close()
print("完成")












print("-----------------")
print("运行结束")



