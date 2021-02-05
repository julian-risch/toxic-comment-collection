# toxic-comment-collection

## Requirements
This script requires the following dependencies to be installed:
- pandas
- openpyxl

## Status
The following Datasets have been included in this project  
leondz/hatespeechdata : https://github.com/leondz/hatespeechdata
|  # | State | Name | Class |
|  - |:-----:| ---- | ----- |
|  1 | Files not found | Are They our Brothers? Analysis and Detection of Religious Hate Speech in the Arabic Twittersphere |  |
|  2 | Done (v1) | Multilingual and Multi-Aspect Hate Speech Analysis (Arabic) | Hate_speech_mlma |
|  3 | Done (v1) | L-HSAB: A Levantine Twitter Dataset for Hate Speech and Abusive Language | Lhsab |
|  4 | Done (v1) | Abusive Language Detection on Arabic Social Media (Twitter) | abusive_lang_twitter_ar |
|  5 | Done (v1) | Abusive Language Detection on Arabic Social Media (Al Jazeera) | abusive_lang_aljazeera_ar |
|  6 | Postponed (OneDrive) | Dataset Construction for the Detection of Anti-Social Behaviour in Online Communication in Arabic |  |
|  7 | Postponed (Login Required) | Datasets of Slovene and Croatian Moderated News Comments |  |
|  8 | Twitter API required | Offensive Language and Hate Speech Detection for Danish |  |
|  9 | Done (v1) | Automated Hate Speech Detection and the Problem of Offensive Language | Ahsd_en |
| 10 | Done (v1) | Hate Speech Dataset from a White Supremacy Forum | White_supremacy_forum_en |
| 11 | Twitter API required | Hateful Symbols or Hateful People? Predictive Features for Hate Speech Detection on Twitter |  |
| 12 | Done (v1) | Detecting Online Hate Speech Using Context Aware Models | Fox_news_user_comments_en |
| 13 | Twitter API required | Are You a Racist or Am I Seeing Things? Annotator Influence on Hate Speech Detection on Twitter |  |
| 14 | Twitter API required | When Does a Compliment Become Sexist? Analysis and Classification of Ambivalent Sexism Using Twitter Data |  |
| 15 | Password required | Overview of the Task on Automatic Misogyny Identification at IberEval 2018 (English) |  |
| 16 | Done (v1) | CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech (English) | Conan |
| 17 | Not suited | Characterizing and Detecting Hateful Users on Twitter |  |
| 18 | Done (v1) | A Benchmark Dataset for Learning to Intervene in Online Hate Speech (Gab) | Intervene_online_hs_en |
| 19 | Done (v1) | A Benchmark Dataset for Learning to Intervene in Online Hate Speech (Reddit) | Intervene_online_hs_en |
| 20 | Done (v1) | Multilingual and Multi-Aspect Hate Speech Analysis (English) | Hate_speech_mlma |
| 21 |  |  |  |
| 22 |  |  |  |
| 23 |  |  |  |
| 24 |  |  |  |
| 25 |  |  |  |
| 26 |  |  |  |
| 27 |  |  |  |
| 28 |  |  |  |
| 29 |  |  |  |
| 30 |  |  |  |
| 31 |  |  |  |
| 32 |  |  |  |
| 33 |  |  |  |
| 34 |  |  |  |
| 35 |  |  |  |
| 36 |  |  |  |
| 37 |  |  |  |
| 38 |  |  |  |
| 39 |  |  |  |
| 40 |  |  |  |
| 41 |  |  |  |
| 42 |  |  |  |
| 43 |  |  |  |
| 44 |  |  |  |
| 45 |  |  |  |
| 46 |  |  |  |
| 47 |  |  |  |
| 48 |  |  |  |
| 49 |  |  |  |
| 50 |  |  |  |
| 51 |  |  |  |
| 52 |  |  |  |
| 53 |  |  |  |
| 54 |  |  |  |
| 55 |  |  |  |
| 56 |  |  |  |
| 57 |  |  |  |
| 58 |  |  |  |
| 59 |  |  |  |
| 60 |  |  |  |
| 61 |  |  |  |
| 62 |  |  |  |
| 63 |  |  |  |

## Next Steps
### Implementation
* ~~logging https://docs.python.org/3/howto/logging.html~~
* ~~progress bar, tqdm https://github.com/tqdm/tqdm~~
* ~~let's add a requirements.txt so that users can simply run `pip install -r requirements.txt`~~

### Store per csv file: 
* name of the file, e.g., authorYEARlang (schmidt2021de)
* hash (to check whether any changes have been made to the dataset)
* language (en, de)
* source platform (Twitter, ...)

### Store per row in each csv file:
* id (str)
* text (str)
* label1 (str), 
* label2 (str)
This list can be extended later (timestamp, response text, ...)
Let's not use booleans or integers as values in the label column but more explicit strings, such as "offensive"
