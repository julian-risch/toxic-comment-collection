# toxic-comment-collection

## Requirements
This script requires the following dependencies to be installed:
- pandas
- openpyxl

## Status
The following Datasets have been included in this project  
leondz/hatespeechdata : https://github.com/leondz/hatespeechdata 

(can be accessed via : http://ckan.hatespeechdata.com)
|  # | State | Name | Class |
|  - |:-----:| ---- | ----- |
|  1 | Files not found | Are They our Brothers? Analysis and Detection of Religious Hate Speech in the Arabic Twittersphere |  |
|  2 | Done (v3) | Multilingual and Multi-Aspect Hate Speech Analysis (Arabic) | Ousidhoum2019 |
|  3 | Done (v3) | L-HSAB: A Levantine Twitter Dataset for Hate Speech and Abusive Language | mulki2019 |
|  4 | Done (v3) | Abusive Language Detection on Arabic Social Media (Twitter) | Mubarak2017twitter |
|  5 | Done (v3) | Abusive Language Detection on Arabic Social Media (Al Jazeera) | Mubarak2017aljazeera|
|  6 | Postponed (OneDrive) | Dataset Construction for the Detection of Anti-Social Behaviour in Online Communication in Arabic |  |
|  7 | Postponed (Login Required) | Datasets of Slovene and Croatian Moderated News Comments |  |
|  8 | Twitter API required | Offensive Language and Hate Speech Detection for Danish |  |
|  9 | Done (v3) | Automated Hate Speech Detection and the Problem of Offensive Language | Davidson2017 |
| 10 | Done (v3) | Hate Speech Dataset from a White Supremacy Forum | Gibert2018 |
| 11 | Done (v3) | Hateful Symbols or Hateful People? Predictive Features for Hate Speech Detection on Twitter | Waseem2016 |
| 12 | Done (v3) | Detecting Online Hate Speech Using Context Aware Models | Gao2018 |
| 13 | Done (v3) | Are You a Racist or Am I Seeing Things? Annotator Influence on Hate Speech Detection on Twitter | Waseem2016 |
| 14 | Done (v3) | When Does a Compliment Become Sexist? Analysis and Classification of Ambivalent Sexism Using Twitter Data | Jha2017 |
| 15 | Password required | Overview of the Task on Automatic Misogyny Identification at IberEval 2018 (English) |  |
| 16 | Done (v3) | CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech (English) | Chung2019 |
| 17 | Not suited | Characterizing and Detecting Hateful Users on Twitter |  |
| 18 | Done (v3) | A Benchmark Dataset for Learning to Intervene in Online Hate Speech (Gab) | Qian2019 |
| 19 | Done (v3) | A Benchmark Dataset for Learning to Intervene in Online Hate Speech (Reddit) | Qian2019 |
| 20 | Done (v3) | Multilingual and Multi-Aspect Hate Speech Analysis (English) | Ousidhoum2019 |
| 21 | Postponed (includes pictures) | Exploring Hate Speech Detection in Multimodal Publications |  |
| 22 | Uses OLID Dataset | Predicting the Type and Target of Offensive Posts in Social Media |  |
| 23 | Registration required | SemEval-2019 Task 5: Multilingual Detection of Hate Speech AgainstImmigrants and Women in Twitter |  |
| 24 | Done (v3) | Peer to Peer Hate: Hate Speech Instigators and Their Targets | ElSherief2018 |
| 25 | Done (v3) | Overview of the HASOC track at FIRE 2019: Hate Speech and Offensive Content Identification in Indo-European Languages | Mandl2019en |
| 26 | Dataset unavailable | Large Scale Crowdsourcing and Characterization of Twitter Abusive Behavior |  |
| 27 | E-Mail required | A Large Labeled Corpus for Online Harassment Research |  |
| 28 | Postponed (figure out where datasets are) | Ex Machina: Personal Attacks Seen at Scale, Personal attacks |  |
| 29 | Postponed (figure out where datasets are) | Ex Machina: Personal Attacks Seen at Scale, Toxicity |  |
| 30 | Postponed (sql file) | Detecting cyberbullying in online communities (World of Warcraft) |  |
| 31 | Postponed (sql file) | Detecting cyberbullying in online communities (League of Legends) |  |
| 32 | E-Mail required | A Qality Type-aware Annotated Corpus and Lexicon for Harassment Research | Rezvan2018 |
| 33 | Postponed (figure out where datasets are) | Ex Machina: Personal Attacks Seen at Scale, Aggression and Friendliness |  |
| 34 | Done (v3) | CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech (English) | Chung2019 |
| 35 | Done (v3) | Multilingual and Multi-Aspect Hate Speech Analysis (English) | Ousidhoum2019 |
| 36 | Done (v3) | Measuring the Reliability of Hate Speech Annotations:The Case of the European Refugee Crisis | Ross2017 |
| 37 | Done (v3) | Detecting Offensive Statements Towards Foreigners in Social Media | Bretschneider2017 |
| 38 | Done (v3) | Overview of the GermEval 2018 Shared Task on the Identification of Offensive Language | Wiegand2018 |
| 39 | Done (v3) | Overview of the HASOC track at FIRE 2019: Hate Speech and Offensive Content Identification in Indo-European Languages | Mandl2019ger |
| 40 | Website Down | Deep Learning for User Comment Moderation, Flagged Comments |  |
| 41 | Website Down | Deep Learning for User Comment Moderation, Flagged Comments |  |
| 42 |  |  |  |
| 43 |  |  |  |
| 44 |  |  |  |
| 45 |  |  |  |
| 46 |  |  |  |
| 47 | Done (v3) | Overview of the HASOC track at FIRE 2019: Hate Speech and Offensive Content Identification in Indo-European Languages | Mandl2019hind |
| 48 |  |  |  |
| 49 |  |  |  |
| 50 |  |  |  |
| 51 |  |  |  |
| 52 |  |  |  |
| 53 |  |  |  |
| 54 | Done (v3) | CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech (English) | Chung2019 |
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
* 16.02. request Twitter API access
* 23.02. Twitter datasets: One tweet id per line, txt file; 5 new datasets
* 02.03. Twitter datasets: twarc gets tweet texts via API; convert to csv file; 5 new datasets
* 09.03. 5 new datasets
* 16.03. merge class labels or split; combine multiple datasets; 5 new datasets
* postponed: generate dataset statistics


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

### More datasets we should also include:
* https://github.com/punyajoy/Fear-speech-analysis/
