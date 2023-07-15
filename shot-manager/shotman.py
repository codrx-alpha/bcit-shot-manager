import json
import os

class Project:
    def __init__(self):
        self.shows: dict[str, Show] = {}
        self.working_directory: str = os.getcwd()

    def create_project(self, project_name: str, path="", current_directory=True):
        if current_directory:
            directory = os.path.join(os.getcwd(), project_name)
            os.makedirs(directory)

        if not current_directory:
            directory = os.path.join(path, project_name)
            os.makedirs(directory)

    def create_show(self, name: str, studio: str, showrunner: str, seasons: int):
        directory = os.path.join(self.working_directory, name)
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            print("Show already exists!")
        self.shows[name] = Show(name, studio, showrunner, seasons)

    def set_working_directory(self, path: str):
        self.working_directory = path

    def get_all_shows(self):
        for show in self.shows:
            show_data = {
                show.get_name()
            }

            print(show_data)

    def print_shows_list(self):
        print(self.shows)

class Show:
    def __init__(self, name: str, studio: str, showrunner: str, seasons: int):
        self.name = name
        self.studio = studio
        self.showrunner = showrunner
        self.seasons = seasons

    def get_name(self) -> str:
        return self.name

    def get_studio(self) -> str:
        return self.studio
    def get_showrunner(self) -> str:
        return self.showrunner
    def get_seasons(self) -> int:
        return self.seasons







