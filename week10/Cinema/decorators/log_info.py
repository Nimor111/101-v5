from datetime import datetime


def log_info(func):
    def accepter(*args, **kwargs):
        @wraps(func)
        with open("log_info.txt") as f:
            f.write("Reservation made on {}".format(str(datetime.now())))
        return func
    return accepter
