# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887c32
t = int(input())
for T in range(t):
    n = int(input())
    trash = list(input())
    trash = [int(x) for x in trash]
    if(all(trash)):
        print("Case #" + str(T+1) + ": 0")
    else:
        enum = enumerate(trash)
        zeros_list = [i for i, n in enum if n == 0]
        enum = enumerate(trash)
        ones_list = [i for i, n in enum if n == 1]
        total_distance = 0
        for zero in zeros_list:
            minimum = 500000
            for one in ones_list:
                calc = abs(zero - one)
                if(minimum > calc):
                    minimum = calc
            total_distance += minimum
        print("Case #" + str(T+1) + ": " + str(total_distance))
