import smtplib 
import os

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
settings = [] # todo: save settings and make settings in a json files 
username = ""
password = ""
counter = 0
commands = {
   "Q":"exit()",
   "H":"print(commands)", 
   "C":"os.system('clear')", 
}


def SendMail():
  destination = input("Enter the email you want to send this to: ") #todo: save contacts
  message = input("What would you like to say? ") #todo: allow markdown 
  server.sendmail(
    username,
    destination,
    message
  )

while 1: # need to figure out how to allow my password ot be saved 
    username = input("Enter Username: ") 
    password = input("Enter password: ")
    try:
      server.login(username, password)
      break 
    except(smtplib.SMTPAuthenticationError):
      print("Either your username or password is incorrect please try again  make sure to disable secure connection  https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NmLq2JKrgRmgzTtfbkoStaMUeFNvhUpioaAEd3fLzZCUBkFNTMyAJs7rNCFi2YwBRTM7nnCj9J8Vkfn0nv3YhCPD3pKw")
      # I need to figure out how to be able to login without making it less secure 

while 1:
  task = input(": ").upper()
  if task in commands:
    exec(commands[task]) 
  if task == "S":
    SendMail()
  else:
    print('Input invalid, type "HELP" too see the list of commands.')
    # todo: I need to make a way to view emails
