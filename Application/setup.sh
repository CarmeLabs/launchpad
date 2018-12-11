. antenv/bin/activate
pip install azure-cli
az login --service-principal -u 6b4babc2-6161-4be7-83d7-0a431ae7e65e -p meWe6dugYD6Vp+NktOo55E53D5VKsn8ooo97xbjkBjo= --tenant 2a445953-53b6-4847-8084-d3607b7bb4b4
which az > az.txt
az acs kubernetes install-cli
curl -L https://raw.githubusercontent.com/helm/helm/master/scripts/get | bash
rm -f celery*.pid
python manage.py collectstatic --noinput
antenv/bin/celery multi start 2 -A python_webapp_django
GUNICORN_CMD_ARGS="--bind=0.0.0.0 --timeout 600" gunicorn python_webapp_django.wsgi