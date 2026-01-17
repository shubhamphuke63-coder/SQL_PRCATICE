import matplotlib.pyplot as plt
import numpy as np
import sqlite3 as sql
from datetime import date
class student_informations:
    def student_records(self,query):
        con=sql.connect('student.db')
        con1=con.cursor()
        con1.execute(query)
        con.commit()
        con.close()
    def student_info(self):
        query="""CREATE TABLE IF NOT EXISTS student_infos (
    Roll_num INTEGER UNIQUE NOT NULL,
    First_name TEXT CHECK(length(First_name) <= 20) NOT NULL,
    Last_name TEXT CHECK(length(Last_name) <= 20) NOT NULL,
    Father_name TEXT CHECK(length(Father_name) <= 20) NOT NULL,
    Mother_name TEXT CHECK(length(Mother_name) <= 20) NOT NULL,
    Birth_date TEXT NOT NULL,
    Contact_number TEXT CHECK(length(Contact_number) = 13) NOT NULL,
    Admission_date TEXT NOT NULL,
    Branch TEXT CHECK(length(Branch) <= 20),
    Religion TEXT CHECK(length(Religion) <= 20),
    Address TEXT CHECK(length(Address) <= 30),
    Student_id TEXT CHECK(length(Student_id) <= 10) PRIMARY KEY
);"""
        
        self.student_records(query)
        print("Table Created Succesfully")
    def Insert_into_student_infos(self):
        today = date.today()
        datetoday = today.strftime("%d-%m-%Y")
        Roll_num=int(input("Roll Number :"))
        First_name=str(input("First Name :"))
        Last_name=str(input("Last Name :"))
        Father_name=str(input("Father Name :"))
        Mother_name=str(input("Mother Name :"))
        Birth_date=str(input("Birth Date :"))
        Contact_number=int(input("Contact Number +91:"))
        Admission_date= datetoday
        Branch=str(input("Brach :"))
        Religion=str(input("Religion :"))
        Address=str(input("Address :"))
        Student_id="2026"+str(np.random.randint(1, 10, size=5))
        query=f"""INSERT INTO student_infomation(
            {Roll_num},
            "{First_name}",
            "{Last_name}",
            "{Father_name}",
            "{Mother_name}",
            "{Birth_date}",
             {Contact_number},
            "{Admission_date}",
            "{Branch}",
            "{Religion}",
            "{Address}",
            "{Student_id}"
            );"""
        self.student_records(query)
s1=student_informations()
s1.Insert_into_student_infos()       







        
            
        

        
