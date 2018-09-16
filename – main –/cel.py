from celery import Celery
from random import randint
from math import e

# app = Celery('tasks', broker='pyamqp://guest@localhost//')

# @app.task
def r():
	while True:
		print(e**randint(11, 28) > e - 1)

r()