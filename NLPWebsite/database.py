import json

class Database(object):

    def insert(self,name,email,password):

        with open("users.json","r") as rf:
            users=json.load(rf)

            if email in users:
                return 0
            else:
                users[email]=[name,password]
                
                with open("users.json","w") as wf:
                    json.dump(users,wf)

                return 1
    
    def validate(self,email,password):

        with open("users.json","r") as rf:
            users=json.load(rf)

            if email in users:
                password_in_database=users[email][1]
                if(password==password_in_database):
                    return 0
                else:
                    return 1
            else:
                return 2