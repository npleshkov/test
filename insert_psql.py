from datetime import datetime

import psycopg2

try:
   connection = psycopg2.connect(user='dbuserjob',
                                  password='Smurf_2019',
                                  host='127.0.0.1',
                                  port='5432',
                                  database='jobdb')
   cursor = connection.cursor()

   dt = datetime.now()

   base_name = 'contragents_contragent'

   postgres_insert_query = """ INSERT INTO contragents_contragent (first_name, last_name, midle_name, email, phone, education, created_on, is_active ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
   record_to_insert = ('Сергеев', 'Перт','Петрович','test9@gmail.com', '+79120102989', 'secondary', dt, 'true')
   # record_to_insert = ('Петров', 'Иван', 'Иванович', 'test@gmail.com', '8912010')

   postgres_select_query = " SELECT * FROM contragents_contragent "

   cursor.execute(postgres_insert_query, record_to_insert)
   # cursor.execute(postgres_select_query)

   connection.commit()
   count = cursor.rowcount
   print(postgres_select_query)
   print (count, "Record inserted successfully into mobile table")
   cursor.execute(postgres_select_query)
   print(*cursor.fetchall(), sep="\n")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")