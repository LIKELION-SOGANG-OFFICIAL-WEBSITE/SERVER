"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os
import pymysql

pymysql.install_as_MySQLdb()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

load_dotenv()
# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure--0*)1%0g=&ysu!&q(49^f643l2lubc0^c%(c)%(0a54-0%(urv'
SECRET_KEY=os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

    # # 퍼블릭 ip
    # '43.201.6.43:8000',
    # '43.201.6.43',
    # # 프론트
    # 'https://likelion-website.vercel.app/',
    # # 백
    # 'https://api.likelionsg.store',
    # # 프라이빗 ip
    # '172.31.2.232:8000',
    # '172.31.2.232',

ALLOWED_HOSTS = ['*',]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',

    'corsheaders',
    
    #앱
    'application',
    'project',
    'people',
    'visit',
    'generation',

    # S3
    'storages',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # 최상단에 추가해주기
    'django.middleware.common.CommonMiddleware', # cors error 해결
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS 설정
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    # 퍼블릭 ip
    '43.201.6.43:8000',
    '43.201.6.43',
    # 프론트
    'likelion-website.vercel.app/',
    "localhost:3000",
    # 백
    'api.likelionsg.store',
    "127.0.0.1:8000",
    # 프라이빗 ip
    '172.31.2.232:8000',
    '172.31.2.232',
]

# CSRF 설정
CSRF_TRUSTED_ORIGINS = [

    # # 퍼블릭 ip
    'http://43.201.6.43:8000',
    'http://43.201.6.43',
    # 프론트
    'https://likelion-website.vercel.app/',
    "http://localhost:3000",
    # 백
    'https://api.likelionsg.store',
    "http://127.0.0.1:8000",
    # 프라이빗 ip
    'http://172.31.2.232:8000',
    'http://172.31.2.232',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates/application/email/'), #이메일 양식
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        
        # RDS 연동
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : os.environ['DB_NAME'],
        'USER' : os.environ['DB_USER'],
        'PASSWORD' : os.environ['DB_PASSWORD'],
        'HOST' : os.environ['DB_HOST'],
        'PORT' : '3306',
        'OPTIONS':{
            'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# STATIC_URL = 'static/'
STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_ROOT =  os.path.join(BASE_DIR, 'static')


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER =  os.environ['EMAIL_ID'] #인증 이메일 발신자
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASSWORD']  #발신자 이메일 앱 비밀번호
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# media
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

#AWS S3

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'likelion-sg-website-bucket'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME,AWS_REGION)


DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_DEFAULT_ACL = 'public-read'  # 파일에 대한 기본 ACL 설정
AWS_S3_FILE_OVERWRITE = True # 같은 이름의 파일이 있으면 오버라이딩
AWS_QUERYSTRING_AUTH = False
