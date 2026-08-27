class SchedulerMixin():

    def __init__(self):
        return

    def add_noise(self):
        raise NotImplementedError

    def step(self):
        raise NotImplementedError
