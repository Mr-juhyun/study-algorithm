from collections import defaultdict
def solution(genres, plays):
    album = defaultdict(list)
    play_each = defaultdict(int)
    answer = []
    
    for i,gen in enumerate(genres):
        temp = plays[i]
        album[gen].append([temp,i])
        play_each[gen] += temp
        
    play_each = sorted(play_each.items(),key=lambda x:x[1],reverse = True)
    
    for genre,_ in play_each:
        best_song = album[genre]
        best_song.sort(key=lambda x:(x[0],-x[1]))
        
        first = best_song.pop()
        answer.append(first[1])
        
        if best_song:
            second = best_song.pop()
            answer.append(second[1])
            
    return answer

