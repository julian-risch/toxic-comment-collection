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
        mandl2019en.Mandl2019en()
    ]