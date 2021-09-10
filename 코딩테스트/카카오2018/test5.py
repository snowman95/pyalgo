'''
길 찾기 게임

이진트리
모든 x 다른값 가지고 자식은 부모보다 y가 작다

nodeinfo : [ 노드좌표(x,y), ... ]
[[전위순회],[후위순회]] 결과 return

일단 이진트리 만들고 순회만 시키면 되는문제
힙으로 y,-x 순서로 넣는다.
y큰순서, x작은 순서 이렇게 나옴
젤 먼저 나오는걸 부모 노드로 박고
그다음 두개를 좌우로 주고

1. 노드번호를 붙여라
2. 
3. tree[노드번호]= { (좌번호, 우번호), ... }

'''
import heapq,sys
sys.setrecursionlimit(100000)
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
