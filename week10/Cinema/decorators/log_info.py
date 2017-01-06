from datetime import datetime


def log_info(func):
    """
    Log every reservation into a file
    """
    def accepter(*args, **kwargs):
        with open("log_info.txt", 'a') as f:
            f.write("Reservation made on {}\n".format(str(datetime.now())))
        return func(*args, **kwargs)
    return accepter
