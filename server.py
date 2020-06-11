import sentry_sdk

from bottle import Bottle, run
from sentry_sdk.integrations.bottle import BottleIntegration

import os

# read environment variable
DSN = os.environ['DSN']

sentry_sdk.init(
    dsn=DSN,
    integrations=[BottleIntegration(transaction_style='url')]
)


app = Bottle()


@app.route('/')
def index():
    return 'Howdy!'


@app.route('/success')
def success():
    return 'Everything is alright'


@app.route('/fail')
def fail():
    raise RuntimeError('A terrible error has occurred')
    return


if __name__ == '__main__':
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(
            app,
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 5000)),
            server='gunicorn',
            workers=3,
        )
    else:
        run(app, host='localhost', port=8080, debug=True)
