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
