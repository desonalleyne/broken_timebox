from datetime import datetime
from random import randint
from flask import Flask, render_template
from configparser import ConfigParser 

cp = ConfigParser()
cp.read('config.cfg')
lower_m_delta = cp.getint('general','lower_m_delta')
upper_m_delta = cp.getint('general','upper_m_delta')
port = cp.getint('general','port')

app = Flask(__name__)

@app.route('/')
def root():

    sides = ['to', 'past']
    d = datetime.now()
    min_delta = randint(lower_m_delta,upper_m_delta)

    side_idx = randint(0,1)
    side = sides[side_idx]

    hour = d.hour
    minute = d.minute

    if side_idx == 0:
        minute = minute + min_delta
        if minute > 59:
            hour = (hour + (minute / 60)) % 24
            minute = minute % 60
    else:
        minute = minute - min_delta
        if minute < 0:
            hour = (hour + (minute / 60)) % 24
            minute = minute % 60
    broken_time = "The time is {} minute{} {} {:02d}:{:02d} hrs".format(min_delta, 's' if min_delta > 1 else '', side, int(hour), int(minute))
    return render_template('home.html', broken_time=broken_time)

app.run('0.0.0.0', port, debug=True)
