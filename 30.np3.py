#child fees=1.5
#adult fees=4

#this day--total people=2200, total fess collected=5050
#1.5C+4A=5050
#C+A=2200

import numpy as np

solution=np.linalg.solve([[1,1],[1.5,4]],[2200,5050])
print(solution)