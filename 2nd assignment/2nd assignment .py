import json

with open('ex5.json','r') as file:
    ex5=json.load(file)
    file.close()

for x in ex5:
    if x['type'] == "donut" and x['name'] == 'Old Fashioned':
        z=x['batters']['batter']
        
        z.append({'id': '1003', 'type': 'Coffee'})
        

with open('ex5.json','w') as file:
    json.dump(ex5,file,indent=4)
    file.close()