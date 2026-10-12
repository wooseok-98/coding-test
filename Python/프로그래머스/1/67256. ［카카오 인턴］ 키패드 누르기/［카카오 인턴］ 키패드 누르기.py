def solution(numbers, hand):
    answer = ""
    pos = {
        1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2),
        7: (2,0), 8: (2,1), 9: (2,2), 0: (3,1)    
    }

    LEFT = (3,0)
    RIGHT = (3,2)
    
    for n in numbers:
        if n in [1, 4, 7]:
            LEFT = pos[n]
            answer += "L"
        elif n in [3, 6, 9]:
            RIGHT = pos[n]
            answer += "R"
        else:
            dl = abs(LEFT[0]-pos[n][0]) + abs(LEFT[1]-pos[n][1])
            dr = abs(RIGHT[0]-pos[n][0]) + abs(RIGHT[1]-pos[n][1])
            if dl < dr:
                LEFT = pos[n]
                answer += "L"
            elif dr < dl:
                RIGHT = pos[n]
                answer += "R"
            else:
                if hand == "left":
                    LEFT = pos[n]
                    answer += "L"
                if hand == "right":
                    RIGHT = pos[n]
                    answer += "R"   
                    
    
    

    return answer
