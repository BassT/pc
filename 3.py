##One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

import sys
import re
foundLetters = []
pattern = re.compile('[^A-Z]+[A-Z]{3}[a-z]{1}[A-Z]{3}[^A-Z]+')
pattern2 = re.compile('[A-Z]{3}[a-z]{1}[A-Z]{3}')
with open('commentFromEqualityHtml.txt') as f:
        for line in f:
        	m = pattern.search(line)
        	if m != None:
        		sys.stdout.write('Found: ' + m.group() + '\n')
        		m = pattern2.search(m.group())
        		foundLetters.append(m.group()[3])
sys.stdout.write(''.join(foundLetters))
sys.stdout.flush()
