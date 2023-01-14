#!/bin/sh

echo 'Preparing Deployment...'
echo "web: python manage.py migrate && gunicorn locallibrary.wsgi" > "Procfile"
echo 'Created Procfile'
pip3 install gunicorn dj-database-url psycopg2-binary whitenoise
echo "
################################################
##### Generated by prep-deploy.sh #############
################################################
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
ALLOWED_HOSTS = ['.railway.app', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['.railway.app']
CSRF_TRUSTED_ORIGINS = ['https://*.railway.app']
DEBUG = os.getenv('DEBUG', False) == 'True'
##############################################
##############################################
##############################################
" >> './locallibrary/settings.py'
echo "python-3.10.2" > "runtime.txt"
echo "Created runtime.txt"
pip3 freeze > requirements.txt
echo "Created requirements.txt"
python3 manage.py check --deploy
echo "
##############################################
##############################################
##############################################
Check settings.py for any duplicates or mistakes
##############################################
##############################################
##############################################
"