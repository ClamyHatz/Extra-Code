# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
# leaderboard variables
leaderboard_file_name = "D:/CSP/Unit 1/1.2.2/a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")

spot_color = "pink"
spot_shape = "circle"
spot_size = 2

font_setup = ("Arial", 20, "normal")

score = 0

timer = 30

counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----

counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(260, 280)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(-300, 260)

spot = trtl.Turtle()
spot.shape(spot_shape)
spot.turtlesize(spot_size)
spot.fillcolor(spot_color)
spot.penup()

start = trtl.Turtle()
start.shape('square')
start.turtlesize(spot_size)
start.penup()

#-----game functions--------
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    spot.hideturtle()
    wn.bgcolor("red")
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def update_score():
    global score
    score += 1
    score_writer.write(score, font=font_setup)   

def change_position():
    new_xpos = rand.randint(-300, 300)
    new_ypos = rand.randint(-300, 300)
    spot.goto(new_xpos, new_ypos)

def spot_clicked(x,y):
  spot.hideturtle()
  score_writer.clear()
  update_score()
  change_position()
  spot.showturtle()

def start_game(x,y):
  start.hideturtle()
  counter.getscreen().ontimer(countdown, counter_interval)
   
#-----events----------------

spot.onclick(spot_clicked)

start.onclick(start_game)

wn = trtl.Screen()
wn.mainloop()