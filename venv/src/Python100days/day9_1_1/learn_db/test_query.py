import sqlite3

def main():
    conn=sqlite3.connect('test.db')
    cursor=conn.cursor()
    cursor.execute('select * from user')
    msg=cursor.fetchall()
    print(msg)
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()