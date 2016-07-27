from mysql.connector import (connection)

class DAO:

    def _connect(self):
        self.con = connection.MySQLConnection(user='root', password='1234',
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
        sql = """CREATE TABLE NewsOrder (
                        title  VARCHAR(1000), link  VARCHAR(1000), description VARCHAR(1000), pubDate VARCHAR(1000), category VARCHAR(10)) ENGINE = InnoDB DEFAULT CHARSET=utf8"""
        cursor.execute(sql)

    def getHotNews(self):
        cursor = self._get_cursor()
        sql = "select * from NewsOrder"
        cursor.execute(sql)
        newsList = cursor.fetchall()
        cursor.close()

        return newsList



