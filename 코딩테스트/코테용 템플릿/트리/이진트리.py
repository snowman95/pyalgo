'''
아래 예시는 
1~n 노드가 순서대로 좌표위치(x,y)가 주어졌을때
→ [(x,y)..] 

y가 크고, x가 작은 순서로 우선순위큐에서 빼서 이진트리 생성 (idx는 노드번호)
heapq.heappush(q, (-y,x, idx))

x위치가 작은 것이 트리 왼쪽으로 가도록 만든 거임.

'''
import heapq,sys
sys.setrecursionlimit(100000) # 런타임 에러 뜨면 재귀 값 늘려주도록
preodrer_list = []
postorder_list = []

class Node(object):
    def __init__(self, x, idx):
        self.idx = idx
        self.x = x
        self.left = self.right = None

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, x, idx):
        self.root = self._insert_value(self.root, x, idx)
        return self.root is not None

    def _insert_value(self, new_node, x,idx):
        if new_node is None:
            new_node = Node(x, idx)
        else:
            if x <= new_node.x:
                new_node.left = self._insert_value(new_node.left, x, idx)
            else:
                new_node.right = self._insert_value(new_node.right, x, idx)
        return new_node

    def preorder(self, child_node):
        if child_node != None:
            preodrer_list.append(child_node.idx)
            if child_node.left:
                self.preorder(child_node.left)
            if child_node.right:
                self.preorder(child_node.right)

    def postorder(self, child_node):
        if child_node != None:
            if child_node.left:
                self.postorder(child_node.left)
            if child_node.right:
                self.postorder(child_node.right)
            postorder_list.append(child_node.idx)

def solution(nodeinfo):
    answer = []
    bst = Tree()
    idx = 1
    root = 0
    q = []
    for x,y in nodeinfo:
        heapq.heappush(q, (-y,x, idx))
        idx+=1
    
    while q:
        y,x,idx = heapq.heappop(q)
        bst.insert(x, idx)

    bst.preorder(bst.root)
    bst.postorder(bst.root)
    answer.append(preodrer_list)
    answer.append(postorder_list)
    print(answer)
    return answer


nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
solution(nodeinfo)