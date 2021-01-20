import smtplib
from email.message import EmailMessage

import config


def notify(failing_entrypoints):
    failing_entrypoints = '\n'.join(failing_entrypoints)
    subject = '⚠️ Aviso sobre API entrypoints'
    content = f'''Hola,

Los siguientes API entrypoints parecen estar dando problemas:

{failing_entrypoints}

Saludos,
El equipo de informática.
'''

    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = config.NOTIFICATION_FROM_ADDR
    msg['To'] = config.NOTIFICATION_TO_ADDRS

    s = smtplib.SMTP(config.SMTP_SERVER, port=config.SMTP_PORT)
    s.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)
    s.send_message(msg)
    s.quit()
