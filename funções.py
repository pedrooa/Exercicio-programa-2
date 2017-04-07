
meus_ipmon = list()

def lista_meus_ipmons(Inspermons):
    for i in range(3):
        meus_ipmon.append(Inspermons[i])
    return meus_ipmon
def escrita_timer(estringue):
    for char in estringue:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.4)
