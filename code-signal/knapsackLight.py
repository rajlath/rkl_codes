from collections import defaultdict

calls = ["/project1/subproject1/method1","/project2/subproject1/method1","/project1/subproject1/method1", "/project1/subproject2/method1", "/project1/subproject1/method2", "/project1/subproject2/method1", "/project2/subproject1/method1", "/project1/subproject2/method1"]

def countAPI(calls):
    projects = defaultdict(list)
    for i in calls:
        _,proj, subs, meths = i.split("/")
        projects[proj][subs].append(meths)

countAPI(calls)
