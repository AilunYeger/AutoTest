import os
import pymysql
from logger import logger
from sourceLoad import data


# 获取mysql配置
path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'config/setting.ini')
mysql = data.loadIni(path)['MYSQL']
DB_CONF = {
    'host': mysql['MYSQL_HOST'],
    'port': int(mysql['MYSQL_PORT']),
    'user': mysql['MYSQL_USER'],
    'password': mysql['MYSQL_PASSWD'],
    'db': mysql['MYSQL_DB']
}
class MysqlOperator():
    def __init__(self):
        # 连接数据库
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        # 创建游标对象,查询结果以字典格式输出
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):  # 释放资源时关闭连接
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def select_db(self, sql):
        """查询"""
        # 检查连接状态，断开则重连
        self.conn.ping(reconnect=True)
        # 执行sql
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def execute_db(self, sql):
        """增、删、改"""
        # 检查连接状态，断开则重连
        self.conn.ping(reconnect=True)
        # 执行sql
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info(f"数据库更新失败，失败原因:{e}")
            self.conn.rollback()

db = MysqlOperator()

if __name__ == '__main__':
    create_table = 'create table students (' \
                   'id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,' \
                   'name VARCHAR(64) NOT NULL,' \
                   'age INT,' \
                   'sex INT)'

    db.execute_db(create_table)



