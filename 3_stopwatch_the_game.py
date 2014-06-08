# template for "Stopwatch: The Game"

import random
import simplegui
# define global variables
interval = 100 #0.1 second
current_time = 0 #global integer timer
width = 300
height = 200
timer_on = False
success = 0
total_tries = 0
color_palette = ["Aqua", "Blue", "Fuchsia", "Gray", "Green",
                 "Lime", "Maroon", "Olive", "Orange", "Purple",
                 "Red", "Silver", "Teal", "White", "Yellow"]

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(input):
    A = input / 600
    B = "0"
    if (input % 600) >= 100:
        B = ""
    CD =  (input % 600) / 10.0
    return str(A) + ":" + B + str(CD)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer_on
    timer_on = True
    timer.start()
    
def stop():
    global current_time, timer_on, success, total_tries
    timer.stop()
    if timer_on == True:
        second = (current_time % 600) / 10.0
        if (second == int(second)):
            success += 1
        total_tries += 1
        timer_on = False
        
def reset():
    global current_time, timer_on, success, total_tries
    current_time = 0
    timer_on = True
    success = 0
    total_tries = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global current_time
    current_time += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(current_time),
                     [(width/2)-50, (height/2)+10], 40,
                     'White')
    color = color_palette[random.randrange(len(color_palette)-1)]
    canvas.draw_text(str(success) + "/" + str(total_tries),
                     [(width-50), (height-175)], 30, color)

# create frame
frame = simplegui.create_frame("Stopwatch: The Game", width, height)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(interval, timer_handler)

# register event handlers
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
