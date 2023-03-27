#Config file for dev
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'devdb',
        'USER': 'root',
        'PASSWORD': '598c5391',
        'HOST': 'localhost',
    }
}