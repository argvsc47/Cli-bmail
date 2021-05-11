import smtplib 
import os
import imaplib

def SendMail():
  destination = input("Enter the email you want to send this to: ") #todo: save contacts
  message = input("What would you like to say? ") #todo: allow markdown 
  server.sendmail(
    username,
    destination,
    message
  )

def clear():
  if os.name == "posix":
    os.system("clear")
  if os.name == "nt":
    os.system("cls")

mail_server = 'imap.gmail.com'
imap_server = imaplib.IMAP4_SSL(host=mail_server)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
username = ""
password = ""
commands = {
   "Q":"exit()",
   "H":"print(commands)", 
   "C":"clear()" # todo: fix clear error
}

while 1: # need to figure out how to allow my password ot be saved 
    username = input("Enter Username: ") 
    password = input("Enter password: ")
    try:
      server.login(username, password)
      imap_server.login(username, password)
      break 
    except(smtplib.SMTPAuthenticationError):
      print("Either your username or password is incorrect please try again")
      # I need to figure out how to be able to login without making it less secure 

while 1:
  task = input(": ").upper()
  if task in commands:
    exec(commands[task]) 
  elif task == "S":
    SendMail()
  else:
    print('Input invalid, type "HELP" too see the list of commands.')
    # todo: I need to make a way to view emails
   
