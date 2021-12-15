##Roguetech Career ID fetcher
This is just a quick and dirty application to grab the last loaded files career ID.

#build instructions
Load a `pipenv` in the workspace directory by using `pipenv install` followed by
```
pipenv shell
pyinstaller --onefile -w 'main.py'
```
this will compile the app into a single exe file in dist.

##Disclamer.
This is just a small quick and dirty tool i made because i want be lazy in my future and learn something now,
I'm not repsonsible if this program bricks a save, gets you a ban on the persistant map (it really shouldn't and if you do, it's not this app) or if the app becomes sentient and steals your dog, your Significant Other and drinks all of your beer.

beyond that.... I learned Tkinter and made a neat little dynamic Module loader for expanding UI. So the project, beyond it suddenly taking over the world, is complete