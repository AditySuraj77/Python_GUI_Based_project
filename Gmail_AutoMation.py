
import smtplib as st

ob = st.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('adity0to9@gmail.com','havplvbrwpfdbbun')

subject = 'Python Gmail Testing'

body = ' Using Gmail with Python Woo Its Working Nice Great ! '

message = 'subject:{}\n\n{}'.format(subject,body)

recive = ['adity0to9@gmail.com']

ob.sendmail('adity0to9@gmail.com',recive,message)
print('Sent Sucessfully ! ')

ob.quit()