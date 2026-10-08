# most_common()는 내림차순 튜플 리스트 반환
 
from collections import Counter 

def solution(genres, plays):
    answer = []
    
    songs = {}
    count = Counter()
    
    for i, g in enumerate(genres):
        songs.setdefault(g, []).append((i, plays[i]))
        count[g] += plays[i]
        songs[g].sort(key = lambda x: (-x[1], x[0]))

    for g, _ in count.most_common():
        for idx, _ in songs[g][:2]:
            answer.append(idx)
    
    return answer