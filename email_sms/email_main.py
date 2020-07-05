import email_sms.config as config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.utils
import imaplib
from email.mime.base import MIMEBase
from email import encoders

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(config.FROM_ADDR, config.PASSWORD)
    msg = "Some nice msg"
    server.sendmail(config.FROM_ADDR, config.TO_ADDR, msg)
    server.quit()


def encrypted_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    try:
        server.set_debuglevel(True)
        print('Sending ehlo')
        server.ehlo()
        if server.has_extn('STARTTLS'):
            print('Starting TLS Session')
            server.starttls()
            print('Sending ehlo again')
            server.ehlo()
    finally:
        server.quit()


def send_mime_email():
    fromaddr = config.FROM_ADDR
    toaddr = config.TO_ADDR
    msg = MIMEMultipart()
    msg['Subject'] = "Hello from the Author of Automate It!"
    msg['To'] = email.utils.formataddr(('Recipient', toaddr))
    msg['From'] = email.utils.formataddr(('Author', fromaddr))
    body = "What a wonderful world!"
    msgBody = MIMEText(body, 'plain')
    msg.attach(msgBody)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, config.PASSWORD)
    text = msg.as_string()
    print(f'Text is: {text}')
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def send_attachment_email():
    fromaddr = config.FROM_ADDR
    toaddr = config.TO_ADDR
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Email with an attachment"
    body = "Click to open the attachment"
    msg.attach(MIMEText(body, 'plain'))
    filename = "attach.txt"
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment;filename = % s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, config.PASSWORD)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def connect_to_inbox():
    M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    M.login(config.FROM_ADDR, config.PASSWORD)
    print('Inbox:', M.list())
    M.logout()


def get_messages():
    M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    M.login(config.FROM_ADDR, config.PASSWORD)
    M.select("INBOX")
    typ, data = M.search(None, '(SUBJECT "Email with an attachment")')
    typs, msg = M.fetch(data[0].split()[-1], '(RFC822)')
    print("Message is ", msg[0][1])
    M.close()
    M.logout()



