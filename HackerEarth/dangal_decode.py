import re
def check_prime(a):
    
    if   a <= 1 : return False
    elif a <= 3 : return True
    elif a % 2 == 0: return False
    elif a % 3 == 0: return False    
    x= 5
    while x * x <= a:
        if a % x == 0 or a%(x+2) == 0: return False
        x+=6
    return True    

for _ in range(int(input()))    :
    s = input()
    sl= len(s)
    pcnt = 0
    maxp = -1
    alld = re.findall("\d+", s)
    for i in alld:
        ii = int(i)
        if check_prime(ii):
            
            pcnt += 1
            maxp = max(maxp, ii)
    
    print(pcnt, maxp)            
'''
2
sd5f7a9s4d2fas2                                                  
dr15t17rq7tu29lu11yk4
4 7
4 29

10
hgue52a1ax24avc32awf21ax9a32as12ap42ag22a22as42ayycpvkf22a4akswrn18a32a22agpfd22af12a40au12ab0aoy12a12a12avpayhqq9axj22avouwmnbckf42at12a12ay22ajw8afu6a6angokty
n38a29ard6aeo46a25a5ams3avuf10a3alt35a23ar32awdzo11af2ajvw29a49a19ay32a14amo13a5am17aggkud23aggpyne22ae23ak11age7az27a13ag30a5ad11a11al7a5a36aw13awb2an40arr44aqczeumrczj
p14aed11a29avm17a13a10a30avp2aabz2a28a19agpndb2aq5aproz16axt29aa5a35ajx5ah34ay29a19a13a25an11azpig2axzzs5a31ajr12apw17a13a18ad45apu47aq11ama5a31a13aq17al29atj7a24asszncv3arx
tokjwcl7a47ayc13a28aaxg45aeh22a2a7a2ab43a43a7abgcqkozkbj35azshre26ar29au42a5ae6a11a12a13aueo38a13aenhiuz2ai3arst23aukbc43aeti20a3aecz3aq23aifbch29a23ajl13ax32a
rsi3a2alf39a41ah34aynf7a25adynyd29ap16aktwsogf11al3awm3a30adazgvokgc45a29ahyyg23a42a19ay30a28awyb17aphtyzvup13a11agkrz3a23am7a11axvh37ahribz11a11ayp23a26ae2av
3av13aq11atpn3a8aio29aw13aqe24a5a29a11apl39ak23a23ascw16af5ai7a17a23a26ap40a36a7azyi27al3a45ajf3amqmjj7as1a19aadj29a19a32aw28aw33amaaw13aj14aolhp13ai30ak2atd32ayse5a14a29a29aahi
2ag2ajm13a42a11aal2a5adrv2a26aefvryu27a7ak29agp32a11a46axzas40a20agnpnkmu7af26a11a23a29ac7a1amn17ajgnnzax12a11ad7auej2a2af32a46a32and3av46atck14ad3at19aqgv11ajgmx7ap
2aqhd17a13a0a19ao5ax31a21a32am23a28awsfiuso17aqg40ahlof23af11azrp23a19ac18a2a23axfppf5a7ae3at6a2awlbpkltdp20a26a3anm2a35a36a8akk46av35a7a41abbbqp5ai18afwhx2at3am29a3a14a
y5ald37aa29akv2a13abc17a35adc13a29ap45a38ao14ahmv21a7adtbu13a23ass13aoji23abp30av17abt29agjs13atud3a29af25axj3atj36ad24akljq29a39a7ah29a23axfpsylj11a5a41a41a2aw17an39a13a17agl13a
5a5a7adrettktr41a15av7a5awo7a3av3awo8ae2ac23aync3a13alwj12a19at49aixp23an29au29a5adw11a2a26au48at5a20aq17ar48a13aqn28ad22al31am17azv2at3ag3a17azvn1a2ap8athxygkc28aaqn

0 -1
24 29
30 47
24 47
23 41
28 29
25 29
27 41
32 41
30 41

