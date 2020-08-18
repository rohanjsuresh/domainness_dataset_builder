import mysql.connector
import json

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  port='3306',
  database="domainness_dataset_builder"
)


# Using readlines() 
with open('arxiv_titles.json') as f:
    Lines = [line.rstrip() for line in f]
  
count = 1
for line in Lines: 
    mycursor = mydb.cursor()

    jdata = json.loads(line)

    sql = "INSERT INTO demo_frontend_arxiv_titles_in_circulation (title, subject, times_classified) VALUES (%s, %s, %s)"
    val = (jdata["title"], jdata["subject"], "0")
    mycursor.execute(sql, val)
    mydb.commit()
    print(count, end=": ")
    print(mycursor.rowcount, "record inserted.")
    count += 1




    
