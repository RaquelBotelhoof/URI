from time import sleep

print('Contagem regressiva para os fogos em...')
for c in range(10, -1, -1):
    print (c)
    sleep(1)
print('*****BUM*****')