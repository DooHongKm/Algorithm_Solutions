from collections import deque

def solution(players, callings):
    players_dict = {}
    for i in range(len(players)):
        players_dict[players[i]] = i
    for call in callings:
        temp = players_dict[call]
        players_dict[call] -= 1
        players_dict[players[temp-1]] += 1
        players[temp], players[temp-1] = players[temp-1], players[temp]
    return players