from automatico import envia_email

import time

#Enviar O Email de tempos em tempos
'''
while True:
    print('Enviando e-mail')
    envia_email()
    time.sleep(10)
'''
'''
HORA_DEFINIDA = 20
MINUTO_DEFINIDO = 35

#Enviar email em um horario determinado
while True:
    hora_atual   = time.localtime().tm_hour
    minuto_atual = time.localtime().tm_min
    print(f'Hora atual : {hora_atual}: {minuto_atual}')
    if hora_atual == HORA_DEFINIDA and minuto_atual == MINUTO_DEFINIDO:
        print('Enviando e-mail')
        envia_email()

    time.sleep(30)        
'''

lista_email = ['ulissimsqn23@gmail.com', 
            'antoniowandersenai@gmail.com',
            'lsnem22@gmail.com',
            'aquisenai@gmail.com',
            'misterlarry06@gmail.com']
        
for email in lista_email:
    envia_email(email)
    time.sleep(10)
    print('Enviado')


