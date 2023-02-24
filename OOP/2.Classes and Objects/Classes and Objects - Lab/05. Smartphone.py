class Smartphone:

    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = False if self.is_on else True

    def install(self, app, app_memory):
        if self.memory - app_memory >= 0 and self.is_on:
            self.memory -= app_memory
            self.apps.append(app)
            return f"Installing {app}"

        elif self.memory - app_memory >= 0:
            return f"Turn on your phone to install {app}"

        return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"

