def solution(participant, completion):
    players = {}

    for person in participant:
        if person in players:
            players[person] += 1
        else:
            players[person] = 1

    for person in completion:
        if person in players:
            players[person] -= 1

    for key, value in players.items():
        if value == 1:
            return key

    return participant[-1]

# participant 참여한 선수의 이름
# completion 완주한 선수 이름
# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤 완주.