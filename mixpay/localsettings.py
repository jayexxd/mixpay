LOCAL_SETTINGS = True
from settings import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', #django.db.backends.postgresql',
        'NAME': 'mixpaydb',
        'USER': 'fanpu',
        'PASSWORD': 'isitpublicornot',
        'HOST':'localhost',
	# 'PORT':'',
    }
}
