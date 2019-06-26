import mysql.connector
def dbname():
    dbname = str(input("dbname:"))
    while not dbname:
        dbname = str(input("plesesle name"))
    return [dbname]
def create_shell(dbname):
    shell = 'CREATE DATABASE {}'.format(dbname)
    return shell
def drop_shell(dbname):
    shell = 'Drop DATABASE {}'.format(dbname)
    return shell
def zhixing(s):
    mycursor.execute(s)
mydb = mysql.connector.connect(host="localhost",user="root",passwd="yanzhe")
show = "show databases"
while True:
    db_list = []
    mycursor = mydb.cursor()
    mycursor.execute(show)
    for x in mycursor:
        db_list.append((list(x)))
    print("现存在如下数据库:",db_list)
    chose = str(input("create dbname 1:\ndrop   dbname 2:\n\n1或者2 "))
    if chose == "1":
        db_name = dbname()
        if db_name not in db_list:
            db_name = db_name[0]
            zhixing(create_shell(db_name))
        else:
            print("\033[1;35m 已存在此数据库 \033[0m!")
    elif chose == "2":
        db_name = dbname()
        if db_name in db_list:
            db_name = db_name[0]
            zhixing(drop_shell(db_name))
        else:
            print("\033[1;35m 查询无此数据库 \033[0m!")
    elif chose == 'q':
        break
    else:
        print("\033[1;35m 请重新输入1或者2或者q! \033[0m")