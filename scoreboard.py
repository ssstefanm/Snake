from turtle import Turtle


# inherits from turtle
# turtle who knows how to
# track the score and to display it

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 200)
        self.speed("fastest")
        self.write(f"Score: {self.score}", False, "Center", ("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("game over", False, "Center", ("Courier", 20, "normal"))

    def refresh(self):
        self.write(f"Score: {self.score}", False, "Center", ("Courier", 20, "normal"))
