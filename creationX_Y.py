import sqlite3 as sq
import datetime as dt

conn=sq.connect('points.db')
cursor=conn.cursor()
cmd="create table X_Y(X int,Y int);"
cursor.execute(cmd)
conn.commit()
