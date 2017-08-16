# Pygeon
Convert python to c# and make it into an exacutable!

## How to use pygeon
------------------------------
To convert your python app to c#, first rename the python file to main.py.
Then, place pygeon.py in the same directory as your main.py file.
Run the following command to do a "pygeon build":

python pygeon.py build

A file called pygeonapp.cs will be created containing you c# code.

## EXAMPLE: Building the example app
----------------------------------------------
1. Clone or download pygeon.
2. Copy pygeon.py into the example-app folder.
3. Open the command window and cd to the example-app folder.
4. Run "python pygeon.py build".
5. Compile pygeonapp.cs to get the executable.

## IMPORTANT!!!
----------------------
At the moment, to run a pygeon app, you must have python installed and located at C:\Python27.

In later versions, pygeon will download a python runtime temporarily to run the app.
