def init(d,maze,p):
	a = p//d
	b = p%d
	maze[a][b] += 1
	print(maze)

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
