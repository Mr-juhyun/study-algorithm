def solution(players, callings):
    run = {player:i for i,player in enumerate(players)}
    for call in callings:
        idx = run[call]
        players[idx-1],players[idx] = players[idx],players[idx-1]
        run[players[idx]] = idx
        run[players[idx - 1]] = idx - 1
    return players
    
        