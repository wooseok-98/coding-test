def solution(players, callings):
    
    rank = {}
    
    for i, p in enumerate(players):
        rank[p] = rank.get(p, i+1)
        
    for c in callings:
        i = rank[c] - 1
        rank[players[i]] = rank.get(players[i]) - 1
        rank[players[i-1]] = rank.get(players[i]) + 1
        players[i-1], players[i] = players[i], players[i-1]

    return players