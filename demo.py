import mysql.connector
from fastapi import FastAPI
app=FastAPI()

@app.post("/")
def sql_connect():
    mydb = mysql.connector.connect(
        host="b3hz8.h.filess.io",
        user="testdb_perfectly",
        password="fbb60ce6c4ae61f049580f9388d5da26c013ead0",
        database="testdb_perfectly",
        port="3307"
    )
    mypost = mydb.cursor()
    mypost.execute("INSERT INTO users VALUES(2,'sandeep')")
    mypost.execute("INSERT INTO users VALUES(3,'kumar')")
    mydb.commit()
    return{"success"}
@app.get("/")
def sql_connect():
    mydb = mysql.connector.connect(
        host="b3hz8.h.filess.io",
        user="testdb_perfectly",
        password="fbb60ce6c4ae61f049580f9388d5da26c013ead0",
        database="testdb_perfectly",
        port="3307"
    )
    mypost=mydb.cursor()
    mypost.execute("SELECT * FROM users")
    r=mypost.fetchall()
    mydb.commit()
    return r

