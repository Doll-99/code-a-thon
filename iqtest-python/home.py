import cgi
import pymysql
import random
import smtplib 
print("Content-type: text/html\r\n\r\n")
form=cgi.FieldStorage()
    
noofattempts=str(form.getvalue('noofattempts'))

if noofattempts>1:
	print("""
	    <html>
	        <head>
	        </head>
	        <body>
	            <h1><center>You are not eligible to give test</center></h1>
	        </body>
	    </html>
    """)
else:
	print("Location: http://localhost:8080/iqtest/subject.html\r\n\r\n")