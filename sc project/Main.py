from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc
from UserTable import Base, User,Tenth, Inter, Grad

app = Flask(__name__)

engine = create_engine('sqlite:///UserAccounts.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

user_login=False

@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html')



@app.route('/login',methods=['GET','POST'])
def login():
    # print ("a")
    if request.method == 'POST':
        user_id=''
        try:
            print("after try")
            users=session.query(User).filter_by(email_id=request.form['email']).one()
            found=False
            if users.password==request.form['pass']:
                print("in 1st if")
                return render_template('mainpage.html')
            else:
                flash("Password wrong...Try Again !!")
                return render_template('loginPage.html') 
        except: 
            flash("UserName does not exist...Register first !!")
            return render_template('loginPage.html')  
    else:
        return render_template('loginPage.html')


@app.route('/register', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        try:
            users=session.query(User).filter_by(email_id=request.form['email']).one()
            flash("Username already exists")
            return render_template('registration.html')
        except:
            if request.form['pass']==request.form['confipass'] :
                obj=User(request.form['email'],request.form['pass'])
                obj.insertion()
                return render_template('loginPage.html')
            else:
                flash("Please enter the correct password and confirm password")
                return render_template('registration.html')
    else:
        
        return render_template('registration.html')

@app.route('/mainpage/10thInfromation', methods=['GET', 'POST'])
def tenthInfo():
    if request.method=='POST':
        print("after if")
        user=Tenth(request.form['topic'], request.form['message'])
        print("after passing")
        user.insertion()
        print("after insertion")
        query=session.query(Tenth).order_by(desc(Tenth.timestamp))
        return render_template('content1.html',query=query)
    else:
        query=session.query(Tenth).order_by(desc(Tenth.timestamp))
        return render_template('content1.html',query=query)
            # ,query=query)

@app.route('/mainpage/InterInfromation', methods=['GET', 'POST'])
def interInfo():
    if request.method=='POST':
        user=Inter(request.form['topic'], request.form['message'])
        user.insertion()
        query=session.query(Inter).order_by(desc(Inter.timestamp))
        return render_template('content2.html',query=query)
    else:
        query=session.query(Inter).order_by(desc(Inter.timestamp))
        return render_template('content2.html',query=query)
        # ,query=query)

@app.route('/mainpage/GradInfromation', methods=['GET', 'POST'])
def gradInfo():
    if request.method=='POST':
        user=Grad(request.form['topic'], request.form['message'])
        user.insertion()
        query=session.query(Grad).order_by(desc(Grad.timestamp))
        return render_template('content3.html',query=query)
    else:
        query=session.query(Grad).order_by(desc(Grad.timestamp))
        return render_template('content3.html',query=query)
        # ,query=query)





@app.route('/logout',methods=['GET', 'POST'])
def loggingout():
    if request.method=='POST':
        return render_template('homepage.html')

if __name__=='__main__':
    print("a")
    app.secret_key='super secret key'
    app.debug=True
    app.run(host='0.0.0.0', port=5000)