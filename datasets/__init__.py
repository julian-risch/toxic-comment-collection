from . import hate_speech_mlma
from . import lhsab
from . import abusive_lang_twitter_ar
from . import abusive_lang_aljazeera_ar

def get_datasets():
    return [
        hate_speech_mlma.Hate_speech_mlma(),
        lhsab.Lhsab(),
        abusive_lang_twitter_ar.Abusive_lang_twitter_ar(),
        abusive_lang_aljazeera_ar.Abusive_lang_aljazeera_ar()
    ]