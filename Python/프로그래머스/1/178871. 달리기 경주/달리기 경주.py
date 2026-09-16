def solution(players, callings):
    
    rank = {}
    for i, p in enumerate(players):
        rank[p] = i
        
    for c in callings:
        r = rank[c]
        rank[players[r]] = rank[players[r]] - 1
        rank[players[r-1]] = rank[players[r-1]] + 1
        players[r-1], players[r] = players[r], players[r-1]
        
    return players