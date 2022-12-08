# importing the module
import ast

# reading the data from the file
with open('dictionary.txt') as f:
    data = f.read()

print("Data type before reconstruction : ",type(data))

# reconstructing the data as a dictionary
d = ast.literal_eval(data)

print("Data type after reconstruction : ",type(d))
print(d)

visited = []  # List for visited nodes.
queue = []  # Initialize a queue
def bfs(visited,graph,node):  # function for BFS
    visited.append(node)
    queue.append(node)

    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        print(m,end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
print("Following is the Breadth-First Search")
bfs(visited,graph,'5')  # function calling
