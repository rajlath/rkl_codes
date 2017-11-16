from copy import deepcopy
for _ in range(int(input())):
    a = [x for x in input()]
    b = [x for x in input()]
    cnt = 0
    x, y = deepcopy(a), deepcopy(b)
    for i in x:
        if i in y:y.remove(i)
        else: cnt += 1
    x, y = deepcopy(a), deepcopy(b)    
    for i in y:
        if i in x:x.remove(i)
        else: cnt += 1
    print(cnt)
            
        
    
'''
10
tttttttttttttttttttttttttttttttttttttsssssssssssssssss
sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss

aaaaaaaaaaaaaaaaaaaaaaaaaaaaa
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

gsadasfdashdasdkjgadhjdyjhasfdasgd
ajdfaghfsdasgdfagsdhgasdfasfdahd

ahjjjjjjjjjjjjjjjjjjjjjjsdgajfhsdhafshdfasjdsahfdasd
aksuhdgyhjagsdjhasdkjasldashdlashdjas

aiustdiagsdiiiiiiiiiyasdhkagdyafdfasdfausda
ajkgdiuagdiyafdiayfdkafdkadfad

aaskjdgiuagdalidiaudghasugd
ausigtduasgdaksdgasldgbslgdisudgs
ajhdasnhccniuadgasfdgsajasdvasdvasdas
alfdlhasdlasgdjasgdlasdgiyasfdsadasd
akusdiluasdasvdihasidasjldsadas
asgdiuasgdiuavdlavdasdvsdlvsulyd
jhghdjhsgfjhsvfjdsvfjhsvfjvsdfsd
slfgyedgflsdgfilydsgfipgdsipfgdsfgd
sduifiusdgfiulsdgfigsdilfuseteygyewrfwurw
lwuigrywfdlfsdfisegfsdgfs

107
104
2
27
15
10
11
7
33
16

107
104
10
33
21
16
19
17
35
16
'''
