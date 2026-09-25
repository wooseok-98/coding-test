def solution(numbers, hand):
    pos = {
        1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2),
        7: (2,0), 8: (2,1), 9: (2,2), 0: (3,1)    
    }

    left = (3, 0)
    right = (3, 2)
    answer = ''

    for n in numbers:
        if n in (1, 4, 7):
            answer += 'L'
            left = pos[n]
        elif n in (3, 6, 9):
            answer += 'R'
            right = pos[n]
        else:
            r, c = pos[n]
            dl = abs(left[0] - r) + abs(left[1] - c)
            dr = abs(right[0] - r) + abs(right[1] - c)

            if dl < dr:
                use_left = True
            elif dr < dl:
                use_left = False
            else:
                use_left = (hand == 'left')

            if use_left:
                answer += 'L'
                left = pos[n]
            else:
                answer += 'R'
                right = pos[n]

    return answer
