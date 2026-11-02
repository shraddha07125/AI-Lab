from collections import deque 
n=int(input("Enter number of disks: ")) 
start=(tuple(range(n, 0, -1)), (), ()) 
goal=((), (), tuple(range(n, 0, -1))) 
queue=deque([(start, [])]) 
visited={start} 
while queue:     
    state, path=queue.popleft()     
    if state==goal:    
        for step in path+[state]:            
            print(step)        
        break    
    for i in range(3):        
        if state[i]:             
            disk=state[i][-1]          
            for j in range(3):               
                if i!=j and (not state[j] or state[j][-1]>disk):      
                    new_state=[list(rod) for rod in state]                
                    new_state[i].pop()          
                    new_state[j].append(disk)              
                    new_state=tuple(tuple(rod) for rod in new_state)              
                    if new_state not in visited:            
                        visited.add(new_state)                     
                        queue.append((new_state, path+[state])) 
