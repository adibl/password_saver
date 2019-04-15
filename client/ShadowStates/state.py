"""
name:
date:
description
"""

from abc import abstractmethod

class State(object):

    @abstractmethod
    def on_press(self):
        """
        run the satae

        :return:
        """
        pass

    @classmethod
    def pass_data(cls):
        """
        run after the window finish, return the data for future windows
        """
        return None

    @classmethod
    def get_data(cls, data):
        """
        get the data from last window
        """
        pass