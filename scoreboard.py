from turtle import Turtle
FONT=('Verdana',15,'normal')
ALIGN='center'
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("D:\Coding\python\projects\snake Game\data.txt")  as data:
            self.high_score=int(data.read())
        self.penup()
        self.goto(x=0,y=270)
        self.color('white')
        self.write(f"Score: {self.score}", font=FONT,align=ALIGN)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=FONT,align=ALIGN)

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open ('D:\Coding\python\projects\snake Game\data.txt' ,mode='w') as data:
                data.write(f'{self.high_score}')
        self.score=0
        self.update_scoreboard()

    def score_refresh(self):
        self.score+=1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", font=FONT,align=ALIGN)
