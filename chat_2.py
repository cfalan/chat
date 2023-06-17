


import os
import time

def read_f(rfile):
	with open(rfile, 'r', encoding='utf-8') as f:
		for line in f:
			word = line.strip()
			chat.append(word)
	return chat


def formating(chat):

	speaker = None
	allen_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in chat:
		element = line.split(' ')
		# print(element[2:])
		time = element[0]
		speaker = element[1]
		if speaker == 'Allen':
			if element[2] == '貼圖':
				allen_sticker_count += 1
			elif element[2] == '圖片':
				allen_image_count += 1
			else:
				for each_element in element[2:]:
					allen_count += len(each_element)
					print(allen_count, each_element)

		elif speaker == 'Viki':
			if element[2] == '貼圖':
				viki_sticker_count += 1
			elif element[2] == '圖片':
				viki_image_count += 1
			else:
				for each_element in element[2:]:
					viki_count += len(each_element)
					print(viki_count, each_element)
		
	print('allen count', allen_count)
	print('allen sticker count', allen_sticker_count)
	print('allen image count', allen_image_count)
	print('viki count', viki_count)
	print('viki sticker count', viki_sticker_count)
	print('viki image count', viki_image_count)

	return output


def write_f(wfile, output):
	with open(wfile, 'w', encoding = 'utf-8') as w:
		for line in output:
			w.write(line + '\n')


chat = []
output = []
wfile = 'gogogo_2.txt'
rfile = 'LINE-viki.txt'

def main():
	chat = read_f(rfile)
	time.sleep(1)

	output = formating(chat)
	time.sleep(1)

	write_f(wfile, output)

main()

'''
python3 chat_2.py

#更新版本用
git add chat_2.py
git commit -m "加入 main()"
git push origin main
'''