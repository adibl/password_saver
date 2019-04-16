"""
name:
date:
description
"""

from abc import abstractmethod
import langid

class State(object):
    @abstractmethod
    def clean(self):
        """
        clean all the data in the lables

        :return:
        """
        pass

    @abstractmethod
    def run(self):
        """
        run the satae

        :return:
        """
        pass

    def run_after(self):
        """
        run after the window finish, return the data for future windows
        """
        return None

    def run_before(self):
        """
        run after the window finish, return the data for future windows
        """
        return None

    def get_data(self, data):
        """
        get the data from last window
        """
        pass


    @staticmethod
    def test_lenguge_data(data):
        return isinstance(data, str)
