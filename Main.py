import smtplib 
import os
import imaplib
import stdiomask

def loadContacts(filename):
  with open(filename, 'w') as file:
    return eval(file.read())
  
def ListInbox():
  imap_server.select()
  _, message_numbers_raw = imap_server.search(None, 'ALL')
  for message_number in message_numbers_raw[0].split():
      _, msg = imap_server.fetch(message_number, '(RFC822)')
      print(msg[0][1])


def SendMail(contacts):
  destination = input("Enter the email you want to send this to: ") #todo: save contacts
  if destination in contacts:
    destination = contacts[destination]
  else:
    print("ERROR: Could not find that person in your contact list")
  message = input("What would you like to say? ") #todo: allow markdown 
  try:
    server.sendmail(
      username,
      destination,
      message
    )
  except(smtplib.SMTPRecipientsRefused):
    print("ERROR: Can not contact that person")

def clear():
  if os.name == "posix":
    os.system("clear")
  if os.name == "nt":
    os.system("cls")

contacts = loadContacts('contacts.json')
mail_server = 'imap.gmail.com'
imap_server = imaplib.IMAP4_SSL(host=mail_server)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
username = ""
password = ""
commands = {
   "Q":exit,
   "H":lambda : print(commands), 
   "C":clear, 
   "S":lambda : SendMail(contacts),
   "L":ListInbox
}

while 1: # need to figure out how to allow my password not be saved 
    username = input("Enter Username: ") 
    password = stdiomask.getpass(prompt=': ', mask='*') 
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
    commands[task]() 
  else:
    print('Input invalid, type "HELP" too see the list of commands.')
    # todo: I need to make a way to view emails and save contacts
