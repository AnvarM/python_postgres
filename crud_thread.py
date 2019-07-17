import postgresql
from datetime import datetime
import threading
import random
import time
    
def insert_message():
    with postgresql.open('pq://dbusrname:dbusrpassword@localhost/dbname') as db:
        insert = db.prepare("INSERT INTO users_messages(send_date, sender_id, receiver_id, msg_subject, msg_body) VALUES($1, $2, $3, $4, $5)")
        date = datetime.now()
        sender_id = 58
        receiver_id = random.choice([100,99,98,97,96,95,94,93,92,91,90,89,88,87,85,82,81])
        subject = "Birthday invitation"
        body = "I want to invite you to my birthday on this Friday, 21.10.2025"
        insert(date, sender_id, receiver_id, subject, body)
        print("Record inserted")
        

nthreads = 10    

#insert 10 records, 1 for each thread
for i in range(nthreads):
    t = threading.Thread(target = insert_message)
    t.start()
    time.sleep(1)
    