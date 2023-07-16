import json
import os

class Project:

    def __init__(self):
        self.shows: dict[str, Show] = {}
        self.working_directory: str = ""

    def create_project(self, project_name: str, path="", current_directory=True):
        if current_directory:
            if not os.path.exists(os.getcwd() + '\\' + project_name):
                directory = os.path.join(os.getcwd(), project_name)
                os.makedirs(directory)
                directory_file = open("config/directory.txt", "w")
                directory_file.write(str(os.getcwd() + '\\' + project_name))
                directory_file.close()

                directory_file = open("config/directory.txt", "r")
                self.working_directory = directory_file.read()
                directory_file.close()
                print(f"'{project_name}' project created!\nWorking directory set to {directory}!")
            else:
                print("Project already exists!")

        if not current_directory:
            if not os.path.exists(os.getcwd() + '\\' + project_name):
                directory = os.path.join(path, project_name)
                os.makedirs(directory)
                self.working_directory = str(directory)
                print(f"'{project_name}' project created!\nWorking directory set to {directory}!")
            else:
                print("Project already exists!")

    def create_show(self, name: str, studio: str, showrunner: str, seasons: int):

        if os.path.isfile("config/directory.txt"):
            directory = open("config/directory.txt", "r")
            path = os.path.join(str(directory.read()) + "\\", name)
            if not os.path.exists(path):
                os.makedirs(path)
                self.shows[name] = Show(name, studio, showrunner, seasons)
                directory.close()
            else:
                print("Show already exists!")
                directory.close()

        else:
            print("Directory file does not exist! Working directory is not set!")

    def set_working_directory(self, path: str):
        directory_file = open("config/directory.txt", "w")
        directory_file.write(path)
        directory_file.close()

    def get_working_directory(self) -> str:
        directory = open("config/directory.txt", "r")
        return directory.read()

    def get_all_shows(self) -> list:
        return list(self.shows)

class Shot:
    def __init__(self, fps: float, shot_number: int, frame_range: str, description: str = ""):
        self.fps = fps
        self.shot_number = shot_number
        self.frame_range = frame_range
        self.description = description

    def update(self, fps: float, shot_number: int, frame_range: str, description: str = ""):
        self.fps = fps
        self.shot_number = shot_number
        self.frame_range = frame_range
        self.description = description

class Show:
    def __init__(self, name: str, studio: str, showrunner: str, seasons: int, shots: dict[int, Shot] = None):
        self.name = name
        self.studio = studio
        self.showrunner = showrunner
        self.seasons = seasons
        self.shots = shots

    def create_shot(self, fps: float, shot_number: int, frame_range: str, description: str = ""):
        self.shots[shot_number] = Shot(fps, shot_number, frame_range, description)

    def update(self, name: str, studio: str, showrunner: str, seasons: int, shots: dict[str, Shot] = None):
        self.name = name
        self.studio = studio
        self.showrunner = showrunner
        self.seasons = seasons
        self.shots = shots

    def get_name(self) -> str:
        return self.name

    def get_studio(self) -> str:
        return self.studio

    def get_showrunner(self) -> str:
        return self.showrunner

    def get_seasons(self) -> int:
        return self.seasons

    def get_all_shots(self):
        print(list(self.shots))








