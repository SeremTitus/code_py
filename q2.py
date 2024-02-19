from itertools import permutations

def solution(a,b,c,d):
    output = []
    to_perm = [a, b, c, d]
    perm = permutations(to_perm)
    for item in list(perm):
        if item[0] > 2:
            continue
        if item[0] == 2  and item[1] > 4:
            continue
        if item[1] > 9:
            continue
        if item[2] > 5:
            continue
        if item[3] > 9:
            continue
        clock = str(item[0]) + str(item[1]) + " : " + str(item[2]) + str(item[3])
        if clock not in output:
            output.append(clock)
    
    return output

print(solution(5,7,9,2))
print(solution(1,8,3,2)) # 12:38, 13:28, 18:23, 18:32, 21:38 and 23:18
print(solution(2,3,3,2)) # 22:33, 23:23 and 23:32
print(solution(6,2,4,7)) # []