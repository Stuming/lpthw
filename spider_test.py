# -*- coding: utf-8 -*-

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://zhidao.baidu.com/question/344311336.html"
WORDS = []

for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())

print(WORDS)