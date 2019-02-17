def find_anagrams(word, candidates):
    return [x for x in candidates if sorted(x.lower()) == sorted(word.lower()) and x.lower() != word.lower()]


#print(find_anagrams("Orchestra",["cashregister", "carthorse", "radishes"]))