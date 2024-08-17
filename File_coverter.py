import pymysql
import pymysql.cursors
from os.path  import exists
connect_db = pymysql.connect(
    host = "127.0.0.1",
    user = "root",
    password = "12345",
    db = "PyMySql",
    port = 3306,
    charset = "utf8mb4",
    cursorclass = pymysql.cursors.DictCursor
)



def send_file():
    with connect_db.cursor() as c:
        sql_command = "Select * from PyMySql.User"
        c.execute(sql_command)
        result =  c.fetchall()
        if not exists("table.txt"):
            with open("table.txt",'w') as f:
                f.write("Table data:")
        with open("table.txt",'w+') as f:
            for table in result:
                for key,value in table.items():
                    f.write(str(key)+ ": " + str(value) + "\n")
                f.write("-------------------- \n")
                
        
    

send_file()
