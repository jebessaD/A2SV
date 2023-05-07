from collections import defaultdict
import sys, threading
def main():
    while True:
        len_nodes = int(input())
        if len_nodes == 0:
            break
        len_edges = int(input())
        graph = defaultdict(list)
        for edge in range(1,len_edges+1):
            start,end = map(int,input().split())
            graph[end].append(start)
            graph[start].append(end)


        visited = set()
        colors = defaultdict()
        ans = "BICOLOURABLE."
        def dfs(parent,color):
            nonlocal ans
            colors[parent] = color
            visited.add(parent)

            for child in graph[parent]:
                if child in colors and colors[child] == color:
                    ans = "NOT BICOLOURABLE."
                if child not in visited:
                    dfs(child, not color)

        
        for i in range(1,len_nodes):
            if i not in visited:
                dfs(i,True)

        print(ans)

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()

