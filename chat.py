


import os
import time

def read_f(rfile):
	with open(rfile, 'r', encoding='utf-8') as f:
		for line in f:
			word = line.strip()
			chat.append(word)
			print(word)
	print(chat)
	return chat


def formating(chat):

	speaker = None

	for line in chat:
		if line == 'Allen':
			speaker = 'Allen'
			# print(speaker)
			continue
		elif line == 'Tom':
			speaker = 'Tom'
			# print(speaker)
			continue
		if speaker:
			speak = (speaker + ':' + line)
			output.append(speak)

		# elif speaker == 'Allen':
		# 	speak = ('Allen: ' + line)
		# 	# print(speak)
		# 	output.append(speak)
		# 	# print(output)
		# elif speaker == 'Tom':
		# 	speak = ('Tom: ' + line)
		# 	output.append(speak)

	print(speaker)
	print(output)
	return output


def write_f(wfile, output):
	with open(wfile, 'w', encoding = 'utf-8') as w:
		for line in output:
			w.write(line + '\n')


chat = []
output = []
wfile = 'gogo.txt'
rfile = 'input.txt'

chat = read_f(rfile)
output = formating(chat)
write_f(wfile, output)

'''
python3 chat.py

#更新版本用
git add chat.py
git commit -m "重構"
git push origin main
'''