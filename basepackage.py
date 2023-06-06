import smtplib
import random
import sqlite3
class send_through_mail:
    def send_otp(receiver):
        try:
          OTP=random.randint(1000,9999)#generate random number betweenn 1000 and 9999
          content='''write your msg'''+str(OTP)
          server=smtplib.SMTP('smtp.gmail.com',587)
          server.starttls()
          server.login('sender_email_adress','encrpyted password(16 characters)')
          #you can find youtube videos to generate encrpyted password for your email
          server.sendmail('sender_email_adress',receiver,content)
          return OTP,0 # returns OTP send to receiver
        except:
          return 1 # returns 1 when any error occured.
     def send_msg(receiver):
        try:
          content='''write your msg'''
          server=smtplib.SMTP('smtp.gmail.com',587)
          server.starttls()
          server.login('sender_email_adress','encrpyted password(16 characters)')
          #you can find youtube videos to generate encrpyted password for your email
          server.sendmail('sender_email_adress',receiver,content)
          return 0 # returns 0 if message is sent .
        except:
          return 1 # returns 1 when any error occured.
           
class connect_database():
    def __init__(self):
        try:
           self.connection=sqlite3.connect("main.db")
           self.cursor=self.connection.cursor()
           self.cursor.execute('''CREATE TABLE  IF NOT EXISTS TABLE_NAME(attributes datatype)''')
        except:
            print('error occured while establishing connection with database')
    def insert_user_data(self,data):
        #data should be a dictionary
        tuplee=(data['user_name'],data['password'])
        insert_query="INSERT INTO USER_DATA VALUES"+str(tuplee)
        self.cursor.execute(insert_query)
        self.connection.commit()
        return 0
    def retrieve_data(self):
        self.cursor.execute('''SELECT * FROM USER_DATA''')
        present_users_data=self.cursor.fetchall()
        return present_users_data#returns list of tuples
    #connection should be closed all activities
