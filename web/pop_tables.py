import MySQLdb as db
import sys

def populate_linkedin(joblist=None):
    conn = db.connect('localhost', 'root', '', 'glass')
    with conn:
        cur = conn.cursor()
        for j in joblist:
            cur.execute("INSERT INTO linkedin (company, title) VALUES (%s,%s)" % 
                (j['company'], j['position']))
    con.close()