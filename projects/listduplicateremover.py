list1=[1,2,3,4,3,3,4]

def duplicateRemover(l):
  return list(dict.fromkeys(l))
print(duplicateRemover(list1))