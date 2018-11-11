class Board:
	def __init__(self, player):
		self.board = [
					[0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0],
					[0,0,0,1,-1,0,0,0],
					[0,0,0,-1,1,0,0,0],
					[0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0]
					]
		self.player = player

	def print_board(self):
		self.print_line()
		print '|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |'
		self.print_line()
		for row in range(0, len(self.board)):
			appendix = '| ' + str(row) + ' |'
			for col in range(0, len(self.board[row])):
				if self.board[row][col] == 0:
					appendix += '   |'
				elif self.board[row][col] == 1:
					appendix += ' X |'
				elif self.board[row][col] == -1:
					appendix += ' Y |'
			print appendix
			self.print_line()

	def print_line(self):
		print '+---+---+---+---+---+---+---+---+---+'

	def loop_board(self):
		for row in range(0, len(self.board)):
			for col in range(0, len(self.board[row])):
				if self.board[row][col] == self.player:
					self.check_moves((row, col))

	def check_moves(self, coordinates):
		# print coordinates
		self.__check_north(coordinates[0], coordinates[1])
		# self.__check_northeast(coordinates[0], coordinates[1])
		# self.__check_east(coordinates[0], coordinates[1])
		# self.__check_southeast(coordinates[0], coordinates[1])
		# self.__check_south(coordinates[0], coordinates[1])
		# self.__check_southwest(coordinates[0], coordinates[1])
		# self.__check_west(coordinates[0], coordinates[1])		
		# self.__check_northwest(coordinates[0], coordinates[1])

	def __check_north(self, current_y, current_x):
		if self.player == 1 and self.board[current_y-1][current_x] == -1:
			print 'true for ' + str(current_y-1) + str(current_x) + ' north'
		elif self.player == -1 and self.board[current_y][current_x] == 1:
			print 'true for ' + str(current_y-1) + str(current_x) + ' north'
		else: 
			print None
			

	def __check_northeast(self, current_y, current_x):
		if self.player == 1 and self.board[current_y-1][current_x+1] == -1:
			print 'true for ' + str(current_y-1) + str(current_x+1) + ' northeast'
		elif self.player == -1 and self.board[current_y][current_x] == 1:
			print 'true for ' + str(current_y-1) + str(current_x+1) + ' northeast'
			

	def __check_east(self, current_y, current_x):
		if self.player == 1 and self.board[current_y][current_x+1] == -1:
			print 'true for ' + str(current_y) + str(current_x+1) + ' east'
		elif self.player == -1 and self.board[current_y][current_x] == 1:
			print 'true for ' + str(current_y) + str(current_x) + ' east'
			

	def __check_southeast(self, current_y, current_x):
		if self.player == 1 and self.board[current_y+1][current_x+1] == -1:
			print 'true for ' + str(current_y+1) + str(current_x+1)  + ' southeast'
		elif self.player == -1 and self.board[current_y][current_x] == 1:
			print 'true for ' + str(current_y) + str(current_x) + ' southeast'
			

	def __check_south(self, current_y, current_x):
		if self.player == 1 and self.board[current_y+1][current_x] == -1:
			print 'true for ' + str(current_y+1) + str(current_x) + ' south'
		elif self.player == -1 and self.board[current_y][current_x] == 1:
			print 'true for ' + str(current_y) + str(current_x) + ' south'
			

	def __check_southwest(self, current_y, current_x):
		if self.player == 1 and self.board[current_y+1][current_x-1] == -1:
			print 'true for ' + str(current_y+1) + str(current_x-1) + ' southwest'
		elif self.player == -1 and self.board[current_y][current_x] == 1:
			print 'true for ' + str(current_y) + str(current_x) + ' southwest'
			

	def __check_west(self, current_y, current_x):
		if self.player == 1 and self.board[current_y][current_x-1] == -1:
			print 'true for ' + str(current_y) + str(current_x-1) + ' west'
		elif self.player == -1 and self.board[current_y][current_x] == 1:
			print 'true for ' + str(current_y) + str(current_x) + ' west'
			

	def __check_northwest(self, current_y, current_x):
		if self.player == 1 and self.board[current_y-1][current_x-1] == -1:
			print 'true for ' + str(current_y-1) + str(current_x-1)  + ' northwest'
		elif self.player == -1 and self.board[current_y][current_x] == 1:
			print 'true for ' + str(current_y) + str(current_x) + ' northwest'
			

