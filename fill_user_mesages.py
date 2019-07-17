import postgresql
import datetime
import time
from datetime import datetime
import random

with postgresql.open('pq://dbusrname:dbusrpassword@localhost/dbname') as db:
    sel = db.query("SELECT id FROM user_profile")
    ins = db.prepare("INSERT INTO users_messages(send_date, sender_id, receiver_id, msg_subject, msg_body) VALUES($1, $2, $3, $4, $5)")
    sbj_initial = "Receipt number: "
    body_initial = "Your receipt was generated automatically, number is "
    #insert 2450 records
    for j in sel:
        time.sleep(1)
        for t in sel:
            if (j[0] != t[0]):
                date  = datetime.now()
                number = random.randint(100000,1000000)
                msg_subject = sbj_initial + str(number)
                msg_body = body_initial + str(number)    
                ins(date, t[0], j[0], msg_subject, msg_body)
            
            
        
    
        
            

    