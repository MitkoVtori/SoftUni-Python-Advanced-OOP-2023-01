from abc import ABC, abstractmethod
import time


class Workable(ABC):

    @staticmethod
    @abstractmethod
    def work():
        pass


class Eatable(ABC):

    @staticmethod
    @abstractmethod
    def eat():
        pass


class Worker(Workable, Eatable):

    @staticmethod
    def work():
        print("I'm normal worker. I'm working.")

    @staticmethod
    def eat():
        print("Lunch break....(5 secs)")
        time.sleep(5)

class SuperWorker(Workable, Eatable):

    @staticmethod
    def work():
        print("I'm super worker. I work very hard!")

    @staticmethod
    def eat():
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Workable):

    @staticmethod
    def work():
        print("I'm a robot. I'm working....")


class BaseManager(ABC):

    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager(BaseManager):

    def set_worker(self, worker):
        assert isinstance(worker, Workable), f"`worker` must be of type {Workable}"

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(BaseManager):

    def set_worker(self, worker):
        assert isinstance(worker, Eatable), f"`worker` must be of type {Eatable}"

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


work_manager = WorkManager()
break_manager = BreakManager()

worker = Worker()
work_manager.set_worker(worker)
break_manager.set_worker(worker)
work_manager.manage()
break_manager.lunch_break()

super_worker = SuperWorker()
work_manager.set_worker(super_worker)
break_manager.set_worker(super_worker)
work_manager.manage()
break_manager.lunch_break()

robot = Robot()
work_manager.set_worker(robot)
work_manager.manage()

# try:
#     break_manager.set_worker(robot)
# except AssertionError:
#     print("Robots don't eat")
