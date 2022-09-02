def solution(lottos, win_nums):

    unknown_num = lottos.count(0)
    Low_Rank = len( set(lottos) & set(win_nums))
    High_Rank = Low_Rank + unknown_num

    Rank = [6,6,5,4,3,2,1]
    answer = [Rank[High_Rank], Rank[Low_Rank]]
    print(Rank[High_Rank], Rank[Low_Rank])
    return answer
solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])

def solution(lottos, win_nums):

    unknown_num = lottos.count(0)
    Low_Rank = len( set(lottos) & set(win_nums))
    High_Rank = Low_Rank + unknown_num

    Rank = [6,6,5,4,3,2,1]
    answer = [Rank[High_Rank], Rank[Low_Rank]]
    print(Rank[High_Rank], Rank[Low_Rank])
    return answer
solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])

def solution(lottos, win_nums):

    unknown_num = lottos.count(0)
    Low_Rank = len( set(lottos) & set(win_nums))
    High_Rank = Low_Rank + unknown_num

    Rank = [6,6,5,4,3,2,1]
    answer = [Rank[High_Rank], Rank[Low_Rank]]
    print(Rank[High_Rank], Rank[Low_Rank])
    return answer
solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])