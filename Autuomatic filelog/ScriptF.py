import os
import time
import psutil
from sys import *
import schedule
from datetime import datetime
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def ProcessDisplay(FolderName = "PC-Vaibhav"):
    Data = []
    
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        
    File_Path = os.path.join(FolderName,"Marvellous%s.log"%time.ctime())
    File_Path = (File_Path.replace(" ","").replace(":",""))
    fd = open(File_Path,"w")
    
    
    for proc in psutil.process_iter():
        value = proc.as_dict(attrs = ['pid','name','username'])
        Data.append(value)
        
    for element in Data:
        fd.write("%s\n"% element)



    subject = "An email with attachment from Python"
    body = "This is an email with attachment sent from Python"
    sender_email = "vaibhavjaisingpure862@gmail.com"
    receiver_email = "pankajgulhane866@gmail.com"   
    password = "outuewyrpo"

# Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
    message.attach(MIMEText(body, "plain"))

    # filename = File_Path  # In same directory as script

# Open PDF file in binary mode
    with open(File_Path, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

# Add header as key/value pair to attachment part
    part.add_header("Content-Disposition",f"attachment; filename= {File_Path}",)

# Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

# Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

    server.quit()
    print("Mail Sent")





def main():
    print("------ Marvellous Infosystems ------")
    print("Script title : "+argv[0])
    
    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application_Name Scheule_Time Directory_Name")
        exit()    
        
    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : It is used to create log file of running processess")
        exit()
            
    schedule.every(int(argv[1])).minutes.do(ProcessDisplay)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()
