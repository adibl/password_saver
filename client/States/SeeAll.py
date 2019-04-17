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
    is_runed = False


    def run(self, *args):
        print 'runnn'

    def run_before(self):
        if not self.is_runed:
            print 'run prosses'
            self.proses = multiprocessing.Process(target=runShadow.main)
            self.proses.start()
            self.is_runed = True
        super(SeeAllState, self).run_before()

    def run_after(self):
        return [self.program_id, ]

    def edit_record(self, event):
        item = self.table.identify_row(event.y)
        if item in self.records.keys():
            self.program_id = self.records[item]
            fsm.edit()
            self.end()

