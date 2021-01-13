import os
from flask import Flask, render_template,request,Request
from cs50 import SQL

db = SQL("sqlite:///garden.db")




project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')
app = Flask(__name__, template_folder=template_path)


@app.route("/")
def home():

   data = db.execute("SELECT *  FROM nursery;")
   return render_template('index.html',data = data)



@app.route("/login")
def login():

   return render_template('login.html') 



@app.route("/signup")
def register():

   return render_template('register.html') 




@app.route("/card/<int:id_p>")
def card(id_p):
   name = db.execute('select name,des,price from plants where id = ?;',id_p)
   print(id_p)
  
   name_nursery = db.execute('select name from nursery join plants on plants.nursery_id = nursery.id where plants.id = ? ;',id_p)
   like = db.execute('select count(*) from like join plants on plants.id = like.plants_id where plants.id = ? ;',id_p)
   print(name)
   
   print(like)
   print(name)

   return render_template('card.html')    




@app.route("/profile",methods = ['GET'])
def profile():
   id_p = request.args.get('id_p')

   name_n = db.execute('SELECT name from nursery where id = ? ; ' , id_p)
   phone = db.execute('SELECT phone from nursery where id = ? ; ' , id_p)
   size_p = db.execute('SELECT count(*) from plants join nursery on nursery.id = plants.nursery_id where nursery_id=? ; ' , id_p)
   name_p = db.execute('select plants.name from plants join nursery on nursery.id = plants.nursery_id where nursery_id =?',id_p)
   print(name_p)
   return render_template('profile.html',
                        name_n = name_n[0]['name'],
                        phone = phone[0]['phone'],
                        size_p = size_p[0]['count(*)'],
                        name_p1 = name_p[0]['name'],
                        name_p2 = name_p[1]['name'],
                        name_p3 = name_p[2]['name'],
                        des1 = name_p[0]['des'],
                        des2 = name_p[1]['des'],
                        des3 = name_p[2]['des'] 
                          )

# name_n = name_n[0]['name'],
#                         phone = phone[0]['phone'],
#                         size_p = size_p[0]['count(*)'],
#                         name_p1 = name_p,
#                         name_p2 = name_p,
#                         name_p3 = name_p,
#                         des1 = name_p,
#                         des2 = name_p,
#                         des3 = name_p 


@app.route("/element")
def element():

   return render_template('element.html')




@app.route("/browser")
def browser():

   return render_template('browser.html')


   




@app.route('/insert.html',methods =['GET','post'])
def edit():

   name = request.form.get("name")
   img_path = request.form.get("img_path")
   des = request.form.get("des")
   phone = request.form.get("phone")
   path = request.form.get("path")

   db.execute('INSERT INTO  nursery(name,phone,img_path,des,path) VALUES(?,?,?,?,?);',name ,phone,img_path,des,path)

   return render_template('insert.html')



if __name__ == "__main__":
   app.run(debug=True,port = 9000)  