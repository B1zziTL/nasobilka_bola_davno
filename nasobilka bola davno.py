#vlozenie modulu
import random

#otvorenie suboru
subor = open("nasobilka_vystup.txt","w")

#zadeklarovanie premennych, zoznamu a slovnika
body = 0
nespravne = 0
opravene = []
nespravne_priklady = {}

for i in range(10): #vygenerovanie 10 prikladov
    prve_cislo = random.randint(1,10)
    druhe_cislo = random.randint(1,10)
    vysledok = prve_cislo * druhe_cislo

    priklad = str(prve_cislo)+"*"+str(druhe_cislo)+"="

    #vypytanie odpovede cez input
    odpoved = int(input(priklad))
    
    if odpoved == vysledok: #podmienka na zapocitanie bodov podla vysledku
        body += 1
    else:
        nespravne += 1
        nespravne_priklady[priklad] = vysledok

    #zapisanie prikladu do suboru
    subor.write(str(prve_cislo)+"*"+str(druhe_cislo)+"="+str(vysledok)+"\n")


def rewind_time(): #funkcia na opakovanie nespravnych prikladov
    #zadeklarovanie globalnej premennej
    global nespravne
    
    for i in range(nespravne): #opakovanie nespravnych prikladov
        #zadefinovanie key a value zo zoznamu
        key = list(nespravne_priklady.keys())[i]
        value = list(nespravne_priklady.values())[i]

        #vypytanie odpovede cez input
        opakovanie = int(input(key))

        if opakovanie == int(value): #podmienka na dalsie ne/opakovanie
            opravene.append(key)
            nespravne -= 1

    if nespravne > 0: #podmienka na pokracovanie
        for i in range(len(opravene)): #vymazanie opravenych prikladov
            del nespravne_priklady[opravene[i]]
        opravene.clear()
        rewind_time()

if nespravne > 0: #podmienka na opakovanie
    rewind_time()

#vypisanie bodov
print("Získal si:",body,"bodov")

#zatvorenie suboru     
subor.close()
