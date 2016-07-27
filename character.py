import random

def player_init(d,maze):
	p = random.randint(0,d*d-1)
	x = p//d
	y = p%d
	maze[x][y] += 1
	return p

def exit_init(d,p,maze):
	while True:
		exit = random.randint(0,d*d-1)
		if exit!=p :			
			x = exit//d
			y = exit%d
			maze[x][y] += 1
			return exit

def boss_init(d,p,e,maze):
	bossnum = d-2
	boss = []
	exist = [d,p]
	while bossnum>0:
		b = random.randint(0,d*d-1)
		if b not in exist:
			bossnum = bossnum-1
			boss.append(b)			
			exist.append(b)
			x = b//d
			y = b%d
			maze[x][y] += 1
	return boss	
'''
def init(d,maze,p):
	a = p//d
	b = p%d
	maze[a][b] += 1
	print(maze)
'''
