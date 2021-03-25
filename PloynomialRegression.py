#import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import pandas as pd

# Generate a function with noise, then perform a polynomial fit and
# estimate the goodness of fit using the Pearson Test Statistics.
# Of course this works if N>>0 (N~400); the regression
# parameters are obtained by using LSM

def PolyFit(x_range,y_obs,degree,graph=False):
    fit=np.polyfit(x_range,y_obs,degree)
    fit_curve=np.poly1d(fit)
    xp=np.linspace(x.min(),x.max(),x.size)
    if graph == True:
        plt.plot(x,y,'.',xp,fit_curve(xp),'r.')
        plt.show()
    return fit_curve

def P_Value(x_range,y_obs,fit_curve,std):
    y_exp=fit_curve(x)
    chi_val=np.sum(np.square(y_obs-y_exp)/np.square(std))
    ndf=x_range.size-fit_curve.coeffs.size
    p_val=st.chi2.cdf(chi_val,ndf)
    #Probability to get a more extreme result than the one obtained
    #should be uniformly distributed
    return 1-p_val

#std, range and data generation
std=4
degree=3
x = np.arange(-2,2,0.05)
noise=np.random.normal(0,std,x.size)
y_=np.poly1d([4,-3,0,0]) #np.exp(x)+noise
y=y_(x)+noise

#Generate n_exp experiments
n_exp=200
p_vect=[]
for i in range(0,n_exp):
    noise=np.random.normal(0,std,x.size)
    y=y_(x)+noise
    fit=PolyFit(x, y, degree)
    p_vect+=[P_Value(x,y,fit,std)]
    i+=1

#Just draw the plot
fit=PolyFit(x, y, degree, graph=True)

#Draw P-Value distribution (sould be uniform)
PVal_Hist=pd.DataFrame(p_vect)
plot=PVal_Hist.plot.hist(bins=10,alpha=0.8)

print("\np value:", P_Value(x,y,fit,std))

