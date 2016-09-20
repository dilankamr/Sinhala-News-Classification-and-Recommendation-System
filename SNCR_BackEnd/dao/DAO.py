from mysql.connector import (connection)

class DAO:

    def _connect(self):
        self.con = connection.MySQLConnection(user='root', password='ilovepera',
                                    host='127.0.0.1',
                                    database='NewsData',
                                    charset='utf8')
        return

    def _get_cursor(self):
        """
        Pings connection and returns cursor
        """
        try:
            self.con.ping()
        except:
            self._connect()
        return self.con.cursor()

    def createTable(self):

        cursor = self._get_cursor()
        # Drop table if it already exist using execute() method.
        cursor.execute("DROP TABLE IF EXISTS NewsOrder")

        # Create table as per requirement
        sql = """CREATE TABLE NewsOrder (ID int NOT NULL AUTO_INCREMENT,
                        title  VARCHAR(1000), link  VARCHAR(1000), description VARCHAR(1000), pubDate VARCHAR(1000), category VARCHAR(10), newsSite VARCHAR (80)) ENGINE = InnoDB DEFAULT CHARSET=utf8"""
        cursor.execute(sql)

    def getHotNews(self):
        cursor = self._get_cursor()
        sql = "select * from NewsOrder"
        cursor.execute(sql)
        newsList = cursor.fetchall()
        cursor.close()

        return newsList

    def getDefenseAndLawNews(self):
        cursor = self._get_cursor()
        sql = "select * from NewsOrder where category='defence'"
        cursor.execute(sql)
        newsList = cursor.fetchall()
        cursor.close()

        return newsList

    def getNews(self , category):
        cursor = self._get_cursor()
        sql = "select * from NewsOrder where category="+"'"+category+"'"
        print sql
        cursor.execute(sql)
        newsList = cursor.fetchall()
        cursor.close()

        return newsList


    def insertNews(self,title,link,description,imgLink,category,newsId,newsSite):
        cursor = self._get_cursor()
        sql = """INSERT INTO NewsOrder(title,link,description,imgLink,category,newsId, newsSite) VALUES ('%s','%s','%s','%s','%s','%s','%s') """ %(title, link, description, imgLink, category,newsId,newsSite)

        cursor.execute(sql)
        self.con.commit()




