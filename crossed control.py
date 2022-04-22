import json
f = open('list1.json')
list1 = json.load(f)
f = open('list2.json')
list2 = json.load(f)

commonfollowers = []
for i in list1:
    for j in list2:
        if i in j:
            usernames = print(i)
            commonfollowers.append(usernames)

with open('commonlist.json', 'w') as f:
    json.dump(commonfollowers, f)
