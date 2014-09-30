mysum = 0
fibctr1 = 1
fibctr2 = 1

while fibctr2 < 4000000:
  if fibctr2 % 2 == 0:
    mysum += fibctr2
  swap = fibctr2
  fibctr2 += fibctr1
  fibctr1 = swap

print mysum
