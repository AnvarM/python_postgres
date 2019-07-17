import postgresql
with postgresql.open('pq://dbusrname:dbusrpassword@localhost/dbname') as db:
    ins = db.prepare("INSERT INTO user_profile (email, name, last_name) VALUES ($1, $2, $3)")
    emails = []
    name = []
    last_name = []
    domain = "@fillthe.db"
    with open("names.txt", "r") as f:
        for line in f:
            line = line.strip()
            full_name = line.split(" ")
            name.append(full_name[0])
            last_name.append(full_name[1])
            emails.append(full_name[0] + "." + full_name[1] + domain)
            
    for i in range(len(emails)):
        ins(emails[i], name[i], last_name[i])
        
            

    