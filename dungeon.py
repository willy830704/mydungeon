import random
import getch 
# from getch import Getch as g
import sys
import maze as m
import character as ch

def message():
	print('   w : up')
	print('   a : left')
	print('   s : down')
	print('   d : right')
	print('   q : quit')

d = 6
maze = []
maze_e = []
maze_b = []
m.init_maze(d,maze)
m.init_maze(d,maze_e)
m.init_maze(d,maze_b)

player = ch.player_init(d,maze)
exit = ch.exit_init(d,player,maze_e)
boss = ch.boss_init(d,player,exit,maze_b)
	
message()

m.pmaze(d,maze)
m.pmaze(d,maze_e)
m.pmaze(d,maze_b)

while True:
	c = getch.getch()
	m.move(d,maze_b)	
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
			stat = m.check(d,maze,maze_e,maze_b)
			cont = m.gameover(stat)
			if cont == 1:
				m.restart(d,maze,maze_e,maze_b,player,exit,boss)
			elif cont == 0 :
				print('GoodBye~')
				break
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
			stat = m.check(d,maze,maze_e,maze_b)
			cont = m.gameover(stat)
			if cont == 1:
				m.restart(d,maze,maze_e,maze_b,player,exit,boss)
			elif cont == 0 :
				print('GoodBye~')
				break
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
			stat = m.check(d,maze,maze_e,maze_b)
			cont = m.gameover(stat)
			if cont == 1:
				m.restart(d,maze,maze_e,maze_b,player,exit,boss)
			elif cont == 0 :
				print('GoodBye~')
				break
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
			stat = m.check(d,maze,maze_e,maze_b)
			cont = m.gameover(stat)
			if cont == 1:
				m.restart(d,maze,maze_e,maze_b,player,exit,boss)
			elif cont == 0 :
				print('GoodBye~')
				break
			m.pmaze(d,maze)
		
			
			








