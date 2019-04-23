from transitions.core import Machine, State


class On(State):
    def __init__(self, *args, **kwargs):
        super(On, self).__init__(*args, **kwargs)

    def enter(self, event_data):
        super(On, self).enter(event_data)


class Off(State):

    def __init__(self, *args, **kwargs):
        super(Off, self).__init__(*args, **kwargs)

    def enter(self, event_data):
        super(Off, self).enter(event_data)
        print 5555

    def exit(self, event_data):
        event_data['mss'] = 4654656
        super(Off, self).exit(event_data)


class MyFsm(object):
    transitions = [
        {'trigger': 'switchOff', 'source': 'on', 'dest': 'off', 'befor': 'get_vars'},
        {'trigger': 'switchOn', 'source': 'off', 'dest': 'on'}
    ]

    def __init__(self):
        # ignore_invalid_triggers will allow to process events not defined for a state
        on = On(name='on', ignore_invalid_triggers=True)
        off = Off(name='off', ignore_invalid_triggers=False)
        self.machine = Machine(model=self, states=[on, off], transitions=self.transitions, initial='off')


machine = MyFsm()
# print(machine.state)  # >>> on
# machine.switchOff()
# print(machine.state)  # >>> off
# try:
# this will raise a MachineException because there is no transition 'switchOff'
# defined in state 'off'
# machine.switchOff()  # raises MachineException
# raise Exception("This exception will not be raised")
# except MachineError:
# pass
print(machine.state)  # >>> off
machine.switchOn()
print(machine.state)  # >>> on
# this will NOT raise an Exception since we configured 'on'
# to ignore transitions not defined for this state
machine.switchOn()
print(machine.state)  # >>> on
