import sqlite3
con = sqlite3.connect("Student_Manager.db")
Curso = con.cursor()

def __init__():
    Curso.execute('''CREATE TABLE IF NOT EXISTS studentData
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      Student_Name TEXT,
                      Father_Name INTEGER,
                      Family_Name TEXT,
                      Gender TEXT,
                      Status INTEGER,
                      payed INTEGER,
                      Age INTEGER,
                      Father_Number INTEGER,
                      Student_Number INTEGER)''')
def Set_data(id , Student_Name, Father_Name , Family_Name , Gender , Status , payed , Age , Father_Number , Student_Number):
    Curso.execute('''CREATE TABLE IF NOT EXISTS studentData
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  Student_Name TEXT,
                  Father_Name INTEGER,
                  Family_Name TEXT,
                  Gender TEXT,
                  Status INTEGER,
                  payed INTEGER,
                  Age INTEGER,
                  Father_Number INTEGER,
                  Student_Number INTEGER)''')
    try:
        Curso.execute('INSERT INTO studentData (id, Student_Name, Father_Name, Family_Name, Gender, Status, payed, Age, Father_Number, Student_Number) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
                  , (id ,
                     Student_Name,
                     Father_Name,
                     Family_Name,
                     Gender,
                     Status,
                     payed,
                     Age,
                     Father_Number,
                     Student_Number))
        con.commit()

    except:
        Curso.execute(
            'INSERT INTO studentData (id, Student_Name, Father_Name, Family_Name, Gender, Status, payed, Age, Father_Number, Student_Number) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            ,  (id,
               Student_Name,
               Father_Name,
               Family_Name,
               Gender,
               Status,
               payed,
               Age,
               Father_Number,
               Student_Number))
        con.commit()
def delete(using):
    pass


id, Student_Name, Father_Name, Family_Name, Gender, Status, payed, Age, Father_Number, Student_Number = None, None, None, None, None, None, None, None, None, None
