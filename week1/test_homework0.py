__author__ = 'ahmedissawi'
from homework import *
from TestSuite import *


# ------------------------------------
# Insert your merge function here
# ------------------------------------




# ------------------------------------
# testing
# ------------------------------------
# create a TestSuite object
suite = TestSuite()
game= TwentyFortyEight(3, 3)
game.new_tile()
game.new_tile()
game.new_tile()
game.new_tile()
game.new_tile()
game.new_tile()
game.new_tile()
game.new_tile()

# test format_function on various inputs
#suite.run_test(game., "Test #1:")




suite.report_results()