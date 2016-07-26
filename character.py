import random

def player_init(d):
	p = random.randint(0,d*d-1)
	return p

def boss_init(d,p):
	while True:
		boss = random.randint(0,d*d-1)
		if boss!=p:
			return boss

def exit_init(d,p,b):
	while True:
		exit = random.randint(0,d*d-1)
		if exit!=p and exit!=b:
			return exit
