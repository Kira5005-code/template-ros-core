#! /usr/local/bin/python

# -*- coding: utf-8 -*-

import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import Encoders

def send_mail(to, denis_msg):
    SMTPserver = 'smtp.mail.ru'
    sender = 'jeka.sudakov@mail.ru'
    destination = [to]

    USERNAME = "jeka.sudakov@mail.ru"
    PASSWORD = "777petuxov"

    text_subtype = 'txt'
    #with open("graph.txt", "rb") as f:
     #   content = f.read()


    try:
      #  part1 = MIMEText(content, text_subtype)
        part2 = MIMEText(denis_msg, 'txt')
        msg = MIMEMultipart('alternative')
       # msg.attach(part1)
        msg.attach(part2)

       # filepath = 'meme.jpg'
       # with open(filepath, 'rb') as f:
        #    img = MIMEImage(f.read())

       # img.add_header('Content-Disposition',
         #              'attachment',
          #             filename=os.path.basename(filepath))
       # msg.attach(img)

        #part = MIMEBase('application', "octet-stream")
        #part.set_payload(open("book.pdf", "rb").read())
        #Encoders.encode_base64(part)

        #part.add_header('Content-Disposition', 'attachment; filename="text.txt"')

        #msg.attach(part)

        msg['Subject']= "hello"
        msg['From']   = sender # some SMTP servers will do this automatically, not all
        msg['To'] = to
        conn = smtplib.SMTP_SSL(SMTPserver, 465)
        conn.set_debuglevel(False)
        conn.login(USERNAME, PASSWORD)
        try:
            conn.sendmail(sender, destination, msg.as_string())
        finally:
            conn.quit()
    except Exception:
        sys.exit( "mail failed; %s" % str(Exception) ) # give a error message



send_mail("jeka.sudakov@mail.ru", "gfhf")
