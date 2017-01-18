from contextlib import contextmanager


@contextmanager
def log(filename, text):
    fn = open(filename, 'r+')
    fn.write(text)
    yield fn
    fn.close()


with log('example.txt', "\nTexttttt") as f:
    print("In block.")
