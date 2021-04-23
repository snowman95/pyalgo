import sys
import itertools
n = int(sys.stdin.readline())
team_ability = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
total_team = set(range(n))
rang = list(range(n))
min_ability_diff = 1e9

for team_a in list(itertools.combinations(rang,n//2)):
    team_b = set(rang).difference(set(team_a))
    ability_diff = 0
    for a in list(itertools.combinations(team_a,2)):
        ability_diff += (team_ability[a[0]][a[1]] + team_ability[a[1]][a[0]])
    for b in list(itertools.combinations(team_b,2)):
        ability_diff -= (team_ability[b[0]][b[1]] + team_ability[b[1]][b[0]])

    min_ability_diff = min(min_ability_diff, abs(ability_diff))
print(min_ability_diff)