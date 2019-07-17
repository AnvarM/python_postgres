import postgresql
with postgresql.open('pq://dbusrname:dbusrpassword@localhost/dbname') as db:
	sql = """CREATE TABLE user_profile (id SERIAL PRIMARY KEY, email TEXT NOT NULL, name TEXT NOT NULL, last_name TEXT NOT NULL)"""
	db.execute(sql)
	sql = """CREATE TABLE users_messages (msg_id SERIAL PRIMARY KEY , send_date TIMESTAMP, sender_id int REFERENCES user_profile(id), 
	receiver_id int REFERENCES user_profile(id), msg_subject TEXT, msg_body TEXT)"""
	db.execute(sql)

