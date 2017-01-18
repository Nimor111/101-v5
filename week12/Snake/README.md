## Snake Game

Today we are going to play with snakes!

Your task is to create the World, in which the snake is going to live, eat and eventually die!

We are not going to give you a lot of information about the implementation of the game! You already know everything needed!

The few things we want to see in your code are:

### Game World

This is the two dimensional class, where the snakes(pythons) are going to live.

```python
class GameWorld():
    def __init__(self, size, contents):
      pass
```

#### Example
```python
game = GameWorld(15)
print(game[3][4])

>>> <main.WorldCell object at 0x7f2bd1359f30>
```

If the user wants access a non existing WorldCell, you need to raise IndexError!


### WorldCell

Each small unit in our Python World is considered as a Cell!

```python
class Cell:
    def __init__(self, contents=None):
        self.content = content
    # methods
    is_empty(self)
```

Content can be only an instance of WorldObject!

#### Example

```python
c = Cell()
c.is_empty() # True

c1 = Cell(Food('Strawberry', energy=2))
c1.is_empty() # False

c2 = Cell(Wall())
c2.is_empty() # False
```

If a cell is already filled with something(Food, Wall, etc), you need to raise `CellError`!

### Food

Inherited WorldObject and comes with name(like 'Banana') and energy (like '4'). If s snake goes to a cell, where is a Food, the snake energy increases with the number of the cell energy.

```python
class Food(WorldObject):
    def __init__(self, name, energy):
        pass

    energy = 5
```

### Wall

```python
class Wall(WorldObject):
    def __init__(self):
        pass

```

### BlackHole

Suddenly there is a black hole in our world and the snake goes in it! : ( Poor, poor python, this means a death for him!

```python
class BlackHole(WorldObject):
    pass

```

## Python(Питоня)

Our python has a head and body.

### PythonPart

Inherited WorldObject

### PythonHead

Inherited PythonPart


### Python class

The magic is here!
Our python has its parts, but we need a whole object to play with!

The class must to have:

- size - If the size is 4, then our python has 4 parts for his body and a head.
- constants for the directions : Python.LEFT, Python.DOWN, Python.RIGHT, Python.UP. These four must be instances of Vector2D
- move(direction) - where direction is one of the four constants.

  This method moves the python with one cell in the given direction.
  The last given direction must be saved in the direction field.

  Once he python is n a cell, which contains Food, the python eats it and it's energy increases with the size of the Food energy. On the next move the body of the python has on additional part!

  If you move the python on one of its parts, the game is over, because the python is dead!

  If you move the python on another python, the game ends -> Python Death!

  If you hit a wall -> Python Death!

  The python cannot move backward! This means that if we was moving left and decides to move right, DirectionError must be raised!

  If you try to go outside of the world -> Python Death!

  If you goes into a black hole -> Python Death!

  And of course, if the python eats all the food in the GameWorld -> End Game! Python wins!


- Initialization

```python
__init__(self, world, coords, size, direction)
```
  Where:

  - world is the GameWorld
  - coords are instances of Vector2D, where the head of the python must be
  - size is the size of the body
  - direction is n which direction to put the python


### Vector2D

This class must to have the following methods:
- add, sub, mul, div, negative

#### Example

```python
class Vec2D:
    def __init__(self, x, y):
      pass

>>> ( Vec2D(1, 1) == -Vec2D(-1, -1) ) # True
```


### Exceptions

```python
class DeathError(Error):
    pass

class DirectionError(Error):
    pass
```

### Context Managers

You need to log everything!
Each game must have different logfile with start and end time, steps made by the python and final result!

If you hit an error during the game, this must be logged in game_error_logfile!



## Game Example

```python
game = GameWorld(15)
p = Python(game, Vec2D(10, 10), 3, Python.LEFT)
print(game)
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ 🐍● ● ● □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □

wall1 = Cell(Wall(), 2, 7)
wall2 = Cell(Wall(), 3, 7)
wall3 = Cell(Wall(), 4, 7)
game.add_content([wall1, wall2, wall3])
print(game)
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ ■ □ □ □ □ □ □ □
□ □ □ □ □ □ □ ■ □ □ □ □ □ □ □
□ □ □ □ □ □ □ ■ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ 🐍● ● ● □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
print(game)
cell = Cell(Food('banana', energy=3), 4, 4)
game.add_content(cell)
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ ■ □ □ □ □ □ □ □
□ □ □ 🍌 □ □ □ ■ □ □ □ □ □ □ □
□ □ □ □ □ □ □ ■ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ 🐍● ● ● □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □ □ □ □
```



### Think wisely! We are sure you know everything to create this game! Good Luck!
