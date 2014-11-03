import sys
import re
pat = re.compile(r'\B#\w+')
print(pat.findall('RT @assholeofday: #Ebola: Rick Wiles hopes it will "cleanse" America of atheism, homosexuality and promiscuity http://t.co/lUPP805PvK http:\u2026'))