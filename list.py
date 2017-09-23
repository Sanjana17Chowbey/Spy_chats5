a = [1, 8, 2, 3, 5, 17, 13, 19, 27, 95, 99]

number = int(raw_input("Choose a number: "))

new_list_generated = []

for i in a:
	if i < number:
		new_list_generated.append(i)

print new_list_generated