import os
# from "data/profiles" import profiles
import time
from flask import Flask, render_template,request,Request,redirect,session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash


db = SQL("sqlite:///garden.db")
# db.cursu


project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')
app = Flask(__name__, template_folder=template_path)
app.secret_key = "212uuHUH87789___221!@#$%^&*()23^tHHH-jju6655GG6gjJUHhygytwstxxww"
@app.route("/")
def home():
    profiles = db.execute('select * from nursery')
    return render_template('index.html',profiles=profiles)


@app.route("/logout")
def logout():
    session.pop('user_id', None)
    session.pop('name', None)
    session.pop('email', None)
    return redirect(('/'))


@app.route("/login",methods =['GET','POST'])
def login():

   if request.method == 'POST':
      check = db.execute('select * from user')
      err = None
      print(request.form.get("phone"))
      phone =request.form.get('phone')
      for ch in check:
         if phone in ch['phone'] or not phone in ch['email']:
            if request.form.get("password") != ch['password']:
               err ='الرمز خاطئ'
               return render_template('login.html',err = err)
            
            else:
               session['user_id'] = ch['id']
               session['email'] = ch['email']
               session['name'] = ch['name']
               return redirect('/')
         else:
            err = 'رقم الهاتف او البريد الالكتروني غير موجود'
            return render_template('login.html',err = err)

   else:
      return render_template('login.html') 



@app.route("/signup",methods=['POST','GET'])
def register():
   if request.method == 'POST':

      error = None
      name = request.form.get('name')
      phone =  request.form.get('phone')
      email =  request.form.get('email')

      if request.form.get('repassword') != request.form.get('password'):
         error = 'كلمة السر غير متطابقة'
         return render_template('register.html',error = error)

      chek = db.execute('select id,name,email,phone from user') 
      for ch in chek:

         if name in ch['name']:
            error = 'الاسم موجود بالفعل'
            return render_template('register.html',error = error)

         if email in ch['email'] or phone in ch['phone']: 
            error = 'لديك حساب بالفعل الرجاء الضغط على تسجيل الدخول'
            return render_template('register.html',error = error)
      


      db.execute('insert into user(name,email,phone,password) values(?,?,?,?)',name,email,phone,request.form.get('password'))
      #s_id = ('select id from user where name = ?',name)
      #session["user_id"] = s_id[0]['id']     
      return render_template('login.html',success="register_success" )

   else:
      return render_template('register.html')

 



@app.route("/profile",methods = ['GET'])
def profile():
    id_p = request.args.get('id_p')
    profiles = db.execute('select * from nursery where id = ?;',id_p)
    profiles_p = db.execute('select * from plants  where nursery_id = ? ;',id_p)
    posts = db.execute("select count() from plants  where nursery_id = ? ;",id_p )
    like = db.execute("select count() from like  where nursery_id = ? ;",id_p )
#    name_p = db.execute('select plants.name from plants join nursery on nursery.id = plants.nursery_id where nursery_id =?',id_p)
#    
    print('------------')
    return render_template('profile.html',profiles = profiles,profiles_p = profiles_p,posts = posts,like =like)



@app.route("/element",methods = ['GET'])
def element():

   plants_id = request.args.get("plants_id")
   plants = db.execute('select * from plants where id=?',plants_id )
   nursery = db.execute('select * from nursery where id=?',plants[0]['nursery_id'])
  # like = request.args.get("like")
  # if like == 1:
  #    like = 0
  #    return redirect("/element")
  # else:
  #    like = 1 
  #    return redirect("/element")  
   

   return render_template('element.html',plants = plants[0],nursery = nursery[0])




@app.route("/browser")
def browser():
   profiles = db.execute('select * from nursery')
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

#@app.route("/like.html",methods = ['POST'])
#def like():
#   if request.form.get("post_id") ==1:
#      like = 24
#   else:
#      like = 23   
#
#   return redirect("element.html",like)



if __name__ == "__main__":
   app.run(debug=True)  