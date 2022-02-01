from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.write(f"{self.player_2_score} : {self.player_1_score}", False, align="center", font=("Arial", 40, "normal"))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.goto(0, 240)
        self.write(f"{self.player_2_score} : {self.player_1_score}", False, align="center", font=("Arial", 40, "normal"))

    def increase_score_of_player1(self):
        self.player_1_score += 1
        self.update_score()

    def increase_score_of_player2(self):
        self.player_2_score += 1
        self.update_score()
