import json
from gui.models import DMoods
from datetime import timedelta
import numpy as np


class Confidence:
    def __init__(self, je):
        self.__je = je
        self.__dm = DMoods.select().where(
            DMoods.log_time.between(je.log_time - timedelta(hours=12), je.log_time + timedelta(hours=12))
        ).order_by(DMoods.log_time.asc())

    def __get_dmoods(self):
        """
        gets emotion
        :return:
        """
        return [np.array([d.smiley, d.sad, d.angry, d.fear, d.surprised, d.disgusted]) for d in list(self.__dm)]

    def __get_sent_em(self):
        """
        gets sent emotion
        :return:
        """
        return [np.array(ja[0]) for ja in json.loads(self.__je.analysis)]

    def __calc_aggregate(self):
        """
        Used for calculating confidence in analyzed emotion
        :return:
        """
        dm_vec = np.zeros((1, 6))
        dms = self.__get_dmoods()
        print(dms)
        if len(dms) <= 0: return dm_vec
        for dm in dms:
            dm_vec += dm
        dm_vec /= len(dms)
        return dm_vec

    def confidence_percentage(self, i):
        """
        Used for calculating confidence in analyzed emotion
        :param i:
        :return:
        """
        aggr = self.__calc_aggregate()
        sms = self.__get_sent_em()

        #print(sms[i])
        return str(np.std(sms[i], axis=0) * 1000) + '%'
