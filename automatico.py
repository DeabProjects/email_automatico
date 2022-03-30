import smtplib
from email.message import EmailMessage


EMAIL_LOGIN = 'deabcontato@gmail.com'
EMAIL_SENHA = '##########'

def envia_email(email_destino):

    mensagem = EmailMessage()

    mensagem['Subject'] = "Podcast"
    mensagem['From'] = EMAIL_LOGIN
    mensagem['To'] = email_destino

    mensagem.set_content('''OLá querido(a) estamos 
                            te convidando, 
                            para ouvir o nosso podcast
                            as 17:00.
                            ''')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
        servidor.login(EMAIL_LOGIN, EMAIL_SENHA)
        servidor.send_message(mensagem)

    
    print('E-mail enviado com sucesso!!!')

