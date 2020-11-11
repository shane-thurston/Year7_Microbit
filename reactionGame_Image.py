from microbit import *
import random

display.scroll('Get Ready')
sleep(random.randint(2000,4000))
display.show(Image.BUTTERFLY)

reactionTime = 0
while not button_b.is_pressed():
  reactionTime = reactionTime + 1
  sleep(10)
  
if reactionTime < 50:
  display.show(Image.HAPPY)
  sleep(500)
  
display.scroll('Your time: ' + str(reactionTime))
