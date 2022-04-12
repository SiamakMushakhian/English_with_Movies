import pysrt
from loguru import logger
from nltk.tokenize import word_tokenize
from tqdm import tqdm


class Subtitle:
    def __init__(self, file_path):
        self.subs = pysrt.open(file_path)
        self.words = []

    def tokenize(self):
        logger.info('Tokenizing subtitle ...')
        for sub in self.subs:
            self.words.extend(word_tokenize(sub.text))

if __name__ == '__main__':
    from collections import Counter

    from src.data import DATA_DIR

    sub_file_path = DATA_DIR / 'subtitles' / 'Game.Of.Thrones.S01E01.1080p.5.1Ch.BluRay.ReEnc-DeeJayAhmed.srt'
    sub = Subtitle(sub_file_path)
    sub.tokenize()
    print('Most common words:', Counter(sub.words).most_common(10))
