#!/bin/python3

import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    done = [0,0,0,0]
    more = 0
    
    
    for i in password:        
        if i in numbers:
            done[0] = 1
        if i in lower_case:
            done[1] = 1
        if i in upper_case:
            done[2] = 1
        if i in special_characters:
            done[3] = 1
            
    needed = 4 - sum(done)    
    len_needed = 6 - len(password)
    if len_needed > 0:
        ans = max(needed, len_needed)
    else:
        ans = needed 
    return ans       
            
            
            
        

if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)

