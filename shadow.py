import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def print_banner():
    print("""
    _____ _               _                                  _           
   / ____| |             | |                                | |          
  | (___ | |__   __ _  __| | _____      _____  ___ _ __   __| | ___ _ __ 
  \___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / / __|/ _ \ '_ \ / _` |/ _ \ '__|
  ____) | | | | (_| | (_| | (_) \ V  V /\__ \  __/ | | | (_| |  __/ |   
  |_____/|_| |_|\__,_|\__,_|\___/ \_/\_/ |___/\___|_| |_|\__,_|\___|_|   
                                                                        
    
    Welcome to Shadowsender - Your anonymous scare mail tool!

    This tool is for educational purposes only.
    Do not use for malicious activities.
    """)

def load_email_credentials():
    email_file = 'login/my-mails.txt'
    if os.path.exists(email_file):
        with open(email_file, 'r') as f:
            credentials = f.read().splitlines()
            if len(credentials) >= 2:
                email = credentials[0].split('=')[1].strip()
                password = credentials[1].split('=')[1].strip()
                return email, password
    return None, None

def load_smtp_config():
    smtp_file = 'login/my-smtp.txt'
    if os.path.exists(smtp_file):
        with open(smtp_file, 'r') as f:
            config = f.read().splitlines()
            if len(config) >= 4:
                host = config[0].split('=')[1].strip()
                port = config[1].split('=')[1].strip()
                user = config[2].split('=')[1].strip()
                password = config[3].split('=')[1].strip()
                return host, port, user, password
    return None, None, None, None

def send_email_via_smtp(host, port, user, password, to_email, subject, body):
    try:
        # Connect to SMTP server
        server = smtplib.SMTP(host, port)
        server.starttls()  # If TLS is needed
        server.login(user, password)

        # Compose email
        message = MIMEMultipart()
        message['From'] = user
        message['To'] = to_email
        message['Subject'] = subject

        message.attach(MIMEText(body, 'plain'))

        # Send email
        server.sendmail(user, to_email, message.as_string())
        server.quit()

        print(f"[+] Email sent to {to_email}")
    except Exception as e:
        print(f"[-] Failed to send email: {str(e)}")

def send_email_via_credentials(email, password, to_email, subject, body):
    try:
        # Connect to Gmail SMTP server (or any other service you configure)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)

        # Compose email
        message = MIMEMultipart()
        message['From'] = email
        message['To'] = to_email
        message['Subject'] = subject

        message.attach(MIMEText(body, 'plain'))

        # Send email
        server.sendmail(email, to_email, message.as_string())
        server.quit()

        print(f"[+] Email sent to {to_email}")
    except Exception as e:
        print(f"[-] Failed to send email: {str(e)}")

def main():
    print_banner()

    email, password = load_email_credentials()
    smtp_host, smtp_port, smtp_user, smtp_password = load_smtp_config()

    if not email and not smtp_host:
        print("[!] No credentials found.")
        use_saved_email = input("[?] Do you want to login using saved email credentials? (y/n): ").strip().lower()

        if use_saved_email == 'y' and email:
            print("[+] Using saved email credentials...")
        else:
            print("[!] Please add your credentials in 'login/my-mails.txt'. Exiting...")
            return

    if email:
        print(f"[+] Using saved email: {email}")
        email_chosen = True
    else:
        print("[!] Email credentials not found!")
        email_chosen = False

    if smtp_host:
        print(f"[+] Using saved SMTP: {smtp_host}")
        smtp_chosen = True
    else:
        print("[!] SMTP configuration not found!")
        smtp_chosen = False

    if not email_chosen and not smtp_chosen:
        print("[!] No valid credentials or SMTP configuration found. Exiting...")
        return

    recipient_email = input("Enter recipient email: ").strip()
    subject = input("Enter subject: ").strip()
    body = input("Enter email body: ").strip()

    if smtp_chosen:
        send_email_via_smtp(smtp_host, smtp_port, smtp_user, smtp_password, recipient_email, subject, body)
    elif email_chosen:
        send_email_via_credentials(email, password, recipient_email, subject, body)

if __name__ == "__main__":
    main()
