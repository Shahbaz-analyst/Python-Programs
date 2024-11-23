# Program to clear the clutter inside a folder

import os

files = os.listdir("clear_clutter")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"clear_Clutter/{file}", f"clear_Clutter/{i}.png")
    i += 1 