#!.venv/bin/python
from app import app


app.config.from_object('config.BaseConfig')

if __name__ == '__main__':
    app.run(port=4999)
