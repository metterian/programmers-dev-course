def solution(seat):
    seat = [str(x)+str(y) for x,y in seat]
    answer = len(set(seat))

    return answer
