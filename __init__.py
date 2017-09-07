'''
Created on Aug 28, 2012

@author: brian
'''
def exercise1(person, teams):
    results = []
    for team in teams:
        if team.members is not None:
            for member in team.members:
                if member.members is not None:
                    for member2 in member.members:
                        if member2.id == person.id:
                            results.append(team.displayname)
                else:
                    if member.id == person.id:
                        results.append(team.displayname)
    return results

from data1 import *

print(str(exercise1(alice, people)))

from data2 import *
print(str(exercise1(alice, people)))


def getPeople(team, depth):
    results = []
    '''Avoid infitive loops. Depth can not be greater than 2 because for a team we have two more teams to consider'''
    if depth > 2:
        return results
    for member in team.members:
        if member.is_team:
            '''Do not append an empty list'''
            if len(getPeople(member, depth + 1)) > 0:
                results.append(getPeople(member, depth + 1))
        else:
            try:
                results.index(member.displayname)
                pass
            except ValueError:
                results.append(member.displayname)
    return results

from data3 import *
print(str(getPeople(c_team, 0)))
