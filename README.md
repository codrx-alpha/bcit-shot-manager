# Shot Manager API

# Summary
An API to create a folder structure for each project and json files with data about projects, shows and shots.

# Instructions

## Setup

- Import shotman module
```
import shotman
```
- Create an instance of the Project class
```
import shotman

project = shotman.Project()
```
- Run the create_project() method on the project instance
```
import shotman

project = shotman.Project()

project.create_project("Project1")
```
- This will set up the base project directory

## Adding shows

- Run the create_show() method on the project instance, supplying it with the required parameters.
```
project.create_show("Castle", "ABC Studios", "Andrew W. Marlowe", 6)
```

# Documentation

## class Project

### Attributes

#### dict Shows
Dictionary containing all shows within a project, in the format [str, Show]

#### str working_directory
The path which the project takes as its current default path for folder creation

### Methods

#### create_project (str project_name, str path = "", bool current_directory = True)
Creates a folder in the current working directory with the given project name, if current_directory is left to default.

#### create_show (str name, str studio, str showrunner, int seasons)
Creates a show folder within the project folder.

#### set_working_directory (str path)
If directory file does not exist, creates directory.txt in the config folder and stores the given path.

#### get_working_directory () -> str
Returns a the working directory path as a string.

#### get_all_shows() -> list
Returns names of all shows in the project instance as a list.

## class Show

### Attributes

#### dict shots
Dictionary containing all shots within a show, in the format [int, Shot].

#### str name
Name of the show.

#### str studio
Name of the studio to which the show belongs.

#### str showrunner
Name of the showrunner.

#### int seasons
Number of seasons the show has.

### Methods

#### create_shot (float fps, int shot_number, str frame_range, str description)
Creates a shot in the shots dictionary.

#### update ()
Updates a show folder within the project folder.

#### get_name() -> str
Returns the name of the show as a string.

#### get_studio() -> str
Returns the name of the studio as a string.

#### get_showrunner() -> str
Returns the name of the showrunner as a string.

#### get_seasons() -> int
Returns the number of seasons in a show as an int.

## class Shot

### Attributes

#### float fps
Frame rate of the shot in frames per second.

#### int shot_number
The shot number of the shot.

#### str frame_range
The range of frames which the shot spans.

#### str description
A description of the shot.

### Methods

#### update(float fps, int shot_number, str frame_range, str description)
Updates the data of a particular shot.
