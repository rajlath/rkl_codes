#s = "http://www.cleartrip.com/signin/service?username=test&pwd=test&12=3&profile=developer&role=ELITE&key=manager"
s = input()
gets=s.split("?")[1]
pos_pwd = gets.find("&pwd")
uname = gets[:pos_pwd]
uname = uname.split("=")
print(uname[0] +": "+uname[1])

pos_profile = gets.find("&profile")
pwd = gets[pos_pwd+1:pos_profile]
pwd = pwd.split("=")

print(pwd[0]+": "+pwd[1:])

pos_role = gets.find("&role")
profile = gets[pos_profile+1:pos_role]
profile = profile.split("=")
if len(profile)>2:
    pro = sum(profile[1:])
print(profile[0] +": "+"".joint(pro))    



pos_key = gets.find("&key")
role = gets[pos_role+1:pos_key]
role = role.split("=")
print(role[0] +": "+ role[1:])

key = gets[pos_key+1:]
key = key.split("=")
print(key[0] + ": "+key[1:])

