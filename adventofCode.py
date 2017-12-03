#!/usr/bin/python3

import math
import collections

inputVal='237369991482346124663395286354672985457326865748533412179778188397835279584149971999798512279429268727171755461418974558538246429986747532417846157526523238931351898548279549456694488433438982744782258279173323381571985454236569393975735715331438256795579514159946537868358735936832487422938678194757687698143224139243151222475131337135843793611742383267186158665726927967655583875485515512626142935357421852953775733748941926983377725386196187486131337458574829848723711355929684625223564489485597564768317432893836629255273452776232319265422533449549956244791565573727762687439221862632722277129613329167189874939414298584616496839223239197277563641853746193232543222813298195169345186499866147586559781523834595683496151581546829112745533347796213673814995849156321674379644323159259131925444961296821167483628812395391533572555624159939279125341335147234653572977345582135728994395631685618135563662689854691976843435785879952751266627645653981281891643823717528757341136747881518611439246877373935758151119185587921332175189332436522732144278613486716525897262879287772969529445511736924962777262394961547579248731343245241963914775991292177151554446695134653596633433171866618541957233463548142173235821168156636824233487983766612338498874251672993917446366865832618475491341253973267556113323245113845148121546526396995991171739837147479978645166417988918289287844384513974369397974378819848552153961651881528134624869454563488858625261356763562723261767873542683796675797124322382732437235544965647934514871672522777378931524994784845817584793564974285139867972185887185987353468488155283698464226415951583138352839943621294117262483559867661596299753986347244786339543174594266422815794658477629829383461829261994591318851587963554829459353892825847978971823347219468516784857348649693185172199398234123745415271222891161175788713733444497592853221743138324235934216658323717267715318744537689459113188549896737581637879552568829548365738314593851221113932919767844137362623398623853789938824592'


print("Day 1")
print("Exercice 1")
previousVal=int(inputVal[:-1])
sumVal=0
for currentVal in inputVal:
    if (int(currentVal) == previousVal):
        sumVal += int(currentVal)
    previousVal= int(currentVal)


print("Solution: "+str(sumVal))

print("Exercice 2")

middle=int(len(inputVal)/2)
secondPart=inputVal[middle:]
sumVal=0
for i in range(0,middle):
    if ( int(inputVal[i]) == int(secondPart[i]) ):
        sumVal+= int(inputVal[i])


print("Solution: "+str(sumVal*2))
print("----")
print("Day 2")
print("Exercice 1")
inputVal2="""3458	3471	163	1299	170	4200	2425	167	3636	4001	4162	115	2859	130	4075	4269
2777	2712	120	2569	2530	3035	1818	32	491	872	113	92	2526	477	138	1360
2316	35	168	174	1404	1437	2631	1863	1127	640	1745	171	2391	2587	214	193
197	2013	551	1661	121	206	203	174	2289	843	732	2117	360	1193	999	2088
3925	3389	218	1134	220	171	1972	348	3919	3706	494	3577	3320	239	120	2508
239	947	1029	2024	733	242	217	1781	2904	2156	1500	3100	497	2498	3312	211
188	3806	3901	261	235	3733	3747	3721	267	3794	3814	3995	3004	915	4062	3400
918	63	2854	2799	178	176	1037	487	206	157	2212	2539	2816	2501	927	3147
186	194	307	672	208	351	243	180	619	749	590	745	671	707	334	224
1854	3180	1345	3421	478	214	198	194	4942	5564	2469	242	5248	5786	5260	4127
3780	2880	236	330	3227	1252	3540	218	213	458	201	408	3240	249	1968	2066
1188	696	241	57	151	609	199	765	1078	976	1194	177	238	658	860	1228
903	612	188	766	196	900	62	869	892	123	226	57	940	168	165	103
710	3784	83	2087	2582	3941	97	1412	2859	117	3880	411	102	3691	4366	4104
3178	219	253	1297	3661	1552	8248	678	245	7042	260	581	7350	431	8281	8117
837	80	95	281	652	822	1028	1295	101	1140	88	452	85	444	649	1247"""


linesTab=inputVal2.splitlines();

sumVal=0
for line in linesTab:
    number=list(map(int,line.split('\t')))
    sumVal+=(max(number)-min(number))


print("Solution: "+str(sumVal))
print("Exercice 2")
sumVal=0
for line in linesTab:
    number=list(map(int,line.split('\t')))
    sortedNumber = sorted(number)
    for i in range(0,len(sortedNumber)):
        first=sortedNumber[i]
        for j in range(len(sortedNumber)-1,i,-1):
            second=sortedNumber[j]
            if first != second and second%first==0 :
                sumVal+=int(second/first)

print("Solution: "+str(sumVal))
print("----")
print("Day 3")
print("Exercice 1")
index=312051
step=1
squareSize=1
lenght=0
while (squareSize<index):
    step+=2
    squareSize=step*step
    lenght+=1

distanceFromEndOfSquare=squareSize-index
Y=0
X=0
middleVal=squareSize-((step-1)/2)
if(distanceFromEndOfSquare<step-1):
    Y=lenght
    X=-(middleVal-index)
elif(distanceFromEndOfSquare<(step-1)*2):
    middleVal-=(step-1)
    X=-lenght
    Y=-(middleVal-index)
elif(distanceFromEndOfSquare<(step-1)*3):
    middleVal-=(step-1)*2
    Y=-lenght
    X=(middleVal-index)
elif(distanceFromEndOfSquare<(step-1)*4):
    middleVal-=(step-1)*3
    X=lenght
    Y=(middleVal-index)

Sum=int(abs(X)+abs(Y))
print("Solution:  "+str(Sum))

print("Exercice 2")

def computeCoord(index):
    step=1
    squareSize=1
    lenght=0
    while (squareSize<index):
        step+=2
        squareSize=step*step
        lenght+=1

    distanceFromEndOfSquare=squareSize-index
    Y=0
    X=0
    middleVal=squareSize-((step-1)/2)
    if(distanceFromEndOfSquare<step-1):
        X=lenght
        Y=-(middleVal-index)
    elif(distanceFromEndOfSquare<(step-1)*2):
        middleVal-=(step-1)
        Y=-lenght
        X=-(middleVal-index)
    elif(distanceFromEndOfSquare<(step-1)*3):
        middleVal-=(step-1)*2
        X=-lenght
        Y=(middleVal-index)
    elif(distanceFromEndOfSquare<(step-1)*4):
        middleVal-=(step-1)*3
        Y=lenght
        X=(middleVal-index)

    return [X,Y]



def sumAround(matrix,x,y):
    one=matrix[x-1][y-1] if x-1>=0 and y-1>0 else 0
    two=matrix[x][y-1] if  y-1>=0 else 0
    tree=matrix[x+1][y-1] if x+1<len(matrix)  and y-1>=0 else 0
    four=matrix[x-1][y] if x-1>=0 else 0
    five=matrix[x+1][y] if x+1<len(matrix) else 0
    six=matrix[x-1][y+1] if x-1>=0 and y+1<len(matrix[x-1]) else 0
    seven=matrix[x][y+1] if x>=0 and y+1<len(matrix[x-1]) else 0
    eight=matrix[x+1][y+1] if x+1<len(matrix) and y+1<len(matrix[x-1]) else 0
    #print(str(x)+" y:"+str(y)+" one: "+str(one)+" two:"+str(two)+" tree:"+str(tree)+" four: "+str(four)+" five:"+str(five)+" six:"+str(six)+" seven:"+str(seven)+" eight:"+str(eight))
    matrix[x][y] = one+two+tree+four+five+six+seven+eight
    

size=1
index = 312051
validMatrix=[]
lastValue=1
while lastValue<index:
    size+=2
    matrix = [[0 for i in range(0,size)] for i in range(0,size)]

    middle=int(size/2)
    matrix[middle][middle]=1

    for i in range(2,size*size+1):
        coord = computeCoord(i)
        #print(coord)
        sumAround(matrix,middle+int(coord[0]),middle+int(coord[1]))
        
    
    lastValue=matrix[size-1][size-1]
    validMatrix=matrix

dico = {}
for line in matrix:
    for value in line:
        if(value > index):
            dico[value-index]=value


a = sorted(dico.items())[0]
print("Solution: "+str(a[1]))



