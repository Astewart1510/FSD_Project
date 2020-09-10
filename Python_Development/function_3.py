import numpy as np

# set weights
weights = np.array([0.05, 0.15, 0.4, 0.134, 0.189, 0.003, 0.074])
weights_t = np.transpose(weights)

# set betas
betas = np.array([1.05, 0.75, 0.84, 0.9134, 1.189, 1.003, 0.574])
betas_t = np.transpose(betas)

# specific volatility
specVols = np.array([0.05, 0.15, 0.4, 0.134, 0.189, 0.003, 0.074])
specVols_t = np.transpose(specVols)

# create S: a diagonal matrix with specVols as entries
S = np.diag(specVols)

# create D: a diagonal matrix of total asset volatilities
D = np.diag(betas)
D_inverse = np.linalg.inv(D)

# market volatility
mktVol = np.array([1.1])

# Variance <=> Total Volatility
# Calculations

pfBeta = weights_t*betas #Portfolio_Beta

sysCov = betas*betas_t*(mktVol**2) #Systematic_Covariance_Matrix

pfSysVol = weights_t*betas*betas_t*weights*(mktVol**2) #Portfolio_Systematic_Variance

specCov = S**2 #Specific_Covariance_Matrix

pfSpecVol = weights_t*(S**2)*weights #Portfolio_Specific_Variance

totCov = betas*betas_t*(mktVol**2) + S**2 #Total_Covariance_Matrix

pfVol = weights_t*betas*betas_t*weights*(mktVol**2) + weights_t*(S**2)*weights # Portfolio_Variance

CorrMat = D_inverse*(betas*betas_t*mktVol**2 + S**2)*D_inverse #Correlation_Matrix