anim={'Gato Montes':2,'Yacare overo':4,'Boa acuática':5} 

for i in anim:
	pal=[]
	for car in i:
		pal.append('_')
	pal[anim[i]]=i[anim[i]]
	let = ' '.join(pal)
	print(let)
