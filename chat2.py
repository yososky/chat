# read file
def read_file(filename):
	lines = []
	with open(filename,'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

# convert
def convert(lines):
	new = []
	person = None
	allen_word_c = 0
	viki_word_c = 0
	allen_sticker_c = 0
	viki_sticker_c = 0
	allen_image_c = 0
	viki_image_c = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_c += 1
			elif s[2] == '圖片':
				allen_image_c += 1
			else:
				for m in s[2:]:
					allen_word_c += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_c += 1
			elif s[2] == '圖片':
				viki_image_c += 1
			else:
				for m in s[2:]:
					viki_word_c += len(m)
	print('Allen said:', allen_word_c, '. Send', allen_sticker_c, 'stickers', '. Send', allen_image_c, 'pictures.')	
	print('Viki said:', viki_word_c, '. Send', viki_sticker_c, 'stickers', '. Send', viki_image_c, 'pictures.')
		#print(s)
	return new

def write_file(filename, lines):
	with open(filename, 'w', ) as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('[LINE]Viki.txt')
	lines = convert(lines)
	#write_file('output.txt',lines)
	
main()