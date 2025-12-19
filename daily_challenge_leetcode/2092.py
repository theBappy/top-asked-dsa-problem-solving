
# Using BFS
from collections import defaultdict, deque


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        timeMeetings = defaultdict(list)
        for meeting in meetings:
            person1, person2, time = meeting
            timeMeetings[time].append((person1, person2))

        knowsSecret = [False] * n
        knowsSecret[0] = True
        knowsSecret[firstPerson] = True

        for t in sorted(timeMeetings.keys()):
            meets = timeMeetings[t]

            adj = defaultdict(list)
            que = deque()
            alreadyAdded = set()
            for person1, person2 in meets:
                adj[person1].append(person2)
                adj[person2].append(person1)

                if knowsSecret[person1] and person1 not in alreadyAdded:
                    que.append(person1)
                    alreadyAdded.add(person1)
                if knowsSecret[person2] and person2 not in alreadyAdded:
                    que.append(person2)
                    alreadyAdded.add(person2)

            while que:
                person = que.popleft()
                for nextPerson in adj[person]:
                    if not knowsSecret[nextPerson]:
                        knowsSecret[nextPerson] = True
                        que.append(nextPerson)
        result = [i for i, knows in enumerate(knowsSecret) if knows]
        return result



# Using min-heap
from heapq import heappush, heappop
from collections import defaultdict


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        adj = defaultdict(list)
        for meeting in meetings:
            person1, person2, time = meeting
            adj[person1].append((person2, time))
            adj[person2].append((person1, time))
        pq = []
        heappush(pq, (0, 0))
        heappush(pq, (0, firstPerson))
        visited = [False] * n
        while pq:
            time, person = heappop(pq)
            if visited[person]:
                continue
            visited[person] = True

            for nextPerson, t in adj[person]:
                if t >= time and not visited[nextPerson]:
                    heappush(pq, (t, nextPerson))

        result = [i for i, v in enumerate(visited) if v]
        return result
