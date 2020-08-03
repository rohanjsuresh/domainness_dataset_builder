import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="domainness_dataset_builder"
)


# Using readlines() 
file1 = open('arxiv_titles.txt', 'r') 
Lines = file1.readlines() 
  
count = 0
for line in Lines: 
    mycursor = mydb.cursor()

    sql = "INSERT INTO demo_frontend_arxiv_titles_in_circulation (title, times_classified) VALUES (%s, %s)"
    val = (line.strip(), "0")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")