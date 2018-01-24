class Song(object):
	
	def __init__(self, lyrics):  #左右各两个下划线
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)
			
happy_bday = Song(["Happy birthday to you",    #把Song这个class赋给happy_bday
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around tha family",
					"With pockets full of shells"])
					
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
