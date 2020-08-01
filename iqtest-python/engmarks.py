import cgi
import pymysql
import random
import smtplib 
print("Content-type: text/html\r\n\r\n")
form=cgi.FieldStorage()
    
1stanswer=str(form.getvalue('1'))
2ndanswer=str(form.getvalue('2'))
3rdanswer=str(form.getvalue('3'))
4thanswer=str(form.getvalue('4'))
5thanswer=str(form.getvalue('5'))

#Checking for correct answers