# creat a maping of states to abbreviation
states = {
    'Wisconsin': 'WI',
    'Illinoise': 'IL',
    'Missouri': 'MO',
    'Minnesota': 'MN',
    'Indiana': 'IN'
}

# creat a basic st of states and family members that live there
members = {
    'WI': 'Opa',
    'IL': 'Dad',
    'MO': 'Mom',
    'MN': 'Katrin',
    'IN': 'Larry'
}

for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

print '.' * 10
for abbrev, member in members.items():
    print "%s lives in %s" % (member, abbrev)

print '.' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and %s lives there" % (
    state, abbrev, members[abbrev])
