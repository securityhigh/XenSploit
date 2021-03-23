from os import system
from sys import argv

try:
	system(f"python3 weevely3/weevely.py {argv[1]} {argv[2]}")

except:
	system(f"python weevely3/weevely.py {argv[1]} {argv[2]}")