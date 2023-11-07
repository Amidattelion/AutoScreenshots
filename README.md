# AutoScreenshots
A simple script that automatically take a screenshot of the screen whenever its content changes (with a configurable sensibility).

# Setup:
The code have only been tested on Windows, but should works on Linux.

**1 - Clone the repository with git (https://github.com/Amidattelion/AutoScreenshots.git) or download and extract it**

**2 - Install the requirements with pip:**

It is advised to first create and activate a dedicated virtual environment before proceeding.
Open a terminal and cd in the "SYMP" folder that you have just extracted, then run the following command to install the python dependencies:

```
$ pip install -r requirements.txt
```

**3 - Edit auto_screenshots.py**

The only thing you may want to change is the sensibility threshold to consider that the screen has changed: this threshold can be edited at line [42], the higher the value the higher the chance to take a screenshot (the lower the required change).

**4 - Launch auto_screenshots.py, screenshots will be stored in the script working folder**
