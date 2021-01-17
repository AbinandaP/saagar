"""
Created on Tue Oct 13 12:48:47 2020

@author: gayathri
"""
       
def x_insertion(X,Y):
    try:
        conn = sq.connect('points.db')
        cursor = conn.cursor()
        cmd = """insert into 'X_Y'(X,Y)
        VALUES(?,?);"""
        data_tuple = (X, Y)
        cursor.execute(cmd,data_tuple)
        conn.commit()
        cursor.close()
    except  sq.Error as error:
        print("error",error)
       

       
def maintable_insertion(DATE,TIME):
    try:
        conn = sq.connect('points.db')
        cursor = conn.cursor()
        cmd = """insert into 'maintable'(DATE,TIME)
        VALUES(?,?);"""
        data_tuple = (DATE,TIME)
        cursor.execute(cmd,data_tuple)
        conn.commit()
        cursor.close()
    except  sq.Error as error:
        print("error",error)
