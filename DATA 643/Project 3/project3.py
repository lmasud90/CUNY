from recommender import generate_predictions 
from numpy import *

num_movies = 4
num_users = 4

predictions = matrix(generate_predictions (num_users, num_movies))

#make two of the rows linearly dependent on two other rows
predictions[0] = predictions[1] + predictions[2]
predictions[-1] = predictions[1]

V, Sigma, Ustar = linalg.svd(predictions)

V = matrix(V)
Ustar = matrix(Ustar)

SigmaDag = zeros((num_movies, num_users))
SigmaDag[[0,1], [0,1]] = 1/Sigma[:2]

S = count_nonzero(SigmaDag)

Sig = mat(eye(S)*Sigma[:S])

new_predictions = V[:,:S]

print new_predictions