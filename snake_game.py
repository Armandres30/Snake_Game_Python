import random
import curses

s = curses.initscr() # initialize screen
curses.curs_set(0) # set cursor to zero
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0) # create new window
w.keypad(1) #set keypad input
w.timeout(100) # refresh screen every 100 miliseconds

snk_x = sw/4 #initiate snake horizontal at 1 quarter of x-axis screen
snk_y = sh/2 #initiate snake vertical at middle of y-axis screen
snake = [ #create snake body with 3 points
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]
food = [sh/2, sw/2] #add food in middle of screen
w.addch(int(food[0]), int(food[1]), curses.ACS_PI) # add character PI as food in middle of screen

key = curses.KEY_RIGHT

while True: # game loop
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:
        curses.endwin() # dead snake, game over because of crash 
        quit()

    new_head = [snake[0][0], snake[0][1]] # y,x

    if key == curses.KEY_DOWN: #change movemente of snake
        new_head[0] +=1
    if key == curses.KEY_UP:
        new_head[0] -=1
    if key == curses.KEY_LEFT:
        new_head[1] -=1
    if key == curses.KEY_RIGHT:
        new_head[1] +=1

    snake.insert(0, new_head) #adds new head after moving

    if snake[0] == food: # add new food when snake eats food
        food = None
        while food is None: # while food is not created outside actual snake body
            nf = [
                random.randint(1,sh-1),
                random.randint(1,sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI) # add PI char food in screen
    else:
        tail = snake.pop() # defines tails as last snake body's part
        w.addch(int(tail[0]), int(tail[1]), ' ') # adds tails in x,y axiss

    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD) # Add
