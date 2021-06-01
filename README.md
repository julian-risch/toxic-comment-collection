# toxic-comment-collection

## Setup
- Clone this repository
- Install dependencies
  ```bash
  pip install -r requirements.txt
  ```
- Complete the upper part of the ```api_config.json``` with your Twitter API Keys. Without the keys some datasets can't be downloaded.
  ```json
  {
    "twitter": {
      "consumer_key": "",
      "consumer_secret": "",
      "access_token": "",
      "access_token_secret": ""
    }
  }
  ```

- Run the script to fetch the datasets. Due to access limitations to the twitter API it might happen that there is no visible progresse for ~10 minutes.
  ```
  python3 main.py
  ```

- Use the following command to get further information on the accessible arguments:

  ```
  python3 main.py --help
  ```

The downloaded Files can be found in the subdirectory defined in ```config.json``` as ```file_directory```.

## Add a new Dataset
- Create a new file in the ```datasets``` folder with the following naming scheme:
  ```
  <paper_author><paper_year><suffix (for duplicate file names)>.py
  ```
- Complete the content of the file like in the following example:
  ```python
  import os
  from . import dataset
  from . import helpers
  
  class Mubarak2017aljazeera(dataset.Dataset):

      name = "mubarak2017aljazeera"
      url = "http://alt.qcri.org/~hmubarak/offensive/AJCommentsClassification-CF.xlsx"
      hash = "afa00e36ff5492c1bbdd42a0e4979886f40d00f1aa5517807a957e22fb517670"
      files = [
          {
              "name": "mubarak2017ar_aljazeera.csv",
              "language": "ar",
              "type": "training",
              "platform": "twitter"
          }
      ]
      comment = """Annotation	Meaning
                    0	NORMAL_LANGUAGE
                   -1	OFFENSIVE_LANGUAGE
                   -2	OBSCENE_LANGUAGE"""

      license = """ """
  ```

- Overwrite the methods ```process``` and ```unify_row``` from the parent class (```dataset.Dataset```) to implement unpack and process the downloaded files. You might use methods from ```datasets/helpers.py```
- The resulting ```.csv``` should have the following columns:
  - id (added automatically)
  - text
  - labels
- Add the newly created file and class to ```datasets/helpers.py```. (```import``` + ```get_datasets()``` method.)
- Run the following command and answer everything with "n" to update ```config.json```:
  ```
  python main.py --genconfig
  ```
- We are happy to adopt your changes. Just create a pull request from your fork to this repository.

## Status
The following Datasets have been included in this project  
leondz/hatespeechdata : https://github.com/leondz/hatespeechdata 

(can be accessed via : http://ckan.hatespeechdata.com)
|  # | State | Name | Class |
|  - |:-----:| ---- | ----- |
|  1 | Done | Are They our Brothers? Analysis and Detection of Religious Hate Speech in the Arabic Twittersphere | Albadi2018 |
|  2 | Done | Multilingual and Multi-Aspect Hate Speech Analysis (Arabic) | Ousidhoum2019 |
|  3 | Done | L-HSAB: A Levantine Twitter Dataset for Hate Speech and Abusive Language | mulki2019 |
|  4 | Done | Abusive Language Detection on Arabic Social Media (Twitter) | Mubarak2017twitter |
|  5 | Done | Abusive Language Detection on Arabic Social Media (Al Jazeera) | Mubarak2017aljazeera|
|  6 | Postponed (OneDrive) | Dataset Construction for the Detection of Anti-Social Behaviour in Online Communication in Arabic |  |
|  7 | Postponed (Login Required) | Datasets of Slovene and Croatian Moderated News Comments |  |
|  8 | tar.bz2 file | Offensive Language and Hate Speech Detection for Danish |  |
|  9 | Done | Automated Hate Speech Detection and the Problem of Offensive Language | Davidson2017 |
| 10 | Done | Hate Speech Dataset from a White Supremacy Forum | Gibert2018 |
| 11 | Done | Hateful Symbols or Hateful People? Predictive Features for Hate Speech Detection on Twitter | Waseem2016 |
| 12 | Done | Detecting Online Hate Speech Using Context Aware Models | Gao2018 |
| 13 | Done | Are You a Racist or Am I Seeing Things? Annotator Influence on Hate Speech Detection on Twitter | Waseem2016 |
| 14 | Done | When Does a Compliment Become Sexist? Analysis and Classification of Ambivalent Sexism Using Twitter Data | Jha2017 |
| 15 | Password required | Overview of the Task on Automatic Misogyny Identification at IberEval 2018 (English) |  |
| 16 | Done | CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech (English) | Chung2019 |
| 17 | Not suited | Characterizing and Detecting Hateful Users on Twitter |  |
| 18 | Done | A Benchmark Dataset for Learning to Intervene in Online Hate Speech (Gab) | Qian2019 |
| 19 | Done | A Benchmark Dataset for Learning to Intervene in Online Hate Speech (Reddit) | Qian2019 |
| 20 | Done | Multilingual and Multi-Aspect Hate Speech Analysis (English) | Ousidhoum2019 |
| 21 | Postponed (includes pictures) | Exploring Hate Speech Detection in Multimodal Publications |  |
| 22 | Uses OLID Dataset | Predicting the Type and Target of Offensive Posts in Social Media |  |
| 23 | Done | SemEval-2019 Task 5: Multilingual Detection of Hate Speech AgainstImmigrants and Women in Twitter | Basile2019 |
| 24 | Done | Peer to Peer Hate: Hate Speech Instigators and Their Targets | ElSherief2018 |
| 25 | Done | Overview of the HASOC track at FIRE 2019: Hate Speech and Offensive Content Identification in Indo-European Languages | Mandl2019en |
| 26 | Done | Large Scale Crowdsourcing and Characterization of Twitter Abusive Behavior | Founta2018 |
| 27 | E-Mail required | A Large Labeled Corpus for Online Harassment Research |  |
| 28 | Done | Ex Machina: Personal Attacks Seen at Scale, Personal attacks | Wulczyn2017attack |
| 29 | Done | Ex Machina: Personal Attacks Seen at Scale, Toxicity | Wulczyn2017toxic |
| 30 | Done | Detecting cyberbullying in online communities (World of Warcraft) |  |
| 31 | Done | Detecting cyberbullying in online communities (League of Legends) |  |
| 32 | E-Mail required | A Qality Type-aware Annotated Corpus and Lexicon for Harassment Research | Rezvan2018 |
| 33 | Done | Ex Machina: Personal Attacks Seen at Scale, Aggression and Friendliness | Wulczyn2017aggressive |
| 34 | Done | CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech (English) | Chung2019 |
| 35 | Done | Multilingual and Multi-Aspect Hate Speech Analysis (English) | Ousidhoum2019 |
| 36 | Done | Measuring the Reliability of Hate Speech Annotations:The Case of the European Refugee Crisis | Ross2017 |
| 37 | Done | Detecting Offensive Statements Towards Foreigners in Social Media | Bretschneider2017 |
| 38 | Done | Overview of the GermEval 2018 Shared Task on the Identification of Offensive Language | Wiegand2018 |
| 39 | Done | Overview of the HASOC track at FIRE 2019: Hate Speech and Offensive Content Identification in Indo-European Languages | Mandl2019ger |
| 40 | Website Down | Deep Learning for User Comment Moderation, Flagged Comments |  |
| 41 | Website Down | Deep Learning for User Comment Moderation, Flagged Comments |  |
| 42 | Done | Offensive Language Identification in Greek | Pitenis2020 |
| 43 | Application required | Aggression-annotated Corpus of Hindi-English Code-mixed Data |  |
| 44 | Application required | Aggression-annotated Corpus of Hindi-English Code-mixed Data |  |
| 45 | Done | Did you offend me? Classification of Offensive Tweets in Hinglish Language | Mathur2018 |
| 46 | Dataset not available | A Dataset of Hindi-English Code-Mixed Social Media Text for HateSpeech Detection |  |
| 47 | Done | Overview of the HASOC track at FIRE 2019: Hate Speech and Offensive Content Identification in Indo-European Languages | Mandl2019hind |
| 48 | Done | Hate Speech Detection in the Indonesian Language: A Dataset and Preliminary Study | Alfina2018 |
| 49 | Done | Multi-Label Hate Speech and Abusive Language Detection in Indonesian Twitter | Ibrohim2019 |
| 50 | Done | A Dataset and Preliminaries Study for Abusive Language Detection in Indonesian Social Media | Ibrohim2018 |
| 51 | Done | An Italian Twitter Corpus of Hate Speech against Immigrants | Sanguinetti2018 |
| 52 | Application required | Overview of the EVALITA 2018 Hate Speech Detection Task (Facebook) |  |
| 53 | Application required | Overview of the EVALITA 2018 Hate Speech Detection Task (Twitter) |  |
| 54 | Done | CONAN - COunter NArratives through Nichesourcing: a Multilingual Dataset of Responses to Fight Online Hate Speech (English) | Chung2019 |
| 55 | XML import required | Creating a WhatsApp Dataset to Study Pre-teen Cyberbullying |  |
| 56 | Files not found | Results of the PolEval 2019 Shared Task 6:First Dataset and Open Shared Task for Automatic Cyberbullying Detection in Polish Twitter |  |
| 57 | Done | A Hierarchically-Labeled Portuguese Hate Speech Dataset | Fortuna2019 |
| 58 | ARFF file format | Offensive Comments in the Brazilian Web: A Dataset and Baseline Results |  |
| 59 | Encrypted | Datasets of Slovene and Croatian Moderated News Comments |  |
| 60 | Application required | Overview of MEX-A3T at IberEval 2018: Authorship and Aggressiveness Analysis in Mexican Spanish Tweets |  |
| 61 |  |  |  |
| 62 | Data not found | hatEval, SemEval-2019 Task 5: Multilingual Detection of Hate Speech Against Immigrants and Women in Twitter (Spanish) |  |
| 63 | Done | A Corpus of Turkish Offensive Language on Social Media | Coltekin2019 |
| Additional 1 | Done | Aggression Detection on Social Media Text Using Deep Neural Networks | Kumar2018 |
| Additional 2 | Done | Predicting the Type and Target of Offensive Posts in Social Media | Zampieri2019 |

<!--- ### More datasets we should also include: --->


### Further ToDos
* Make sure that the script does not fail if api_config is empty -> download datasets that don't need Twitter API
* Multilingual experiments: shuffle combined.tsv and split into train/test set; use binary label mapping and train xlm-roberta-base model
  * none,normal,other,positive,appropriate -> non-toxic
  * idk/skip -> discard 
  * rest -> toxic
