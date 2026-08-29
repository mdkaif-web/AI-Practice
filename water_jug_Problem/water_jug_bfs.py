def get_neighbour(state):
    cap_a=4
    cap_b=3
    neighbours=[]
    a,b=state
    amount_a=cap_a - a
    amount_b=cap_b - b
    #Fill A,If a is less than capacity
    if a < cap_a:
        new_state=(cap_a,b)
        neighbours.append(new_state)
    #Fill B,If b is less than capacity
    if b < cap_b:
        new_state=(a,cap_b)
        neighbours.append(new_state)
    #Empty A 
    new_state=(0,b)
    neighbours.append(new_state)

    #Empty B
    new_state=(a,0)
    neighbours.append(new_state)

    # Pour A to B 
    if a > 0 and b < cap_b:
        amount=min(a,amount_b)
        new_state=(a-amount,b + amount)
        neighbours.append(new_state)

    # Pour B to A
    if b > 0 and a < cap_a:
        amount=min(b,amount_a)
        new_state=(a+amount,b - amount)
        neighbours.append(new_state)

    return neighbours

#Display Goal Path:
def display_path(path):
    i=1
    for node in path:
        print(f"Step -> {i}")
        print(node)
        i+=1 
    return


#BFS implementation for searching goal
def bfs(state,goal):
    queue=[state]
    parent={state:None}
    visited=set()
    while queue:
        current=queue.pop(0)
        if current == goal:
            path=[]
            while current:
                path.append(current)
                current=parent[current]
            return path[::-1]
        visited.add(current)
        for neighbour in get_neighbour(current):
            #To stores only unique nodes which are not in visited and also not in queue
            if neighbour not in visited and neighbour not in queue:
                queue.append(neighbour)
                parent[neighbour]=current


goal=(4,2)
path=bfs((0,0),goal)
display_path(path)






    

    
