import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)

server.login('nico.penaredondo@gmail.com','Trini12tas')

msg ="\n Hello!!!!!!!!!!!!! Sent from python script"
server.sendmail("nico.penaredondo@highlysucceedlimited.com","nico.penaredondo@highlysucceedlimited.com",msg)