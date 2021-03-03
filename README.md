# Automation

Automating regular life tasks...

# MoveFiles.py

## Version 2.0: March 3, 2021

**commit: 87d34d237aefc1085c0140e80325bca4fc4a0648**
I have removed watchdog fully from the project. I did not even try to solve the major bug

## Version 1.0: March 2, 2021

**commit: 06e3524abb3a14024d208c5e0c4b2e1cb0e32351**
Using watchdog module I was able to observe a single path and move files to other folders as soon as a new file was entered into that trackable path.

**_Known Bug_**
It seems that copying and pasting files into the path causes watchdog to try and move it multiple times, this causes an error as it tries to move a file that does not exist as it has "already moved it". With some research I concluded that the file is not fully being copied over but watchdog is so fast it just moves half of the file size to the destination. Seems like this could be fixed by implementing a variable tracking the file size and then executing the move once it is fully copied over.
