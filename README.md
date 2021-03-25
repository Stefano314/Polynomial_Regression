**Hi There!**

This is a simple code that generates some points from a generic function in a given range and adds them some gaussian random noise. 
Then it performs a polynomial regression over those points (using numpy functions), together with a goodness of fit analysis, using the Pearson Chi Square.
It also plots the fit curve and the empirical P-Value distribution; of course it is necessary to reproduce the p-value generation a sufficiently large number of times (advice: >100 times) in order to have a good p-value distribution.
