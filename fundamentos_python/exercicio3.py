import time
import winsound
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)
winsound.Beep(2500, 500)
print("Foguete lançado!")
