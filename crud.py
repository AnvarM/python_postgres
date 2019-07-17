import postgresql
from datetime import datetime

def select_top_10_messages_for_sender(db, sender_id):
    select = db.query("SELECT * FROM users_messages where sender_id = {} order by send_date desc limit 10".format(sender_id))
    for s in select:
        print(s)
        
def select_top_10_messages_for_receiver(db, receiver_id):
    select = db.query("SELECT * FROM users_messages where receiver_id = {} order by send_date desc limit 10".format(sender_id))
    for s in select:
        print(s)

def delete_record_by_id(db, id):
    delete = db.prepare("DELETE FROM users_messages where msg_id = $1")
    delete(id)
    
def insert_message(db, sender_id, receiver_id, subject, body):
    #insert with prepared statement
    insert = db.prepare("INSERT INTO users_messages(send_date, sender_id, receiver_id, msg_subject, msg_body) VALUES($1, $2, $3, $4, $5)")
    date = datetime.now()
    insert(date, sender_id, receiver_id, subject, body)        

with postgresql.open('pq://dbusrname:dbusrpassword@localhost/dbname') as db:
    insert_message(db, 55, 65, "test", "tes22")        
        
    
        
            

    