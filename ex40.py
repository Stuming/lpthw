# -*- coding: utf-8 -*-

class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)
			
	def change_the_lyrics(self, new_lyrics):
		self.lyrics = new_lyrics
			
happy_bday = Song(["Happy birthday to you",
				   "I don’t want to get sued",
				   "So I’ll stop right there"]) # remember to use []
				   
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
						
happy_bday.sing_me_a_song()

print('-' * 10)

bulls_on_parade.sing_me_a_song()

print('-' * 10)

happy_bday.change_the_lyrics(["Happy birthday to you again",
							 "And I wish you happy everyday."])
happy_bday.sing_me_a_song()