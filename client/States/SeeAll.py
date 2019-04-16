"""
name:
date:
description
"""
from client.window_order import fsm, shadow_fsm
from client.ShadowStates import runShadow
from client.GUI.SeeAll import SeeAllGui
from .state import State
import multiprocessing


class SeeAllState(SeeAllGui, State):
    def run(self, *args):
        print 'runnn'

    def run_before(self):
        self.proses = multiprocessing.Process(target=runShadow.main)
        self.proses.start()
        super(SeeAllState, self).run_before()

    def run_after(self):
        shadow_fsm.close()
        self.proses.join()
