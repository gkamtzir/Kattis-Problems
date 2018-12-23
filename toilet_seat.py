data = list(input())

initial_state = data.pop(0)

policies = {
    '1': {
        'score': 0,
        'current_state': initial_state
        },
    '2': {
        'score': 0,
        'current_state': initial_state
        },
    '3': {
        'score': 0,
        'current_state': initial_state
        }
    }

for person in data:
    #Policy 1
    if policies['1']['current_state'] != person:
        policies['1']['current_state'] = person
        policies['1']['score'] += 1
    if person != 'U':
        policies['1']['current_state'] = 'U'
        policies['1']['score'] += 1
    #Policy 2
    if policies['2']['current_state'] != person:
        policies['2']['current_state'] = person
        policies['2']['score'] += 1
    if person != 'D':
        policies['2']['current_state'] = 'D'
        policies['2']['score'] += 1
    #Policy 3
    if policies['3']['current_state'] != person:
        policies['3']['current_state'] = person
        policies['3']['score'] += 1

for policy in policies:
    print(policies[policy]['score'])
