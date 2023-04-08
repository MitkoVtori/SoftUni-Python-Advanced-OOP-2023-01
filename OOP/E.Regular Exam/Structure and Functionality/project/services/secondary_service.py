from project.services.base_service import BaseService


class SecondaryService(BaseService):

    def __init__(self, name: str):
        capacity: int=15
        super().__init__(name, capacity)

    def details(self):
        return f"{self.name} Secondary Service:\nRobots: {' '.join([x.name for x in self.robots]) if self.robots else 'none'}"

