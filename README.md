#爬虫入门之爬取百度搜索次数
##简介
###由于学校举办了实习生招聘会，但是太多的公司让人眼花缭乱，所以萌生了写一个爬虫到百度上查询公司名字搜索次数来查看公司热度的想法
##环境配置
###Python语言，BeautifulSou扩展
##使用说明
###1.新建一个company.txt，包含所有要搜索的关键词，每个占一行。
####例如存放内容如下：
```中山益达服装有限公司
广州银联网络支付有限公司
广州速游网络科技有限公司
中国人民人寿保险股份有限公司广东省分公司广州营业部
广东今科道同科技有限公司
南京华苏科技股份有限公司
广东南方数码科技股份有限公司
蓝鸥科技有限公司广州分公司
广东凯通软件开发有限公司
广州华南教育科技发展有限公司
联讯证券股份有限公司
高新兴科技集团股份有限公司
广州讯猫软件有限公司
```
###2.将search.py下载下来，与company.txt放在同一个目录下，命令行方式使用方法如下:
```python
python search.py
```
##存在问题
###可能出现卡住的现象或者跳出python原生库httplib的异常IncompleteRead，这个异常出现不固定，目前并不知道如何解决