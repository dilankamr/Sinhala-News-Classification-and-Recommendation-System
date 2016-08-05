from future_builtins import ascii

import feedparser
import re
import urllib2 as urllib2

from bs4 import BeautifulSoup
# from mysql import (connection)
from mysql.connector import (connection)
from SNCR_BackEnd.Aggregator.DAO import *

class newsUpdater:

    def job(self, link, newsContentClassName, imageClassName):
        db = connection.MySQLConnection(user='root', password='1234',
                                        host='127.0.0.1',
                                        database='NewsData',
                                        charset='utf8')

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        print("Scheduler is running.......")
        feed = feedparser.parse(link)
        for entry in feed['items']:

            length=len(entry['link'].split('/'))

            sql1="SELECT * FROM NewsOrder WHERE newsId >= '%s'"%(entry['link'].split('/')[length-1])
            cursor.execute(sql1)
            result=cursor.fetchall()
            if len(result)==0:
                length = len(entry['link'].split('/'))
                # converting title into a url
                title = entry['title'].replace(" ", "")
                asci = ascii(title)
                asci = asci[1:].replace("'", "")
                urlTitle = asci.replace("\\", "%")
                url = entry['link'] + '/' + urlTitle
                content = urllib2.Request(url)
                res = urllib2.urlopen(content).read()
                try:
                    soup = BeautifulSoup(res, "html.parser")
                except:
                    print "Error"
                imageRows = soup.find_all('div', attrs={"class": imageClassName})
                imageDetails = re.findall('"([^"]*)"', str(imageRows))

                newsContentRows = soup.find_all('div', attrs={"class": newsContentClassName})
                dao = DAO()
                print 'inside if condition'
                dao.insertNews(entry['title'], entry['link'], entry['description'].split('<a')[0], imageDetails[2], 'null',entry['link'].split('/')[length - 1])

                print entry['title']

            else:
                print 'No new news'

