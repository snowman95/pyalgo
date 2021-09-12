'''
유저는 1번에 1명 유저 신고
신고 횟수 제한없음. 계속 다른유저 신고가능 (같은유저는 1번만 신고가능함)

k번 이상 신고되면 정지되고, 유저신고한 사람들한테 메일로 알려줌
※ 정지된 사람도 신고가능함!!

신고처리 메일을 몇번 받았는지 결과를 리턴

1. kill_list  [유저명]:신고된 횟수
2. user_list [유저명]:[신고한 새끼들]
3. mail_list [유저명]:메일통보 횟수

그리고 마지막에
신고된 횟수가 k이상인것들 뽑아서
그 유저들을 신고한새끼들 메일통보 횟수 증가

'''
def solution(id_list, report, k):
    answer = []
    kill_list = dict()
    user_list = dict()
    mail_list = dict()
    for i in id_list:
        user_list[i] = []
        kill_list[i] = 0
        mail_list[i] = 0

    for row in report:
        user, kill_target = row.split()
        new_key = user+kill_target
        if user not in user_list[kill_target]:
            kill_list[kill_target] +=1
            user_list[kill_target].append(user)

    for user in id_list:
        if kill_list[user] >= k:
            for kill_me_target in user_list[user]:
                mail_list[kill_me_target] +=1

    for user in id_list:
        answer.append(mail_list[user])
    return answer

id_list = ["con", "ryan"]#["muzi", "frodo", "apeach", "neo"]
report =["ryan con", "ryan con", "ryan con", "ryan con"]
k =2
solution(id_list, report, k)