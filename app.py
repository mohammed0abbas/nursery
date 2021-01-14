import os
# from "data/profiles" import profiles
import time
from flask import Flask, render_template,request,Request
from cs50 import SQL

db = SQL("sqlite:///garden.db")
# db.cursu


project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')
app = Flask(__name__, template_folder=template_path)

@app.route("/")
def home():
    profiles = db.execute('select * from nursery')
    print("---------count :",len(profiles))
    return render_template('index.html',profiles=profiles)



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




#@app.route("/profile",methods = ['GET'])
#def profile():
#    id_p = request.args.get('id_p')
#      
#    name_n = db.execute('SELECT name from nursery where id = ? ; ' , id_p)
#    phone = db.execute('SELECT phone from nursery where id = ? ; ' , id_p)
#    size_p = db.execute('SELECT count(plants.name) from plants join nursery on nursery.id = plants.nursery_id where nursery_id=? ; ' , id_p)
#    name_p = db.execute('select plants.name from plants join nursery on nursery.id = plants.nursery_id where nursery_id =?',id_p)
#    
#    return render_template('profile.html',profile=current_id_data[0])

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

   return render_template('browser.html',profiles=profiles)


   




@app.route('/insert.html',methods =['GET','POST'])
def edit():   
   print('-----edit function is running..')
   if request.method=='GET':
      print('-----Get methon detected.. returining insert.html template..')
      return render_template('insert.html')
   else:
      print('-----Post method detected')
      name = request.form.get("name")
      phone = request.form.get("phone")
      img_path = request.form.get("img_path")
      des = request.form.get("des")
      path = request.form.get("path")
      print('-----Post data recived...')
      # db.cursor()
      db.execute('INSERT INTO  nursery(name,phone,img_path1,des,path) VALUES(?,?,?,?,?);',name ,phone,img_path,des,path)
      print('-----INSERT SUCCESS')
      # db.commit()
      # db.close()
      print('-----Commit is done. redirecting...')
      # return render_template('insert.html?hi')
      time.sleep(5) 
      return render_template('insert.html',inserted=True)

      


@app.route('/plant.html',methods =['GET','POST'])
def plant():   
   print('-----edit function is running..')
   if request.method=='GET':
      print('-----Get methon detected.. returining insert.html template..')
      return render_template('plant.html')
   else:
      print('-----Post method detected')
      name = request.form.get("name")
      img_path = request.form.get("img_path")
      des = request.form.get("des")
      price=request.form.get("price")
      nur_id = request.form.get("n_id")
      print('-----Post data recived...')
      # db.cursor()
      db.execute('INSERT INTO  plants(name,img_path1,des,price,nursery_id) VALUES(?,?,?,?,?);',name ,img_path,des,price,nur_id)
      print('-----INSERT SUCCESS')
      # db.commit()
      # db.close()
      print('-----Commit is done. redirecting...')
      # return render_template('insert.html?hi')
      time.sleep(5) 
      return render_template('plant.html',inserted=True)



if __name__ == "__main__":
   app.run(debug=True,port = 9000)  