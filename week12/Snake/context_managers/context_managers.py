from contextlib import contextmanager
from datetime import datetime


@contextmanager
def start_log(filename, mode):
    with open(filename, mode) as s:
        s.write("Game started at {}\n".format(datetime.now().isoformat()))
    yield


@contextmanager
def end_log(filename, mode):
    with open(filename, mode) as e:
        e.write("Game ended at {}\n".format(datetime.now().isoformat()))
    yield


@contextmanager
def move_log(filename, mode, direction):
    with open(filename, mode) as r:
        r.write("Game : Snake moved {} on {}\n"
                .format(direction, datetime.now().isoformat()))
    yield


@contextmanager
def food_log(filename, mode):
    with open(filename, mode) as r:
        r.write("Game : Snake ate food on {}\n"
                .format(datetime.now().isoformat()))
    yield
