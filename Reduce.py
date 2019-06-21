#!/usr/bin/env python
# -*- coding: utf-8 -*-'''

import sys

ocorrencia = {}
x = 0

for linha in sys.stdin:
	#lê a chave e valor gerada pelo map
	chave,valor = linha.split("\t", 1)

	try:
		valor = int(valor)

	except ValueError:
		continue;

	try:
		ocorrencia[chave] = ocorrencia[chave] + valor
	except:
		ocorrencia[chave] = valor
#Fiz um contador para cada de tweet apartir do id_tweet registrado por determinada empresa.
for id_tweet in ocorrencia.keys():
	x += 1
	#print '%s' % (ocorrencia[id_autor])
print 'Foram respondidos:' , x, 'Tweets'
	
