# most_common()는 내림차순 튜플 리스트 반환
 
from collections import Counter 

def solution(genres, plays):
    answer = []
    
    songs = {}
    count = Counter()
    
    for i, g in enumerate(genres):
        songs.setdefault(g, []).append((plays[i], i))
        count[g] += plays[i]
        songs[g].sort(key = lambda x: (-x[0], x[1]))
    
    print(songs)
    print(count)
    
    for g, _ in count.most_common():
        for _, idx in songs[g][:2]:
            answer.append(idx)
    
    return answer