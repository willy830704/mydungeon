import random
import getch 
# from getch import Getch as g
import sys
import maze as m
import character as ch

def message():
	print('   w : up              d : right')
	print('   s : down            a : left')
	print('   q : quit            h : hint')
	print()
	
d = m.choose_difficult()

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

m.pmaze(d,maze,'p')

while True:
	c = getch.getch()
	
	# c = Getch()
	if c=='q':
		sys.exit(0)	
	if c=='w':
		m.move(d,maze_b)	
		now = m.nowpos(d,maze)
		if now[0]==0:
			print('Don\'t go up! You want to DIE?')	
			m.pmaze(d,maze,'p')		
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
			m.pmaze(d,maze,'p')
	if c=='s':
		m.move(d,maze_b)	
		now = m.nowpos(d,maze)
		if now[0]==d-1:
			print('Don\'t go down! You want to DIE?')
			m.pmaze(d,maze,'p')
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
			m.pmaze(d,maze,'p')
	if c=='a':
		m.move(d,maze_b)	
		now = m.nowpos(d,maze)
		if now[1]==0:
			print('Don\'t go left! You want to DIE?')
			m.pmaze(d,maze,'p')
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
			m.pmaze(d,maze,'p')
	if c=='d':
		m.move(d,maze_b)	
		now = m.nowpos(d,maze)
		if now[1]==d-1:
			print('Don\'t go right! You want to DIE?')
			m.pmaze(d,maze,'p')
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
			m.pmaze(d,maze,'p')
	if c == 'h':
		m.pmaze(d,maze,'p')
		m.pmaze(d,maze_e,'e')
		m.pmaze(d,maze_b,'b')
		
			
			








