# Python: The Snake
## About
It's my first try of making a game in python on my own. The concept is to make a simple, retro styled snake game and my goal it to create:
* Game working in system console
* Snake moving on the screen and reacting on player actions to change directions
  * W - turn up
  * S - turn down
  * A - turn left
  * D - turn right
* Snake moving to the other side of the board when hit the wall
* Apples which can be eaten by snake and make him longer
* Game speed up with each apple eaten
* Local stored highscores
## Screenshoots
![ss1](/screenshots/ss_2.png) ![ss1](/screenshots/ss_4.png) ![ss1](/screenshots/ss_3.png) ![ss1](/screenshots/ss_5.png)
## Technologies & Setup
* Tested on Linux Fedora 32, but also could work on Windows
* Python 3.8.5
## Additional
The game uses python keyboard library which needs root privilages on linux, so you have to run it with it
```
sudo python main.py
```
