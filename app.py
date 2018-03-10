from peewee import *
from flask import Flask, url_for, render_template, request, redirect, session

mysql_db = MySQLDatabase('sql9224506', user='sql9224506', password='NqDZ2Yd2yg',
                         host='sql9.freemysqlhosting.net', port=3306)


app = Flask(__name__)
app.secret_key = 'very secret key here'

class BaseModel(Model):

    class Meta:
        database = mysql_db

class brandregister(BaseModel):
    id=IntegerField(primary_key=True)
    BRANDNAME = CharField(max_length=50,unique=True)
    BRANDPASSWORD = CharField(max_length=50)
    BRANDEMAIL = CharField(max_length=50)
   
    

class brandlogin(BaseModel):
    id=IntegerField(primary_key=True)
    BRANDNAME = CharField(max_length=50,unique=True)
    BRANDPASSWORD = CharField(max_length=50)
   

@app.route('/', methods=['GET', 'POST'])
def home():

    if  session.get('logged_in'):
        return render_template('result.html')
        
    else:
        return render_template('login.html')

    

       


@app.route('/login', methods=['GET', 'POST'])
def Login():
    
    if request.method == 'GET':
        return render_template('login.html')
    else:
        brandname = request.form['brandname']
        brandpasswd = request.form['brandpassword']
        try:
            l = brandlogin.get((brandlogin.BRANDNAME == brandname) & (brandlogin.BRANDPASSWORD == brandpasswd)).BRANDPASSWORD
            if l is not None:
                session['logged_in'] = True
                session['brandname']=brandname
                return redirect(url_for('home'))
            else:
                return "INCORRECT LOGIN"
                

        except:
            return "INCORRECT LOGIN"

@app.route('/register/', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        brandname = request.form['brandname']
        brandpasswd = request.form['brandpassword']
        brandemail = request.form['brandemail']

        try:
            
            if brandname=="" or brandpasswd == "" or brandemail == "":
                raise NameError

            brandregister.create(BRANDNAME=brandname,BRANDPASSWORD=brandpasswd,BRANDEMAIL=brandemail)
            brandlogin.create(BRANDNAME=brandname,BRANDPASSWORD=brandpasswd)

        except NameError:
            return "all fields are mandatory"
        except:
            return "username or email already in use"
        

        return render_template('login.html')
    return render_template('register.html')

@app.route("/logout")
def logout():
    
    session['logged_in'] = False
    return redirect(url_for('home'))





if __name__ == '__main__':

   
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)






