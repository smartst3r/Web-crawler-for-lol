import pickle


objects = []
with (open("file.pkl", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break
			
# print(objects[0][0])

with open('formated.txt', 'w') as writer:
	for i in objects[0]:
		writer.write(i.get('name')+' \n')
		###going into each value within categories
		for count, val in enumerate(i.get('categories')):
			# if type(count) == int:
				# print(count)
			if count == 2 or count == 3 or count == 4 or count==0:
				continue
			if 'Champion' in val or 'champion' in val:
				writer.write(val+' \n')
			
		writer.write(' \n'+' \n')
		
