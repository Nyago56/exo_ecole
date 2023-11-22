import time

i = 0
print("Début")


while True:
    try:
        i = i + 1
        for o in range(i):
            print("CIAO", end='', flush=True)
        time.sleep(1)
        print(" ")
    except KeyboardInterrupt as Exc:
        repr(Exc)
        break

    
    
print("Fin")

