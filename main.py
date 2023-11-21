import time

i = 0
print("Début")

try:
    while True:
        i = i + 1
        for o in range(i):
            print("CIAO", end='', flush=True)
        time.sleep(1)
        print(" ")
except KeyboardInterrupt:
    print("\nInterruption du programme par l'utilisateur.")
    
print("Fin")

