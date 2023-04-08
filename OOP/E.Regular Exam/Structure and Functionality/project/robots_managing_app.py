from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService
from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot


class RobotsManagingApp:

    def __init__(self):
        self.robots = [] # objects
        self.services = [] # objects

    def add_service(self, service_type: str, name: str):
        if service_type not in ["MainService", "SecondaryService"]:
            raise Exception("Invalid service type!")

        if service_type == "MainService":
            service = MainService(name)

        else:
            service = SecondaryService(name)

        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in ["MaleRobot", "FemaleRobot"]:
            raise Exception("Invalid robot type!")

        if robot_type == "MaleRobot":
            robot = MaleRobot(name, kind, price)

        else:
            robot = FemaleRobot(name, kind, price)

        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [x for x in self.robots if x.name == robot_name][0]
        service = [x for x in self.services if x.name == service_name][0]

        if isinstance(robot, MaleRobot) and isinstance(service, SecondaryService):
            return "Unsuitable service."

        if isinstance(robot, FemaleRobot) and isinstance(service, MainService):
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [x for x in self.services if x.name == service_name][0]
        if robot_name not in [x.name for x in service.robots]:
            raise Exception("No such robot in this service!")

        robot = [x for x in service.robots if x.name == robot_name][0]
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = [x for x in self.services if x.name == service_name][0]
        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = [x for x in self.services if x.name == service_name][0]
        total_sum = 0
        for robot in service.robots:
            total_sum += robot.price
        return f"The value of service {service_name} is {total_sum:.2f}."

    def __str__(self):
        return '\n'.join([x.details() for x in self.services])

