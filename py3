#!/bin/python3


import subprocess
import readline
from math import *
from types import *
from text import text


PS1 = '    ~ '
PS2 = ' | '
CLEAR_CODE = subprocess.check_output(["clear"]).decode("UTF-8")


def listToString(obj, indent, obj_char):
	obj = list(obj)
	if len(str(obj)) < 30:
		return obj_char[0]+" " + ", ".join(f"{toString(i, indent + 1)}" for i in obj) + " "+obj_char[1]
	else:
		return obj_char[0]+"\n" + ",\n".join(f"{(' '*2*indent)}{toString(i, indent + 1)}" for i in obj) + "\n"+(' '*2*(indent-1))+obj_char[1]


def dictToString(obj, indent):
	obj = list(obj.items())
	if len(str(obj)) < 30:
		return "{ " + ", ".join(f"{toString(i, indent + 1)}: {toString(j, indent + 1)}" for i, j in obj) + " }"
	else:
		return "{\n" + ",\n".join(f"{(' '*2*indent)}{toString(i, indent + 1)}: {toString(j, indent + 1)}" for i, j in obj) + "\n"+(' '*2*(indent-1))+"}"


def toString(obj, indent=1):
	if obj == None:
		return f"{text.brmagenta}None{text.r}"
	elif type(obj) == int:
		return f"{text.magenta}{str(obj)}{text.r}"
	elif type(obj) == float:
		return f"{text.magenta}{str(obj)}{text.r}"
	elif type(obj) == complex:
		return f"({text.brmagenta}{str(obj.real)}{text.r}+{text.brmagenta}{str(obj.imag)}{text.brgreen}j{text.r})"
	elif type(obj) == str:
		obj = obj.replace('\\', '\\\\')
		obj = obj.replace('\n', '\\n')
		obj = obj.replace('\t', '\\t')
		if len(obj) <= 1: return f"'{text.yellow}{obj}{text.r}'"
		else:             return f"\"{text.yellow}{obj}{text.r}\""
	elif type(obj) == list:
		return listToString(obj, indent, '[]')
	elif type(obj) == tuple:
		return listToString(obj, indent, '()')
	elif type(obj) == set:
		return listToString(obj, indent, '{}')
	elif type(obj) == dict:
		return dictToString(obj, indent)
	elif type(obj) == FunctionType or type(obj) == MethodType or type(obj) == BuiltinFunctionType or type(obj) == BuiltinMethodType:
		return f"{text.cyan}{obj.__name__}{text.r}()"
	else:
		return str(obj)


def testToString():
	print(f'''
{text.b}# Data Types :-{text.r}
NULL    = {toString(None)}
INT     = {toString(256)}
FLOAT   = {toString(pi)}
COMPLEX = {toString(3 + 4j)}
STR     = {toString("Hello, World!")}
CHAR    = {toString('a')}
LIST 1  = {toString([1, 2, [3, [6, 7, 8], 5], 3, 4])}
LIST 2  = {toString([1, 2])}
TUPLE 1 = {toString((1, (4, (7, 8, 9), 6), 3))}
TUPLE 2 = {toString((3, 4, 5))}
SET     = {toString({1, 2, 3, 5, 6, 7, 8})}
DICT 1  = {toString({"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "LIST": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]})}
DICT 2  = {toString({"one": 1, "two": 2})}
print() = {toString(print)}
'''[1:-1])


def ml_input(ps2='', nobreak=False):
	stdout = ''
	if nobreak:
	    line_no = 1
	else:
	    line_no = 2
	while True:
		try:
			line = input(f"{str(line_no).rjust(3)}{ps2}") + '\n'
			if line == '\n' and not nobreak:
			    break
			stdout += line
			line_no += 1
		except KeyboardInterrupt:
			print()
			break
		except EOFError:
			exit()
	print()
	return stdout


def shell(stdin):
	if   stdin == "clear":
		print(CLEAR_CODE, end='')
		return True
	elif stdin == "exit":
		exit()
		return True


def run(stdin):
	if stdin.strip('\t\n ') == '': return
	if shell(stdin): return
	if stdin == '```':
	    return run(ml_input(PS2, nobreak=True))
	stdout = None
	try:
		stdout = eval(stdin, globals())
	except Exception as e_eval:
		if "unexpected" in str(e_eval).lower():
			stdin += '\n' + ml_input(PS2)
			return run(stdin)
		else:
			try:
				exec(stdin, globals())
			except Exception as e:
				if "indented" in str(e).lower():
					stdin += '\n' + ml_input(PS2)
					return run(stdin)
				stdout = e
	if stdout != None:
		print(toString(stdout))


def main():
	print()
	while not False:
		try:
			stdin = input(PS1)
			run(stdin)
		except KeyboardInterrupt:
			print()
		except EOFError:
			break


main()

