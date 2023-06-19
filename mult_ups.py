import numpy as np

def mult_ups(X, k, M = 10):
  eps_divide = 1e-6                                                 #define a small number to ensure we never divide by 0
  m,N = np.shape(X)                                                 #determine the size of X for initializing A and S
  
  if M < 1:
    raise Exception("Not a valid number of iterations.")            #error if number of iterations is less than 1
    
  A = np.abs(np.random.randn(m,k))                                  #initialize factor matrices
  S = np.abs(np.random.randn(k,N))
  
  errors = [np.linalg.norm(X-A@S,'fro')**2]                          #initialize error array
  
  for i in range(M):
    A = A*((X@np.transpose(S))/(A@S@np.transpose(S) + eps_divide))  #update for A
    S = S*((np.transpose(A)@X)/(np.transpose(A)@A@S + eps_divide))  #update for S
    
    errors.append(np.linalg.norm(X-A@S,'fro')**2)                    #record error
  
  return A, S, errors
