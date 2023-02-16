import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__ (self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      self.contents += value * [key]

  def draw(self, number):
    try:
      balls = random.sample(self.contents, number)
    except:
      balls = copy.deepcopy(self.contents)

    for ball in balls:
      self.contents.remove(ball)
    return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    copy_hat = copy.deepcopy(hat)
    balls = copy_hat.draw(num_balls_drawn)

    expectedballs = []
    for key, value in expected_balls.items():
      expectedballs += value * [key]

    if drawn_balls(expectedballs, balls):
      count += 1
  
  return count / num_experiments

def drawn_balls(expected_balls, actual_balls):
  for y in expected_balls:
    if y in actual_balls:
      actual_balls.remove(y)
    else:
      return False
  return True
