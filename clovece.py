import random
def gensachovnicu(n):
    sachovnica = [[" " for i in range(n+1)] for i in range(n+1)]#vytvorime prazdnu sachovnicu(zoznam)
    for x in range(1,n+1):                                      #dva vnorene for cykly zarucia aby sme presli cez kazdu suradnicu sachovnice, okrem prveho riadka a stlpca, ktore budu vyplnene cislami(preto range(1,n+1))
        for y in range(1,n+1):                                 
            sachovnica[x][0]= (x-1)%10                          #nulty riadok a nulty stlpec budu len cisla, pre vacsie ako 10 piseme len druhu cislicu(napr 14 ako 4)
            sachovnica[0][y]= (y-1)%10                          
            if x == int(n/2) or x == int(n/2)+2:                #ak sme v prvom riadku pred stredom alebo v prvom riadku po strede, vyplnime cely riadok *
                sachovnica[x][y]="*"                            
            if y == int(n/2) or y == (int(n/2)+2):              #ak sme v prvom stlpci pred stredom alebo v prvom stlpci po strede, vyplnime cely stlpec *
                sachovnica[x][y]="*"                            
            if x == int(n/2)+1:                                 #ak sme v strednom riadku sachovnice, tak najprv vyplnime cely riadok Dckami (domov), a potom na zaciatok a koniec tohoto riadku dame *
                sachovnica[x][y] = "D"
                sachovnica[x][1] = "*"
                sachovnica[x][n] = "*"                          
            if y == int(n/2)+1:                                 #rovnako, ak sme v strednom stlpci, tak najprv vyplnime cely stlpec Dckami, a potom na zaciatok a koniec dame *
                sachovnica[x][y] = "D"
                sachovnica[1][y] = "*"
                sachovnica[n][y] = "*"                          
    sachovnica[int(n/2)+1][int(n/2)+1]="X"                      #na zaver do stredu sachovnice dame X a vratime hotovu sachovnicu pripravenu na hru
    return sachovnica

def tlacsachovnicu(sachovnica):                                 #funkcia na vytlacenie sachovnice ju tlaci riadok po riadku
    for i in range(len(sachovnica)):
        print(*sachovnica[i])
            
def moznosti(n):
    tahy = [[0,0] for i in range((n-1)*4)]                      #pocet policok po ktorych sa pohybuju hraci je (n-1)*4 kde n je velkost sachovnice, pricom kazda moznost ma dve suradnice
    i=0                                                         #i je pomocna premenna vdaka ktorej sa posuvame cez zoznam tahy
    for x in range(1,int(n/2)+1):                               #nasleduje par riadkov, kde sa nacitaju vsetky mozne suradnice pohybu panacika
        tahy[i] = [x,int(n/2)+2]                                #vyuzivam tu znalost toho, ze sa panacik raz pohybuje po vertikalnej strane "kriza" sachovnice a nasleduje horizontalna
        i+=1                                                    #preto sa raz strieda premenna x a raz y, aby bolo vidno kedy sa hybe po vyske a kedy po sirke
    for y in range(int(n/2)+3, n+1):                            #ohranicenia for cyklov vychadzaju z dolezitych bodov sachovnice, co su zaciatky a konce ramien "kriza", zaciatok a koniec sachovnice           
        tahy[i] = [int(n/2),y]                                  #vzdy, ked sa panacik hybe po nejakej strane kriza, tak jedna suradnica zostava stala a druha sa krok po kroku bud zmensuje alebo zvacsuje
        i+=1                                                    #kriz ma pre hocijaku velkost n vzdy 12 stran, z coho vyplyva ze budeme mat 11 for cyklov a posledna strana je pokryta uz 
    for x in range(int(n/2)+1,int(n/2)+3):                      #len jednoduchym priradenim, kedze nam zostava uz len jedna mozna pozicia panacika
        tahy[i] = [x,n]                                         #na zaver vratime zoznam moznych tahov pre hraca A, a ked tento zoznam pretocime o polovicu, tak aj pre hraca B      
        i+=1
    for y in range(n-1,int(n/2)+1,-1):
        tahy[i] = [int(n/2)+2,y]
        i+=1
    for x in range(int(n/2)+3, n+1):
        tahy[i] = [x,int(n/2)+2]
        i+=1
    for y in range(int(n/2)+1, int(n/2)-1,-1):
        tahy[i] = [n,y]
        i+=1
    for x in range(n-1, int(n/2)+1, -1):
        tahy[i] = [x,int(n/2)]
        i+=1
    for y in range(int(n/2)-1, 0, -1):
        tahy[i] = [int(n/2)+2,y]
        i+=1
    for x in range(int(n/2)+1, int(n/2)-1, -1):
        tahy[i]= [x,1]
        i+=1
    for y in range(2, int(n/2)+1):
        tahy[i] = [int(n/2),y]
        i+=1
    for x in range(int(n/2)-1, 0, -1):
        tahy[i] = [x, int(n/2)]
        i+=1
    tahy[i] = [1,int(n/2)+1]
    return tahy                                                 

def gendomcekyA(n):                                             #funkcia na generovanie suradnic domcekov hraca A 
    domceky = [[0,0] for i in range(int((n-3)/2))]              #je ich (n-3)/2, kde n je velkost sachovnice
    for x in range(int((n-3)/2)):                               #vo for cykle na kazdu poziciu [x][1] dame konstantnu hodnotu stredu sachovnice, lebo vsetky domceky su v jednom stlpci
        domceky[x][1] = int((n/2)+1)
        domceky[x][0] = x + 2                                   #na poziciu [x][0] davame hodnoty od 2 az po pocet domcekov na sachovnici
    return domceky                                              #vratime zoznam pozicii domcekov, podobne ako pri vsetkych moznych tahoch hraca

def gendomcekyB(n):                                             #funkcia na generovanie suradnic domcekov hraca B funguje podobne ako pre hraca A, len ideme od spodu
    domceky = [[0,0] for i in range(int((n-3)/2))]
    for x in range(int((n-3)/2)):
        domceky[x][1] = int((n/2)+1)
        domceky[x][0] = n - x - 1
    return domceky

def pohyb(sachovnica, kocka, i, q, tahy, tahyB, h1,h2,doma,domceky):
        kocka = random.randint(1,6)                                             #vo funkcii pohyb najprv vygenerujeme pre hraca X cislo kocky      
        i = i + kocka                                                           #nasledne toto cislo priratame k pozicii panacika vzhladom na zoznam tahy
        print("\n",h1," hodil:",kocka,"\n")                                           
        if(i>=len(tahy)):                                                       #ak je pozicia panacika vacsia nez dlzka zoznamu tahy, panacik sa uz moze dostat do domceky
            cislodomu = i - (len(tahy))                                         #zistime cislo domceka
            i = i - kocka                                                       #odratame hodnotu kocky od pozicie panacika, aby sme sa pripravili na pripad, ze panacik bude hadzat znova
            kocka = 0
            if(cislodomu >= (n-3)/2):                                           #ak je cislodomu vacsie nez (n-3)/2, hrac domcek prestrelil a nejde nikam
               print("Hrac ",h1," prestrelil domcek\n")
            elif(sachovnica[domceky[cislodomu][0]][domceky[cislodomu][1]] == h1):   #podobne, ak uz je obsadeny domcek, hrac nikam nejde
                print("Tento domcek hraca ",h1," uz je obsadeny\n")
            else:
                sachovnica[tahy[i][0]][tahy[i][1]] = "*"                        #ak ale neplati ani jedna z predloslych podmienok, panacik moze ist do domceka
                sachovnica[domceky[cislodomu][0]][domceky[cislodomu][1]] = h1      
                tlacsachovnicu(sachovnica)
                print("\nHrac ",h1," sa dostal do domceka\n")
                i = 0
                doma+=1                                                         #ak sa pocitadlo panacikov dostane na pozadovanu hodnotu, vyhlasime ze hrac vyhral
                if(doma==(n-3)/2):
                    print("Hrac ",h1," vyhral")
                    return i,q,sachovnica,doma,True
        sachovnica[tahy[i-kocka][0]][tahy[i-kocka][1]] = "*"                    #na predoslu poziciu hraca dame *
        if(sachovnica[tahy[i][0]][tahy[i][1]] == h2):                           #este skontrolujeme, ci nahodou hrac nevyhadzuje hraca2, ak ano, tak vynulujeme poziciu hraca2
            print("Hrac ",h1," vyhodil hraca ",h2,"\n")
            q = 0
            sachovnica[tahyB[q][0]][tahyB[q][1]] = h2 
        sachovnica[tahy[i][0]][tahy[i][1]] = h1                                 #posunieme panacika na pozadovanu poziciu
        tlacsachovnicu(sachovnica)
        return i,q,sachovnica,doma,False

def hra(n):                                                     #vo funkcii hra nacitame do premennych tahy a tahyB vsetky moznosti pohybov panacikov 
    tahy = moznosti(n)                                          #do premennej tahyB ulozime rovnako zoznam tahy, len zaciname od stredu tohoto zoznamu, aby bol panacik a v pociatocnej pozicii oproti A                
    tahyB = [[0,0] for i in range((n-1)*4)]                     #to zaistime tak, ze priratame polovicu dlzky zoznamu tahy k pomocnej premennej i a zaroven berieme do uvahy zvysok po deleni dlzkou
    for i in range(len(tahy)):                                  #tohoto zoznamu, aby nam tato hodnota nepretiekla cez velkost zoznamu tahy a zapisali sa nam do tahyB vsetky moznosti
        tahyB[i][0] = tahy[(i+int(len(tahy)/2))%len(tahy)][0]   
        tahyB[i][1] = tahy[(i+int(len(tahy)/2))%len(tahy)][1]   
    i = 0                                                       #premenna i predstavuje aktualnu pozicia panacika hraca A vzhladom na zoznam tahy, to iste q pre hraca B
    q = 0
    kocka = 0                                                   #kocka predstavuje aktualne hodene cislo pre hraca A, kockaB pre hraca B
    kockaB = 0
    domceky = gendomcekyA(n)
    domcekyB = gendomcekyB(n)
    doma = 0
    domaB = 0
    sachovnica = gensachovnicu(n)    
    sachovnica[tahy[i][0]][tahy[i][1]] = "A"                    #nastavime obom hracom figurky na ich start a vykreslime sachovnicu                                       
    sachovnica[tahyB[q][0]][tahyB[q][1]] = "B"
    w = False
    tlacsachovnicu(sachovnica)    
    while w == False:                                                #ideme do while cyklu, ktory skonci, az ked jeden hrac vyhra                                                      
        i,q,sachovnica,doma,w = pohyb(sachovnica,kocka, i, q, tahy, tahyB, "A", "B",doma,domceky)
        if w == True:
            break
        q,i,sachovnica,domaB,w = pohyb(sachovnica,kockaB, q, i, tahyB, tahy, "B", "A",domaB,domcekyB)
n = int(input("Zadaj neparne cislo o velkosti aspon 5 a najviac 15"))   #od uzivatela vyziadame velkost sachovnice a zistime, ci splna podmienky, (cislo neparne a o velkosti aspon 5)
while(n%2 == 0 or n < 5 or n > 15):                                     #cisla su obmedzene na neparne z dovodu zadania, a velkost cisla je odmedzena na interval <5,15> z toho dovodu
    n = int(input("Zadaj ine cislo"))                                   #ze ak by bolo cislo mensie ako 5 a neparne(napr.3) uz by panacik nemal domcek a nemal by sa kam dostat
hra(n)                                                                  #podobne, velkost sachovnice je najviac 15, a to preto, ze kocka ma cisla od 1 po 6 a pri velkosti napr 17
                                                                        #mame uz 7 domcekov, cize panacik by sa nikdy nevedel dostat do domceka, lebo v pravidlach je, ze panacikovia sa 
                                                                        #vnutri domcekov uz hybat nemozu (dva riadky while cyklu pred zavolanim hra(n) sa daju ale zakomentovat a vtedy pri zadani nevhodneho
                                                                        #cisla bude hra bezat do nekonecna)
