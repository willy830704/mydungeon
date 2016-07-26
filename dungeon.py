import random
import getch 
# from getch import Getch as g
import sys
import maze as m
import character as ch

d = 5

#maze = [[0,0,0],[0,0,0],[0,0,0]]
maze = []
for i in range(d):
	maze.append([])
	for j in range(d):
		maze[i].append(0)


player = ch.player_init(d)
boss = ch.boss_init(d,player)
exit = ch.exit_init(d,player,boss)

	
m.init(d,maze,player)
print(boss,exit,player)

m.pmaze(d,maze)
while True:
	c = getch.getch()
	# c = Getch()
	if c=='q':
		sys.exit(0)
	
	if c=='w':
		now = m.nowpos(d,maze)
		if now[0]==0:
			print('Don\'t go up! You want to DIE?')	
			m.pmaze(d,maze)		
		else:
			x = now[0]
			y = now[1]
			maze[x][y]=0
			maze[x-1][y]=1
			m.pmaze(d,maze)
	if c=='s':
		now = m.nowpos(d,maze)
		if now[0]==d-1:
			print('Don\'t go down! You want to DIE?')
			m.pmaze(d,maze)
		else:
			x = now[0]
			y = now[1]
			maze[x][y]=0
			maze[x+1][y]=1
			m.pmaze(d,maze)
	if c=='a':
		now = m.nowpos(d,maze)
		if now[1]==0:
			print('Don\'t go left! You want to DIE?')
			m.pmaze(d,maze)
		else:
			x = now[0]
			y = now[1]
			maze[x][y]=0
			maze[x][y-1]=1
			m.pmaze(d,maze)
	if c=='d':
		now = m.nowpos(d,maze)
		if now[1]==d-1:
			print('Don\'t go right! You want to DIE?')
			m.pmaze(d,maze)
		else:
			x = now[0]
			y = now[1]
			maze[x][y]=0
			maze[x][y+1]=1
			m.pmaze(d,maze)
			








