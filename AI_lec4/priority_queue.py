from queue import PriorityQueue

pq1 =  PriorityQueue()

pq1.put((0,'a'))
pq1.put((5, 'b'))
pq1.put((3, 'c'))

while not pq1.empty():
    priority, element = pq1.get()
    print(element)
