# random module for random food generation.
import random
# curses module provides keyboard handling and screen painting
import curses

# initialize module and recieve a windowObject which represents the screen.
s = curses.initscr()

# set cursor visibility to invisible.
curses.curs_set(0)

# get screen dimensions from a tuple.
sh, sw = s.getmaxyx()

# return a new window which dimensions are set by the first two parameters and set left upper corner by the last two parameters
w = curses.newwin(sh, sw, 0, 0)

# keypad(1) let curses take over control of escape sequences instead of leaving it in hands of the input stream system.
w.keypad(1)

# set delay in the response time of the window, parameter is expressed in miliseconds.
w.timeout(75)

# set initial location of the snake
snk_x = sw/4
snk_y = sh/2 

# snake body composition
snake=[
	[snk_y, snk_x],
	[snk_y, snk_x-1],
	[snk_y, snk_x-2]
]

# initial food location
food = [sh/2, sw/2]

# print food on screen.
w.addch(food[0], food[1], curses.ACS_PI)

# setting initial key as right direction key.
key = curses.KEY_RIGHT


while True:
	# get a character as the next key.
	next_key = w.getch()
	key = key if next_key == -1 else next_key

	if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
		curses.endwin()
		quit()

	new_head = [snake[0][0], snake[0][1]]

	if key == curses.KEY_DOWN:
		new_head[0] +=1
	if key == curses.KEY_UP:
		new_head[0] -=1
	if key == curses.KEY_LEFT:
		new_head[1] -=1
	if key == curses.KEY_RIGHT:
		new_head[1] +=1

	snake.insert(0, new_head)

	if snake[0] == food:
		food = None
		while food is None:
			nf = [
				random.randint(1, sh-1),
				random.randint(1, sw-1)
			]
			food = nf if nf not in snake else None
		w.addch(food[0], food[1], curses.ACS_PI)
	else:
		tail = snake.pop()
		w.addch(tail[0], tail[1],' ')

	w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)