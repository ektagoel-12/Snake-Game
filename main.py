from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collosion with food
    if snake.head.distance(food) < 15:
       snake.extend()
       food.refresh()
       scoreboard.score_refresh()

    #Detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        scoreboard.reset()
        snake.reset()


    #Detect collision with tail
    #if head collides with any segment in the tail:
            #trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
           scoreboard.reset()
           snake.reset()



screen.exitonclick()