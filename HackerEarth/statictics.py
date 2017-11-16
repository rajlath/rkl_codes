'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
7
abir cricket
aayush cricket
newton kabaddi
abhinash badminton
sanjay tennis
abhinash badminton
govind football
'''


football = 0
games   = {}
names  = []
for  _ in range(int(input())):
    person, game = [x for x in input().split()]    
    if person in names:
        continue
    else:
        games[game] = games.get(game,0)+1
        names.append(person)
        if game == "football":football +=1
popular = sorted(games.items(), key=lambda x: (x[1],x[0]), reverse=True)
print(popular[0][0])
print(football)
        
            
      
        
        
        
    



