import mysql.connector
from mysql.connector import Error

class MySQLDatabase:
    def __init__(self, host, database, user, password):
        self.connection = None
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        """建立数据库连接"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("数据库连接成功")
        except Error as e:
            print(f"数据库连接失败：{e}")

    def close(self):
        """关闭数据库连接"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("数据库连接已关闭")


    def execute_query(self, query, params=None):
        """执行查询并返回结果"""
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params if params else ())
            result = cursor.fetchall() if cursor.with_rows else None
            return result
        except Error as e:
            print(f"执行查询失败：{e}")
        finally:
            cursor.close()

    def insert(self, table, data):
        """插入数据"""
        keys = ', '.join(data.keys())
        # 创建一个参数列表，其中包含所有值
        values = list(data.values())
        # 参数化查询，不需要手动构造VALUES部分
        query = f"INSERT INTO {table} ({keys}) VALUES (%s)"
        print(query)
        print(values)
        # 由于我们使用参数化查询，所以values参数是一个单一的元组，包含所有的值
        return self.execute_query(query, values)

    def update(self, table, data, conditions):
        """更新数据"""
        updates = ', '.join([f"{key}=%s" for key in data.keys()])
        query = f"UPDATE {table} SET {updates} WHERE {conditions}"
        self.execute_query(query, list(data.values()))

    def delete(self, table, conditions):
        """删除数据"""
        query = f"DELETE FROM {table} WHERE {conditions}"
        self.execute_query(query)

    def select(self, query):
        """执行SELECT查询"""
        return self.execute_query(query)