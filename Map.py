#!/usr/bin/env python

import sys

for linha in sys.stdin:
	#separa campos
	campos = linha.split(';')

	id_tweet = campos[0]
	id_autor = campos[1]
	data = campos[2]
	tweet = campos[3]
	div = tweet.split(" ")
	div.lower()
	
	if '"@empresa2' in sorted(div):
		if 'contact' in sorted(div):
			print '%s\t%s' % (id_tweet, "1")
