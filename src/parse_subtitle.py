import pysrt


class Subtitle:
    def __init__(self, file_path):
        subs = pysrt.open(file_path)

    def tokenize(self):
        # TODO: parse subtitle and return token
        words = []

        return words