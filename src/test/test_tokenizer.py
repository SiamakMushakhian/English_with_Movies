from collections import Counter

from src.data import DATA_DIR
from src.parse_subtitle import Subtitle

def test_tokenizer():
    sub_file_path = DATA_DIR / 'subtitles' / 'Game.Of.Thrones.S01E01.1080p.5.1Ch.BluRay.ReEnc-DeeJayAhmed.srt'
    sub = Subtitle(sub_file_path)
    sub.tokenize()

    assert '.' == Counter(sub.words).most_common()[0][0]