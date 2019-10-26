from pathlib import Path

p=Path('../../Desktop')
print(p.exists()) 

#return true or false based on the result
#making a dir

#p1=Path('dd')
#p1.mkdir()

#deleting a dir

p2=Path('dd')
p2.rmdir()

#searching for a file or multiple file
p3=Path()

#p3.glob(*.py) returns a generater object we can itterate

for file in p3.glob('*.py'):
    print(file)
    
