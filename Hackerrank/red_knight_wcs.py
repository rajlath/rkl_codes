class graph(object):
    '''
    unweighted directed graph
     _vmap  and _vprev is an empty python dict
    all vertex are represented by a simple index
    '''
    def __init__(self):
        '''
        vamp will have adj.list of x
        vrev will have adj.list of previous x
        '''
        self._vmap = {}
        self._vprev= {}

    def add_edge(self, start, end):
        '''
        add an edge to the graph
        '''
        if start in self._vmap:
            self._vmap[start].append(end)
        else:
            self._vmap[start] = [end]

    def bfs_shortest(self, start):
        '''
        bfs implementation of shortest path algo
        '''
        queue = [start]
        self._vprev[start] = None
        while len(queue) != 0:
            v = queue[0]
            queue.pop(0)
            if v in self._vmap:
                v_adj = self._vmap[v]
            else:
                continue
            for nextv in v_adj:
                if nextv in self._vprev:
                    '''
                    # and self._vprev[nextv] is not None:
                    # nextv has already found its parent
                    '''
                    continue
                else:
                    queue.append(nextv)
                    self._vprev[nextv] = v

    def get_path(self, end):
        '''
        return shortest path as python list
        '''
        v = end
        path = []
        while v in self._vprev and self._vprev[v] is not None:
            path.insert(0, v)
            v = self._vprev[v]

        if  self._vprev[v] is not None and v in self._vprev:
            path.insert(0, v)

        else:
            print("Destination %d does not exist or unreachable" % (v))

        return path

class chessboard(object):
    '''
    a chessboard of size n * n
    '''
    def __init__(self, n):
        '''
        respresent chessboard in a graph
        arguments:
        n int size of the board
        '''
        self._size = n
        self._board = graph()
        '''
        offset based on priority mentioned
        '''
        next_point = ((-2, 1), (-2, -1), (0, 2), (2, 1), (2, -1), (0, -2))
        directions = ( "UL", "UR", "R", "LR", "LL", "L" )
        for x in range(n):
            for y in range(n):
                start = self.point_to_index(x, y)
                for dx, dy in next_point:
                    nx = x + dx
                    ny = y + dy
                    if self.is_valid(nx, ny):
                        end = self.point_to_index(nx, ny)
                        self._board.add_edge(start, end)

    def is_valid(self, x, y):
        '''
        check if x, y coordinates are within board boundry
        '''
        return 0 <= x < self._size and 0 <= y < self._size

    def point_to_index(self, x, y):
        '''
        map a chessboard cell to graph vertex index
        '''
        return x * self._size + y

    def index_to_point(self, p):
        return (p // self._size, p % self._size)

    def solve_knight(self, st_x, st_y, en_x, en_y):
        '''
        solve function
        '''
        start = self.point_to_index(st_x, st_y)
        end   = self.point_to_index(en_x, en_y)

        self._board.bfs_shortest(start)
        path = [self.index_to_point(x) for x in self._board.get_path(end)]
        last = (st_x, st_y)
        pth  = []
        next_point = ((-2, 1), (-2, -1), (0, 2), (2, 1), (2, -1), (0, -2))
        directions = ( "UL", "UR", "R", "LR", "LL", "L" )
        for x, y in path:
            print(x, y, last[0], last[1])
            visit = (x - last[0], y - last[1])
            print(visit)
            last = (x, y)
            pth.append(directions[next_point.index(visit)])

        # return [(x , y ) for x, y in path]
        return " ".join(pth)





n = int(input())
se=[int(x) for x in input().split()]
chess = chessboard(n)
print(chess.solve_knight(se[0], se[1], se[2], se[3]))


