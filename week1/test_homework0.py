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

# test format_function on various inputs
suite.run_test(merge([2, 0, 2, 4]), [4, 4, 0, 0], "Test #1:")
suite.run_test(merge([0, 0, 2, 2]), [4, 0, 0, 0], "Test #2:")
suite.run_test(merge([2, 2, 0, 0]), [4, 0, 0, 0], "Test #3:")
suite.run_test(merge([2, 2, 2, 2]), [4, 4, 0, 0], "Test #4:")
suite.run_test(merge([8, 16, 16, 8]), [8, 32, 8, 0], "Test #5:")

suite.report_results()

test = TwentyFortyEight(4, 5)
print "Your Initial Grid: ", test
print "Expected Grid:      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]"
print
test.set_tile(0, 0, 2)
test.set_tile(1, 2, 4)
test.set_tile(2, 1, 8)
test.set_tile(3, 4, 16)

# test format_function on various inputs

print "Your Grid after set_tile: ", test
print "Expected current grid:     [[2, 0, 0, 0, 0], [0, 0, 4, 0, 0], [0, 8, 0, 0, 0], [0, 0, 0, 0, 16]]"
print
suite.run_test(test.get_tile(0 , 0), 2, "Test #1:")
suite.run_test(test.get_tile(1 , 2), 4, "Test #2:")
suite.run_test(test.get_tile(2 , 1), 8, "Test #3:")
suite.run_test(test.get_tile(3 , 4), 16, "Test #4:")
suite.run_test(test.get_tile(1 , 1), 0, "Test #5:")

game = TwentyFortyEight(3, 3)
game.set_tile(0, 0, 2)
print game
suite.run_test(game.get_tile(0, 2), 0, "Test #6:")

suite.report_results()