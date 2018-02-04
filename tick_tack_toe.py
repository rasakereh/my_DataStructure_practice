class Cell:
	'Each cell is represented using this class'
	content = ' '
	
	def put(self, _content):
		if(self.content == ' '):
			self.content = _content
			
			return True
		
		return False

class GameBoard:
	'Class as a blueprint of GameBoard'
	cells = [[Cell() for j in range(3)] for i in range(3)]
	

class Game:
	'The whole game is here :)'
	board = GameBoard()
	turn = 'X'
	
	def showState(self):
		print(chr(27) + "[2J")
		print('This is "{0:s}" turn:\n'.format(self.turn))
		print('\t         |         |         \n')
		print('\t    {0:s}    |    {1:s}    |    {2:s}    \n'.format(self.board.cells[0][0].content, self.board.cells[0][1].content, self.board.cells[0][2].content))
		print('\t         |         |         \n')
		print('\t---------+---------+---------\n')
		print('\t         |         |         \n')
		print('\t    {0:s}    |    {1:s}    |    {2:s}    \n'.format(self.board.cells[1][0].content, self.board.cells[1][1].content, self.board.cells[1][2].content))
		print('\t         |         |         \n')
		print('\t---------+---------+---------\n')
		print('\t         |         |         \n')
		print('\t    {0:s}    |    {1:s}    |    {2:s}    \n'.format(self.board.cells[2][0].content, self.board.cells[2][1].content, self.board.cells[2][2].content))
		print('\t         |         |         \n')
		
		if self.isEnd():
			print('Player {0:s} won!!!\n'.format(self.turn))
	
	def nextStep(self):
		while True:
			[row, col] = input().split(',')
			[row, col] = [int(row)-1, int(col)-1]
			if not(row in range(3) and col in range(3)):
				continue
				
			if(self.board.cells[row][col].put(self.turn)):
				break
		
	def switchTurn(self):
		if(self.turn == 'X'):
			self.turn = 'O'
		else:
			self.turn = 'X'
		
	def gameFlow(self):
		while True:
			self.showState()
			self.nextStep()
			if self.isEnd():
				self.showState()
				return
			self.switchTurn()
		
		
	def isEnd(self):
		for rows in self.board.cells:
			if(' ' != rows[0].content and rows[0].content == rows[1].content and rows[1].content == rows[2].content):
				return True
		
		if(self.board.cells[0][0].content == self.board.cells[1][1].content and
			self.board.cells[1][1].content == self.board.cells[2][2].content and
			self.board.cells[2][2].content != ' '):
				return True
				
		if(self.board.cells[2][0].content == self.board.cells[1][1].content and
			self.board.cells[1][1].content == self.board.cells[0][2].content and
			self.board.cells[0][2].content != ' '):
				return True
		
		return False
		
		
game = Game()
game.gameFlow()

