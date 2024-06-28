def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph[from_member]['following']:
        if from_member in social_graph[to_member]['following']:
            return "friends"
        else:
            return "follower"
    elif from_member in social_graph[to_member]['following']:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != "_":
            return row[0]
    for i in range(len(board)):
        column = [row[i] for row in board]
        if len(set(column)) == 1 and column[0] != "_":
            return column[0]
    diag1 = [board[i][i] for i in range(len(board))]
    diag2 = [board[i][len(board) - 1 - i] for i in range(len(board))]
    if len(set(diag1)) == 1 and diag1[0] != "_":
        return diag1[0]
    if len(set(diag2)) == 1 and diag2[0] != "_":
        return diag2[0]
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    if not isinstance(route_map, dict):
        raise TypeError("Route map should be a dictionary.")
    
    if (first_stop, second_stop) not in route_map.keys():
        raise ValueError("This is wrong")
    
    current_stop = first_stop
    accumulated_travel_time = 0

    route_map = {
    ('Stop1', 'Stop2'): 10,
    ('Stop2', 'Stop3'): 15,
    ('Stop3', 'Stop1'): 20
}
    while True:
        for stops, data in route_map.items():
            start, end = stops

            if current_stop == start:
                accumulated_travel_time += data.get("travel_time_mins", 0)
                current_stop = end

                if current_stop == second_stop:
                    return accumulated_travel_time