# Autor : Pires Baptiste
# Date : 15/01/2019
# Mail : pires.baptiste.contact@gmail.com

"""
DESCRIPTION :

This Sublime Text packahe allows you to generat lorem text randomly from 1 to 500 words.

It's easy to use, there is an example :

First, you can type just "lo" and it will insert you 25 words, it's the default 
number of words if you don't specify one. 

If you type "lorem2" then press CTRL + SPACE for the auto-completion, it will
generate your lorem.

The allowed range starts from 0 to 500. If you type "lorem0", it will insert 1 word.

If you have any suggestions to improve this plugin, please send me a message at the 
email specified in the header of the file
"""

import sublime
import sublime_plugin
from re import search, sub
from random import randint

class GenerateLorem(sublime_plugin.EventListener):

	# Event autocompletion called
	def on_query_completions( self, view, prefix, locations ):

		# Get the region
		region = view.sel()[0].a		
		
		# Get the word next to the cursor
		word = view.substr(view.word(region))

		# This regex check if the word contains at least "lo" if it doesn't there is no 
		# reason to continue
		if search("^[l,L]o[rem]{0,3}[0-9]{0,}$", word) == None:
			return
		else:
			# There we check the number of 
			nb_word = sub(r"[^\0-9]", "", word)
			
			# Some test to get the number of words wanted
			if len(nb_word) == 0:
				lorem_len = 25
			else:
				if int(nb_word) <= 500 and int(nb_word)!= 0:
					lorem_len = nb_word
				elif int(nb_word) == 0:
					lorem_len = 1
					print("uh")
				else:
					lorem_len = 500
			
			# Some lorem words
			lorem_words = "dolor sit consectetuer adipiscing elit diam onummy nibh tincidunt ut laoreetm magnaaAliquam erat ut wisi enim minim veniam quis exerci tation ullamcorper lobortis nisl ut ex ea commodo".split()
			
			# Formatting the returned str 
			# Need to do that because if the user wants 1 word we can't insert "Lorem ipsum"
			if lorem_len == int(1):
				lorem_str = "Lorem"
			else:
				lorem_str = "Lorem ipsum"

			# Still formating return str
			for i in range(int(lorem_len) - 2):
				if i%10 ==0 and i!=0:
					lorem_str += ". " + lorem_words[randint(0, len(lorem_words) - 1)].capitalize()
				else:
					lorem_str += " " + lorem_words[randint(0, len(lorem_words) - 1)]

			lorem_str += "."

			# Creating the returned array 
			completions_data = []
			completions_data.append( ("lorem" + str(nb_word), lorem_str))

			return (completions_data)

		return 0