import mysql.connector

def main():
    conn=mysql.connector.connect(user='root',password='password',database='robserver')
    cursor=conn.cursor()
    cursor.execute('select * from user')
    msg=cursor.fetchall()
    print(msg)
    cursor.close()
    conn.close

if __name__ == '__main__':
    main()