def func(list):
    i=0
    while i<len(list)-1:
      if list[i]==list[i+1]:
        return True
      i+=1
    return False
print(func(list="hello"))
