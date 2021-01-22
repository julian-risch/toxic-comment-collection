from . import hate_speech_mlma
from . import lhsab
from . import tweet_classification

def get_datasets():
    return [
        hate_speech_mlma.Hate_speech_mlma(),
        lhsab.Lhsab(),
        tweet_classification.Tweet_classification()
    ]