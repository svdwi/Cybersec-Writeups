import os 
import hashlib

file1 = open("/home/svdwi/Desktop/rockyou.txt","r")
lines = file1.readlines()
flag="7adebe1e15c37e23ab25c40a317b76547a75ad84bf57b378520fd59b66dd9e12"
n = 0 

for line in lines:
	line = line.rstrip("\n")
	line ="castorsCTF{"+line+"}"
	hash1 = hashlib.sha256(line).hexdigest()
	if flag == hash1:
		print( line + ":  "+ hash1 )
		break
