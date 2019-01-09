with open('input.txt') as f:
    print(sum([len(line.strip()) - len(eval(line)) for line in f]))
    
with open('input.txt') as f:
    print(sum([line.strip().count('\\') + line.strip().count('"') + 2 for line in f]))    