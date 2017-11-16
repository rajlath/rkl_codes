'''
Input:
2
5 200
600 300 100 350 200
5 890
5123 3300 783 1111 890

Output:
NO
YES
 

Explanation
Example case 1.The first person that Chef asked has a rating of 600, which is more than 200 so he tells Chef to go to his left. The second person Chef meets has a rating of 300, also tells Chef to go to the left. The third person that chef asked has a rating of 100 so he tells Chef to go to the right. Then Chef asked a person with rating 350, that means Chef went beyond the person with rating of 300, which should never happen, so Chef must have made a mistake while writing this sequence.
'''
for _ in range(int(input())):
    noe, rez = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()] 
    leftmax = arr[0]
    invalid = False  
    for i in range(1, noe):
        if arr[i] > rez:
            left = True
            leftmax  = arr[i]
        else:
            right = True
            rightmax = arr[i]     
            
        
        
        
    
                 
                        
                      
                
        
