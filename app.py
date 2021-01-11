import os
from flask import Flask, render_template,request
from cs50 import SQL

db = SQL("sqlite:///garden.db")




project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')
app = Flask(__name__, template_folder=template_path)


@app.route("/")
def home():

   data = db.execute("SELECT * FROM nursery;")
   return render_template('index.html',data = data)



@app.route("/login")
def login():

   return render_template('login.html') 



@app.route("/signup")
def register():

   return render_template('register.html') 




@app.route("/card/<int:id_p>")
def card(id_p):
   id_p = 0
   name = db.execute('select name,des,price from plants where id = ?;',id_p)
  
   name_nursery = db.execute('select name from nursery join plants on plants.nursery_id = nursery.id where plants.id = ? ;',id_p)
   like = db.execute('select count(*) from like join plants on plants.id = like.plants_id where plants.id = ? ;',id_p)
   print(name)
   
   print(des_p)
   print(like)
   print(name)

   return render_template('card.html')    




@app.route("/profile")
def profile():

   return render_template('profile.html')




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