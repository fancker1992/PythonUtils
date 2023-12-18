#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mico 
@File ：mysql_client.py
@IDE  ：PyCharm 
@Author ：飞熊
@Date ：2022/9/26 11:26 上午 
"""
import pymysql


class MysqlClient():
    def __init__(self, host, username, password, port):
        # 打开数据库连接
        self.db = pymysql.connect(host=host,
                                  user=username,
                                  password=password,
                                  port=port,

                                  charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()

    def insert(self, sql):  # 单条插入   只传入sql
        self.cursor.execute(sql)
        self.db.commit()

    def insert_into(self, sql, data):  # data为元组形式（）
        self.cursor.execute(sql, data)
        self.db.commit()

    def insert_into_batch_sql(self, sql):  # 批量插入,只传入sql
        self.cursor.executemany(sql)
        self.db.commit()

    def insert_into_batch(self, sql, data):  # 批量插入
        self.cursor.executemany(sql, data)  # data需为嵌套元组形式((),())
        self.db.commit()

    def query(self, query_sql):
        self.cursor.execute(query_sql)
        return self.cursor.fetchall()  # 获取所有数据

    def update(self, sql):  # 更新数据
        self.cursor.execute(sql)
        self.db.commit()

    def close_db(self):
        self.cursor.close()
        self.db.close()
