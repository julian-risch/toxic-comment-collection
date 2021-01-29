from . import hate_speech_mlma
from . import lhsab
from . import abusive_lang_twitter_ar
from . import abusive_lang_aljazeera_ar
from . import ahsd_en
from . import white_supremacy_forum_en
from . import fox_news_user_comments_en

def get_datasets():
    return [
        hate_speech_mlma.Hate_speech_mlma(),
        lhsab.Lhsab(),
        abusive_lang_twitter_ar.Abusive_lang_twitter_ar(),
        abusive_lang_aljazeera_ar.Abusive_lang_aljazeera_ar(),
        ahsd_en.Ahsd_en(),
        white_supremacy_forum_en.White_supremacy_forum_en(),
        fox_news_user_comments_en.Fox_news_user_comments_en()
    ]