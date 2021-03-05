# Automation

Automating regular life tasks... By Sam Silver

## MoveFiles.py

For organizing/unclutter your downloads folder! This program will separate all files in a specified location into folders with titles with the hopes of making your folder a tiny bit prettier.

### Version 2.0: March 3, 2021

**commit: 87d34d237aefc1085c0140e80325bca4fc4a0648**
I have removed watchdog fully from the project. I did not even try to solve the major bug as I re-thought how I would be using the program. I did not want the program constantly running and taking up resources as I do not download something every minute. Since I only download a couple thing a day, if even, I decided to just run the program each time my computer starts up, therefore, watchdog is not needed. It was fun to explore watchdog and see its capabilities, perhaps I will come back to the pervious version and use it for a different purpose sometime down the road.

### Version 1.0: March 2, 2021

**commit: 06e3524abb3a14024d208c5e0c4b2e1cb0e32351**
Using watchdog module I was able to observe a single path and move files to other folders as soon as a new file was entered into that trackable path.

**_Known Bug_**
It seems that copying and pasting files into the path causes watchdog to try and move it multiple times, this causes an error as it tries to move a file that does not exist as it has "already moved it". With some research I concluded that the file is not fully being copied over but watchdog is so fast it just moves half of the file size to the destination. Seems like this could be fixed by implementing a variable tracking the file size and then executing the move once it is fully copied over.

## nasaPicOfDay.py

This program will change you background image to the NASA pic of the day! Majority of the code was taken from https://www.youtube.com/watch?v=VLNcnROUTb8&t=499s&ab_channel=PythonEngineer

I plan on setting this code to launch every time I log into my laptop!

## BitcoinTracker.py

This program checks the price of bitcoin every 5 minutes. If it is lower than a certain threshold then send a notification to ITFFF (App on my phone)

It is very simple at this point but there is a lot more I could do with this program... potentially a project for later.
