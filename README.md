## 起因

发现很多爆出的0day，在很早就有利用

如：用友nc的任意文件读取，早在乌云2015年就有了

http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-0148227

```
/NCFindWeb?service=IPreAlertConfigService&filename=../../../../../etc/passwd
```

![image-20220805161102650](/Users/conan/Desktop/wooyun/README.assets/image-20220805161102650.png)

诸如此类的还有很多0day都是组件，文件的历史漏洞，所以产生了爬取所有乌云漏洞url的想法

## 结果

根据镜像站爬的 http://wy.zone.ci/，很卡不太容易一步完成，分三步前前后后几天爬完的

这里放出来所有文件 方便师傅们进行其他操作和分析

1. 爬取所有wooyun漏洞编号
2. 根据编号正则匹配url
3. 处理url 获取路径
4. 最终人工筛查 生成了该字典