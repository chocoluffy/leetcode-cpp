from collections import defaultdict
def evaluateActions(actions):
    loc_map = defaultdict(list)
    support_map = defaultdict(lambda: [[], None, 0]) # [supported, location, if attacked]
    for line in actions:
        data = line.strip().split(" ")
        if len(data) > 3:
            name, location, action, action_arg = data
        else: # hold
            name, location, action = data
        if action == "Hold":
            curr_location = loc_map[location]
            if len(curr_location) > 0:
                support_map[curr_location[0]][2] = -1
                support_map[name][2] = -1 # cannot support others.
            loc_map[location].append(name)
            support_map[name][1] = location
        elif action == "Move":
            curr_location = loc_map[action_arg]
            if len(curr_location) > 0:
                support_map[curr_location[0]][2] = -1
                support_map[name][2] = -1 # cannot support others.
            loc_map[action_arg].append(name)
            support_map[name][1] = action_arg
        elif action == "Support":
            support_map[name][1] = location
            loc_map[location].append(name)
            support_map[action_arg][0].append(name)
    for l, names in loc_map.iteritems():
        score_set = defaultdict(lambda: "")
        print l, names
        for n in names:
            cnt = 1
            curr_support = support_map[n][0]
            for help in curr_support:
                if support_map[help][2] == -1: # no effect
                    continue
                else:
                    cnt += 1
            print n, cnt
            if cnt not in score_set:
                score_set[cnt] = n
            else:
                support_map[n][1] = "[dead]"
                print n, 'and', score_set[cnt]
                support_map[score_set[cnt]][1] = '[dead]'
                score_set[cnt] = n # replace
    print support_map
    print loc_map

actions = [
    "A Munich Support B",
    "B Bohemia Move Prussia",
    "C Prussia Hold",
    "D Warsaw Move Munich"
]
evaluateActions(actions)