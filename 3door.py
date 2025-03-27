try:
    from graphics import Rectangle, Text, Point, GraphWin
except ImportError:
    print(
        "Error: graphics.py is missing or not installed. Make sure it is available in your working directory or install it if necessary.")
    exit()

from random import randint
from time import sleep

# window
win = GraphWin("Three Door Game", 500, 500)
initial_click_text = Text(Point(250, 450), "Click to guess which is the secret door!")
initial_click_text.draw(win)
initial_text = Text(Point(250, 100), "I have a secret door")
initial_text.draw(win)

# quit button
p1 = Point(350, 10)
p2 = Point(450, 60)
quit_button = Rectangle(p1, p2)
quit_button.setFill("white")
quit_button.draw(win)
quit_text = Text(quit_button.getCenter(), "Quit")
quit_text.draw(win)

# score board numbers
wins = 0
loses = 0

# score board graphic
p1 = Point(50, 20)
p2 = Point(100, 70)
wins_box = Rectangle(p1, p2)
wins_box.draw(win)
wins_text = Text(Point(75, 10), "Wins")
wins_text.draw(win)
wins_score_text = Text(wins_box.getCenter(), f"{wins}")
wins_score_text.draw(win)

p1 = Point(100, 20)
p2 = Point(150, 70)
loses_box = Rectangle(p1, p2)
loses_box.draw(win)
loses_text = Text(Point(125, 10), "Loses")
loses_text.draw(win)
loses_score_text = Text(loses_box.getCenter(), f"{loses}")
loses_score_text.draw(win)

# doors
p1 = Point(50, 120)
p2 = Point(150, 420)
door_1 = Rectangle(p1, p2)
door_1.setFill("yellow")
door_1.draw(win)
door_1_text = Text(door_1.getCenter(), "Door 1")
door_1_text.draw(win)

p1 = Point(200, 120)
p2 = Point(300, 420)
door_2 = Rectangle(p1, p2)
door_2.setFill("yellow")
door_2.draw(win)
door_2_text = Text(door_2.getCenter(), "Door 2")
door_2_text.draw(win)

p1 = Point(350, 120)
p2 = Point(450, 420)
door_3 = Rectangle(p1, p2)
door_3.setFill("yellow")
door_3.draw(win)
door_3_text = Text(door_3.getCenter(), "Door 3")
door_3_text.draw(win)

while True:
    secret_door = randint(1, 3)

    point = win.getMouse()

    if door_1.getP1().getX() <= point.getX() <= door_1.getP2().getX() and door_1.getP1().getY() <= point.getY() <= door_1.getP2().getY():
        chosen_door = 1
    elif door_2.getP1().getX() <= point.getX() <= door_2.getP2().getX() and door_2.getP1().getY() <= point.getY() <= door_2.getP2().getY():
        chosen_door = 2
    elif door_3.getP1().getX() <= point.getX() <= door_3.getP2().getX() and door_3.getP1().getY() <= point.getY() <= door_3.getP2().getY():
        chosen_door = 3
    else:
        continue

    if chosen_door == secret_door:
        wins += 1
        wins_score_text.setText(f"{wins}")
        initial_text.setText("You win!")
        if chosen_door == 1:
            door_1.setFill("green")
        elif chosen_door == 2:
            door_2.setFill("green")
        elif chosen_door == 3:
            door_3.setFill("green")
    else:
        loses += 1
        loses_score_text.setText(f"{loses}")
        initial_text.setText("Sorry, incorrect!")
        if secret_door == 1:
            door_1.setFill("green")
        elif secret_door == 2:
            door_2.setFill("green")
        elif secret_door == 3:
            door_3.setFill("green")

        if chosen_door == 1:
            door_1.setFill("red")
        elif chosen_door == 2:
            door_2.setFill("red")
        elif chosen_door == 3:
            door_3.setFill("red")

    initial_click_text.setText("Click anywhere to play again")
    win.getMouse()

    door_1.setFill("yellow")
    door_2.setFill("yellow")
    door_3.setFill("yellow")

    initial_click_text.setText("Click to guess which is the secret door!")
    initial_text.setText("I have a secret door")

    point = win.getMouse()
    if quit_button.getP1().getX() <= point.getX() <= quit_button.getP2().getX() and quit_button.getP1().getY() <= point.getY() <= quit_button.getP2().getY():
        win.close()
        break

