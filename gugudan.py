for x in range(2,10):
  print("#  %d단  #"%(x), end=' ')
print()
for i in range(1, 10):
    for j in range(2, 10):
        print("%dX %2d= %2d"%(j,i,i*j),end=' ')
    print()