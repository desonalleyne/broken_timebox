from datetime import datetime
from random import randint
from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():

    sides = ['to', 'past']
    d = datetime.now()
    min_delta = randint(1,120)

    side_idx = randint(1,1)
    side = sides[side_idx]

    hour = d.hour
    minute = d.minute

    if side_idx == 0:
        minute = minute + min_delta
        if minute > 59:
            hour = hour + (minute / 60)
            minute = minute % 60
    else:
        minute = minute - min_delta
        if minute < 0:
            hour = hour + (minute / 60)
            minute = minute % 60

    return "The time is {} minute{} {} {}:{:02d}".format(min_delta, 's' if min_delta > 1 else '', side,hour,minute)

app.run('0.0.0.0', 8000)
