import smtplib, ssl
from email.message import EmailMessage
#https://myaccount.google.com/apppasswords # Google App Passwords

def saada_kiri(kellele,kellelt):
    kiri="Tere, see on testkiri!"
    smtp_server="smtp.gmail.com"
    port=587 #465
    #sender_email=kellelt
    password="kwfb sooo qtde xmse"  # Asenda oma rakenduse parooliga
    #receiver_email=kellele
    message=EmailMessage()
    message.set_content(kiri)
    message["Subject"]="Testkiri"
    message["From"]="Marina Oleinik"
    message["To"]=kellele
    context=ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server,port) as server:
            server.starttls(context=context)
            server.login(kellelt,password)
            server.send_message(message)
            print("Kiri saadetud edukalt!") #server.quit()
    except Exception as e:
        print(f"Midagi läks valesti ...{e}")
kellele=input("Sisesta kellele saata: ")
kellelt=input("Sisesta kellelt saata: ")
saada_kiri(kellele,kellelt)