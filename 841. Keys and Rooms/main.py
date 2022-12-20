class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms[0]) == 0:
            return False
        s = {0}
        queue = []
        
        for i in rooms[0]:
            if i not in s:
                queue.append(i)
        
        while queue:
            room = queue.pop(0)
            s.add(room)
            for i in rooms[room]:
                if i not in s and i not in queue:
                    queue.append(i)

        if len(s) == len(rooms):
            return True
        return False