import psycopg2

class Databases():
    def __init__(self):
        try: 
            self.db = psycopg2.connect(host='localhost', dbname='testdb',user='postgres',password='password',port=5432)
            self.cursor = self.db.cursor()
        except Exception as e :
            print('연결실패 왤까',e)
    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self,query,args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()