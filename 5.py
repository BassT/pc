## found banner.p file in source view
## google yields: .p is python pickle file - something with serialization

import pickle, pprint

with open("banner.p", "rb") as f:
	data = pickle.load(f)
##	pprint.pprint(data)

for nested_list in data:
	string = ""
	for element in nested_list:
		string = string + (element[0] * element[1])
	print(string)
