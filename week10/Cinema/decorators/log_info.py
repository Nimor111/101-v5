from datetime import datetime


def log_info(func):
    """
    Log every reservation into a file
    """
    def accepter(*args, **kwargs):
        @wraps(func)
        with open("log_info.txt") as f:
            f.write("Reservation made on {}".format(str(datetime.now())))
        return func(*args, **kwargs)
    return accepter
