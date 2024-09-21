class BestAlbum:
    def __init__(self,play,num):
        self.play = play
        self.num = num

    def __lt__(self,other):
        if self.play == other.play:
            return self.num > other.num
        return self.play < other.play
    
from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_playtime = {}
    album = defaultdict(list)
    
    for idx,gen in enumerate(genres):
        genre_playtime[gen] = genre_playtime.get(gen,0) + plays[idx]
        album[gen].append(BestAlbum(plays[idx],idx))
    
    genres = sorted(genre_playtime.items(),key=lambda x:-x[1])
    
    for gen,_ in genres:
        song = album[gen]
        song.sort()
        answer.append(song.pop().num)
        if song:
            answer.append(song.pop().num)
    return answer

