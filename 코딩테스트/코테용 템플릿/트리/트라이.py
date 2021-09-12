'''
트라이 / Radix tree / Prefix tree 
한 단어의 접두사(접두어)를 모두 저장
(해당 단어에 도달하기까지의 문자들을 저장한다)

사용
검색어 자동완성, 사전에서 찾기 그리고 문자열 검사 등
aa?? 이런 문자가 몇개가 있는지 쿼리날려서 확인하는 경우

예시
donghoon 이라는 단어를 보면,
dong 도 접두사가 될 수 있고, 
do 도 접두사가 될 수 있다. 
트라이에서는 이 단어들이 서로 포함관계에 있다는 것을 알려준다.

설명
단어의 각 글자마다, 
if 존재하지 않으면 새로 만들고
else 존재한다면 그 글자로 들어가는 동작을 수행한다.
단어의 끝에는 끝이라는 표시를 해 둔다. 
트라이의 루트로부터 글자를 따라가다가, 표시가 된 곳을 방문한다면, 
지금까지의 자취가 곧 하나의 단어가 된다.

시간복잡도
M개의 문자열을 트라이 구조에 넣기 (가장 긴 문자열이 L)  : O(M*L)
트라이는 문자열의 길이 N 에 대해서 삽입과 검색을 O(N)에 해낸다.

응용
- ??aa 이렇게 접두사를 모르는 경우의 검색
→ 역순 트라이 생성

- aa??이면서 단어의 길이가 N인 문자 검색
→ 단어 길이마다 트라이 구조 생성
길이3인 트라이 구조
길이4인 트라이 구조
...


'''
class Node(object):
    def __init__(self, key, data=None):
        self.key = key # 해당문자
        self.data = data # 문자열이 끝나는 위치 
        # 끝나는 문자열 없으면 data=None 그대로
        # car가 r에서끝나면 key=r인 노드의data=car입력
        self.children = {} #자식노드

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head
        for char in string:
            # 1) 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            # 2) 같은 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            cur_node = cur_node.children[char]
        # 마지막 문자의 노드 data=해당 문자열 입력
        cur_node.data = string

    # 문자열 존재여부 확인 (True/False 반환)
    def search(self, string):
        # 가장 아래 노드에서 부터 탐색 시작
        cur_node = self.head
        for char in string:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False
        #탐색이 끝난 후 해당 노드의 data값이 존재한다면
        #문자가 포함되어있다는 뜻이다.
        if cur_node.data != None:
            return True

trie_tree = Trie()
trie_tree.insert("123")


'''
??abc, abc?? 이런 것의 개수를 찾아야 하는 경우

검색 키워드는 소문자와 ?(글자하나)

개수를 찾기위해 트라이 생성시 노드 지날때마다 노드에 count+1을 저장.
search() 하다가 ?가 나오면 중단. 이때의 count값이

출력은 queries로 들어온 각각의 검색 키워드들이 매치되는 단어의 수를 배열로 반환
'''
class Node(object):
    def __init__(self, key, data=None):
        self.key = key # 해당문자
        self.count = 0 # 
        self.children = {} #자식노드

class Trie(object):
    def __init__(self):
        self.head = Node(self)

    def insert(self, string):
        cur_node = self.head

        for char in string:
            cur_node.count +=1
            # 1) 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            # 2) 같은 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            cur_node = cur_node.children[char]
        cur_node.count +=1

    # prefix로 시작하는 문자열 개수 확인하기 (return 정수)
    def starts_with(self, prefix, break_string='?'):
        cur_node = self.head
        result = 0
        for char in prefix:
            if char == break_string: # 예를들어 ?를 만나면 중단.
                break
            if char in cur_node.children : 
                cur_node = cur_node.children[char]
            else:
                return 0
        return cur_node.count 


words = []
queries = []

answer = []
tries = {}
reverse_tries = {}

for word in words:
    word_size = len(word)
    if word_size in tries:
        tries[word_size].insert(word)
        reverse_tries[word_size].insert(reversed(word))
    else:
        trie = Trie()
        reverse_trie = Trie()

        trie.insert(word)
        reverse_trie.insert(word)

        tries[word_size] = trie
        reverse_tries[word_size] = reverse_trie

for query in queries:
    query_size = len(query)
    if query_size in tries:
        if query != '?':
            trei = tries[query_size]
            answer.append(trie.starts_with(query))
        else:
            trie = reverse_trie[query_size]
            reverse_trie.append(reverse_trie.starts_with(query))
    else:
        answer.append(0)