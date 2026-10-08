from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    time = 0
    trucks = deque(truck_weights)
    bridge_weight = 0
    
    while trucks:
        time += 1
        out = bridge.popleft()
        bridge_weight -= out
        
        if bridge_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            bridge_weight += truck
        else:
            bridge.append(0)
            
    return time + bridge_length
            
            
    