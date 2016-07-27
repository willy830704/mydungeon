import getch
import character as ch

def init_maze(d,maze):
	for i in range(d):
		maze.append([])
		for j in range(d):
			maze[i].append(0)
	return maze

def nowpos(d,maze):
	for i in range(d):
		for j in range(d):
			if maze[i][j]==1:
				return [i,j]

def pmaze(d,maze):
	print('  ',end='')
	for i in range(d):
		print("=====",end="")
	print()
	for i in range(d):
		print(' |',end='')
		for j in range(d):
			print('|',end='')
			if maze[i][j]==0:
				print('   ',end='|')
			else:
				print('@_@',end='|')
		print('|')
		print('  ',end='')
		for j in range(d):
			print('=====',end='')
		print()
	print()

def check(d,maze,maze_e,maze_b):
	for i in range(d):
		for j in range(d):
			if maze[i][j] == maze_b[i][j] and maze[i][j]==1:
				return 2
	for i in range(d):
		for j in range(d):
			if maze[i][j] == maze_e[i][j] and maze[i][j]==1:
				return 1
	return 0

def gameover(stat):
	if stat == 2:
		print ('Boss gets you !  Continue? (y/n)' )
		while True:
			c = getch.getch()
			if c == 'y':
				return 1
			if c == 'n':
				return 0
	elif stat == 1:
		print ('You have escaped successfully ! Continue? (y/n)')
		while True:
			c = getch.getch()
			if c == 'y':
				return 1
			if c == 'n':
				return 0
	else :
		return 2

def restart(d,maze,maze_e,maze_b,player,exit,boss):
	for i in range(d):
		for j in range(d):
			maze[i][j] = 0
			maze_e[i][j] = 0
			maze_b[i][j] = 0
	player = ch.player_init(d,maze)
	exit = ch.exit_init(d,player,maze_e)
	boss = ch.boss_init(d,player,exit,maze_b)
		
def move(d,maze_b):
	for i in range(1,d-1):
		for j in range(1,d-1):
			if maze_b[i-1][j] == 1 or maze_b[i+1][j] == 1 or maze_b[i][j-1] == 1 or maze_b[i][j+1] == 1:
				maze_b[i][j] += 2
	for i in range(d):
		print (maze_b[i])


