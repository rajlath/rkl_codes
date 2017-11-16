'''
SAMPLE INPUT 
3
5 1
jhoolz littleboy cooldude findingathar findingnemo
3 1
bawa chunnu kundan
3 2
kaddu babykaddu littlejhool
SAMPLE OUTPUT 
cooldude
bawa
kaddu babykaddu

10
1 1
almnsvy
10 4
bcgikklnpsvz bccdhiijkklmpprrtt iillpxz bdgnr bccfggikkkllmmpqstuvwwxyz adefggghkllmpqttuvyz afgmottz aaaaacdeghijklmmquyy agjkorswx egjklpssxy
10 6
hwyz dfggkknnooqstuuvxyy befgghiijkkkppuz acddghhijjlmmnoooqtuuvwwwy aabbbdefjnnoooqrsuvvvyz abbffgiknnopvw abfggjlmnnooprstuuuv i bijnnoqqtuvwxy eilmpuvx
9 7
aeimqsvyy abcchkoootz cdgiimoqrrrtuvwx aabbcdegijkmmmprttvwxxxx aaddefhhmmnnopqrvvvwxyy ddehimssvwwyz ccgikmnnpqqsxz acciimmnooqrrrww bbccefhhijjlmnrrs
5 1
abcdeghhiiijjjklnosuwwxxy cdeefijkort efhijjllnpsssstuuwx dffglnnoopuuvx aaccfgijjkppvwxy
5 1
h bcddegghhikoouvvz bcefghhikllnnnoppppqrruz bghjjloqrruvwwx aabcdghiiijjkmqtuuuw
1 1
aabkkklmmnnooopqrrtwz
3 1
aadehijklnnnoqqrsuxz dgikqrstuvz abdffggiijnoopqv
1 1
bcfgghijlnnpprstvvwxz
10 8
ddfhhiiijjkmmnoopprsuxyyzz acccefghhllmnopwwwxz dhhkmmoopsstwyyyy abbceeegiimnnopqsuvwwyyz abbfggjjkmnnnosuvxyz hrt aacfggjllqtvxx bbcdhiinoopqstuvvxz bbccdiklmmppqqrttuxxz aehhhoortvvwxxy

#myoutput
almnsvy 
bdgnr hwyz i ccgikmnnpqqsxz dffglnnoopuuvx 
h 
aabkkklmmnnooopqrrtwz 
dgikqrstuvz 
bcfgghijlnnpprstvvwxz 
abbfggjjkmnnnosuvxyz hrt 

#correct output
almnsvy
bdgnr bcgikklnpsvz iillpxz afgmottz
hwyz i dfggkknnooqstuuvxyy abbffgiknnopvw aabbbdefjnnoooqrsuvvvyz eilmpuvx
ccgikmnnpqqsxz aeimqsvyy acciimmnooqrrrww abcchkoootz cdgiimoqrrrtuvwx aaddefhhmmnnopqrvvvwxyy ddehimssvwwyz
dffglnnoopuuvx
h
aabkkklmmnnooopqrrtwz
dgikqrstuvz
bcfgghijlnnpprstvvwxz
abbfggjjkmnnnosuvxyz hrt dhhkmmoopsstwyyyy abbceeegiimnnopqsuvwwyyz aacfggjllqtvxx bbccdiklmmppqqrttuxxz ddfhhiiijjkmmnoopprsuxyyzz acccefghhllmnopwwwxz
'''
from collections import OrderedDict, defaultdict
import operator

for _ in range(int(input())):
    me = set("littlejhool")  
    n, k = [int(x) for x in input().split()]
    crush = [x for x in input().split()]
    ans = {}
    
    for i in crush:
        temp = set(i)
        temp2 = temp & me
        ans[i] = temp2
    finalans = sorted(ans.items(), key=operator.itemgetter(1))
    for i in range(k):
        if i == k - 1:
            print(finalans[i][0])
        else:
            print(finalans[i][0],end=" ")

                
                        
            
    
    
        
