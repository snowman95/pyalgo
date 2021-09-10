
'''
오픈채팅방

채팅방에서 닉네임을 변경하는 방법은 다음과 같이 두 가지이다.
1. 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
2. 채팅방에서 닉네임을 변경한다.
닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경된다.

채팅방은 중복 닉네임을 허용
채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때,
모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 하도록 solution 함수를 완성하라.

ㅇㅋ

recode 배열 1~10만 이하


Enter, Change [유저아이디]
Leave [유저아이디] [닉네임]

유저아이디를 dict로 하자
'''
def solution(record):
    answer = []
    history = []
    id_dict = dict()
    for row in record:
        a = row.split()
        command = a[0]
        arg = a[1:]
        if command == "Enter":
            uid, nickname = arg
            id_dict[uid]= nickname
            history.append((uid,True))
        elif command == "Change":
            uid, nickname = arg
            id_dict[uid] = nickname
        else: #Leav
            uid = arg[0]
            history.append((uid,False))

    for uid, option in history:
        if option :
            answer.append(f'''{id_dict[uid]}님이 들어왔습니다.''')
        else : 
            answer.append(f'''{id_dict[uid]}님이 나갔습니다.''')
    return answer

rec = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(rec)