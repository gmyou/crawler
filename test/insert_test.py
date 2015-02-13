# -*- coding:utf-8 -*-
import re
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

soup = BeautifulSoup(open('../resource/KMug.html'))
# print (soup.prettify())

print len(soup.select('table.xectl tr.ctl_list1'))
print len(soup.select('table.xectl tr.ctl_list2'))
print len(soup.find_all('tr', attrs={"class": re.compile("^ctl_list")}))

lists = []
dic = {}
#for link in soup.select('table.xectl tr.ctl_list1'):
for link in soup.find_all('tr', attrs={"class": re.compile("^ctl_list")}):
    no = link.select('td.ctl_nb')
    print no[0].get_text()
    dic['no'] = no[0].get_text()
    
    sbj = link.select('td.ctl_sj')
    if (sbj):
        print sbj[0].select('a')[0].get_text()
        print sbj[0].select('a')[0]['href']
        print sbj[0].select('a')[0]['title']
        dic['subject'] = sbj[0].select('a')[0].get_text()
        dic['url'] = sbj[0].select('a')[0]['href']
        dic['content'] = sbj[0].select('a')[0]['title']
            
    name = link.select('td.ctl_name')
    print name[0].get_text()
    dic['name'] = name[0].get_text()
    
    hit = link.select('td.ctl_hit')
    print hit[0].get_text()
    dic['hit'] = hit[0].get_text()
    
    date = link.select('td.ctl_date')
    print date[0].get_text()
    dic['date'] = date[0].get_text()
    
    print
    
    lists.append(dict(dic))
    
for l in list(enumerate(lists)):
    print l
    sql = """INSERT INTO `openchannel`.`data`
    (`data_id`,
    `config_id`,
    `channel_id`,
    `no`,
    `subject`,
    `url`,
    `content`,
    `name`,
    `hit`,
    `date`)
    VALUES
    (<{data_id: }>,
    <{config_id: }>,
    <{channel_id: }>,
    <{no: }>,
    <{subject: }>,
    <{url: }>,
    <{content: }>,
    <{name: }>,
    <{hit: }>,
    <{date: }>);
    """
    print sql
