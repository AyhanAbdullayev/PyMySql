import pymysql

#Connect to Db
pymysql1 = pymysql.connect(
    host = "127.0.0.1", # or "localhost"
    user = "root",
    password = "12345",
    db = "PyMySql",
    port = 3306,
    charset = "utf8mb4",
    cursorclass  = pymysql.cursors.DictCursor
) 

#Create Table 

def create_table():
    with pymysql1:
        with pymysql1.cursor() as cursor:
            sql_command = """Create Table if not exists PyMySql.User(                            
                                id int primary key auto_increment,
                                Name varchar(100),
                                SurName varchar(70),
                                Email varchar(100),
                                Password varchar(100)
                        );"""
            cursor.execute(sql_command)
        pymysql1.commit()



#Insert into

def insert_into_table(Name,SurName,Email,Password):
    with pymysql1:
        with pymysql1.cursor() as cursor:
            sql_command = "Insert Into PyMySql.User (Name,SurName,Email,Password) Values (%s,%s,%s,%s)"
            cursor.execute(sql_command,(Name,SurName,Email,Password))
        pymysql1.commit()


#Update Table

def update_table(Name,id):
    with pymysql1:
        with pymysql1.cursor() as cursor:
            sql_command = """Update  PyMySql.User
                            Set Name = %s 
                            Where id = %s"""
            cursor.execute(sql_command,(Name,id))
        pymysql1.commit()


#Get Table Fetchall

def get_table():
    with pymysql1.cursor()  as cursor:
        sql_command = "Select * from PyMySql.User"
        cursor.execute(sql_command)
        return cursor.fetchall()




#Get Table Fetcone

def get_table():
    with pymysql1.cursor()  as cursor:
        sql_command = "Select * from PyMySql.User"
        cursor.execute(sql_command)
        return cursor.fetchone()

#Get Table Fetcone

def get_table():
    with pymysql1.cursor()  as cursor:
        sql_command = "Select * from PyMySql.User"
        cursor.execute(sql_command)
        return cursor.fetchmany(size=2)

#Get single row 

def get_single_row(Name):
    with pymysql1.cursor() as c:
        sql_command = "Select * from PyMySql.User Where Name = %s"
        c.execute(sql_command,(Name))
        result =  c.fetchone()
        print(result)


# Get Name

def get_name(Name):
    with pymysql1.cursor() as c:
        sql_command = f"Select * from PyMySql.User Where Name like '%{Name}%'"
        c.execute(sql_command)
        return c.fetchall()

        
# Delete row 

def del_table(id):
    with pymysql1:
        with pymysql1.cursor() as c:
            sql_command = """Delete from PyMySql.User
                             Where id = %s"""
            c.execute(sql_command,(id))
        pymysql1.commit()

