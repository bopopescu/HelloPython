import sqlite3

def main():
    conn=sqlite3.connect('test.db')
    cursor=conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
    print(cursor.rowcount)
    # print(cursor.execute('select * from user'))
    cursor.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()