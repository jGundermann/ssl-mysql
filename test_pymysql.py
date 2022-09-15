#!/usr/bin/env python3
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="swat",
    cursorclass=pymysql.cursors.DictCursor,
    ssl_ca="./certs/ca.pem",
    ssl_cert="./certs/client-cert.pem",
    ssl_key="./certs/client-key.pem",
    autocommit=True,
)

with conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM City LIMIT 10;")

        for row in cursor.fetchall():
            print(row)
