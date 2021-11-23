def coleta_tempos():
    tempos = []
    tempo = int(input())
    while tempo >= 0:
        tempos.append(tempo)
        tempo = int(input())
    return tempos


def exibe_tempos(tempos):
    for tempo in tempos:
        if tempo < media:
            print(tempo)


tempos = coleta_tempos()
media = sum(tempos) / len(tempos)
print(f'MEDIA: {media:.2f}')
exibe_tempos(tempos)
