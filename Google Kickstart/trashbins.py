# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887c32
t = int(input())
for T in range(t):
    n = int(input())
    trash = list(input())
    trash = [int(x) for x in trash]
    if(all(trash)):
        print("Case #" + str(T+1) + ": 0")
    else:
        zeros_list, ones_list = [], []
        for i in range(n):
            if trash[i] == 0:
                zeros_list.append(i)
            else:
                ones_list.append(i)
        total_distance = 0
        for zero in zeros_list:
            minimum = 125000250000
            for one in ones_list:
                calc = abs(zero - one)
                if(minimum > calc):
                    minimum = calc
            total_distance += minimum
        print("Case #" + str(T+1) + ": " + str(total_distance))
