import random
import getch 
# from getch import Getch as g
import sys

maze = [[0,0,0],[0,0,0],[0,0,0]]

player = random.randint(0,8)

def init(maze,p):
	a = p//3
	b = p%3
	maze[a][b] += 1
	print(p)

def clear(maze):
	for i in range(3):
		for j in range(3):
			if maze[i][j]==1:
				maze[i][j]=0
				return [i,j]

def pmaze(maze):
	for i in range(3):
		print(maze[i])
 
init(maze,player)	
pmaze(maze)
while True:
	c = getch.getch()
	# c = Getch()
	if c=='q':
		sys.exit(0)
	
	if c=='w':
		now = clear(maze)
		if now[0]==0:
			print('Do not do it! You want to DIE?')
		else:
			x = now[0]-1
			y = now[1]
			maze[x][y]=1
			pmaze(maze)
	if c=='s':
		now = clear(maze)
		x = now[0]+1
		y = now[1]
		maze[x][y]=1
		pmaze (maze)
	if c=='a':
		now = clear(maze)
		x = now[0]
		y = now[1]-1
		maze[x][y]=1
		pmaze(maze)
	if c=='d':
		now = clear(maze)
		x = now[0]
		y = now[1]+1
		maze[x][y]=1
		pmaze(maze)
			








