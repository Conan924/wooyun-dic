import requests
import re


def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
  file = open(filename,'a')
  for i in range(len(data)):
    s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
    s = s.replace("'",'').replace(',','') +'\n'  #去除单引号，逗号，每行末尾追加换行符
    file.write(s)
  file.close()
  print("保存文件成功")

pattern = re.compile(r"wooyun-2\d{3}-\d{7}")

for a in range(911,2962):
    burp0_url = "http://wy.zone.ci:80/bugs.php?page="+str(a)  # 2961页
    burp0_headers = {"Upgrade-Insecure-Requests": "1",
                     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                     "Referer": "http://wy.zone.ci/bugs.php", "Accept-Encoding": "gzip, deflate",
                     "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    req = requests.get(burp0_url, headers=burp0_headers)
    result = pattern.findall(req.text)
    text_save('id.txt', result)
    print('page='+str(a))






