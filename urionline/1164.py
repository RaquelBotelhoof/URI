n = int(input())
letra = 'A'

for linha in range(1, n + 1):
    print(letra * linha)
    letra = chr(ord(letra) + 1)
