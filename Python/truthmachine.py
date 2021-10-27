import time
a = input()
if a == '0':
    print('0')
    time.sleep(2)
elif a == '1':
    while True:
        print('1')
else:
    print('Invalid choice.')
    time.sleep(2)
