from sendgrify.core import SendGrid

import config

sendgrid_handler = SendGrid(
    api_key=config.SENDGRID_APIKEY,
    from_addr=config.NOTIFICATION_FROM_ADDR,
    from_name=config.NOTIFICATION_FROM_NAME,
)


def notify(failing_entrypoints):
    failing_entrypoints = '\n'.join(failing_entrypoints)
    subject = '⚠️ Aviso sobre API entrypoints'
    msg = f'''Hola,

Los siguientes API entrypoints parecen estar dando problemas:

{failing_entrypoints}

Saludos,
El equipo de informática.
'''
    sendgrid_handler.send(to=config.NOTIFICATION_TO_ADDRS, subject=subject, msg=msg)
