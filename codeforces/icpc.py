'''
SAMPLE INPUT 
6
2 1
arjit
tijra
9 3
umknhvlktyodvzfmltrwrpudxyrkasuujbdjjeltgl
okqtwhafffhdjpaocxkekdrcklirpnogzfzqvmfyskavakuatxgzcj
ktuothmyxjkvgghzydyoducbuoqtqxmyhaacakcunwwkiibzcvdwjkpkyklevxxtkhzgznjgomwlbrgqcqjyatdllpolb
pnqetpiouhehqdifitqrzqqnr
hkjzfhazokpcdrcypozudukauantnrmecpkiroluwrif
tzztkzzvr
sunnnyaybrrqobjmwrix
qjyahcbulxuilizwnxyxasklxuuk
bsbqagwvwceoyzivnksoukxdgsfvijutofagwpspinwbgzcdagaoxlwkebjkdukhxsxvcxiibqzjjztizfsih
6 3
asmhleggpyystednwefpopaaerzeqnwbpzroziawchu
rgtmqfdtbennow
kfokbhpspltmklhjbiiuauzmywxonlsxsznweqbmlkcdeeebaguspkntropcjdfuaqugykkiaotla
tygvgucwpdarozqyzeotxmabtookvcubzqeighazswqaedwxeldpefbvzsllbicvpxmpoxywlufidufqqfafapimvbejhrbm
qldkwemmfejrwehfewnmsommbmbfvlqffkkpttztfvgswqijbbxrjhwqvlrhfvzhezebjfucvwbifyem
dawmsmxyrcsiefnkfrlgwbezgbdolihrfbbuuywcmtakqfhdwnwxebfbkqpwy
5 5
ijnkqzqrqjwawxlfjlsabbghqmdlpaafyywznlzkpsbgesyptnltggficwscdhhdywib
ixgwtqnxasbavtrqlixcgtrgcqcuskwizisid
rlpoeuisxatniyrkfoikiyuczqtizkpmmlwhipj
dhzovlttjgjmrybbyrmprvylxpivneq
qyrmurtijfclgkfxpctdzxnoxeosngramqtpobcflhfstvlntmdludjrppdnlsaaxxes
4 2
ocszcdlpvqlnjvfhyrisb
rffyqbihqgixgtno
cqyykquktczedjkmtsqbsjjptqdgnszkoegdtwccwtmk
flwvkeggjyzyqyprirkjomtqgkognicqhggcccthlicagzluxazevmwrmvvltssxlrqrwgimxoqbcaenyxu
9 3
hvp
hbrkhvdabjrpaiuldhoyzljtoavnm
sawezqvmhesrcydpjsfynuwrgvcbkdhqcacqjwvolwdjptanwchklcexlvuffjvxviwcoamwramubzoitsjobiqnv
erqvmgwllcxpppjtzzbbhxtvoay
smzepbbhkmytngpqgxhykpepiamr
sfiouuhbakcofggmktcavsmcgovyhqgrvbzgc
ogcm
mwrsaxczcffjhbfonvzzbdaubwqozqgufpws
vfncxgieynotwwvdzueqqk

Possible
Not possible
Not possible
Not possible
Not possible
Not possible

Possible
Not possible
Not possible
Possible
Not possible
Not possible
''' 
for _ in range(int(input()))         :
    nos, each = [int(x) for x in input().split()]
    camps = {}
    for i in range(nos):
        curr = len(input())
        camps[curr] = camps.get(curr, 0) + 1
    camps_needed = len(camps)
    if each % camps_needed == 0:
        print("Possible")
    else:
        print("Not Possible")    
    
