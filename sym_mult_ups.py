import numpy as np

def sym_mult_ups(A, k, alpha = 1, M = 10):
  eps_divide = 1e-6                                                 #define a small number to ensure we never divide by 0
  n,n = np.shape(A)                                                 #determine the size of X for initializing A and S
  
  if M < 1:
    raise Exception("Not a valid number of iterations.")            #error if number of iterations is less than 1
  if alpha < 0:
    raise Exception("Not a valid alpha hyperparameter.")
    
  W = np.abs(np.random.randn(n,k))                                  #initialize factor matrices
  H = np.transpose(np.abs(np.random.randn(k,n)))
  
  errors = [np.linalg.norm(A-H@np.transpose(H),'fro')**2]           #initialize error array
  
  for i in range(M):
    Abar = np.vstack((A,np.sqrt(alpha)*np.transpose(W)))
    Wbar = np.vstack((W,np.sqrt(alpha)*np.eye(k)))

    H = np.transpose(np.transpose(H)*((np.transpose(Wbar)@Abar)/(np.transpose(Wbar)@Wbar@np.transpose(H) + eps_divide)))
                                                                    #update for H        
    W = H                                                           #update W        
    
    errors.append(np.linalg.norm(A-H@np.transpose(H),'fro')**2)     #record error
  
  return H, errors
