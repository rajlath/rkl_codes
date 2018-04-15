d,p={"G":"C","C":"G","T":"A","A":"U"},print
try:p("".join(d[x] for x in input()))
except:p("Invalid Input")