import smtplib
from email.message import EmailMessage

from istacpy.indicators.lite import indicators

import config


def verify_indicators():
    failing_entrypoints = []
    all_indicators = indicators.get_indicators()
    for indicator_code, _ in all_indicators:
        indicator = indicators.get_indicator(indicator_code)
        try:
            indicator.get_data()
        except Exception:
            failing_entrypoints.append(
                indicator.api_response.get('selfLink', indicator_code)
            )
    return failing_entrypoints


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


if __name__ == "__main__":
    failing_entrypoints = verify_indicators()
    if failing_entrypoints:
        notify(failing_entrypoints)
