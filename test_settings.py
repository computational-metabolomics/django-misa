import os
SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'gfiles',
    'metab',
    'misa',




    'easy_thumbnails',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
DEBUG = True


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test-django-mogi',
    }
}


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'djangobower.finders.BowerFinder',
)

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."),
)

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')


STATIC_URL='/static/'

EXTERNAL_DATA_ROOTS = { 'RDS': {

                            'path': '/tmp',
                            'user_dirs': True,
                            'help_text': 'Research data store for current user',
                            'filepathfield': False   # if false will use charfield path, if true filepathfield will look
                                                    # recursively in a selected folder but will be to slow for complicated
                                                    # folder structure
                            },
                        'DMA': {

                            'path': '/tmp/',
                            'user_dirs': False,
                            'help_text': 'Deep Metabolome Annotation research data store',
                            'filepathfield': False
                         }
                        }