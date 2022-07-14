import operator
votes= ["john","johnny","jackie","johnny","john" 
"jackie","jamie","jamie","john","johnny","jamie",
"johnny","john"]

def winner(votes):
    map = dict()
    for s in votes:
        if s in map.keys():
            map[s] += 1
        else:
            map[s] = 1
            
    return map

w = winner(votes)
print(w)