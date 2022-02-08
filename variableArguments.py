def avg(*args):
   a = str(float(sum(args)/len(args))).split(".")
   if len(a[1]) > 2:
      a[1] = a[1][:2]
   else:
      a[1] += '0'
   print(a)
   return float('.'.join(a))

print(avg(2, 5))
