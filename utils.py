# -*- coding: utf-8 -*-
#!/usr/bin/env python 
import string 

class Utils: 
	def cleanStopWordsPunctuations(self, line, stopList): 
		texts = [] 
		line = line.translate(None, string.punctuation) 
		for word in line.lower().split(): 
			if not word in stopList: 
				texts.append(word) 
		print (texts) 
		return texts 



