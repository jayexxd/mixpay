LOCAL_SETTINGS = True
from settings import *
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', #django.db.backends.postgresql',
        'NAME': 'localdb',
        'USER': 'vortex',
        'PASSWORD': 'Bad2655pW',
        'HOST':'localhost',
	# 'PORT':'',
    }
}
