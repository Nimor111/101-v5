class PandaAlreadyThereError(Exception):

    def __init__(self, message):
        super(PandaAlreadyThereError, self).__init__(message)