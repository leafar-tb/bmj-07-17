# bmj-07-17
berlin mini jam july 2017

## Dependencies
- python
- pygame
- numpy
- scipy

With apt you can use
```
sudo apt-get install python python-numpy python-scipy python-pygame
```
to install the needed packages for Python 2.7.

We currently support Python 2 and 3 but developed for Python 3 so support for version 2 may be dropped.

Pygame for Python 3 is supposed to be in the official sources for aptitude, but I couldn't find it. You can of course always use pip to install the needed packages:

```
sudo apt-get install python3 python3-pip
pip3 install numpy scipy pygame
```

## Execution
With all dependencies installed you may navigate to the project root directory and call

```
python Main.py
```
or

```
python3 Main.py
```
depending on your Python version.

## How to play
Use WASD or the arrow keys to navigate the player (green cross) through the maze. Your goal is to reach the stairs located somewhere on the level. Upon reaching the stairs you will enter the next level.

If you get in contact with an enemy (red cross) you will lose health. If you lose all your health the game is over. You can replenish health by picking up health potions (pinkish? squares).
