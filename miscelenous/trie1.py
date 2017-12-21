contact_dicts = {}
for _ in range(int(input())):
    command, val = [x for x in input().split()]
    if command == "add":
        prefixes = [val[0:i] for i in range(1, len(val)+1)]
        for prefix in prefixes:
            contact_dicts[prefix] = contact_dicts.get(prefix, 0)+1
    if command == "find":
        if val in contact_dicts:
            print(contact_dicts[val])
        else:
            print(0)
