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
# Use sqrt()+1 better result
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

print("---")
print("Day 4")

inputVal="""oaoe rxeq vssdqtu xrk cjv yaoqp loo
mveua dogbam szydvri hyzk lbega abzqw xwjn wniug kwbre
npaoy uivpxwd oynpa rcdk uixpvdw
yserir iikzcm ieuroca iuwcfov rvb giti crdpdcv mxpps
spyuhgo lucasl ucllsa bymnjig yflbv nxitmlf
xlxyhwz xla mpye fvjegwg fezlfrt inetrh vhg xpvstx ydhvq
xgue cvtmh myg ontvvyw ygm oqzrdrw
srdfsjf dli kccb kauk kauk apa doefc cdffkhh cdffkhh
msizb elqiov lqn epamk onmnlst baawab ncafwaf jrataml iyzhy svycuec
wdzqpcn dkgdumv wdzqpcn qxdmwib cjsigi bgcihgh fmua
kpvbzf kpvbzf svyq flg shwtgp
ywrynt cesjtgk hsvitr brpiul lxgvvrl cesjtgk cesjtgk xuflpfn
tik mrpht gkv unqp wypscc vmwiu ldrigk okbc wztc
zpy kyzvijv bilpf etbrgk edza vuz jzgn
yoa rgppd kzpopd cffjk murcb jmt raace iwt
aobgkja drc ztkd qskxxbv lve lev rhhoqex bmd eolf ybxjr yiiut
zhjcfms fpabnu aozp delsc mge yqi eovg pwefafe
gukf iys qztqxz xhsssz pfqq slg jdbp pfqq yabztc asow ygh
fmr ijgmjrc zbhwsmx ylgccz ycydcyx hjjset
zybsr iqisbs hffmij ikby lwufzvg gwd
ruk rku kur ydurp upmebe
baqide zdijcf ezqfe ovrldez delzrov szimd irmk busim ppv zepqk mlwpl
bxlvp dxumme byaada cgyn diz
xlxr jhili bmcke nkl vuhqsn lxzb zmyuxgk qcqr tyxe
wvth gyerrd yewrta kgri yewrta
fall jpyuusu lffybb ivmtmzx alfl yjupusu
lzvcg xwnt mjyiklh vwlz qejj mjyiklh dmcwq qejj
vgutb smc yvnsbgd bxmjd qmhia krxz luhgg emnrp
uuvhtia aiuutvh brstbr tsrbrb
howd japlq lhk qtsfdq htfufj qkyywy anxxxqw jtmryw cdtajh
pksswl jprpccl wpklss yyrbo
furp pfru bftha iekamfc bixwmr sslovex
nrqobo hyb byh hby
mugix kzlbtuq hmju ysstccs hmju btsuh
hsrlhw zilj jtvto zilj fjq
lvol xic hqqdeo gmsug yqe wue vhmrq buj juv wxexdot
lqeybb odpv mttm bxqy vqbqr ylbei wyjcxco urufsuz kyq
youbiz kvrea xsfcp zaz zybiou earvk qpf
bowsref ooobtic apiushu kplpyza
hxfhoyy ybbe ceebt recegzz ftnlv ukaf gpvx opvd lqnvk ybbe ygnwa
jpbgc aahm aahm aahm
qyvheb xyb elt oaksuj dvgpmel poiowc ykgbgpz dxpit ytg
vgsv yrjo vjss kyfvim izwo yrjo vgsv
hkk xmqx crlki dtp nuh okef okef xomktit viia nuh tplhrx
bmkjclx sbwe bwes bsbnqd nqbsbd
gfwrl vocwln hsuxkz zpclb qprrvlt bkcluvs pqy sxucrla npb fensz
adjklj nyr btmav roxv jrri vqfnis gzsab ogskmaj
bvjm fer ztgfx mtp vvhps hptzrar wpy yhvmh qklfwpf edgrdts vmhhy
lngra nrlga xokqu mgq
mksdk bkkbfsq hazlai nixee vyxh hpvebeg jujoqe wkw mzpxixm
kxrkkx qivtt xsm xsm rqvgdjl jilosjs rji
xiqga rez igqxa odiilj izoiwf xgqia
aepioo krcr aepioo jhigtx krcr qubkv jgo zybyvy wbsguz
ntyscmf duwvvb kga xvaypk sfjlg daguzm kqat otj zmnki
ggxaery jazo ggxaery zevobo zux wfnd wbyd hmhmo oaakvab jsimsw
vqdnvgy qiex yqeweds yqvdvgn iqcukgc bvrc osi
esjzak krwe ivbri hnbah iuvb begybsk ctxmlym gjqi lcscum
hyxdilx tsv evckza bdbscwj jlihiqk dciuj hamd dqsm ydihxxl
lurtwhx ygwf pwhj whxtrlu zfvywxr gcrl zvl wienpqb woto
mfaektr ocvho ukfx ukfx old daqwotk pybjtiz kumkiq tmql lqou tmql
guwy ceqsyvs svteymr nrovwz tesymrv rmsveyt
pigilsu zpyiohn zpyiohn xzl pryi zpyiohn ohdz
pziqfg hhrzdr wxl zpqigf
psnmnxz oed edo deo
tkdp tkdp auozn tfyo wmp jtp wjyskeh dag ojdvw gbptp deiqi
xkr nmsbk mreiv occcvva eca bupc gvaoopu jdhr flh ptgdumz mks
dlevn vmwzws dlevn dlevn
qwx qnuqgc rtzc yvym sft wxq fhv fts nyvrfxz ydjvcq tnwz
debkk pullndo ezaibw ldnloup nllupdo wiiw nij
hng rpd aud epq opzjh jnzge
rmtauf nwinyl nwnliy pjzahm lywnin
cgiv omva fos irse uytiqu iqjo riplx capa dhdl echbyjw cutfam
fqrqmi jfrj zllh gfhhq fqrqmi mmyqv
yoepae uabuxlz jzqy yoepae sxena jzqy
bfr jlrycal ndg xejwjdp khwg wckevqb tud xljzem ntfbazf lkr
aomdwt sji sij jsi wlsvvva kgjzqj whhf
ogorbil orlgiob iorlbog xapwiqs jxb
tnn sxgdikv ynick ynick aumwthl rwhx eqxd jdbzyk kbil pmnifp dpeips
vzeoilq son olqvh jawmny
vsifce kcighpn mubl zkgwm
ncagxs ilohd lyq oqhjf nfeij qmtvf qpru tfmtaj
pfjkcpr dqrfde efqddr edqdrf
wdyygax hscx ptmro wqko ecnfkhj ywui
gdv nrnrzdc vyq vyq vesrj vyq jwxg
oqhrr daoew zpoduh zwmoss nfkh vubf xza kju rhrpt fvsc
oqp ppyq swvin mut uacwd swivn ucdaw icfj ldcujh cejl
dar bqp ajdhuej sxwt bqp tppexrh tppexrh
sitplaj xnb ldopp mqd gwtk uhnvozu ljz dqm ylzy qltf gwtjksx
eqkvncb jdp pahwje avhrer awb zqnwfhx zohmcz fitbyab
xlnel gjzviy cndpuoj jvwxs qsd kwli quisju kyoix imzg
czqjkk evyima ixpelbv eobpd wwuxxof pbxc dgj
czsigs lbdaynp amsexn aemsxn easnmx rsitdzf
xdpc xfbp lrjwlo ntnnob sbe bse
suud fws zgn kvfimsi
wnexa diexvky oemdq uasxzhq qxa kevyixd lpw unluohs
ylruxt beqvn vbenq ogsov mvftu sovog gshtb qriaxko vthgfr jwj
gmz wcjb cqjlb hijz qwuluuf xdpu jybdf ajiv xizwb
fcxos spz idg rjb uhr ert bxia urh xfxp ixba bnvxy
uxiie eixiu wgmwbj euiix qknyd wtaojk naeqfz qmhnulk uscgwxa
qwyxd jno xelqd isdjht qxz dbwnr bfzhewu opxmkgj igfiuck
ljpphwc ijzic pfsemsc mfedoxy pad wsk beqjpbj gbjr imce xumhr
causc ogypj csacu pdokc itpgjl xfx nyt yytg srhrup bontz xbalwnj
asohjj qer pfgwo qgdw wgdq
gpzvyhh tsnx tyu kswlgb whju zkkpdm bmh hdov
unux lhrn unux lhrn rxr
epq ksew pqct jib pqebafk jib pyfjy gnu pqct
anzbbs oyhm moyh mhyo
dpk zael zael mxots zfcum
aehljyc wrj lfhife xbss ztszba vlg eljycah ihffle coypll
aoqedco bogk bogk aoqedco sanwwo
udmbz yxe dft rzolgtp nwwjpti
efu qcls rtx mestnqt pkh ciekj scrv uswd oroowx lcztvt
urnwt uapni ood lzce
zjiqxt jzqxti infgde xbmi kawilp kaipwl
lsfn kxfw zgzdfq meqwql zpqqu otert
taajsho gbeoguv bpi nxeuy
dpoyzi rqlzx rqlzx udhuwjm qnu bnuma udhuwjm gfezx cbjpfp woir
mjbv isni ixjtjue fwsk ncgwpn vqnmq pivz jbmv qoakqou argval dacvksc
xxjcn amdgdhh iup hlk xxjcn elx
gyhocay ofqosv nldfqay aqu dsrz lmekze bus lmekze gfoq lmekze vkor
xidyqq bimvxu zrkg rpcdca ymg nmxkkqu gygcmp euemr
gvd ywog ywog gvd hwjzzq
byu ggpwrl lpexjcf hgy jee febgcae valcgc tcfwicu texqi lxfjepc qeraxcs
lkjejsb eonp jtsbps pfvlos neop ikwnb avzxnk
big pjgttfb eetr jobjfae odvl jheh tuz ystrh tuz tuz ige
czubaxq czubaxq pbxgs jhuopn snmhhc qwmcka xdhxfuz jhuopn eummw
xdwduc sqcano zopaco ozbbc bczob eas cbbzo
oanpgo tiav bbssup ttzchih tpb xmfnqwa ghdx uepmz fzqbx
ahha zsbdq jggv zfcjdp dzcfpj dkew jxmelbf jgsohj oghsjj
awdy plulzw gdi jiiq lod rog mrf uihaz sebk guvb
tlhwro sapaws ovlbbfh xctruk spzpzm latyy
ligaot xfhacs jvk xbnpu yuanx yvvi gjek
nfwuug nxccj dxpfvfq pvxcvy ayss lfwz wwole ewowl xceybeb efs zfwl
lzowlql armo yrlgfg kbl vudahci yav evdi ofak ysmfjk upe
qtmmqrl gxi rrhbi pydbopp yvevlq ovwwdrt mrppov lzzs yjyrxh srzo
hytkyas wpuqvf fftiso fftiso
yutais qjdbzo kewsi opy ysl zyvyoty wkp
qtbad bxfjkwa stcdk lyre tabdq yler
friyh ivp hshy ksmanzq mzdbbub ncbx mhzki friyh vyjk hshy
ijeysr aww evn ttqvshg xkd zjy honvuqy zyj quvyohn gphcir
okft smja fkto etb
pbi zhyy kyjdho mqsuyic vegocmw gdkskg kgavjag dbqh wamfijz ktihnrg
csqix soz ingra gvslgk
ugxgzqt pdn hiynufo lpfabmi rmwj uhsqoo pmlzad ferdup guzqtxg voxd
wkixiq vck vck sylv ttqcbwv ywqta vblz mhohx frv
phns ozeghgm dfodkyv iyc psnh tedotyz xqz gqbyj ydttezo kxgju mvip
chc jdjo pyq usyn vtrbnq ohnx dsxpdzn mgbc ysun mlalmu mqemyuw
qrkosx wcwcv brvbwo nvxwg bvrwob
bovt gpb rwm gpb pitttl rwm rvfzn tbo
zczkb tmpwtj kackkx yzqkzso rsg ema ereo jptvfd jptvfd flbjfii
fcdyetv jqelvx jlevqx cfvetyd
dtyp wfh rxtpwr nolbro iozrs mnshu tkesvyk pkmkf
lvecoh ohpb brlqwx immgqe dzfac bwlrxq hng clxmpd qodfyv
sjbc dsoqk dqosk iyla lqzrsgi tjgt mfxshtd ztmc
nxveg vmxf jwnub kujji aqkonjl xtit xitt
jsft pmojruo vtvjox wimrlhj rezqi rnv hjnvdka
vnl vzgltnl mry kkqf fekwjw knsrvt nct kqy infvys
jbvm igq gvcl crry ylia nbqcq ouduen jklepay
ermsf emrsf uksuvz zrnlun
ecksf dkydasw wddasky pmfhi yltmedt bdovedg vfnyoze ufcki civrjs ohozga
hvf gfqgc adbeykt jdz zmgonhi yua kifxyoy umsza ivnbvoc whnpi gtbinze
nmy fsdu myn iiw
yrkwca jkxc yrkwca yrkwca kxqtvqh
ildxc taopx spykdz dzbpcxp wzgka cbyr xpvrzbk
qqp axdmvo cmppp shx
uldyu luyud uduly rgcmugh
woc vjdpyq cwshqq tlh fzyuz cbwgp egpy sfw
adyv cnrn bhaxvx ofdbkn yxrtir cnrn
ycz ednsydc bqsdcpx adnq bydb tqy tqy vqzpy erdcnv
mouv ouiy gld stdv gwr lxlfq gdl ldg
gtx bbvr fxytm veofwp bvbr opefvw
pcf scu ovso rawtjxs kzxgnuy ifcn tvibap
ugcbob xkjgtx ugcbob ilkkx dikca wpxyq retqhlu ugcbob ylmt tigcmmm
gmnde ool qeuwc ctux
wpajwn gooy fedmjur pxiq xkyniyp xtgi eyfpc gjx
uaivt kvfyn mpsya qxu kvnyf wvoeaz mbt fkyvn
jth awxbprn kpcodj qxegybo
sfvitld mdzczg pdptzm fmz himb eutpyi mgrde gubsta tfsldvi dfistvl
piabmr fckmhrv twnlnka jyb selqflm iwcutk pvvann
uxjfm rmleg ochuj ruiq aobxbb tpuusot uhwjojw tutopus
dzj qdyxzk oan rtpz ona qkdzyx nkunr
urjydh dfreifg tmbetd aakc vdr dkdkldw xgvtfsa ivv doadb axgvstf
fdjhr ujgbj ulkm dfzh tmhx zfdh ckt ortg
obe ywwge rgqmt cfcnyt atn fdkdrwz lmb zwpe sqfoc yllxs akdlsso
ckhbu jfqhkml abenw ckp xvjy wsyhxox jzsz hqksq
tjx zlh zgyrjpe bdorry uofh hgkzl ezixges kaxlkjw ztijupu hlgkz
belj ipbygk dxe cqoyukw jnncelh ihvom qstbowu rocqsz ifiztlf fjrf nsit
vyswalv reaqae hzoqyun lbci ibqfljz cgjflqf kos
njrzfvu nxw nxw bdsgnxp
gxlgn qrx nspbvl pzuob nggxl ipak wjr lggxn zas
xkd sooef fsayaob tfsiyl
ecldvh jugto ghfpbev xzlc
rpyattn spb ajdplq eaorgi ackirxg knrap cobdeu qca pkp zkc
bhh tczwffg bhh bhh hrjx jwyu gry kkgghnx
zsav frsakbr bvzd gafr homzjw frsakbr yasgz homzjw kqa
nbd mekhfif mekhfif keuoag nbd
mzv vzm utuxhuf uufuhtx
siy tdbii qtu yrxar ruubale yrxar lsvnr yqxq ruubale
wstykuz fxnuszr tgmkw eovvrd ohheh raf degh hzoeun tiou wpt cqnw
dzbyhrv vzlbvn ncoa xfglcye ncoa sykfps ghi
lvi ilv xalhd ztejzb
zaeu diz zaeu gtdjsz fmoxgju diz uvh
zef lmkqlcs jnhgqww qsm fuatcq ixfa
wgp gvu rpmxrjh yokepvc yokepvc lywdl bbvvbf yokepvc
etjfs gjh tvmxb agovg yihn rmmh nue jfil
zgcco slios jbfodb wpthe ydvit regizw regizw qosou slios cto jfz
kmmq lnafaha ddos hrsjtxk zjch rfynx eovks
ezeuzu jfpv oinrstv vsw naoz enrcy svw jfvp kgmfwf cfisxzo
ljtv watps equf ljtv equf
axijki zotolsi ryqujrm xmhug fhz lkgaw umzokxh ktr jsdsfat trk iosoztl
vpqvvvn ydjz tcqc asffcxr rxb fyt vyham fys
agxrcxl obcncq htod ved ozesk obcncq iwqmksk fsijtg iidyy lxu ozesk
orsyqt otqrys pnaax qtrsoy
oyisc chu ahdp abhbtry kjsqve tkpux tkpux sxzu sxzu
wquw umlbwf mxzdbvb upp fopxe aub bau eritni punrpfc esnkyg
jjlzy hozskgo jjlzy aiq jjlzy sgfyhsd
ejghc ejghc ejghc igacslu
unzmg fugzotb nxkdlds ewn hydj fbr iuly oiwwkbg scnozau sfi dsishk
xuhjduu hfloaga xhuuduj mbavfkd nrnl ral erc mntev elpoqgq
seydro onpi qjey skgkiox fbdgyt xhr rhvz dpsjcj tfzd spjdcj btqn
difyxz cdm jlzsz oycm txyssd wckqshu ihya yjyb
nmrhlif wcreso chtqfov qcftvoh lqp egd erc myep plq cjdh
hcnwgkq kkrpxxj gwe xqgea kkrpxxj nxz mumqbw kwxhlz kkrpxxj otqy
rxbioyf cszah mhu mhu mhu
qpbrf jzink ojy idt nrjykzu
omnrq kkol dex eaqdmej dnpaum ynnntw ddwewsh ztcenhc zqdrq hmi
ngmqpu owmcuz gop gdbsfc nyott cdsflq ngmqpu
srus lrexy aqgkqvm tiyjm
wxa qopky glaaekv ykopq lna gyxvpx xwa hly dbvo
vqf sqrqw phxn xiw gejyzip ugg gghhugl zyqae
ylj cyolrx giim yrchuu yrchuu ylj
rixa yfusuqn yfusuqn yfusuqn
lpm gboakz ylyv gje yxu ahokxb ixwnpu hlcka cndhbbm nkmvts xdtqbc
veul zjvz regtyp njwfpm
pdlyjbn edawa xbcmyew gme yuk yek nfknzgn ehjz
rcgun ulv ntbwnvg ptf givapv bych gmxxxf iajqpb gwh ipavvg
qvpwk grbb gptdgrh sij vunv hsb uegsmt uos vkxdd
iun aagzlj elqcq vkrk awl yyt dxfhkwq hbkeht
cgf omofuz zddgwef iyosk hmou
mvjorn zseyo wpfjlac kpxb dlh ggo zgxoso txzuy jfbmv lacjpwf vha
twrsrw pxv iklzg rtfcl kfbcjix uyvowpa kfbcjix ofnsf adqm
qvi ivr plxfrg awugjh fxbv ztlljk qvi jdkfts xyq jdkfts uqwgdr
phs eimuuf lmxq wmp
laf gmuowr rplgkh orentm whor lkrhgp mjwr zapz mdqtqyq ttkfkf
fxk wdbl fjh ojqxp yvs fkx ysv ngksb
oclyxqu tpajqun vvmj twin zclk
srcwxs xiduxd tqpfc sbqybp sdtzw gizfn bpji kaolpuy
pfkmk olmsaz uffy uyff
crpazh pcrzha lew lkhcjij stfxq
nkbb rnlo icnzg rnlo ejanu mofx ujblud
abte xnjfo boz fnxzid nqfhifm jmnmsgh
lvck nfll szdgrxc nghig szdgrxc oytahh cibk szdgrxc
sduf jgv rrt spxw fdus
gplutjv ufep fuzrnj tmko zzpj cpd mvtrzq
ycdiav qvr ycdiav tjngezs mphk oykgcei ycdiav
egbkscg ksgcbeg qmw jdbj
kbgx otnfyc agouh iai lyhqd yzihyq ouagh snzhxa xyxrgz
kdpqljx rin dlxms ukdzedc duezdkc ikgplm ffk vdmie qziajdf ftfwl
prrzhj okffaot tlrxpjd aquc dbonaef enfdoab nwbtuh
vyzf ijo cdhek bvlgxt kvldmp kvldmp vfvg
zhijgyb yfkkal utb brew vfj ztiftq
kodsuol ubnbdv iozwfum ayqxgnj qkp yiiv wbkgi psi wnfa epw
iok mecjsp lccn nrb kobca wkznctc afjjlrt
yrw yhsva hgx nxjfbb
dbdj vef xjssylt hjlld bqbmx ihfmz uhij zoh opzrmy mfq
wqhcq usyfuc wqhcq pmf aryq nhvtkh
nkviwge snpfdza nadzfsp evvdnrl qled ekqs qumle myhky
rgljws kjuk txgeein ajmph pjhdy pmvr upae yfh
vmepn wekgc qfwybl midbac vmepn ddqmbu vmepn uhfccp yuh zzz gnx
hyqv fud xdc bssziiv mwo xfrsn xqehs mwo
djhr qxhfy vdjs ueoi mbmwa lkeumzd hyxfq krbyy ywvcstf wdkum xfqyh
heprtex wgxpign lvm vlm ypswfxr ggxipwn hdszz blrv ppy
fwalim sbqj zewxcaf qjsb cjgujwr uclxro wceu wmaifl rnd
gmivd spncot jxeycn notspc nzb wie ceyjxn xlam
cfujai hfvux hhtwe hfvux oputz oam
gmwu xwthnkp xwthnkp mdxa xwthnkp
shfqzi hdq uyyqjrd wczfvy wciko hdq nuywebl
dtkq qnb uzmo ypxfja cekqe cekqe tnaibc uzmo pmtnb
apdz exdze pop pvm pce hywvftx jrjezgd jkajq jcdjli
satq czv cfhyca cshnyh cshnyh rcu cshnyh
mxp ujq fmrnzxx xqv mxp
nel whnnxak lwzlre mrxq kpo pko bsa gimtzwb
okssco iuke vcnv okssco liawwc vcnv aztl
kjvq rye eawplkw qzxt jkqv bxbfyv
bphssax ylemih wsm jnpxce jgh repsyj ieypbz asx
dwivit ptcwt qwectqk ttwcp bklpa ivditw
ies knj zemmcto mczotme yanr kjdrwr mcry ndols
dqzdpg adb ulsv ulsv qux ppmoru sjcn dpihqz
akazkk kssdguo cgigktm indfh wwh kevuhv dclpjv kgtd ehjxous
spogxy jyzhag qumd brk cbu akbpjxb spie
jgyn cxbar axtkwh hktgcm cfsla xll rpauwl cgpziuh dyc brcxa
dodey dysnjxe kzmyytw tzddd cnupwmv
nqab whxkb kvc kvc jcjhywy mbbpfwj fxozlt whxkb qwz
ihmif xhjc lmfk yjrsioo uvtd qvtqsgt dqd
uvzedxd afli hkrigd lkzkzu ncki toam hoaefui
zmvywjv jsjf nrbrgt mbs yog eexuo
ukzab euwb qnkanyt lgeqf qefgl ewub
zbol bolz ilncu ciunl
hjryu qyl ajwju rplplr skbdsl xvto
ojfotbx zvta jofxtbo ejjnhi jyeiz yzeij
ivr pvrwef ivr zgnm jscgaoq hfjuzju cea hfjuzju ehszaz
yikp gul ugbniac jehm fwqxb hqbhi hlfr iyuuf vacrao fwqxb
plsjh efu napxwe jfxfjz efacqcp sythfxc sythfxc napxwe qncqc
meuf rcjzf mhluz kbrk tzjrcn omoiprl khs oyzad yuzbz
exvzzuc ckqfivf uoyidkg mwztyf wxtg uzrls gudioyk wfihpzn tdmwhf
qoovwqm bldswvy xkb yqrcluk qyrclku cluqyrk qgakbv urclhse
rmmymgg ytpqtuq ibt tmedibz tmbsdg ytpqtuq cxbnng
qkyeo frjjht vkpt ikztq avzqon diw noqzva dvkhwdt
opz usos kdqseyb cdxvve nahjc hbr rhsfm hcjna wnczls kky
sgeml uyaoe ked utxab hxqa glems wbdo kzrjsq
isp bmebt becira ixoz yeakj fmueu
jrd qyys cik bmaief zxllza rsu swvodiv ivvdsow ikpvwaj jdr qte
gzjjre tkjhdn lrqmvw gues ositymc xhfiutm
kcnble oxoh zggvo zjz auub kunoj snil zggvo lgql
yyfmd wbwmizs vmb clba bpzzjz nlt wgukoe hedlp osxz
skic mgcr chkj eiiy kdhch gcanziz dpecug fccp
jhnejy akpwbj mhrunvm wjzwyhe lwxostl gfe niuhj iuf bewur
nuursk gehzvck szm fllr bfaq ijpjp gehzvck bfaq
ecx etrsadp lyekp lxf flx tadreps
gbo wzkner hky ggoqu
yiitvf tyvifi xpnbk iiytfv
okpjxyq mmxcha pujgv ltgfdk wpporh bfle tuupth ukyyjgv vlnwhz
phbs qtpolnh udito ukx kjqsi jbwf sgkkwgm udito mwwb wihg
mces dhc qccy sxyilmb qmki dyqnr qsh aigaemz oofdw hbifiz
yyben jjklnz whwswg tox vgytp noijcv jjsa ybney eyrvg htjl vxli
detb tus rloz zymvmg zpe
usvkehi kxgvo rna scnaljd jmowud ipfkkf rxvpie nxysvj pvquagf fjhsvef
ytosun puwdoix oyc qdufuw ysunot
htw biy htw oxot oxot
xgzi nbq lxxtmt nbq lxxtmt fnzmmno
lko bdbj kcqvc torg enbfbj sbooco afjbclm dendwq
cgih ikmfn lyhzhxd ubq ixrori tofbo
glfhfzs gihsccj yic mlci slne
wdiu lhl hdlhzo voo yhqckcy axnz yqyi fyss qhvtsbc
aotbk zfokegh uax myhehay terwus hmzic fdwojh wjuwlp
ucbiex eigq qqe ifqw sxakwl xkwsal qeq
pknvybh qkrwi povvd phairw qst inklob yrryv bcuv dolvr okwe iexrpbw
kkah qrt dihygsm nly rblqvrm sxguxj yspmre
gzhhkjt uimif bssle vdiaa wkohq nrgboi htkojiw
aeb xihgva vwcjbjh lri nlwbxun sargiey uyekrc
fnnwfbj yyccaxu fhqb nlmwhc ymbqky ooljix mfijg ryykirn womn rygezi qsdwgpw
itfs udfr sitf gml
gknztly vay ypy jpid pyy mbpfmwz pfmzbwm qqec
bbhmw uus xffgd xcjzrlk kyecv zcerxe
ncpc otqzotf godtu yhcpsyw ncpc fbs
ggoiqm ofk pryqt kqdbo ktek kklhlju iqgmgo gqoimg flscx
gsgmvy tktzj kgi ikyz pthtk hxt gik
bunvugy fefqpkk juwk aent
atm tma dzyret jmuqke xbayiit jumqke
dilfw qws ldwfi lnujld ywrogk kjh adaj khmlb hkbml
veaemc xugf udpphf mydi jbvebgp ngyhly pufdph vbgepbj
vyd tisntn qmc yzal
uxdlc piw mwjnk qiar xwpspf sxktemh jmw
qhhvar pox aed bgwq doe uyktv pox vriy ndel pzx aed
tswei dtfb yhj krxu yqio wtzpm wtzpm yqio
bjzp zzp qdzdfv tzkbl nggbfqs vquqds xiud xgrkb
ffvjfwp jbzslqo ffvjfwp pchzrqv ffvjfwp pkd nlav
czepixn yurmsw ucckih qqlnxjj exipznc
xeu llc jnmp dmz pnmj stqzao
fzvu uscqp xerkzkg roivhri fzvu yiwae xguz ajpg
qdzk uyyoi cspmnc qdzk nwknfx fnngvla cbl
acg utwrv cahupdm xgat elb aemkf wmkdzj kfmae ahlrwu yxfcj
vdumh rcd rgc hpqk qeum fpgva qkhmuji rjxpuzk ommk
ztvm ntxkav ajv avj ippodg sukg bivcslu tes gdlrbnt bdlkaye xpgslef
aygsym pwq owxmx xjw
dkhykf pfqeyo lfq saoewy qldrky sdgrrcr frdqn tkfezop doo saoewy
cwof mqlscm iqxhb nnkex nxx glgpbn
noq zikmeyx yodahj ssu qqmifa plcbv rsahsd
nvc fuwiyq myv hjn rtuoq zoyp rqnt xchlrg
dziscfa nbzsuvp rbnrban cjdprp dkj zcry ckxtm
stpm ifcbmmw dpkpzo sot ydpeydw nusp nkciqa psnr
udikjfr foqnxl whq ojuspzz ddyz emdktzb gfio mnd hyb
vchdphx zkrtky ucyifqx ryzl txdixd cip aid cip
wcz ywzwpp viswpsm qfus uzopaq mhps sidjky kipvjg
wehhc rzujn urprwzw gkwzhk rhrpph xkzzl rzujn yddlb
wlhif foh rpvylg gruiqdv daih yflhbr coe yflhbr hvluddj
hfzi ffjntj fdth crkrzdr nyel nlxm cawze bfjz neixnw uygqvmw zayf
guthfwn kcinec glhaiqv rfgbi cbrm
mvqv lszqu eyjn suq lavyjbh ujivbza aianl wik noy zth
zkn ren ncoyj fppsy dwgtgqz til
ybxepr hrzcrxs zhrscxr uvpxxl eprxby vzgg
xhi zess zet mtpcu ibz nkwq cbzb etz kjjcns
kvmu rxgw xboplw enlqcxi uxysl xboplw kvmu oqxislh xeg qwhdc spsddge
dxaao ltjjn cpsvnxe core aojgu pbss nudwi
llro yoy tixzyc beim qirnb lffcr gzm
quxetbf gfpll gqyav dckhp xbfetqu xaebz xuqfteb
fblkc hsydxqt bvmwujr rak
epeohq olrwyft cmrvov fbdyxbg
uzqk pkhizw jbrnlvx aqkq mtmjmy gpcln gaqt rinrz gwis gpcln
ttkcu ttkcu mcq xao lhnxdph djj ylet atdln xao
pmwn svqktkm isopar krrfbna knrw kbm zsohxrk xlsmm knrw cmoikq etqeggc
undrw issrttk mcoe pvufl bwjwqkx jdz undrw vje
kfzqbb djpcjv ixctsvb rqsntv fcqz
agezraf ezrfaga pftdwrk slsxu axw
ezvkn smwko utdlu nizby
ygl dwtrpsh qzz cuntrr hdrn lujcx iwc bll qvjhg
jrdrvj ledrjp noqx igodve odgiev
zonvzgy ujnzj ujnzj zonvzgy ckzd
rmg lmib fdn nfd gfobw wrc iro nsz
acgxvh sdn zcef sdn jvgnmhi xitkqgy tbascbh
ykuzk ovp mikolx xxgpylt secuf yrtilra wnoypy mty lmnagx
wwmlins mxwye kjntv sadc wnvyoov rzdawl
ali ncsrq tcbjzpu oiw iimxlbp mwi hdvdl dqnicf lxit
sql vywv vycj nprzb tdqe qwvljm myhpvxy hdixbk ywqpn xvue vrno
etncz etncz czqw moz uaxbtm axlslow fhephy moz
wsriuaj umjkx mhxau luzf wmo kyx jidl ufuoz cbk
msfrvbt bxnd msfrvbt yut qwbx
rhag vfkqf rekoz buw qffvk wxs ghra
meignx dhdu xacg hmiqkd nrijc gcxa gwap lov ybtyr vol
qoqns swib mlegyjn ojdtt tvdrrhg oetg xdret nzpq
ntc zowllt dwiyht ztdeifx velaumx jfxxsqt uefmb gwn
bgykxl bykan tvvgcpa wdcsj coonage hpocfz sqmihw pnagv uozsh
wass vve ngyd yyvxmsq rsaypsa newxyc adqmbm xqsvymy ygdn idysq
ybo vpjcf tsbpc hcdszr qrxwjqr bzz tgjhkpu hgtxkt stpbc woro
ogszrg rszt owufa cohmv msygfw fud fzi lhts sfiy dfu gxsuj
fclumcq ejuj jkbu hbsv ythmpoo xdzg dkvrdue
rbf sunzzl sokgih rngqli xndnuj rbf smiea mqzpzb fwpcx smiea
uuuxchs uuuxchs fzna qlj tcjnv oghk fzna
zuiyk tbn nqma wptoecs xndgbqm mqan wmcahvm qpir
ztexf pqsc icxqsuf tkgr itnn yorg oyvqaj yoxggqk lep
ehm hysd jfv iugyt jyvh
fenjp zjtvvhb xfe dgxoah ljn ixvdyi fenjp odnlr
uosxyy euicgp lrsc euicgp mcszotm kvxrpk jfo oxu xyeiv fhdwl wbw
tsmdp gshgm kpb tlx kfznsu gglefv pkb gcnydo eavgrc rgd lgefvg
xuq svh cmzt bxxlvfm rtblxpu imuexhl lbre hqyedxa hwkgaak
hhlfj mlrdv dlsn zgcy hciiuzw uwciihz iizhcwu gwx
ukqoj kjqou hlk nfyz lusf kebvmrw ccaj ewmicq useba
jlnnl jsmox vnw ucr ggithr usqe allzc pfumkkm jlnnl
mswpbk lffjwq icc kef zlba uolrrl fqlfwj tbc
bfmra hdgczrw dgmnod afbmr fnczx
dcqrso cgbymsg jbx ofpbp rmtygip syly
yrmn wzkt lqys tzkw sqyl fxoc
wal zgjy cwnqyaf bhz dbpft owx
xnrautk dlsyot nzbohog xmzsbh soec wyy
kde jpkvbs eyzw ukgiv ggrtzcd vikgu mxqy jyh crdtgzg ebzet
psg jsykdw drpqzl qzqbge ldqpzr wsdykj lmhbldv hbognjp nqej fmxoq guuf
ueo ncedaju ijasprn rvxb mxkddl qvgdlbx bpj bpf pxewuf chvo lvrq
zlmg eciyqi xfbeoq pupyrc bfqexo ituqab pycrpu
jsk clo vqxzl aja jfbce ldov
muss tzg iksvdej zpw fxwhrv eeye fxwhrv
kjjd dzf zkppx qdwlx irudds kjgd pdrz rgogy qdwlx egx rjxldp
szjpf aouvl ehxq exqh
nzweop qlkje welkfs jqmvqi coc
ivmjzk usk auvmc vvcnwn qubihx vkms fbt udn uyto jjt kxqy
rayw ijaklcr ywra qkj qytxeh pmnfh qffvsft tyxheq
pea cqy tkg qidvx qidvx pea skgrndq
iijm xgwq zzpskl qtjezqt yqjwy dhbq
dfuv iqw iejb bjei iwq
ogrmldp xdc dcx cqhbwlp
wzwb xrjl keciql ckky litdr bmurdk anjs nyggesn ygwt svmee
bvkkzj rcr lozrw mgpwkm lwm yecsr ykl tzny aeus jmq mchopp
rsnvaa oikce angqn rnvsaa mhc
hsiov kxqpxtc rzh vjrqlx xxtkpqc wiunol qckxtpx
aosek lhi ruqgd rmr
agqvlao pvhcgz esw kwnpefs qsrvxz hgkgrs mpx odaiqi
dvqkrzf dawioo jtaco oeutol ravp apvr frjunad
wss nahhsh pfwgcfr rvvvq uqxxmhq qax vtrkfou medfj
imdyfc sez gve kgtryl kmqklg
crmg yhkpa bsfouax kyttpa who mcrbzaj kcsktxe yfv
zpw zlab pzw pwz okb
fgqlb byhkhfn qglfb ladle ifa
skr zwwjnr iub wekt biu jnrwwz
mpvt mpvt havn ztf
odqhd uxrswp ppj eztyj nxzwm fvxyadn tostwy odo abyp meqdm ktqkvh
fgufup uabd vhxem imto imto vhxem
vrpxxhi kii zwatqg nokg wesxju xplc sumte muwjj
nsse iquhoc giuv pxaa qpqn zrfk kywjr spz kgzc lfa
cjjgarr psvwoap ivijyt nfbxu ktiuy jajrgrc goyc
yrfzf wyxda gsslsy oeyve jczghf cbuwf iwnu izyrtho dyoup toizyhr vzzrr
bwqgxsr ufy cnouypd qwxbgsr efdkfe rwsblis bhvyws oodh
piqpez yhqahjp oxu qtomld
vjvpnwy kajjaim lcxmbyd fkdy ywvvnjp xcn nbwlklo
qghq mihdp vuv ocrzsw mlmkn rgnbfcm qgufcks btlulb effsrih
psazbfo vbpr efcspj yrjl pqjrfe relxjc nzzvb yviuhc
tbbhdbm uxhawtk bmdhtbb rqxrr pspjzx krtmf pnaz srcej rsjec
owikzec glvbqy jhknyuz jkaxu ldhnlpx wdp
qvuv wteohr daynue nehs gzqu porzrsk cqokye zzsbqox rqh ogxtn pskorrz
gnm grlfoon lxid isxa
jes iixswl umgbg qfixa xnecpns asm nopsmo axaopsm qahwpqd
orr auvlruu mqq uurlvua urauuvl fjrcuo mqht tkdgps tdvnhvq iezdv
txwyzy zzwk bzi etfg gtef
qyydr lllgosq qyydr lllgosq
xqm uyl ldpowm pxhi ievvvez hmhzwmr ldpowm jaw
qlvfq efgivhr rfhhu gvw bxgsrp sgbnjh ekgbp cyof rvghph nxfekia xym
lgladv ogj cir jxx msz fshf ayheu wpmke zckng vgrlv lxgmge
fcmp aabxdp hpxbb bblpy mpcf eju pnkv jxwoy hmv fgynps pbdxaa
jcrh dgg lzyiv ojop vhk vdb uinoetv
utlzcf ziizdo njffmxe uhyjxdb cztluf yjdhbxu
ubl cgz tyg nljl
slwe qaos ybcwdoh ogazkj tqh opggnzt ffrscl opggnzt izeh
evitfwb jpivmn dpnxzuf gdkx zprogl xehb
dktt kpnkizb rreq gjmosa iekdtpj rcxk eweawk qrre olv
cmcw vmw mujx mujx ypqfz
nzxcl fzwa ftcrc immendi tmxzzi hslye eibc tmxzzi
abfc jdqvk lichxx uiomtz tlq
mnkthoj nohjktm eued izmcjj
ullh wju bxfsif icnrmmj qnufw zubcnmo yewz phovhv
ndfvd gcyt wnm badaww twm jahlat ndfdv mtw xrq bechxx dnp
ceg gcxgu gnudeib utsynwx dpg wpsnp ahbbvkt wpsnp iou
wutcg congyz erkj ibtcics
xsbq lyycse qbsx ppgutls lroo tyor
hfiwoy hclhl gcwgqox ogo hlqr ultkaz yke iwohyf oog
bcl nemims udwkmlm nokck tkwny ulkihcu knwty pngamqg yxtphkn kuihlcu
nwsr enrutc eqcfb uxmdgju rfnzhsn tzk vysc
wbtki vjmkk kvjkm ibwkt sckvbv
xjxnow tli woxldj rotrtz nfkhcz ibh mla ybxldg
cwtpkhr oxywg qpwrgfm dfjpfuc kpcopa
byczby tbfkonk ytlczzf bbyczy
khuvrne rnamlgt akjtu qlx odr git xmiazr icwsxsq
jfm bneh tkdzuad bsr oruvmqq uauw zjlp gwov hot jkjbex
jjo uvk vlpy lpxd irntb uvk ehhsqv fxhvt jjo fpa
qrwu mgnw hvflf ytspp mco ikvbqg fflvh wts cbbf"""
print("Exercice 1")
result=0
for line in inputVal.splitlines():
    tabline=line.split(" ")
    if len(tabline) == len(set(tabline)) :
        result+=1       
print("Solution: "+str(result))	

print("Exercice 2")
result=0
for line in inputVal.splitlines():
    tabline=line.split(" ")
    if len(tabline) == len(set(tabline)) :
        expose=[]
        for exposed in tabline:
            expose.append(''.join(sorted(exposed)))
        if len(expose) == len(set(expose)) :
            result+=1
print("Solution: "+str(result))

print("---")
print("Day 5")


instruction =[1,0,2,-1,1,-4,-4,-5,-2,-1,-4,-8,-8,-1,-6,-9,-3,-14,-6,2,-15,-9,-5,-9,-14,-4,-3,-23,-24,2,-24,-22,-31,-23,-5,1,-35,-11,0,-30,-18,-25,-24,2,-35,-33,-29,-2,-27,-44,-19,-19,-40,-52,-26,-20,-37,1,-40,-36,-29,-37,-56,-59,-34,-31,-17,-24,-14,-57,-16,-68,-27,-60,-73,-16,-60,-6,-45,-38,-48,-33,-68,-12,-51,-49,-10,-28,-66,-88,-8,-83,-5,-2,-39,-39,-12,-87,-63,-55,-55,-26,-5,1,-68,-100,-98,-71,-15,-96,-100,-107,-45,-46,-3,-13,-25,-110,-63,-84,2,-107,-11,-50,-8,-55,-96,-76,-26,-103,-42,-43,-94,-31,-112,-64,-72,-95,-20,-51,-27,-129,-108,-75,-92,-18,-18,-68,-43,-71,-59,-70,-122,-64,-39,-146,-134,-120,-3,-137,-88,-93,-155,-66,-34,-85,-142,-55,-141,-5,-74,-110,-32,-148,-90,-108,-9,-75,-55,-64,-14,-5,-131,-31,-119,-115,-170,-110,-52,-187,-44,-169,-53,-154,-79,-48,-26,-175,-153,-198,-139,-119,-119,-93,-80,-101,-65,-112,-186,-1,-171,-71,-209,-76,-121,-104,-159,-91,-54,-6,-18,-196,-40,-155,-103,-98,-191,-66,-83,-206,-142,-118,-211,-216,-141,-197,-131,-77,-46,-110,-124,-56,-165,-183,-94,-87,-55,-110,-208,-37,-99,-63,-86,-197,-176,-235,-202,-131,-49,-22,-247,-253,-256,-114,-49,-126,-104,-105,-87,-230,-61,-83,-24,-196,-31,-267,-118,-139,-83,-45,-251,-84,-187,-104,-192,-224,-145,-219,-266,-62,-27,-255,-2,-117,-240,-199,-295,-177,-185,-245,-29,-47,-55,-64,-147,-154,-217,-211,-291,-254,-44,-103,-271,-37,-244,-313,-200,-34,-197,-72,-309,-124,-134,-9,-244,-254,-160,-5,-84,-28,-26,-162,-261,-102,-85,-305,-38,-54,-57,-320,-94,-13,-92,-34,-114,-194,-128,-220,-259,-298,-76,-31,-185,-212,-10,-7,-329,-80,-135,-278,-264,-322,-82,-3,-9,-334,-89,-217,-56,-99,-16,-103,-167,-148,-41,-311,-125,0,-135,-252,-288,-293,-18,-19,-358,-186,-117,-65,-170,-34,-256,-376,-81,-106,-92,-389,-147,-203,-335,-320,-240,-373,-337,-239,-7,-214,-292,-55,-388,-143,-251,-111,-240,-259,-187,-278,-9,-312,-336,-382,-226,-203,-318,-277,-142,-65,-80,-237,-347,-92,-166,-322,-306,-289,-64,-53,-162,-16,-357,-395,-57,-409,-225,-10,-169,-232,-326,-219,-59,-173,-315,-420,-432,-100,-434,-426,-160,-450,-394,-145,-146,-42,-320,-296,-150,-159,-129,-62,-345,-99,-378,-234,-144,-323,-378,-202,-181,-334,-135,-446,-295,-290,-202,-366,-333,-322,-311,-439,-180,-319,-264,-467,-397,-411,-177,-235,-280,-220,-371,-379,-270,-157,-75,-5,-82,-137,-161,-17,-423,-216,-10,-189,-278,-467,-506,-118,-435,-468,-357,-169,-333,-32,-266,-85,-515,-76,-80,-442,-190,-199,-173,-264,-314,-46,-360,-384,-140,-213,-32,-345,-367,-179,-295,-1,-8,-520,-300,-229,-538,-488,-291,-234,-159,-384,-318,-257,-379,-263,-495,-77,-227,-108,-20,-515,-293,-475,-127,-247,-467,-10,-29,-539,-233,-461,-347,-512,-339,-298,-419,-252,-333,-515,-203,-104,-56,-456,-101,-101,-68,-235,-188,-522,-558,-151,-337,-572,-47,-411,-177,-172,-178,-527,-357,-192,-342,-516,-215,-453,-183,-144,-13,-417,1,-537,-588,-512,-450,-343,-383,-167,-342,-235,-394,-227,-580,-226,-437,-314,-460,-279,-7,-157,-125,-520,-208,-69,-308,-9,-554,-628,-556,-329,-60,-3,-378,-188,-498,-600,-639,-52,-577,-332,-600,-119,-572,-261,-58,-542,-115,-328,-15,-411,-19,-56,-417,-332,-449,-629,-440,-523,-284,-304,-302,-71,-87,-197,-160,-461,-348,-339,-367,-87,-352,-232,-598,-441,-660,-332,-228,-676,-387,-240,-222,-62,-581,-102,-63,-589,-37,-427,-238,-687,-67,-315,-408,-685,-6,-664,-64,-515,0,-606,-494,-465,-73,-79,-553,-86,-513,-699,-8,-485,-376,-659,-214,-632,-694,-370,-35,-639,-373,0,-584,-538,-69,-293,-500,-537,-476,-578,-566,-123,-464,-321,-434,-238,-651,-61,-69,-207,-297,-537,-456,-122,-80,-517,-581,-411,-418,-734,-536,-278,-92,-416,-573,-308,-302,-645,-555,-314,-33,-715,-484,-89,-746,-254,-334,-509,-651,-556,-615,-447,-239,-545,-173,-4,-390,-526,-252,-654,-747,-313,-430,-625,-625,-578,-407,-28,-113,-54,-404,-671,-483,-801,-530,-191,-41,-694,-209,-158,-49,-608,-43,-34,-710,-96,-417,-297,-553,-310,-206,-634,-419,-795,-104,-91,-687,-105,-248,-693,-286,-63,-33,-199,-68,-248,-297,-281,-692,-654,-521,-240,-432,-515,-58,-711,-671,-433,-357,-228,-531,-457,-269,-76,-428,-590,-533,-787,-833,-453,-199,-113,-274,-144,-495,-481,-727,-356,-164,-711,-143,-503,-702,-783,-858,-494,-114,-18,-615,-243,-306,-312,-378,-823,-689,-119,-228,-769,-508,-298,-77,-465,-447,-348,-392,-751,-642,-841,-654,-617,-119,-490,-139,-359,-58,-34,-554,-168,-675,-104,-772,-232,-124,-460,-815,-856,-260,-3,-303,-771,-398,-282,-353,-192,-227,-645,-598,-345,-197,-881,-242,-159,-693,-537,-887,-44,-302,-252,-496,-590,-126,-883,-301,-697,-439,-928,-69,-192,-30,-273,-944,-606,-319,-638,-319,-391,-573,-268,-231,-649,-781,-936,-434,-435,-287,-282,-778,-608,-844,-708,-26,-162,-697,-168,-280,-472,-96,-470,-334,-38,-739,-936,-655,-946,-599,-562,-12,-912,-406,-532,-458,-828,-764,-314,-880,-897,-499,-412,-774,-249,-579,-294,-883,-558,-963,-228,-775,-205,-515,-662,-335,-926,-2,-865,-763,-23,-543,-715,-243,-343,-176,-68,-326,-926,-481,-517,-517,-885,-238,-400,-560,-390,-96,-285,-213,-680,-221,-856,-451,-33,-391,-589,-443,-695,-276,-415,-362,-789,-909,-905,-71,-919,-644,-237,-239,-458,-705]


instruction2=list(instruction)
print("Exercice 1")
pos = 0
size=len(instruction)
count=0
while (pos<size):
    old=pos
    pos+=instruction[pos]
    instruction[old]+=1
    count+=1
    

print("Solution: "+str(count))
print("Exercice 2")

#pos = 0
#size=len(instruction2)
#count=0
#while (pos<size):
#    old=pos
#    pos+=instruction2[pos]
#    instruction2[old]+=1 if instruction2[old]<3 else -1
#    count+=1

print("Solution: "+str(count))





print("---")
print("Day 6")


print("Exercice 1")
currentInput = [5,	1,	10,	0,	1,	7,	13,	14,	3,	12,	8,	10,	7,	12,	0,	6]

def contains(list1,matrix):
    for list in matrix:
        if( list1 == list):
            return True
    return False

previousStep = []
count =0
while (not contains(currentInput,previousStep)):
    count+=1
    previousStep.append(list(currentInput))
    maxVal = max(currentInput)
    index = currentInput.index(maxVal)
    currentInput[index]=0
    index+=1
    while (maxVal > 0):
        if(index>=len(currentInput)):
            index=0
        currentInput[index]+=1
        maxVal-=1
        index+=1

print("Solution: "+str(count))





print("Exercice 2")
currentInput = [5,	1,	10,	0,	1,	7,	13,	14,	3,	12,	8,	10,	7,	12,	0,	6]

def contains(list1,matrix):
    for list in matrix:
        if( list1 == list):
            return True
    return False

previousStep = []
count =0
while (not contains(currentInput,previousStep)):
    count+=1
    previousStep.append(list(currentInput))

    maxVal = max(currentInput)
    index = currentInput.index(maxVal)
    currentInput[index]=0
    index+=1

    while (maxVal > 0):
        if(index>=len(currentInput)):
            index=0
        currentInput[index]+=1
        maxVal-=1
        index+=1


bigIndex= previousStep.index(currentInput)
size = len(previousStep)
count = size-bigIndex

print("Solution: "+str(count))

print("---")
print("Day 7")

inputVal = """wdysq (135) -> sxldvex, wiasj
vjwuuft (33) -> inuci, neddz, rwamq
oislgqy (77)
lphki (233)
wgbviwb (417)
vikip (136) -> eofyk, dkexo, xzsxx
elmieqh (19) -> dbziu, spefs, krtxpw
tmzef (79)
ectlgy (232) -> zmstcy, ncobxr
sdatyo (91)
uisri (11)
smqimxg (132) -> husor, olzys
pltzthr (82)
szaqj (188) -> ptnndxj, fljpye
jqdngi (58)
uazwsu (15)
xrrhso (79)
gxeehd (68) -> iweii, rnqlzmv, hpmtom, vfzwqfr, xfzxrd, sgqhelx, hibjkps
evkoenr (43) -> oecxbyt, qbthgst
qivuzn (52)
udeev (389) -> lphki, qthzk, hpgsb
izgqzs (96) -> vbxzk, ubrrdtd
naxtp (65)
mvtkwn (42)
sxldvex (34)
tnlpmw (49)
rzbrbmy (31) -> dvnqv, helyy
esavxwq (81)
yqgru (465) -> gfuyuz, elmieqh, xckzut, tmbhjxf
ygypj (1303) -> ohcuki, ejdjxu, ytabct
yggqq (855) -> gowlaq, ebtoxi, xpljwl
ubaxya (92)
pjkzokv (23)
lvarp (76)
yrysmsi (14)
nofepy (23)
apjeywv (132) -> kclmmu, exsugls
licrtwb (56)
gspffet (84) -> wqzxa, lptaikg
gkrqba (82)
mqreb (126) -> jvdoo, paykww
xtidu (12)
kjauagn (88)
vvafqjs (56) -> qbvhefh, vfhgfb, iqtyv, ebdva, uxqkau, tydtcxc
snuewn (118024) -> vvafqjs, mhaucon, kikva, mqnbmre
gtkii (163) -> txcon, vuvwa
oaoisa (61)
ssqrs (24)
ybditq (21)
xgqxofa (119) -> bedzc, hdbkw, zwgsh
wxfir (71)
pxvse (19)
xemcuk (23)
paunv (28) -> zzvhmse, mubkcmk, vksephm, cbsdget, mellhhn
couhjsv (11)
tuzpls (58)
puomwl (90) -> wtxjnc, jdjbnc
wudlze (78)
ibslyw (153) -> ksncpee, npvuz
zzmczwl (54)
kidvt (3136) -> tuzzzct, qtqhwon
patlvg (20)
yvvxtg (90)
epxwjhy (22)
epvyxld (17)
xhecnbf (85) -> yituewe, wwhyd
mqsrwsz (26)
bhyzi (73)
batky (18815) -> woctu, iykjtnw, tpiwftj
sdponx (44)
qhotyqx (95) -> vdwfz, agthd, tuwedv, ixkkdyc, lnlkwq, bvmhqar, rlwmfp
nubqteb (89)
zygfdu (70)
tkerz (18)
solqvvf (10)
akiaxs (86)
jsfqyd (70)
aialff (68)
uiilkiq (73)
adlyhbs (46)
tnljdhr (20)
frctm (471) -> isqnx, euhgw, nrfqc, cmmnjch, zevrg
jjklma (105) -> xrrhso, uyjor
lpmnwh (56) -> orrfh, bqfzqra
owxski (23)
gqxyh (18)
lpyntz (91)
ivvyjos (81)
qssjswr (268)
jkbks (225)
jwbdb (83)
axqrke (119) -> mgoic, yivgs, bxggi, xamfjfv
uwizlce (24)
wuwhup (50)
suawycj (60)
wazvn (99)
wtxjnc (53)
ebtoxi (64) -> ttbns, voxychz, umsdpa, ajjmsnw
uuhoydu (82) -> gvucdh, hesyq, glwsf
tshyvej (1373) -> ebiovn, uvzpp, pblqb
bhakbq (991) -> izqxal, nhhytw, flmma, isgky, coqek
hcsjun (60) -> inelfwo, qcnstq, eymmhh, lpyntz
otjbn (67) -> szaqj, kkhlzm, jtzdqn
vtwud (10735) -> jldhlug, ikfzj, tsevkec
heztht (86)
rqonynk (65) -> olzqxap, oyhqsok
esbdjah (61)
hdinwud (1515) -> bdiftdg, ydtuje, aambg
rbbjcq (71)
kimffjc (155)
wifrwut (91)
hrlgs (9)
ieowdj (76)
vpqsjbj (147) -> eziosif, rptcpf
rlurjca (51) -> gtbjtpi, ohpkkhx, zkwnhn, cagvlf, zvlobk, ahsqaob, iactix
yzykfd (43) -> atqfhm, kazwz
kikva (6131) -> gkpalaj, jafrv, uekzf
lsoen (51)
uexqjw (10923) -> dxczurt, omqhf, ylfxp, qofsaux
nlnphv (117) -> vzlzrt, ypiwnt
bemxocu (78)
etcsuuv (312)
ihwbmt (27)
oorvvpt (63)
dvnqv (88)
ntlawn (60)
jhaow (45)
kccpv (17)
kbybvzk (89)
ctcmfv (49)
ujqjrz (89)
xekft (62)
wihtv (1278) -> qgbbhdv, adlyhbs
agthd (158) -> ucnehpw, hnutx
vuytzn (21)
svcqds (7)
emqqf (5)
uqddsal (17) -> trait, sdatyo
uhwlk (252) -> sxtto, qyvsaxn
ttbgzv (46) -> rokri, pygoqsv
oecxbyt (71)
xunvu (33)
mvbtomp (35)
uxqkau (693) -> qubhi, gneut, htmcpcy, qmncyu, wdysq
ycrnaf (177) -> ssqrs, twimkx
nlalji (28)
dgvvo (37)
niydqsy (33)
pprvv (89)
tmbhjxf (135) -> jutep, vkhiz
iaftm (63)
zjnrzph (81) -> gsxmqnw, gnxfwv
ggzqccl (5)
wwtiby (121) -> kytha, dgzywn
zismp (58)
hjbrfba (28)
xnlkkx (79) -> puomwl, xnbvupf, hgksz
bptaz (38)
ozaogat (15)
hxxml (27) -> emazu, kproiw
xpptslq (76)
ilohfvn (10)
hadddf (128) -> geapi, ocltuv
gtprqg (17)
qofsaux (209) -> bbnjml, fwskxq
xpljwl (128) -> ufust, aialff
thhbhrm (41) -> smqkli, ovtfd
xamfjfv (36)
jdjbnc (53)
kecpcmj (72)
ixkkdyc (80) -> wutzrk, antev
ysnbr (35)
cyvwwa (190) -> jtqxxa, pgmtcg, btvsj
uyjor (79)
oztxmy (76)
cancxr (213) -> ivdvlvq, ykxalh
zlads (14)
peokkb (167) -> mqkqtjo, qpchzkg, epssvr, yzose
iauxpc (81)
qbodszw (945) -> rgdvqu, oktgjb, abstvp
dmwutl (73) -> desuqj, etjwno
fcaht (134) -> ajidd, kigxtt
fkgkcwd (51) -> mqwagy, gvtve, djvbdm, ckapp, ldiqm, ezspaq, pyrvg
dqzkic (1032) -> inglhm, dgxdydd, hxhhhu
ydtykm (75)
zatfy (35)
rmenjck (89)
nrfqc (238) -> zgxjjm, fwide
schexn (97)
lrplxk (22)
nroecsv (44)
kiawm (64)
zpfuxux (73)
mvdkbch (28)
sufdte (71) -> gfjeud, rbbjcq
xmjunhp (45)
wsnsqx (7)
etyaxa (13)
cfrqn (57)
tslujme (60)
bebuqpx (33)
wwyuud (11)
gtotarq (95)
vtopekt (65)
hxhhhu (230)
aubvpzf (73)
kllsasv (73) -> enuvuv, jlhipos, hittl, smyzyqg
mgiuz (94)
dsytvn (296) -> mxfonyo, yihru
icsxziz (256)
agflbq (73)
amtrbok (12)
qcebc (20)
eymmhh (91)
pbpva (95)
rodxm (199) -> rzvlc, vnmml, rrmlgct
ekblpi (97) -> flwbwcq, ecwpa, usgpgi, pknsw, gkjwl, zzfom
ltpmtif (86)
bkfnip (4873) -> murnoa, qhzem, udeev
yhiab (249) -> sdponx, yvattv
hbaai (70) -> rmnkup, dgtsic
anazjn (225)
zjjyjj (101) -> viwez, ihwbmt, qnwwjwt
husly (98)
jlhipos (20)
xflsc (2516) -> qodow, vdkhvyp, masvpfj
cenqs (156) -> jhaow, mivmhi
rgrcla (84) -> nroecsv, pexfst
pdddwgk (30)
upefkx (75)
abstvp (46) -> wqgoxl, gbwaobo
glzmsn (93)
bgtzw (37)
flvrfdl (146) -> ybditq, vuytzn, yqdaz
jmzpxql (47)
wulvcf (89)
mxfonyo (20)
aambg (69)
jfjvw (32)
uslhk (8)
wwzjdv (45)
zwtsg (248) -> bjjtifj, ogbov
mbxyf (56)
xckzut (157) -> gaalz, upefkx
trseebo (18)
hbcpm (32)
ggoaczz (88)
zangrh (66)
ktbto (55) -> pdqzfg, mfoismz, mkirruz
rhpcgg (197) -> evkoenr, klpzhup, cigew
kbbcau (25)
porttu (92) -> haaqbj, lttlp
gfsgzni (73)
pyaqqhu (134) -> kdkobz, szvocp
eiyiuq (54)
fjgjfpc (17)
lvvkjx (56)
kinah (22)
ivdvlvq (31)
njerlzh (35)
zzdae (63)
rrkbjhn (78)
hnutx (50)
oqokji (198)
voxychz (50)
zovlqz (56)
ulood (81)
yzttfu (15)
htmcpcy (203)
jmytuxi (221) -> dvuctqv, sgilmx, fqdolnu, rdrncg
rehhbv (17)
ixkpaf (59) -> jqbdh, atvtit, qcebc
antev (89)
jfikdf (20)
ykxalh (31)
vqwclk (19) -> ewldimp, wkeqlvj, ouxuh
hxeqn (528) -> kimffjc, qpgphk, vqfiq
umsdpa (50)
aodfzpi (69)
wutzrk (89)
jyjvpeb (81)
ttbns (50)
wmewl (977) -> yhiab, iordzi, uuhoydu
ydejjeb (159) -> yvcanc, jrrubn
bykuuwe (80)
iesjhoq (336) -> bhzfx, sxexfai, mjounwc
kdrhj (1832) -> rrkbjhn, gzpgvqq
smyzyqg (20)
kigxtt (80)
rokvo (7)
wpcng (50)
koevsvb (97)
yihru (20)
krtglj (18)
cmfwwv (40)
jsaujq (1397) -> rgrcla, vqwclk, rxilrp
gmjxxi (97)
ekvmhd (49)
lttlp (66)
takbkro (200) -> ngjipr, inhfutj
whvpgmw (54)
lqaveh (97)
qthzk (187) -> wntmkg, pjkzokv
haaqbj (66)
vxufrto (40)
zseldo (181) -> hdvtd, papbxya
psmgm (95)
clwtgt (34)
bpwxvvw (89)
pmyrysb (77)
gjclsl (75)
olzys (57)
woqoljk (99)
ocodtdz (30) -> gjclsl, ogioyhi
nbybi (54)
veiaf (139) -> vlqqgb, iaftm
uvzpp (165) -> mxvba, jjtafg
qodow (63) -> oqxnfd, rpxaf, sybnvtp
kouye (58)
dlhuell (84) -> schexn, otzinx
nlrlj (145) -> veknoj, lfpjfv, yrlnu, ugelox
sambc (138) -> mnoinr, pkordz
bypqww (50)
rgkfzk (35)
kiatxq (1232) -> dispgy, irnjtjo, iqpoc
gigtu (60)
xzsrv (89)
dhafpel (636) -> vxddev, nxkpnt, zbuftv
bqfzqra (71)
rcbqqok (243) -> ofrogun, wwyuud
oaqkk (69)
dgxdydd (132) -> mudewqe, bazwto
vxddev (128) -> bzpjiss, qmjamoi
iqtyv (800) -> lvtotof, zddmrx, yzykfd, nlnphv
vdcmrrr (93) -> xuoyxmc, amrcopl, fcnsfy
jutep (86)
cyanr (23)
cxyxa (97)
tuzkv (153) -> iflll, tipewrj
cdegn (52)
mvijo (35)
xnbvupf (60) -> frlgjzf, wtorpp
rwopuzo (15)
uxfsb (76)
qedyqs (157) -> bjzbqzq, alfqryh
rwhgw (76)
csmjozb (79) -> sasym, wmewl, kdrhj, btvmyff, sqkfgo, jcputh
jbujmr (294)
xvjfw (8)
ekfwu (17)
ebiovn (225) -> mnufo, rokvo
ohcuki (197) -> alsfpfg, xsfryrh
zavisuv (15)
glwsf (85)
vurdlqx (196) -> acfdkr, aefjv
ihksnmq (95)
ecwpa (248) -> soyta, ytomr
jldhlug (234)
oazfz (61)
rdrncg (16)
rrrmaka (51)
qhgzopn (66) -> tmzef, iiiupn
ifetn (86)
plgjg (99)
okjds (73)
algkwbg (99)
ugmhzm (56)
vvnhm (135) -> ntrtfv, ihuqmbd
csuywzh (1788) -> wgvpotf, fwtxvo, vikip, bpzhj, bomuft, otjbn, zsotrv
pawpvkj (47)
zzvkwsb (148) -> hjfucl, gxcft
aivbhtz (78)
nyckm (23)
qwqpht (68)
kbuurtb (62)
ahexrp (19)
dlikiv (247) -> kinah, sthtydb
udiai (50)
lopnwz (91)
xbtvux (73)
gvtve (222) -> typbqmw, vdsaccd, sdlta, uisri
vczyhcg (8)
edswttn (58)
kqaua (89)
lmnuii (536) -> rlwoz, gjvmrh, ukapl, lthoz, boahhv, ylpxahm, rqonynk
kwlyw (193) -> hcruo, kecpcmj
trskdr (322) -> hdrfo, bimxf
clbmn (33)
scffzsr (48)
ewldimp (51)
qhixu (21) -> roorbg, oruhqn, psmgm
ypcup (94)
vrszijz (56)
vksephm (157) -> ngkax, tkerz
sxtto (30)
tkojiz (12)
elygt (569) -> bixtvg, xsqbapj, ocodtdz
vdctvf (84) -> iauxpc, cuyweja
rktxkyb (108) -> xjbot, flwjj
zckdwxe (54)
vfzwqfr (54) -> mphzxio, clbmn, donnc, niydqsy
iqpoc (260) -> zlads, jhapr
pojst (51)
ueitm (169) -> emqqf, qqstwmn
dgzywn (39)
ldcmzd (130) -> mertvs, ggoaczz
xtgmmc (306)
mjounwc (9)
ftbiwxy (62)
ogioyhi (75)
fkitgnx (69)
gvucdh (85)
opsrep (43)
olsycb (59)
jiizacd (49)
qbthgst (71)
nxqvwm (69)
rvrzp (113) -> xrqhewm, ifetn
pkordz (84)
vempqu (6)
ulmwqtm (230)
zwgsh (43)
srgob (561) -> plrig, djbtbrk
rmnkup (47)
btvmyff (1442) -> mrqtrkq, zjjyjj, uqkskjn
nrfyua (11)
nuozixg (1064) -> nnelc, zmzobfp, oggljxs
icrvj (22)
vksphlf (1423) -> kdykksn, wwtiby, uqddsal
xmnbar (58)
ukapl (195)
lijszmh (44)
zzonk (28)
jhapr (14)
mrqtrkq (88) -> zaxbfog, pawpvkj
aibtig (109) -> ggzqccl, hyxtojc
vuvwa (87)
ahysv (90)
mqwagy (88) -> uxlisdh, rmenjck
xpttnwd (95)
oullg (25) -> dlhuell, imrwgqw, hadddf, rktxkyb, zwtsg, wllrov
bwsgfa (22)
vmiykci (153)
jcgvp (18) -> mvbtomp, zatfy
wetluzb (33)
zvnzrr (37)
sgilmx (16)
geabygu (96)
kakvi (41)
fuujiy (92) -> xnfuz, urrhqwc, fmdfm
ppvsy (285)
nyuxiu (122) -> nzvqjrt, dhzsao
tjwynpa (75)
gowlaq (138) -> uwvfga, bnvlydl
snywwu (26) -> snqey, aodfzpi
cvude (41)
snqey (69)
ejqam (17)
pgmtcg (47)
rtcqml (85) -> zangrh, dspug
ezspaq (215) -> rehhbv, epvyxld, oguxu
ytabct (89) -> frfotet, zerxp
nxkpnt (248)
qubhi (107) -> lnznpq, scffzsr
tfotbwz (424)
wkgyfpp (824) -> ccbie, iesjhoq, kdffrsb
wjsxcmb (95)
ztdbvxb (53) -> zismp, dqoagdt, yxfjglq, givaxj
ouxuh (51)
xfzxrd (22) -> kakvi, mjlvx, wridnv, zeexkde
rekerpj (7)
redkli (81)
qdkhjb (53)
yituewe (95)
ocnkhq (10)
iaayhc (300) -> fwhhoz, ycrnaf, jkbks, anazjn, yhzjjgc, pocwgw
mjlzzq (212) -> hwycny, gmzabjk
rhaoo (36) -> kdzhiq, ydkhmp, dsytvn, wzezz
fqkzcq (293) -> gztng, oiaxzp
essijo (1248) -> wuqapgg, msmxf
ckapp (94) -> clktah, akiaxs
nktwwvp (159) -> qivuzn, cdegn
qxwdzl (50)
lfpjfv (48)
lmfclbd (14)
cglyptu (240) -> icrvj, epxwjhy, tpmqmg
dhzsao (24)
bckfa (16) -> ntlawn, tslujme, ccjze, woklobt
mivmhi (45)
bfjxeyo (24)
plrig (53)
ijlooi (1429) -> jcgvp, zvsgd, fzafkj
pyhcj (64)
gdvbtjk (71)
fxrkz (70)
husor (57)
riiaj (44) -> lvvkjx, mbxyf
lxmvg (4738) -> msjbv, ijoaqyv, yname
wntmkg (23)
helyy (88)
muxvdx (57) -> veiaf, rcbqqok, gfnmx, zezeds, ktbto, qedyqs
rroub (41)
hnwfe (89)
enuvuv (20)
wzzlsg (18)
hpgsb (81) -> xpptslq, jtoryw
woklobt (60)
jicyq (18)
lybwr (64)
ujgpnsy (12)
mbtweib (86)
vgzejbd (10) -> vuoqao, vwkkml, kmpfxl, snuewn, jjgjvki, fiprusz
vgfveov (198)
lvtotof (49) -> pprvv, gsckda
ylpxahm (33) -> jyjvpeb, tytsynv
glximrw (53)
iykjtnw (542) -> dizqtw, oiozpzq, dmwutl
xuoyxmc (51)
wpvale (18626) -> wihtv, isbdm, gxeehd
jruttt (28)
urrhqwc (84)
yfyaho (7)
klpzhup (11) -> befwz, mypula, xmnbar
kclmmu (49)
qcnstq (91)
sasym (13) -> vimnt, eoign, lusub, peokkb, mlhaxv
mgoxhns (130) -> edswttn, ioycu
stzzli (89)
ltesfzf (44) -> sufdte, vpqsjbj, oghyxz, hxxml, mnhrjdv
yxfjglq (58)
fuhbay (82)
gxcft (25)
rwamq (86)
qxqwmye (68)
ketopn (42)
tmsmb (84) -> pkxrm, pbbkg
zerxp (75)
zpbrw (95)
wuqapgg (66)
nmsats (82)
vvzctek (9)
cmoty (91)
qkkhj (88)
pocct (99)
xyfvxng (45)
mqnbmre (2069) -> vecnb, azhddw, muxvdx, qbodszw, yggqq
msjbv (918) -> nktwwvp, qijleb, ttnoqm, ulaio, furlcyu
mkirruz (70)
mubkcmk (163) -> solqvvf, ocnkhq, wntitz
lvzzwy (89)
ypiwnt (55)
bveilrx (306) -> pxvse, ahexrp
shiaqps (45)
mlhaxv (297) -> ctcmfv, ekvmhd
eiohuhm (72)
isqnx (122) -> azgohsw, pltzthr
qqstwmn (5)
fiwvclv (80)
zobti (87)
qbvhefh (53) -> ylazd, cyvwwa, sfkpzr, zsjlevq, zseldo
xqgxel (54)
yrlnu (48)
rrmlgct (19)
jtzdqn (178) -> lsoen, pojst
nffvt (37)
axtepsa (13)
ngkax (18)
viwez (27)
kdykksn (7) -> geabygu, cfiqn
zvlobk (419) -> mdfkbxa, wzzlsg
xsqbapj (164) -> xqxvktz, xvjfw
nzvqjrt (24)
gbqbg (18)
hskko (38)
bgmntpq (6)
zddmrx (227)
dgtsic (47)
iijfq (73)
qytxu (71)
mklcsj (54)
jnwdraz (63) -> aubvpzf, zpfuxux
hudde (1072) -> wyrfplr, rzbrbmy, ujmfmiu
jcoyk (18)
dspug (66)
qgbbhdv (46)
neddz (86)
boahhv (195)
ajjmsnw (50)
lusub (209) -> nrloleu, lfwpqb
bkgise (17)
xsgyar (568) -> fesce, vfteg, thhbhrm, vvnhm
mudewqe (49)
trait (91)
fljpye (46)
xobszr (61)
pkxrm (57)
qrynkpt (22) -> kswafh, oztxmy, zejcp
frlgjzf (68)
aomksx (70) -> pmyrysb, robpw
gjvmrh (167) -> xxtyban, mfjdb
atvtit (20)
ihuqmbd (34)
mfjdb (14)
rptcpf (33)
ljitswv (89)
zkujvlv (51)
ydtuje (69)
emazu (93)
sqkfgo (1451) -> ueitm, okbtg, cnzynyj
flmma (86) -> ygglox, ocvrlia
jnqgs (76)
ctken (72)
kxdbyp (20)
ktlkx (112) -> etyaxa, axygpr, rqsyc, axtepsa
hesyq (85)
tydtcxc (919) -> swcsd, nkclzqq, dhcopz
sqbxzl (12)
dispgy (52) -> olsycb, ynecxzo, esqvkcm, xclsj
djbtbrk (53)
svjnd (47)
fizbyu (78)
vqfiq (61) -> zdrhuz, jmzpxql
tqsrg (70)
dulrvcq (2086) -> apjeywv, vurdlqx, bwemy, ulmwqtm, qkxtwct
gfjeud (71)
xdzgwl (220) -> jicyq, prbbfe
jcputh (196) -> xdzgwl, rodxm, piutfin, ezmot, bckfa, zyisjsj, icsxziz
gbwaobo (94)
mlyar (44)
zsotrv (751) -> wudlze, hjmreq
chxgqe (47)
junva (83)
fmdfm (84)
ewwab (70)
hdrfo (51)
qijleb (111) -> qngug, voxemk
qmjamoi (60)
pyrvg (230) -> shcavm, trseebo
joszidy (95)
rxilrp (138) -> gtprqg, xqgqp
ptnndxj (46)
typbqmw (11)
fesce (39) -> fuhbay, jozav
oeixw (65)
gjhfseh (20)
zeexkde (41)
ynecxzo (59)
oqfpo (78)
keazynv (68)
gnsdn (51) -> njerlzh, rgkfzk, lhyzwtf
sqljeh (20)
dclmckh (93)
rqsyc (13)
wvwjep (70)
ncobxr (8)
builgr (78)
xkdjbxo (81)
bzpjiss (60)
vfomix (95)
wtorpp (68)
pruui (1276) -> glaosn, xgqxofa, ggkael
monhu (76)
piutfin (156) -> wpcng, qxwdzl
wrwim (10)
jrrubn (52)
vkdytw (24)
vdtdmy (26)
pbbkg (57)
uwviodb (208) -> bkxfso, evrtfzj
vfhgfb (1084) -> gnsdn, ttbgzv, pyaqqhu, riiaj
iordzi (223) -> cfrqn, nzuhp
biffdx (42)
bpsesr (50)
cglfuq (199) -> vempqu, noogeuk, bgmntpq
bkxfso (19)
oopnu (88)
wlavb (92)
gmzabjk (41)
ehrfv (57) -> pruui, eondv, ygypj, vksphlf
lpwuzn (89)
cnzynyj (89) -> wwzjdv, xyfvxng
dgmtgrv (12)
hpmtom (50) -> zzpwgcd, qxqwmye
jafrv (719) -> qhgzopn, aomksx, porttu
msmxf (66)
ldiqm (266)
llydxxz (37)
vdsaccd (11)
cbsdget (81) -> licrtwb, zovlqz
qgwhbwh (62)
epuqu (17)
loojs (43)
ovshy (95)
qhayeqe (86) -> opsrep, loojs, fvukbun
amrcopl (51)
tsncd (108) -> zygfdu, jsfqyd
oguxu (17)
skyaki (69)
ufxfx (25)
mpzyapm (19409) -> elygt, ltesfzf, dhqrk
lthoz (150) -> rwopuzo, uazwsu, ozaogat
xxtyban (14)
ggkael (54) -> gmjxxi, koevsvb
yuyhys (12)
qngug (76)
kazwz (92)
owysb (71)
eondv (25) -> uxggaix, ngfxax, ztdbvxb, jmytuxi, hkxfb, rvrzp, ppvsy
oyhqsok (65)
iflll (97)
xjbot (85)
tytsynv (81)
rsyxcdq (157)
vuoqao (102055) -> kahduw, lxmvg, vtwud, ktcffyf, ggdoqnl
ocvrlia (48)
cpuxdo (75) -> rroub, cvude
tpiwftj (482) -> cancxr, xhecnbf, ilcmx
eaoxb (2777) -> cfrbz, vmiykci, kllsasv
alfqryh (54)
gfnmx (214) -> ekfwu, ejqam, kccpv
daerl (14)
nvahhge (14)
rzvlc (19)
ktcffyf (1777) -> dhafpel, jtyljl, nmcewof, rhaoo, xsgyar, otetl, essijo
pntvfpd (49)
hkxfb (285)
ngfcc (87)
yqdaz (21)
qzwauo (49)
kdkobz (11)
tslbp (224) -> mvijo, qolgxnd
vlqqgb (63)
zsjlevq (175) -> bemxocu, builgr
xzsxx (79) -> zugkqyx, jubeqci
yvattv (44)
nhhytw (44) -> skyaki, nxqvwm
zmzobfp (75) -> ntxtwk, yhvdjl, xzsrv
sretj (240) -> wsnsqx, rekerpj, knciro, svcqds
awwhgzp (70)
adqnigs (72)
oipscid (85)
xsyqdlv (26)
eoign (134) -> aujeia, ngfcc, zobti
nfulfov (14) -> aivbhtz, exlwxxi, oqfpo
fqehxv (168) -> lgonp, vxufrto
impzr (70) -> lybwr, pyhcj
bnvlydl (63)
olzqxap (65)
frfotet (75)
ajidd (80)
qyvsaxn (30)
rlwoz (19) -> kjauagn, qkkhj
hysssy (12)
ptmsqz (81)
kahduw (31) -> qhotyqx, xhxek, bhakbq, ivgpv, lmnuii, frctm
ejdjxu (41) -> wazvn, algkwbg
ylfxp (99) -> heztht, mbtweib
isgky (80) -> kecckss, obakqyf
xclsj (59)
qhzem (47) -> fnkgp, ujipv, tuzkv
zaxbfog (47)
uekzf (1315) -> qjxikz, bptaz
gkjwl (50) -> pucdapo, zckdwxe, xqgxel, vcprhe
xqgqp (17)
ntrtfv (34)
ufust (68)
yvcanc (52)
jtqxxa (47)
rfumv (92)
qjxikz (38)
sybnvtp (59)
pugxio (62)
olfwppt (154) -> bwsgfa, lrplxk
ugelox (48)
oruhqn (95)
rlwmfp (158) -> bypqww, wuwhup
qnwwjwt (27)
hjmreq (78)
paykww (22)
aefjv (17)
hvpess (1924) -> vaxtfaa, wbnmb
dbziu (96)
xnfuz (84)
tpmqmg (22)
qrinzet (69)
ldrpjd (88)
pocwgw (13) -> glximrw, bhmirp, rcqkas, qdkhjb
sxexfai (9)
euhgw (208) -> xrbkzmk, xsyqdlv, vdtdmy
ulaio (203) -> pdddwgk, sakmm
vnmml (19)
ksncpee (28)
pucdapo (54)
ucnehpw (50)
btvsj (47)
veknoj (48)
papbxya (75)
sdzhsq (94)
orrfh (71)
gnxfwv (68)
grthhzv (244) -> dgmtgrv, tkojiz
dxcozh (35) -> phrpja, ahysv
vekndsc (94)
ujmfmiu (39) -> vrszijz, ugmhzm, sdrcc
jctafp (62)
bhmirp (53)
tmqlkof (28)
wyrfplr (109) -> qzwauo, pntvfpd
shcavm (18)
xmkegiw (28)
ydkhmp (290) -> cyanr, nofepy
ivkcc (70)
ujipv (183) -> gkrqba, nmsats
lnznpq (48)
xqxvktz (8)
wzezz (264) -> bfjxeyo, vkdytw, uwizlce
nvgohm (26)
ydqtt (158) -> oeabdth, bkgise, fjgjfpc
nmcewof (1182) -> plgjg, imtzl
bbnjml (31)
iweii (8) -> lvzzwy, nubqteb
kmpfxl (134829) -> csuywzh, ehrfv, bkfnip
dbkxe (34)
sfkpzr (76) -> lsszcka, manlcoz, oipscid
bbyoqzx (14)
uuavydd (43)
hjehgnc (489) -> ujqjrz, wulvcf
qmncyu (17) -> ofveqm, qgwhbwh, ftbiwxy
zzfom (210) -> jruttt, mvdkbch
cigew (185)
nozgflw (89)
trfjf (174) -> hskko, evbeo
idqhx (12)
noogeuk (6)
ccjze (60)
bedzc (43)
uymju (8) -> ectlgy, pchapba, tsncd
jvwvi (86)
xrqhewm (86)
ifijr (28)
tuzzzct (50)
zwrjdk (82)
ekvzyod (11)
vivco (626) -> okhisbv, biffdx, rbascuz
atujmm (250)
bdiftdg (69)
wqzxa (82)
jtoryw (76)
sttlowq (207) -> xmkegiw, tmqlkof
wqkoep (90)
sdloeq (14)
hzruk (47)
mgoic (36)
mqkqtjo (57)
gsxmqnw (68)
pexfst (44)
ycfbxe (254) -> tnljdhr, jfikdf
kenxmax (91)
yhvdjl (89)
gzpgvqq (78)
inglhm (94) -> qwqpht, keazynv
uytmyv (91)
wqgoxl (94)
yfxbu (32) -> jbujmr, mjlzzq, hcrys, mwfksx, fcaht, ycfbxe, tslbp
mnhrjdv (185) -> lmfclbd, sdloeq
gcasp (17)
jjgjvki (99205) -> suuppr, csmjozb, uexqjw, cckrzh, yuzzsk
zvqvvyp (39)
bgpab (1781) -> qmqpbm, rdwxvvp, vjwuuft, dlikiv, acaqfng
prbbfe (18)
gaalz (75)
robpw (77)
rcqkas (53)
axsimnf (403) -> yfyaho, qeyjc
mypula (58)
mnahxn (52) -> cxyxa, lqaveh
smqkli (81)
nkclzqq (44) -> bhyzi, okjds, gfsgzni
soyta (9)
cagvlf (267) -> ypcup, mbffei
dvuctqv (16)
hdvtd (75)
lexqf (96)
cuyweja (81)
vfteg (17) -> dclmckh, iihwb
fzuosl (94)
ipctg (80) -> zzyxzr, rqdtsp, esbdjah
yuzzsk (3542) -> ijlooi, yqgru, oullg, ekblpi, hudde
tpvhe (42) -> sretj, grthhzv, luqqu, uwqee, qssjswr, kbrwk
gpbdzes (96) -> dgvvo, zvnzrr
cmfwvem (23)
befwz (58)
mellhhn (166) -> vvzctek, hrlgs, evqbli
bmxolxn (20) -> bpwxvvw, sfnix, fxnap
rnqlzmv (88) -> tnlpmw, hrfbh
qeyjc (7)
jozav (82)
gjahajj (62)
qyfzonc (89)
ngjipr (24)
sepmxir (33) -> uuavydd, xocoiqa
qizpmf (98)
mroft (77)
lyeyx (61)
gtgovt (134) -> gqxyh, gbqbg
hrihd (50)
pygoqsv (55)
dxczurt (89) -> rupxxhm, lopnwz
mdfkbxa (18)
hcruo (72)
ytomr (9)
bhzfx (9)
mbgapsj (39)
omqhf (105) -> jwbdb, junva
wntitz (10)
zugkqyx (89)
ntxtwk (89)
phrpja (90)
ilcmx (129) -> xbtvux, agflbq
hhcoc (63)
bxggi (36)
obakqyf (51)
xrbkzmk (26)
sthtydb (22)
xvljr (21744) -> nfulfov, takbkro, gspffet, fqehxv
hofirm (33)
okhisbv (42)
uldgij (64)
sakmm (30)
zbuftv (62) -> glzmsn, oacnj
jxevsc (57) -> wvwjep, jilzdse, fxrkz, vkgfrb
ioycu (58)
ysuttai (72)
ttnoqm (133) -> vtopekt, naxtp
ereyjs (54)
hgksz (174) -> msuvilq, couhjsv
luqqu (112) -> yfaihrb, fizbyu
bixtvg (180)
kswafh (76)
fwide (24)
ghgou (12)
aujeia (87)
lgqad (75)
szvocp (11)
yivgs (36)
lnlkwq (216) -> nvahhge, bbyoqzx, daerl
qtcck (137) -> lgqad, ngtdwvu
wkeqlvj (51)
vbxzk (75)
uqkskjn (132) -> kbbcau, ufxfx
gacpvy (26)
ccbie (90) -> cmoty, uytmyv, dmiccse
suuppr (9751) -> uymju, rhpcgg, vivco
fqdolnu (16)
vcprhe (54)
iihwb (93)
swcsd (91) -> ltpmtif, jvwvi
nbwaei (61)
zdgyktc (84) -> jnqgs, uxfsb, xkzcttf
bimxf (51)
pdqzfg (70)
bomuft (785) -> xobszr, idpttp
kytha (39)
zyisjsj (58) -> woqoljk, pocct
hwycny (41)
ofveqm (62)
oqxnfd (59)
pnpsnjp (803) -> zpbrw, pbpva
ysekeoo (126) -> suawycj, gigtu
gneut (203)
zdrhuz (47)
qmqpbm (7) -> owysb, gdvbtjk, qytxu, wxfir
imrwgqw (170) -> yhncv, mklcsj
dymzl (72)
vzlzrt (55)
lfwpqb (93)
dirhtk (65) -> hrihd, udiai, bpsesr
donnc (33)
iactix (293) -> ulood, xkdjbxo
acaqfng (271) -> wrwim, ilohfvn
tuwedv (150) -> eiyiuq, ereyjs
mjlvx (41)
fwhhoz (72) -> rrrmaka, zkujvlv, fyaco
msuvilq (11)
mxvba (37)
smvskd (1262) -> cglfuq, rtcqml, zjnrzph
ggdoqnl (9436) -> hjehgnc, xnlkkx, srgob
aifpyc (61)
vwkkml (148790) -> hvpess, nuozixg, tshyvej, yfxbu, kiatxq
tipewrj (97)
pblqb (7) -> kouye, ibydam, jqdngi, tuzpls
oktgjb (70) -> lcbgeev, zwrjdk
dqoagdt (58)
xkzcttf (76)
zevrg (108) -> stzzli, kbybvzk
lomrivn (92)
grkzvkj (124) -> xemcuk, cmfwvem
uwvfga (63)
frxshon (95)
zzvhmse (157) -> ujgpnsy, idqhx, hysssy
ahsqaob (75) -> gtotarq, joszidy, frxshon, vfomix
jqbdh (20)
kvzmie (69)
oiaxzp (22)
spefs (96)
fxnap (89)
azhddw (909) -> smqimxg, mgoxhns, izgqzs
epssvr (57)
kxhvvgi (8) -> ihksnmq, wjsxcmb
etjwno (91)
tlwxovy (91)
capuc (91)
evbeo (38)
djvbdm (50) -> zzmczwl, whvpgmw, szqdapo, nbybi
mbffei (94)
uwqee (90) -> qyfzonc, nozgflw
bpzhj (251) -> hbaai, gfsnz, snywwu, ktlkx
dhcopz (207) -> hjbrfba, nlalji
jilzdse (70)
lgonp (40)
zvsgd (58) -> yzttfu, zavisuv
rdwxvvp (203) -> mlyar, lijszmh
wridnv (41)
ovtfd (81)
kttsf (35)
murnoa (238) -> gpbdzes, gtgovt, mqreb, grkzvkj, nyuxiu
otzinx (97)
bjjtifj (15)
irnjtjo (12) -> ubaxya, lomrivn, rlhmcf
zezeds (79) -> kbuurtb, pugxio, gjahajj
ofrogun (11)
bjzbqzq (54)
qolgxnd (35)
vdkhvyp (52) -> kfkfyx, mgiuz
rlhmcf (92)
okbtg (35) -> dymzl, eiohuhm
kkhlzm (96) -> wlavb, rfumv
dmiccse (91)
esqvkcm (59)
zzyxzr (61)
tegtsu (72)
kbrwk (124) -> tegtsu, adqnigs
mertvs (88)
awmmdn (49)
pknsw (74) -> lexqf, pxadg
fwtxvo (71) -> ibslyw, jnwdraz, ydqtt, flvrfdl
flwjj (85)
asbmk (76)
sdlta (11)
vdwfz (234) -> amtrbok, brpgc
exsugls (49)
yfaihrb (78)
oghyxz (213)
manlcoz (85)
mnoinr (84)
ibydam (58)
hjfucl (25)
lcbgeev (82)
ygglox (48)
xhxek (425) -> uwviodb, cenqs, mnahxn, ysekeoo, vdcmrrr, vdctvf
krtxpw (96)
zgxjjm (24)
vkhiz (86)
inhfutj (24)
qkxtwct (166) -> jfjvw, hbcpm
mfoismz (70)
voxemk (76)
inuci (86)
wllrov (200) -> nvgohm, mqsrwsz, gacpvy
fyaco (51)
ngtdwvu (75)
kfkfyx (94)
iiiupn (79)
gkpalaj (76) -> jjklma, ydejjeb, sttlowq, axqrke, ipctg
ubrrdtd (75)
fwskxq (31)
nzuhp (57)
npvuz (28)
fnkgp (65) -> vekndsc, sdzhsq, fzuosl
roorbg (95)
cfiqn (96)
fcnsfy (51)
idpttp (61)
vaxtfaa (83)
jubeqci (89)
uxggaix (195) -> shiaqps, xmjunhp
vvlimno (63)
txcon (87)
ocltuv (75)
kdffrsb (187) -> ldrpjd, oopnu
imtzl (99)
jvdoo (22)
yhzjjgc (93) -> xunvu, bebuqpx, wetluzb, hofirm
clktah (86)
givaxj (58)
fiprusz (88) -> bgydix, mpzyapm, xvljr, bnywvsx, snmey, batky, wpvale
wgvpotf (115) -> tmsmb, zzvkwsb, olfwppt, impzr
ohpkkhx (385) -> kttsf, ysnbr
eofyk (41) -> ctken, jyrzc, ysuttai
ubllty (91) -> qizpmf, husly
aqgumo (47)
zezbp (91)
mphzxio (33)
gfuyuz (209) -> jiizacd, awmmdn
rpxaf (59)
aewlgu (62) -> oazfz, aifpyc, oaoisa, nbwaei
coqek (166) -> uslhk, vczyhcg
kecckss (51)
jqlbenn (65)
jyrzc (72)
azgohsw (82)
qtqhwon (50)
furlcyu (85) -> lpwuzn, hnwfe
evqbli (9)
zwvhgce (121) -> chxgqe, hzruk
xsfryrh (21)
jjtafg (37)
acfdkr (17)
rupxxhm (91)
nnelc (342)
hdbkw (43)
usgpgi (182) -> ketopn, mvtkwn
thxqmj (81)
bgydix (16136) -> tpvhe, excdqtl, yjvfni, iaayhc
pxadg (96)
uiryg (2879) -> aibtig, sepmxir, ixkpaf
exlwxxi (78)
vecnb (897) -> atujmm, qrynkpt, trfjf
zkwnhn (329) -> oorvvpt, zzdae
ezmot (96) -> bykuuwe, fiwvclv
vrxkr (37) -> jxevsc, gtkii, nlrlj, kwlyw, fqkzcq
zmstcy (8)
axygpr (13)
yzose (57)
kproiw (93)
lptaikg (82)
cmmnjch (6) -> ewwab, awwhgzp, tqsrg, ivkcc
qpgphk (33) -> lyeyx, cqfsg
hittl (20)
wbnmb (83)
tsevkec (54) -> yvvxtg, wqkoep
mwfksx (216) -> mbgapsj, zvqvvyp
bvmhqar (224) -> epuqu, gcasp
oeabdth (17)
pchapba (70) -> kqaua, ljitswv
gsckda (89)
gtbjtpi (265) -> ovshy, xpttnwd
xocoiqa (43)
woctu (56) -> qrorhfv, axsimnf, wgbviwb
foxvut (77)
zerhdhs (150) -> xtidu, yuyhys, ghgou, sqbxzl
rqdtsp (61)
dizqtw (103) -> ieowdj, vgkhk
ebdva (718) -> vgfveov, zerhdhs, kxhvvgi, oqokji, lpmnwh
ikfzj (212) -> nrfyua, ekvzyod
hcrys (63) -> foxvut, oislgqy, mroft
vkgfrb (70)
bwemy (92) -> oaqkk, kvzmie
yname (1373) -> qhayeqe, dxcozh, dirhtk, zwvhgce
desuqj (91)
bnywvsx (19757) -> pnpsnjp, paunv, hxeqn
wiasj (34)
lhyzwtf (35)
gztng (22)
szqdapo (54)
flwbwcq (142) -> xekft, jctafp
ijoaqyv (91) -> ldcmzd, sambc, aewlgu, wrkoi, xtgmmc, cglyptu, qhixu
knyvyft (81)
ngfxax (139) -> uiilkiq, iijfq
atqfhm (92)
masvpfj (184) -> ifijr, zzonk
yhncv (54)
wwhyd (95)
oggljxs (314) -> awrbrc, yrysmsi
sdrcc (56)
sgqhelx (60) -> hhcoc, vvlimno
snmey (84) -> bgpab, xflsc, kidvt, rlurjca, uiryg, eaoxb, dulrvcq
qpchzkg (57)
mhaucon (2652) -> smvskd, wkgyfpp, fkgkcwd, jsaujq
brpgc (12)
vimnt (91) -> rwhgw, asbmk, lvarp, monhu
excdqtl (378) -> hcsjun, trskdr, tfotbwz
uxlisdh (89)
isbdm (1276) -> aqgumo, svjnd
alsfpfg (21)
zzpwgcd (68)
glaosn (86) -> ptmsqz, ivvyjos
fvukbun (43)
rokri (55)
qrorhfv (93) -> redkli, thxqmj, esavxwq, knyvyft
eziosif (33)
jqgfu (40)
nbqaqp (298) -> owxski, nyckm
hyxtojc (5)
awrbrc (14)
ogbov (15)
rbascuz (42)
kdzhiq (63) -> kenxmax, tlwxovy, zezbp
geapi (75)
oiozpzq (127) -> uldgij, kiawm
fzafkj (88)
zejcp (76)
wrkoi (124) -> capuc, wifrwut
dhqrk (173) -> zdgyktc, etcsuuv, uhwlk
jtyljl (348) -> bveilrx, nbqaqp, fuujiy
otetl (1340) -> patlvg, gjhfseh
mnufo (7)
cfrbz (117) -> krtglj, jcoyk
lsszcka (85)
rgdvqu (166) -> dbkxe, clwtgt
yjvfni (1179) -> ofnqgn, rsyxcdq, cpuxdo
gfsnz (14) -> ydtykm, tjwynpa
knciro (7)
sfnix (89)
cqfsg (61)
izqxal (142) -> kxdbyp, sqljeh
ivgpv (1040) -> ubllty, qtcck, bmxolxn
bazwto (49)
twimkx (24)
evrtfzj (19)
ofnqgn (19) -> qrinzet, fkitgnx
nrloleu (93)
ylazd (201) -> jqlbenn, oeixw
hrfbh (49)
dkexo (146) -> nffvt, llydxxz, bgtzw
hibjkps (106) -> cmfwwv, jqgfu
oacnj (93)
inelfwo (91)
vgkhk (76)
cckrzh (6841) -> hdinwud, dqzkic, vrxkr"""







print("Exercice 1")
children = []
node=[]
dico = {}
dicoChildren = {}
i=0
for line in inputVal.splitlines():
    line=line.replace('(','')
    line=line.replace(')','')
    line=line.replace(',','')
    tab=line.split(' ')
    array=[]
    array.append(tab[0])
    array.append(tab[1])
    array2=[]
    for indx in range(len(tab)-1,2,-1):
        children.append(tab[indx])
        array2.append(tab[indx])
    node.append(tab[0])
    dico[tab[0]]=int(tab[1])
    dicoChildren[tab[0]]=array2

for i in children:
    node.remove(i)
#print(str(dico))


print("Solution: "+str(node[0]))
root=node[0]

print("Exercice 2")
solution=[]
def computeSum(node):
    count = int(dico[node])
    children = dicoChildren[node]
    previous=[]
    i=0
    for child in children:
        previous.append(computeSum(child))
        count+=int(previous[i])
        i+=1
    if(2==len(set(previous))):
        val=max(previous)
        inx=previous.index(val)
        valNode = int(dico[children[inx]])
        valNode-=val-min(previous)
        solution.append(valNode)
            
    
    return count


for k in dico.keys():
    total = computeSum(k)

print("Solution: "+str(solution[0]))


count=0
print("---")
print("Day 8")

print("Exercice 1")

print("Solution: "+str(count))


print("Exercice 2")
print("Solution: "+str(count))


print("---")
print("Day 9")

print("Exercice 1")

print("Solution: "+str(count))


print("Exercice 2")
print("Solution: "+str(count))



print("---")
print("Day 10")

print("Exercice 1")

print("Solution: "+str(count))


print("Exercice 2")
print("Solution: "+str(count))

























