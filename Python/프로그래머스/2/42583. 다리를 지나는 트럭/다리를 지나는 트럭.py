from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    bridge_sum = 0
    time = 0
    
    while trucks:
        time += 1
        out = bridge.popleft()
        bridge_sum -= out
        
        if bridge_sum + trucks[0] <= weight:
            t = trucks.popleft()
            bridge.append(t)
            bridge_sum += t
        else:
            bridge.append(0)
    
    return time + bridge_length