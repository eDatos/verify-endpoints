from prettyconf import config

SENDGRID_APIKEY = config('SENDGRID_APIKEY')
NOTIFICATION_FROM_ADDR = config('NOTIFICATION_FROM_ADDR')
NOTIFICATION_FROM_NAME = config('NOTIFICATION_FROM_NAME')
NOTIFICATION_TO_ADDRS = config('NOTIFICATION_TO_ADDRS', cast=config.list)
