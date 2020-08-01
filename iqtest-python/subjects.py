import cgi
import pymysql
import random
import smtplib 
print("Content-type: text/html\r\n\r\n")
form=cgi.FieldStorage()



if str(form.getvalue('apt')):
	print("Location: http://localhost:8080/iqtest/aptque.html\r\n\r\n")

elif str(form.getvalue('eng')):
	print("Location: http://localhost:8080/iqtest/engque.html\r\n\r\n")

elif str(form.getvalue('math')):
	print("Location: http://localhost:8080/iqtest/mathque.html\r\n\r\n")

elif str(form.getvalue('gk')):
	print("Location: http://localhost:8080/iqtest/gkque.html\r\n\r\n")

elif str(form.getvalue('exit')):
	print("Location: http://localhost:8080/iqtest/home.html\r\n\r\n")