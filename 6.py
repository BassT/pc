import zipfile, re

number = [90052]

with zipfile.ZipFile("channel.zip") as myzip:
	file_names = myzip.namelist()
	for i in range(1000):
		try:
			filename = str(number[0]) + ".txt"
			f = myzip.read(filename)
			file_names.remove(filename)
			number = re.findall("^Next nothing is ([0-9]{1,5})$", f.decode())
			## print(number)
			## if number != None:
				## print("opening: " + number[0] + ".txt (" + str(i) + ")")
		except IndexError:
			print(file_names)
			break

## Collect the comments. (from 46145.txt)
## Opened 908 files
## 908 chain files + 1 readme file = 909 files, but archive contains 910 files
## --> find out which is missing!
## Forget to count start (90052.txt) --> no files missing, all have been openend
