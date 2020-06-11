## Установить переменную окружения  
heroku config:set DSN=https://_some_data_source_name_.ingest.sentry.io/5255034  

## Прочитать переменную окружения  
DSN = os.environ['DSN']  
