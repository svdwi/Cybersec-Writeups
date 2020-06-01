from pwn import *

help_dict = { 
    'one': '1', 
    'two': '2', 
    'three': '3', 
    'four': '4', 
    'five': '5', 
    'six': '6', 
    'seven': '7', 
    'eight': '8', 
    'nine': '9', 
    'zero' : '0',
    'minus':'-',
    'plus':'+',
    'divided-by':'//',
    'multiplied-by':' * '
}

r=remote('chals20.cybercastors.com',14429)
print(r.recv())
r.sendline("\n")
while(1<2):
	query=(r.recv())
	query=query.split()
	print(query)
	for j in range(len(query)):
		if(query[j] in help_dict):
			query[j]=help_dict[query[j]]

	query=''.join(query[-4:-1])

	ans=(eval(query))
	print(ans)
	r.sendline(str(ans))
	print(r.recv())
