from . import dataset
from . import helpers
import os


class Elsherief2018(dataset.Dataset):
    
    name = "elSherief2018"
    url = "https://github.com/mayelsherif/hate_speech_icwsm18/archive/master.zip"
    hash = "34365d3d398b0a345a4278df30d851761cb6dc34c7a38f4bdfb77f20fae164c2"
    files = [
        {
            "name": "elSherief2018en.csv",
            "language": "en",
            "type": "training",
            "platform": "twitter"
        }
    ]
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.unzip_file(tmp_file_path)

        base_path = os.path.join(tmp_file_path, "hate_speech_icwsm18-master")        
        
        files = {
            os.path.join(base_path, "twitter_hashtag_based_datasets/ethn_blackpeoplesuck.csv"): ["racism","ethnicity","black"],
            os.path.join(base_path, "twitter_hashtag_based_datasets/ethn_whitepower.csv"): ["racism","ethnicity","white"],
            os.path.join(base_path, "twitter_hashtag_based_datasets/istandwithhatespeech.csv"): ["prohatespeech"],
            os.path.join(base_path, "twitter_hashtag_based_datasets/rel_nomuslimrefugees.csv"): ["racism","religious","islamophobia"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/archaic_boojie.csv"): ["archaic_boojie"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/archaic_chinaman.csv"): ["archaic_chinaman"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/archaic_hillbilly.csv"): ["archaic_hillbilly"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/archaic_surrendermonkey.csv"): ["archaic_surrendermonkey"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/archaic_whigger.csv"): ["archaic_whigger"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/archaic_whitenigger.csv"): ["archaic_whitenigger"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/archaic_wigerette.csv"): ["archaic_wigerette"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/archaic_wigger.csv"): ["archaic_wigger"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/class_bitterclinger.csv"): ["class_bitterclinger"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/class_conspiracytheorist.csv"): ["class_conspiracytheorist"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/class_redneck.csv"): ["class_redneck"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/class_rube.csv"): ["class_rube"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/class_trailerparktrash.csv"): ["class_trailerparktrash"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/class_whitetrash.csv"): ["class_whitetrash"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/disability_retard.csv"): ["disability_retard"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/disability_retarded.csv"): ["disability_retarded"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/ethn_camelfucker.csv"): ["ethn_camelfucker"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/ethn_coonass.csv"): ["ethn_coonass"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/ethn_housenigger.csv"): ["ethn_housenigger"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/ethn_mooncricket.csv"): ["ethn_mooncricket"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/ethn_nigger.csv"): ["ethn_nigger"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/ethn_raghead.csv"): ["ethn_raghead"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/ethn_spic.csv"): ["ethn_spic"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/ethn_trailerparktrash.csv"): ["ethn_trailerparktrash"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/ethn_trailertrash.csv"): ["ethn_trailertrash"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/ethn_wetback.csv"): ["ethn_wetback"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/ethn_whitenigger.csv"): ["ethn_whitenigger"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/ethn_whitetrash.csv"): ["ethn_whitetrash"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/gender_bint.csv"): ["gender_bint"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/gender_cunt.csv"): ["gender_cunt"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/gender_dyke.csv"): ["gender_dyke"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/gender_twat.csv"): ["gender_twat"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/nation_bamboocoon.csv"): ["nation_bamboocoon"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/nation_camelfucker.csv"): ["nation_camelfucker"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/nation_chinaman.csv"): ["nation_chinaman"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/nation_limey.csv"): ["nation_limey"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/nation_plasticpaddy.csv"): ["nation_plasticpaddy"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/nation_sidewayspussy.csv"): ["nation_sidewayspussy"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/nation_surrendermonkey.csv"): ["nation_surrendermonkey"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/nation_whigger.csv"): ["nation_whigger"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/nation_whitenigger.csv"): ["nation_whitenigger"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/nation_wigger.csv"): ["nation_wigger"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/nation_zionazi.csv"): ["nation_zionazi"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/rel_camelfucker.csv"): ["rel_camelfucker"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/rel_muzzie.csv"): ["rel_muzzie"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/rel_souptaker.csv"): ["rel_souptaker"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/rel_zionazi.csv"): ["rel_zionazi"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/sexorient_dyke.csv"): ["sexorient_dyke"],
            os.path.join(base_path, "twitter_key_phrase_based_datasets/sexorient_faggot.csv"): ["sexorient_faggot"]
        }

        tmp_file_path = helpers.merge_csvs(files)
        tmp_file_path = helpers.download_tweets_for_csv(tmp_file_path, "tweet_id", api_config)

        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "elSherief2018en.csv"))

    @classmethod
    def unify_row(cls, row):
        return row