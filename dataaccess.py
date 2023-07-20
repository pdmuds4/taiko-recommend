from var import Var
from db import DB 

class DataAccess:
    def get_table(self,i):
        query = f"SELECT * FROM lv{str(i)} "
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)
        

    def get_song(self, title, master=False, level=None, num=False):
        if level is not None:
            if master==True:
                query = f"SELECT * FROM lv{level} WHERE title = %s || '(裏譜面)' "
            else:
                query = f"SELECT * FROM lv{level} WHERE title = %s "
                    
            data = (str(title),)
            db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
            return db.execute(query, data)
        else:
            k = 5
            while k<=10:
                if master==True:
                    query = f"SELECT * FROM lv{k} WHERE title = %s || '(裏譜面)' "
                else:
                    query = f"SELECT * FROM lv{k} WHERE title = %s "
                    
                data = (str(title),)
                db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
                return_data = db.execute(query, data)
                if len(return_data) == 0:
                    k+=1
                else:
                    if num == True:
                        return return_data, k
                    else:
                        return return_data
                

    def get_other(self, title):
        i = DataAccess.get_song(self,title,num=True)[1]
        query = f"SELECT * FROM lv{i} WHERE title != %s "
        data = (str(title), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)




# if __name__ == "__main__":
#     a = DataAccess()
#     print([i[0] for i in a.get_table(5)])
#     print(DataAccess.get_song(a, "Vixtory", master=True))
#    print(DataAccess.get_other(a, "Vixtory"))
