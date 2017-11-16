'''
Ugly or Beautiful
You are given an array, , of  non-zero positive integers. The array is said to be beautiful if all the following constraints are satisfied:

The array consists of unique elements.
The array elements are not sorted in ascending order.
All the array elements should have a value between  to  inclusive, i.e., , where, .
If the array is beautiful, print Beautiful; otherwise print Ugly.

For example, array  = [1, 2, 3, 4] is considered Ugly because all elements are sorted in ascending order hence violating the second constraint.

Input Format

The first line of the input is an integer , the total number of queries. Each query consists of two lines. 
The first line of each query contains an integer  denoting the total number of elements in the array and the second line of each query contains  space separated integers describing the array, .

Constraints

, where, 
Output Format

For each query, print Beautiful if the array is beautiful; otherwise print Ugly on a new line.

Sample Input 0

5
4
1 2 3 4
4
1 2 4 3
4
1 1 2 3
4
1 2 6 4
4
4 3 2 1

Sample Output 0

Ugly
Beautiful
Ugly
Ugly
Beautiful
Explanation 0

The array,  does not satisfy the second constraint, so the array is Ugly.
The array,  satisfies all the three constraints, so the array is Beautiful.
The array,  does not satisfy the first constraint, so the array is Ugly.
The array,  does not satisfy the third constraint, so the array is Ugly.
The array,  satisfies all the three constraints, so the array is Beautiful.
'''

NosOfCases = int(input().strip())
for i in range(NosOfCases):
	NosOfElements = int(input().strip())
	elements      = [int(x) for x in input().strip().split()]
	isOk = True
	
	#check for The array consists of unique elements.
	if len(set(elements)) != len(elements):isOk = False
	
	#The array elements are not sorted in ascending order.
	if isOk:		
		if all(elements[i] <= elements[i + 1] for i in range(NosOfElements-1)):
			isOk = False
			
			
		
	#All the array elements should have a value between 1 to  NosOfElements inclusive
	if isOk:		
		tmp = [x for x in elements if x in range(1,NosOfElements+1)]
		isOk = len(tmp) == NosOfElements
		
		
		
	print("Beautifil" if isOk else "Ugly")	
			
		
		
