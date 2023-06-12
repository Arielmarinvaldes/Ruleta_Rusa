import random


bala  = random.randint(1, 6)

for i in range(1, 7):
    input("Presione Enter para disparar")
    if i == bala:
        print("Estas muerto")
        break
    