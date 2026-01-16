import matplotlib.pyplot as plt
import numpy as np
import sqlite3 as sql
class student_information:
    def student_records(self,query):
        con=sql.connect('student.db')
        con1=con.cursor()
        con1.execute(query)
        con.commit()
        con.close()
    def student_info(self):
        query="""CREATE TABLE student_info(
                Roll_no INTEGER PRIMARY KEY,
                First_name TEXT CHECK (length(First_name)<20) NOT NULL,
                Last_name TEXT CHECK (length(Last_name)<20) NOT NULL,
                Father_name TEXT CHECK (length(Father_name)<20) NOT NULL,
                Mother_name TEXT CHECK (length(Mother_name)<20) NOT NULL,
                Birth_date DATE NOT NULL,
                Contact_number INTEGER CHECK (length(Contact_number)=13)
                )
                
                """
        https://github.com/shubhamphukepa/100-days-of-DSA.githttps://github.com/shubhamphukepa/100-days-of-DSA.git

        
