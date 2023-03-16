from abc import ABC, abstractmethod


class BaseWorker(ABC):

    @staticmethod
    @abstractmethod
    def work():
        pass


class Worker(BaseWorker):

    @staticmethod
    def work():
        print("I'm working!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, BaseWorker), '`worker` must be of type {}'.format(BaseWorker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()

class SuperWorker(BaseWorker):

    @staticmethod
    def work():
        print("I work very hard!!!")


class LazyWorker(BaseWorker):
    ''' This is a bonus class. It is not in the conditions. '''

    @staticmethod
    def work():
        print("Let me sleep!")


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
lazy_worker = LazyWorker() # bonus instance
try:
    manager.set_worker(super_worker)
    manager.manage()

    manager.set_worker(lazy_worker)
    manager.manage() # bonus print
except AssertionError:
    print("manager fails to support super_worker....")
