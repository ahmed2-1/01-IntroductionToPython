"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Tom Ahmed.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(20)
###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
turtle_x = rg.SimpleTurtle()
turtle_x.pen = rg.Pen("red", 2)
turtle_y = rg.SimpleTurtle()
turtle_y.pen = rg.Pen("blue", 2)
turtle_x.pen_up()
turtle_y.pen_up()
turtle_x.go_to(rg.Point(-320,0))
turtle_y.go_to(rg.Point(-320,0))
turtle_x.pen_down()
turtle_y.pen_down()
for i in range(12):
    for j in range(5):
        turtle_x.left(72)
        turtle_x.forward(50)
    turtle_x.forward(80)
    for k in range(5):
        turtle_y.right(72)
        turtle_y.forward(50)
    turtle_y.forward(80)
window.close_on_mouse_click()



