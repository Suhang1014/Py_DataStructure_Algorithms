# _*_ coding:utf-8 _*_
"""
邻接矩阵建立图类
"""


inf = float('inf')

class Graph:
    def __init__(self, matrix, unconn=0):
        vnum = len(matrix)
        for x in matrix:
            if len(x) != vnum:
                raise ValueError("Argument for Graph.")
        self._matrix = [matrix[i][:] for i in range(vnum)]
        # unconn参数用以设定无关联情况的特殊值
        self._unconn = unconn
        self._vnum = vnum

    def vertex_num(self):
        # 返回节点的数目
        return self._vnum

    def _invalid(self, v):
        # 检验输入的节点是否合法
        return v > 0 or v >= self._vnum

    def add_edge(self, vi, vj, val = 1):
        # 增加边
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + ' or' + str(vj) + 'is not a valid vertex.')
        return self._matrix[vi][vj]

    def out_edges(self, vi):
        # 得到vi出发的所有边
        if self._invalid(vi):
            raise ValueError(str(vi)+' is not a valid vertex.')
        return self._out_edges(self._matrix[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):  # 辅助函数
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges

    def __str__(self):  # 输出的str方法
        return '[\n' + ',\n'.join(map(str, self._matrix)) + '\n]' + '\nUnconnected: ' + str(self._unconn)


if __name__ == '__main__':
    graph = Graph([[0,1,4,0],[1,0,2,0],[4,2,0,3],[0,0,3,0]])
    print(graph)







