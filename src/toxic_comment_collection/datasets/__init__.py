from . import ousidhoum2019
from . import mulki2019
from . import mubarak2017twitter
from . import mubarak2017aljazeera
from . import davidson2017
from . import gibert2018
from . import gao2018
from . import chung2019
from . import qian2019
from . import waseem2016
from . import jha2017
from . import elsherief2018
from . import mandl2019en
from . import mandl2019ger
from . import mandl2019hind
from . import bretschneider2017
from . import ross2017
from . import wiegand2018
from . import pitenis2020
from . import mathur2018
from . import alfina2017
from . import ibrohim2019
from . import ibrohim2018
from . import sanguinetti2018
from . import fortuna2019
from . import coltekin2019
from . import albadi2018
from . import basile2019
from . import founta2018
from . import wulczyn2017toxic
from . import wulczyn2017aggressive
from . import wulczyn2017attack
from . import sigurbergsson2019
from . import kulkarni2021
from . import novak2021
from . import kumar2018
from . import zampieri2019
from . import bretschneider2016wow
from . import bretschneider2016lol

def get_datasets():
    return [
        ousidhoum2019.Ousidhoum2019(),
        mulki2019.Mulki2019(),
        mubarak2017twitter.Mubarak2017twitter(),
        mubarak2017aljazeera.Mubarak2017aljazeera(),
        davidson2017.Davidson2017(),
        gibert2018.Gibert2018(),
        gao2018.Gao2018(),
        chung2019.Chung2019(),
        qian2019.Qian2019(),
        waseem2016.Waseem2016(),
        jha2017.Jha2017(),
        elsherief2018.Elsherief2018(),
        mandl2019en.Mandl2019en(),
        mandl2019ger.Mandl2019ger(),
        mandl2019hind.Mandl2019hind(),
        bretschneider2017.Bretschneider2017(),
        ross2017.Ross2017(),
        wiegand2018.Wiegand2018(),
        pitenis2020.Pitenis2020(),
        mathur2018.Mathur2018(),
        alfina2017.Alfina2017(),
        ibrohim2019.Ibrohim2019(),
        ibrohim2018.Ibrohim2018(),
        sanguinetti2018.Sanguinetti2018(),
        fortuna2019.Fortuna2019(),
        coltekin2019.Coltekin2019(),
        albadi2018.Albadi2018(),
        basile2019.Basile2019(),
        founta2018.Founta2018(),
        wulczyn2017toxic.Wulczyn2017toxic(),
        wulczyn2017aggressive.Wulczyn2017aggressive(),
        wulczyn2017attack.Wulczyn2017attack(),
        sigurbergsson2019.Sigurbergsson2019(),
        kulkarni2021.Kulkarni2021(),
        novak2021.Novak2021(),
        kumar2018.Kumar2018(),
        zampieri2019.Zampieri2019(),
        bretschneider2016wow.Bretschneider2016wow(),
        bretschneider2016lol.Bretschneider2016lol(),
    ]


def get_dataset_by_name(name):
    all_datasets = get_datasets()
    return next(filter(lambda dataset: dataset.name == name, all_datasets), None)
