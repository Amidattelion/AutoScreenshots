"""
https://github.com/Amidattelion

Copyright (C)  2013-2014 np1

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along
with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import pyautogui
from PIL import Image, ImageChops
import time
import numpy as np

# Initialize a variable to store the previous screenshot
previous_screenshot = None

while True:
    # Capture the current screenshot
    current_screenshot = pyautogui.screenshot()

    # If there is a previous screenshot, compare it with the current one
    if previous_screenshot is not None:
        # Calculate the absolute difference between the images
        diff = ImageChops.difference(current_screenshot, previous_screenshot)

        # Calculate the relative variance of the sum of pixel differences
        array = np.array(diff)
        diff_sum = np.std(array)

        # You can adjust the threshold for considering it a change
        # A higher threshold means it requires a larger change to save the screenshot
        threshold = 10  # You can adjust this value as needed
        print(diff_sum)
        if diff_sum > threshold:
            # If the difference is above the threshold, save the screenshot
            timestamp = int(time.time())
            file_name = rf"./screenshot_{timestamp}.png"
            current_screenshot.save(file_name)

            print(f"Saved screenshot as {file_name}")
    else:
        print("Initial screenshot taken")

    # Update the previous screenshot
    previous_screenshot = current_screenshot

    # Sleep for a specified interval (e.g., 5 seconds) before taking the next screenshot
    time.sleep(5)
