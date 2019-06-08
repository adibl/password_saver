"""
name:
date:
description
"""
import multiprocessing

from client.GUI.SeeAll import SeeAllGui
from client.ShadowStates import runShadow
from client.window_order import fsm
from .state import State


class SeeAllState(SeeAllGui, State):
    is_runed = False

    def run(self, *args):
        print 'runnn'

    def run_before(self):
        if not self.is_runed:
            self.program_id = None
            print 'run prosses'
            self.proses = multiprocessing.Process(target=runShadow.main)
            self.proses.start()
            self.is_runed = True
        super(SeeAllState, self).run_before()

    def pass_data(self):
        if self.program_id is not None:
            return {'url': self.program_id}

    def edit_record(self, event):
        item = self.table.identify_row(event.y)
        if item in self.records.keys():
            self.program_id = self.records[item]
            fsm.edit()
            self.end()

    def delete_user(self):
        fsm.to_delete()
        self.end()

    def clean(self):
        super(SeeAllState, self).clean()
