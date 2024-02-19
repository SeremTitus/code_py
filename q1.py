# There are N players (numbered from 0 to N−1) participating in a tournament. The K-th player's
# skill level is skills[K]. No two players have the same skill level.
# The tournament is played in rounds for as long as there are at least two players remaining. A
# single round of the tournament consists of one or more matches. In a match, two players
# compete against each other. The loser is eliminated and the winner advances to the next round.
# In the first round player 0 faces player 1, player 2 faces player 3, etc. In the second round the
# winner of the match between player 0 and player 1 faces the winner of the match between
# player 2 and player 3, etc. The player with the higher skill level wins the match.
# For example, for skills = [4, 2, 7, 3, 1, 8, 6, 5], the tournament is as follows (numbers in circles
# are skill levels):
# For each player, find the last round in the tournament in which they participate.
# Write a function:
# struct Results solution(int skills[], int N);
# that, given an array skills of N integers, returns an array results of N integers, where results[K]
# denotes the number of the last round in which the K-th player participates.
# Assume that the following declarations are given:
# struct Results {
# int * results;
# int R; // Length of the array
# };
# Examples:
# 1. Given skills = [4, 2, 7, 3, 1, 8, 6, 5], the function should return [2, 1, 3, 1, 1, 3, 2, 1], as
# described above.
# 2. Given skills = [4, 2, 1, 3], the function should return [2, 1, 1, 2].
# 3. Given skills = [3, 4, 2, 1], the function should return [1, 2, 2, 1].
# Write an efficient algorithm for the following assumptions:
# 1. N is an integer power of 2 within the range [2..262,144];
# 2. each element of array skills is an integer within the range [1..N];
# 3. the elements of skills are all distinct



def solution(skills):
    result = []
    for i in skills:
        result.append(0)
    next_round = skills
    round_count = 0
    while len(next_round) > 2:
        round_count += 1
        for x in range(0, len(next_round), 2):
            print(x)
            if next_round[x] > next_round[x+1]:
                result[skills.index(next_round[x+1])] = round_count
                del next_round[x+1]
            else:
                result[skills.index(next_round[x])] = round_count
                del next_round[x]
    return result

print(solution([4, 2, 7, 3, 1, 8, 6, 5]))
print(solution([4, 2, 1, 3]))
print(solution([3, 4, 2, 1]))