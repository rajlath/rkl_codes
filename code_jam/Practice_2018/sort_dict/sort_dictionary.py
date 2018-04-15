'''
testcases = int(raw_input());
for y in range(1,testcases+1):
	number_of_stations = int(raw_input());
	stations ={};
	for x in range(number_of_stations*2):
		stations[raw_input()] = raw_input()
	for x in stations.keys():
		if x not in stations.values():
			source = x ;
			break;
	print "Case #%s:"%(y),
	while stations.has_key(source):
		print source+"-"+stations[source],
		source = stations[source]
	print ""

Input

Output

2
1
SFO
DFW
4
MIA
ORD
DFW
JFK
SFO
DFW
JFK
MIA

Case #1: SFO-DFW
Case #2: SFO-DFW DFW-JFK JFK-MIA MIA-ORD
'''

in_file = open("C-small-practice.in", "r")
out_file= open("C-small-practice.out","w")
no_test_case = int(in_file.readline().strip())


for case in range(no_test_case):
    station_cnt = int(in_file.readline().strip())
    routes = {}
    for _ in range(station_cnt):
        a, b = in_file.readline().strip(), in_file.readline().strip()
        routes[a] = b
    for key in routes.keys():
        if key not in routes.values():
            start = key
            break
    route = []
    while start in routes:
        route.append("-".join([start, routes[start]]))
        start = routes[start]
    out_file.write("Case #{}: {}".format(case+1," ".join(route)))
    out_file.write("\n")

