for _ in range(int(input())):
    s = input()
    vowels = sum([1 for x in s if x in 'aeiou'])
    print(vowels, len(s)-vowels)