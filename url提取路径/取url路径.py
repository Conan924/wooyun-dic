def qzj(y, q, h, k=0):
    wzq = y.find(q, k)
    wzh = y.find(h, wzq + len(q))
    if wzq != -1 and wzh != -1:
        return y[wzq + len(q):wzh]
    else:
        return ''

def qyb(y, z):
    if y.find(z) != -1:
        return y[y.rfind(z) + len(z):len(y)]
    else:
        return ''

txtfile = open('去重.txt')
for line in txtfile:
    url = line.replace('\n','')
    host = qzj(url, "//", "/")
    jg = qyb(url, host)
    logwt = open('路径.txt', 'a', encoding='utf8')
    logwt.write(str(jg) + '\n')
    print("写入成功"+host)
logwt.close()
print("完成")