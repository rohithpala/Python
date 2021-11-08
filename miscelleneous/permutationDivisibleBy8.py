def permute(data, i, length):
    if i == length:
        if int(''.join(data)) % 8 == 0:
            return 'YES'
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]

def checkDivisibility(arr):
    result = []
    for num in arr:
         if int(num) % 8 == 0:
              result.append('YES')
         elif permute(list(num), 0, len(num)) == 'YES':
              result.append('YES')
         else:
              result.append('NO')
    return result

if __name__ == '__main__':
     print(checkDivisibility(['61', '75']))