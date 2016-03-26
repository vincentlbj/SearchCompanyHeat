# encoding: utf-8
from bs4 import BeautifulSoup
import urllib2
import sys
import re
import random
import httplib
#设置多个user_agents，防止百度限制IP
user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0', \
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0', \
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \
    (KHTML, like Gecko) Element Browser 5.0', \
    'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)', \
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', \
    'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14', \
    'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \
    Version/6.0 Mobile/10A5355d Safari/8536.25', \
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/28.0.1468.0 Safari/537.36', \
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']

#通过关键字得到网页
def get_page(key_words):
	url = 'http://www.baidu.com/s?wd=' + key_words
	domain = urllib2.Request(url)
	r = random.randint(0,11)
	domain.add_header('User-agent', user_agents[r])
	page = urllib2.urlopen(url)
	return page

#解析网页，查找搜索次数
def search_nums(page):
	try:
		soup = BeautifulSoup(page, 'html.parser')
	except Exception as e:
		print (Exception,":",e) 
	print ('解析成功').decode('utf-8')
	tags = soup.find_all('div', attrs = {'class':'nums'})
	#提取数字
	num = re.findall(r'[,0-9]+',tags[0].get_text())[0].replace(',','')
	return int(num)

#主函数
def search_company(file_name):
	dict = {}
	for line in open(file_name):
		company = line.strip('\n')
		page = get_page(company)
		print ('获取'+company+'页面成功').decode('utf-8')
		dict[company] = search_nums(page)
	#进行从大到小排序
	list = sorted(dict.items(), lambda x, y: cmp(x[1], y[1]), reverse = True)
	for i in list:
		print(i[0]+'搜索次数为: '+str(i[1])).decode('utf-8')
		
#此两行代码据说可以解决IncompleteRead异常
httplib.HTTPConnection._http_vsn = 10 
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'

print('start,please wait')
search_company('company.txt')
print('search over')