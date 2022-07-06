from flask import Flask, render_template, request, session
from flask import Flask, render_template, request, redirect,url_for
from flask import request
#from flask_mysqldb import MySQL
import pymysql
#import MySQLdb.cursors
import datetime
import time
import calendar
app = Flask(__name__)

#Change this to your local database host,then change the user and passwd to your own one
def connectDB():
     db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1999311', db='trycycle_qa', charset='utf8')
     cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
     return cursor,db
@app.route('/')
def index():
    return render_template("login.html")
@app.route('/changepassword/',methods=['GET', 'POST'])
def changepassword():
    newpassword=request.form['password']
    cursor,db= connectDB()
    cursor.execute("UPDATE user SET USER_PASSWORD=%s WHERE USER_ID = %s ",(newpassword,session['userIDchange']))
    db.commit()
    db.close()
    return render_template("login.html")
@app.route('/set_password/',methods=['GET', 'POST'])
def set_password():
    session['userIDchange']=request.form['user_id']
    chooseq=request.form['Secret_Question']
    answer=request.form['secret_answer']
    cursor,db= connectDB()
    cursor.execute("SELECT USER_SEC_Q , USER_SEC_ANSWER FROM user WHERE USER_ID=%s ",session['userIDchange'])
    data=cursor.fetchone()
    if(int(chooseq)==int(data['USER_SEC_Q']) and answer ==data['USER_SEC_ANSWER'] ):
         return render_template("newpassword.html")
    else:
         return render_template("login.html")
@app.route('/security')
def security():
    return render_template("Security.html")
@app.route('/monthly_rental')
def monthly_rental():
    return render_template("monthly_rental.html")
@app.route('/monthly_rental_display',methods=['GET', 'POST'])
def monthly_rental_display():  
     label={"1-10":0,"11-20":0,"21-end":0}
     month=request.form['Month']
     year=request.form['Year']
     cursor,db= connectDB()
     cursor.execute("SELECT RENTAL_START_TIME FROM rentallog")
     data=cursor.fetchall()
     for i in range(len(data)):
        datemounth=data[i]['RENTAL_START_TIME'].month
        datemyear=data[i]['RENTAL_START_TIME'].year
        datemday=data[i]['RENTAL_START_TIME'].day
        datemounthstr=calendar.month_abbr[datemounth]
        if datemounthstr==month and  int(datemyear)==int(year):
            if int(datemday)>=1 and int(datemday)<=10:
                   
                   label["1-10"]+=1
            elif int(datemday)>10 and int(datemday)<=20:
                   
                   label["11-20"]+=1
            elif int(datemday)>20 and int(datemday)<=31:
                   
                   label["21-end"]+=1
    
     return render_template("monthly_rental.html",labelvalue=label)
@app.route('/defects_report')
def defects_report():
    label={}
    listmounth=[]
    cursor,db= connectDB()
    cursor.execute("SELECT DEFECT_TIMESTAMP FROM defectlog ORDER BY DEFECT_TIMESTAMP")
    datamouth=cursor.fetchall()
    for i in range(len(datamouth)):
        date=datamouth[i]['DEFECT_TIMESTAMP'].month
        label[calendar.month_abbr[date]]=0
        listmounth.append(calendar.month_abbr[date])
    for key in listmounth:
        temp=label[key]
        count=temp+1
        label[key]=count
        
    print(label)
    return render_template("defects_report.html",label=label)
@app.route('/Premium_User')
def Premium_User():
    listdata=[]
    cursor,db= connectDB()
    cursor.execute("SELECT * FROM user WHERE USER_CATEGORY='2' AND USER_SUBSCRIPTION ='1' ")
    data1=cursor.fetchall()
    numbersub=len(data1)
    
    cursor.execute("SELECT * FROM user WHERE USER_CATEGORY='2' AND USER_SUBSCRIPTION ='0' ")
    data2=cursor.fetchall()
    numberunsub=len(data2)
  
    
    listdata.append(numbersub)
    listdata.append(numberunsub)
    return render_template("Premium_User.html",VALUES=listdata)
@app.route('/user/')
def user():
    return render_template("profile.html")
@app.route('/subscribe/',methods=['GET', 'POST'])
def subscribe():
    uid=session['id']
    cursor,db= connectDB()
    sub=1
    cursor.execute("UPDATE user SET USER_SUBSCRIPTION=%s WHERE USER_ID = %s ",(sub,uid))
    db.commit()
    db.close()
    session["is_premium"]=1
    return render_template("upgrade_success.html")
@app.route('/logout/')
def logout():
    session.clear()
    return render_template("login.html")
@app.route('/history/')
def history():
    return render_template("index.html")
@app.route('/topUp')
def topUp():
    return render_template("top_up.html")
@app.route('/topUp_account/', methods=['GET', 'POST'])
def topUp_account():
    userCurrentBal = request.form['amount']
    uId=session['id']
    Balancenow=session['balance']
    B=float(userCurrentBal)
    newresult=float(Balancenow+B)
    cursor,db= connectDB()
    cursor.execute("UPDATE user SET USER_BALANCE=%s WHERE USER_ID = %s ",(newresult,uId))
    db.commit()
    db.close()
    Balance=round(newresult,2)
    session['balance']=Balance
    return render_template("topup_success.html")
@app.route('/uhome/')
def C_home():
    #Customer
    return render_template('Customer_home.html')
@app.route('/ohome/')
def O_home():
    #Customer
    return render_template('Operator_home.html')
@app.route('/mhome/')
def M_home():
    return render_template('manager_home.html')
@app.route('/park', methods=("POST", "GET"))
def park():
    return render_template('park.html')
@app.route('/report', methods=("POST", "GET"))
def report():
    return render_template('report.html')
@app.route('/', methods=("POST", "GET"))
def home_user():
       return render_template('Customer_home.html')   
@app.route('/report_list', methods=("POST", "GET"))
def report_list():
        postcoode = request.form['reportcode']
        cursor,db= connectDB()
        cursor.execute("SELECT * FROM bikestation WHERE BS_POSTCODE=%s",postcoode)
        bikesation=cursor.fetchone()
        if  bikesation:
             bikesationnumber=bikesation['BIKESTATION_ID']
             cursor.execute("SELECT * FROM bike WHERE BIKESTATION_ID = %s AND BIKE_HEALTH_STATUS=1 ",bikesationnumber)
             data=cursor.fetchall()
             return render_template('report_list.html',tot = len(data), data = data)
        else:
             msg="Not a vaild staion"
             return render_template('Customer_home.html',msg=msg) 
@app.route('/drop_list', methods=("POST", "GET"))
def drop_list():   
    uid = session['id']
    cursor,db= connectDB()
    cursor.execute("SELECT RENTAL_BIKE_ID FROM rentallog WHERE RENTAL_USER_ID = %s AND RENTAL_PRICE is NULL ",uid)
    data=cursor.fetchone()
    if data:
        return render_template('drop.html',bikeID = data['RENTAL_BIKE_ID'])
    else:
        msg="You have no current rent bike,please make a order first"
        return render_template('Customer_home.html',msg=msg)
@app.route('/rent', methods=("POST", "GET"))
def rent():
    return render_template('rent.html')
@app.route('/list', methods=("POST", "GET"))
def list():
    if request.method == 'POST' and 'postcoode' in request.form:
        # Create variables for easy access
        postcoode = request.form['postcoode']
        session["postcoode"]=postcoode;
        cursor,db= connectDB()
        cursor.execute("SELECT * FROM bikestation WHERE BS_POSTCODE=%s",postcoode)
        bikesation=cursor.fetchone()
        bikesationnumber=bikesation['BIKESTATION_ID']
        session["pickup"]=bikesationnumber
        cursor.execute('SELECT * FROM bike WHERE BIKESTATION_ID = %s AND BIKE_HEALTH_STATUS=1 AND BIKE_STATUS=0 ',bikesationnumber)
        data=cursor.fetchall()
        db.close()
    return render_template('rent_list.html',tot = len(data) ,data = data)
@app.route('/login/', methods=['POST'])
def login():
    
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        emailaddress = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        #db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1999311', db='trycycle_qa', charset='utf8')
        cursor,db= connectDB()
        cursor.execute('SELECT * FROM user WHERE USER_MAIL_ID = %s AND USER_PASSWORD= %s', (emailaddress, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
           session['loggedin'] = True
           session['id'] = account['USER_ID']
           session['POSTCODE'] = account['POSTCODE']
           session['Name']= account['USER_MAIL_ID']
           session["is_premium"]=account['USER_SUBSCRIPTION']
           session['Email']= account['USER_MAIL_ID']
           session['Phone']=account['USER_PHONE']
           session['card']='visa card'
           session['balance']=account['USER_BALANCE']
           session['Addresscode']=account['POSTCODE']
           session['usertype']=account['USER_CATEGORY']
           if int(session['usertype'])==2:
              return redirect(url_for('C_home'))
           elif int(session['usertype'])==1:
              return redirect(url_for('O_home'))
           elif int(session['usertype'])==0:
              return redirect(url_for('M_home'))
        else:
            
           msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    db.close();
    return render_template('login.html', msg=msg)

@app.route('/rentbike/', methods=['POST'])
def rentbike():
        userId=session['id'] 
        bikeId = request.form['bike_id']
        print(bikeId)
        currentB=session['balance']
        cursor,db= connectDB()
        cursor.execute('SELECT * FROM rentallog WHERE RENTAL_USER_ID = %s AND RENTAL_PRICE is NULL', userId)
        # Fetch one record and return result
        account = cursor.fetchone()
        # if this user have not rent a bike then he can have one 
        if account :
            msg="You have an ongoing rent order!"
        elif currentB<=0:
            msg="Your account has a negative balance, please recharge first!"
        else:
            bikeId = request.form['bike_id']
            starttime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
            #in list function make this session
            startstation=session["pickup"]
            cursor.execute('INSERT INTO RENTALLOG VALUES(NULL,%s,%s,%s,NULL,%s,NULL,NULL,NULL)', (userId,bikeId,startstation,starttime))
            msg="You have make a rent order!"
            cursor.execute("UPDATE bike SET BIKE_STATUS='1' WHERE BIKE_ID= %s",bikeId)
        db.commit()   
        return render_template('Customer_home.html', msg=msg)
    
@app.route('/returnbike/', methods=['POST'])
def returnBike():
        """
        When returning bicycles, the returned bicycle station, return time and timeduration should be recorded, and the bill also need be calculated
        """
        #Get some necessary parameters,
        #I assume here that the front-end stores the user's information through the session (or cookie) when logging in, so I can simply read it here, and I don’t even need any class to store it, because the car return function only involves simple data interaction.
        userId=session['id']
        bikeId=request.form['bike_id']
        #discountType=session['type']
        #The return station should be user input and passed in through the front end
        endpostcode=request.form['returnPosscode']
        
        
        endtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        endTime=datetime.datetime.strptime(endtime,"%Y-%m-%d %H:%M:%S")
        #Database
        cursor,db= connectDB()
        #find this user and his start rent record
        cursor.execute("SELECT USER_SUBSCRIPTION FROM user WHERE USER_ID= %s ",userId)
        datas=cursor.fetchone()
        sub=datas['USER_SUBSCRIPTION']
        
        cursor.execute("SELECT BIKESTATION_ID FROM bikestation WHERE BS_POSTCODE= %s ",endpostcode)
        datas=cursor.fetchone()
        endstation=datas['BIKESTATION_ID']
        
        cursor.execute("SELECT RENTAL_START_TIME FROM rentallog WHERE RENTAL_USER_ID = %s AND RENTAL_PRICE is NULL ",userId)
        data=cursor.fetchone()
    
        startTime = data['RENTAL_START_TIME']
        rentalPeriod = (endTime - startTime).seconds
        DURATION_minutes=(rentalPeriod/60)
        
        cursor.execute('SELECT BIKE_RENTAL_PRICE FROM bike WHERE BIKE_ID = %s', bikeId)
        bike = cursor.fetchone()
        bikeprice=bike['BIKE_RENTAL_PRICE']
        #Calculation balance:Uncertain policy
        
        Balance=0.00
        if int(sub)==1:
           balance=float(float(DURATION_minutes)*float(bikeprice)*0.8)
        else:
           balance=float(float(DURATION_minutes)*float(bikeprice))
        Balance=round(balance,2)
        #insert the data    
        cursor.execute('UPDATE rentallog SET RENTAL_END_BSID=%s,RENTAL_END_TIME=%s,RENTAL_DURATION=%s,RENTAL_PRICE=%s WHERE RENTAL_USER_ID = %s AND RENTAL_PRICE is NULL', (endstation,endtime, DURATION_minutes, Balance,userId))
        
        cursor.execute("SELECT USER_BALANCE FROM user WHERE USER_ID = %s ",userId)
        data=cursor.fetchone()
        currentBalance = data['USER_BALANCE']
        currentBalance=round((currentBalance-Balance),2)
        cursor.execute('UPDATE user SET USER_BALANCE=%s  WHERE USER_ID = %s', (currentBalance,userId))
        cursor.execute("UPDATE bike SET BIKE_STATUS='0' WHERE BIKE_ID = %s", bikeId)
        cursor.execute("UPDATE bike SET BIKESTATION_ID=%s WHERE BIKE_ID = %s", (endstation,bikeId))
        session['balance']=currentBalance
        db.commit()
        db.close()
        #Return to any view that calls this function and display msg
        msg = 'You have successfully return a bike a bill is create for you!'
        return render_template('Customer_home.html', msg=msg)
    
@app.route('/reportbike/', methods=['POST'])   
def reportBike():
       uId=session['id']
       bikeId=request.form['bike_id']
       print(uId)
       print(bikeId)
       bikePart=request.form['bikeparts']
       commint=request.form['comments']
       dstatus=1
       starttime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
       cursor,db= connectDB()
       cursor.execute("UPDATE bike SET BIKE_HEALTH_STATUS='0' WHERE BIKE_ID = %s ",bikeId)
       cursor.execute('INSERT INTO defectlog VALUES(NULL,%s,%s,%s,%s,%s,NULL,%s)', (bikeId,uId,int(bikePart),dstatus,starttime,commint))
       db.commit()
       db.close()
       msg='The report is successful, we will deal with it as soon as possible!'
       return render_template('Customer_home.html', msg=msg )
@app.route('/repirebike/')   
def repirebike():
       cursor,db= connectDB()
       cursor.execute("SELECT BIKE_ID FROM bike WHERE BIKE_HEALTH_STATUS='0' ")
       bikeneedrepire=cursor.fetchall()
       if bikeneedrepire:
          return render_template('repire_list.html', tot1 = len(bikeneedrepire) ,data1 = bikeneedrepire) 
       else:
          msg='No bike needs to be repaired!'
          return render_template('Operator_home.html',msg=msg)
@app.route('/repirethebike/', methods=['POST'])    
def repirethebike():
       rbikeId = request.form['bike_id']
       repiretime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
       cursor,db= connectDB()
       cursor.execute("UPDATE bike SET BIKE_HEALTH_STATUS='1' WHERE BIKE_ID = %s ",rbikeId)
       cursor.execute("UPDATE defectlog SET DEFECT_STATUS='0',DEFECT_REPAIR_TIMESTAMP=%s WHERE DEFECT_BIKE_ID = %s AND DEFECT_REPAIR_TIMESTAMP is NULL ",(repiretime,rbikeId))
       db.commit()
       db.close()
       msg='The repair is successful'
       return render_template('Operator_home.html',msg=msg)
@app.route('/trickbike/')   
def trickbike():
       cursor,db= connectDB()
       cursor.execute("SELECT BIKE_ID FROM bike WHERE BIKE_STATUS='1' ")
       bikerentede=cursor.fetchall()
       bikepostcode=[]
       cursor.execute("SELECT BIKE_ID,BIKESTATION_ID FROM bike WHERE BIKE_STATUS='0' ")
       freenbike=cursor.fetchall()
       for i in range(len(freenbike)):
           bikesId=freenbike[i]['BIKESTATION_ID']
           cursor.execute("SELECT BS_POSTCODE FROM bikestation WHERE BIKESTATION_ID=%s ",bikesId)
           s=cursor.fetchone()
           bikepostcode.append(s['BS_POSTCODE'])
    
       return render_template('trickbike.html', tot1 = len(bikerentede) ,data1 = bikerentede,tot2=len(freenbike),data2=freenbike,data3=bikepostcode) 
@app.route('/movelist/')
def movelist():
       cursor,db= connectDB()
       bikepostcode=[]
       cursor.execute("SELECT * FROM bike WHERE BIKE_HEALTH_STATUS='1' AND BIKE_STATUS='0' ")
       freenbike=cursor.fetchall()
       
       for i in range(len(freenbike)):
           bikesId=freenbike[i]['BIKESTATION_ID']
           cursor.execute("SELECT BS_POSTCODE FROM bikestation WHERE BIKESTATION_ID=%s ",bikesId)
           s=cursor.fetchone()
           bikepostcode.append(s['BS_POSTCODE'])
       return render_template('move_list_bike.html',tot2=len(freenbike),data2=freenbike,data3=bikepostcode) 
@app.route('/<int:bike_id>/movetoanstation',methods=['GET','POST'])
def movetoanstation(bike_id):
       session["bikeneedtomove"]=bike_id
       return render_template('move_list_bike_goalstation.html') 
@app.route('/moveaction/',methods=['POST'])
def moveaction():
       goalstaionpostcode=request.form['postcoode']
       bikeId=session["bikeneedtomove"]
       cursor,db= connectDB()
       cursor.execute("SELECT * FROM bikestation WHERE BS_POSTCODE=%s",goalstaionpostcode)
       bikesation=cursor.fetchone()
       bikesationnumber=bikesation['BIKESTATION_ID']
       cursor.execute("UPDATE bike SET BIKESTATION_ID=%s WHERE BIKE_ID = %s ",(bikesationnumber,bikeId))
       db.commit()
       db.close()
       msg='The move is successful'
       return render_template('Operator_home.html',msg=msg)
@app.route('/addbike/')
def addbike():
    return render_template('Addbike.html')  
@app.route('/addabike/',methods=['POST'])
def addabike():
    price= request.form['price']
    goalstaionpostcode=request.form['addpostcode']
    cursor,db= connectDB()
    cursor.execute("SELECT * FROM bikestation WHERE BS_POSTCODE=%s",goalstaionpostcode)
    bikesation=cursor.fetchone()
    bikesationnumber=bikesation['BIKESTATION_ID']
    s1=1
    s2=0
    price=float(price)
    cursor.execute('INSERT INTO bike VALUES (NULL,%s,%s,%s,%s,%s)',('abc',int(bikesationnumber),s1,s2,price))
    db.commit()
    db.close()
    msg='Add a new bike'
    return render_template('Operator_home.html',msg=msg)
@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method =='POST':
        if 'username' in request.form and 'Secret_Question' in request.form and 'password' in request.form and 'pincode' in request.form and 'secret_answer' in request.form:
            emailaddress = request.form['username']
            password = request.form['password']
            phone = request.form['phone']
            user_pincode = request.form['pincode']
            secret_question = request.form['Secret_Question']
            secret_answer = request.form['secret_answer']
            default_balance=5
            bal=float(default_balance)
            usertype=2
            sub=0
            selt_secret_question=int(secret_question)
            cursor,db= connectDB()
            cursor.execute('INSERT INTO user VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (phone, user_pincode,emailaddress,password,bal,usertype,int(selt_secret_question),secret_answer,sub))
            db.commit()
            db.close()
            return redirect(url_for('index'))
    return render_template('Register.html')

if __name__ == '__main__':
    
    app.debug = False # debug model,must be False when product
    app.config["SECRET_KEY"]="nqwoheioqu12317648"
    app.run()