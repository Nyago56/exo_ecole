import time
i=0
print("début")
while True :
	i=i+1
	for o in range(i):
		print("CIAO", end='', flush=True)
	time.sleep(1)
	print(" ")
print("fin")
