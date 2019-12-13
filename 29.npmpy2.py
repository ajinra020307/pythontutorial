import numpy as np

a=np.array([1,2,3,4])
b=np.array([4,4,4,4])
#dot products

dotp=np.sum(a*b)
dotpp=(a*b).sum()
np.dot(a,b)
a.dot(b)
#length of vector
magnitude=np.sqrt((a*a).sum())
mag=np.linalg.norm(a)

#angle between two vectors
cosangle=a.dot(b)/(np.sqrt((a*a)).sum()*np.sqrt(b*b).sum())
actualangleinradians=np.arccos(cosangle)

#matrix representation

m=np.array([[1,2],[2,3]])
M=np.matrix([[1,2],[2,3]])

#converting matrix into an np array
ma=np.array(M)
#transpose of a matrix
T=ma.T
#creating zero vectors and matrix
z=np.zeros(10)  # 1 dimension
Z=np.zeros((10,10)) #2 dimension

o=np.ones(10)
O=np.ones((10,10))

#creating random vectors
r=np.random.random((10,10))

#creating random vectors guassian random numbers

G=np.random.randn(10,10)
#mean of guassian distribution
G.mean()
#variaqnt of guassian distribution
G.var()

#matrix products
aa=np.array([[1,2,5],[7,3,6],[2,4,3]])

#inverse of matrix
aainv=np.linalg.inv(aa)
#a inverse dot a will always gives an identity matrix
aainv.dot(aa)
#determinants of matrix
det=np.linalg.det(aa)
#dialgonal of a matrix
#if we pass a 2d array to diag an 1d array of diagnols is returned
#if we pass a 1d array to diag a two dimwnsional array is returned
dia=np.diag(aa)
np.diag([2,2])

#elementwisw multiplication of matrix
em=np.outer([1,2],[3,4])
#dot product
dd=np.inner([1,3],[4,5])
#sum of diagnols of a matrix
ds=np.diag([1,2]).sum()
ff=np.trace(aa)

#3 dimensional random distribution
d3=np.random.randn(10,3)
#finding covariance of a matrix
#while finding covariance transponse the matrix
np.cov(d3.T)

#solving vectors
v1=np.array([[2,1],[3,2]])
v2=np.array([15,25])

solution=np.linalg.inv(v1).dot(v2)
np.linalg.solve(v1,v2)
print(solution)