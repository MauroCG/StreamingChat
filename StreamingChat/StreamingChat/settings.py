from unipath import Path

BASE_DIR = Path(__file__).ancestor(2)

SECRET_KEY = 'bkkh0h7&c()lx#cqvo4nq+=@^$xwjehl#bs(2bb^@8qd3sbd3@'

DEBUG = True

ALLOWED_HOSTS = ['*']


DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'social_django',
    'channels',
)

LOCAL_APPS = (
    'apps.login',
    'apps.chat',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'StreamingChat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'StreamingChat.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'chat2',
        'USER': 'postgres',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]


# Settings for python social auth

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'
SOCIAL_AUTH_LOGIN_URL = 'login'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'index'
SOCIAL_AUTH_LOGOUT_REDIRECT_URL = 'login'

SOCIAL_AUTH_FACEBOOK_KEY = '2194934260560558'
SOCIAL_AUTH_FACEBOOK_SECRET = '212212a484931ec18cc44e67962d3689'

SOCIAL_AUTH_INSTAGRAM_KEY = 'db5686757c764366a28291b3bf04363f'         
SOCIAL_AUTH_INSTAGRAM_SECRET = '99d12232608c4c73b1179c8fe02080f3' 
SOCIAL_AUTH_INSTAGRAM_EXTRA_DATA = [('user', 'user'),]

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email'] 
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       
    'fields': 'id, name, email, link'
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                
        ('name', 'name'),
        ('email', 'email'),
        ('link', 'profile_url'),
    ]


# Settings for django channels

ASGI_APPLICATION = 'StreamingChat.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}