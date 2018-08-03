class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = []


    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key not in self.keys:
            self.keys.append(key)



    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key in self.keys:
            self.keys.remove(key)
        return self.keys


    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.keys

'''
Input:
["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]
[[],[1],[2],[1],[3],[2],[2],[2],[2]]
Output:
[null,null,null,true,false,null,true,null,true]
Expected:
[null,null,null,true,false,null,true,null,false]
'''


hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
print(hashSet.contains(1))     #returns true
print(hashSet.contains(3))     #returns false (not found)
hashSet.add(2)
print(hashSet.contains(2))     #returns true
hashSet.remove(2)
print(hashSet.contains(2))     #returns false (already removed)

