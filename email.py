import yagmail
import keyring
try:
  yagmail.SMTP('hibernationhacks2021', 'hibernationhacks').send('dama2468@gmail.com', 'Request to View Medical Records', 'Dr. John Doe has requested access to view your documents on your SecuredHealth account. If you would like to grant access, please click the following link www.securehealth.com/myaccount.html')
  print("Email sent successfully")
except:
  print("Error, email was not sent")
