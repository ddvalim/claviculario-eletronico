class EOFErrorException(Exception):
    def __init__(self):
        super().__init__("EOF Error")
