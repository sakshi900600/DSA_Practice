
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return None

        q = deque()
        dct = {}

        dct[node] =  Node(node.val)
        q.append(node)

        while q:
            curr_node = q.popleft()

            for neigh in curr_node.neighbors:
                if neigh not in dct:
                    dct[neigh] = Node(neigh.val)
                    q.append(neigh)

                dct[curr_node].neighbors.append(dct[neigh])
    
        return dct[node]
        


if __name__ == "__main__":
    # input graph
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    solution = Solution()
    cloned_graph = solution.cloneGraph(node1)

    # Print the cloned graph 
    print("Cloned Graph:")
    print(f"Node: {cloned_graph.val}, Neighbors: {[n.val for n in cloned_graph.neighbors]}")

    # Output:
    # Cloned Graph:
    # Node: 1, Neighbors: [2, 4]
    
