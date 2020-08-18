import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="domainness_dataset_builder"
)


# Using readlines() 
with open('cs_titles.json') as f:
    Lines = [line.rstrip() for line in f]
  
count = 0
for line in Lines: 
    mycursor = mydb.cursor()

    jdata = json.loads(line)

    sql = "INSERT INTO demo_frontend_arxiv_titles_in_circulation (title, subject, times_classified) VALUES (%s, %s, %s)"
    val = (jdata["title"], jdata["subject"], "0")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")



with open('cs_titles.json') as f:
    lines = [line.rstrip() for line in f]
