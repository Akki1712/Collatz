import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, expon, gamma, lognorm, chi2
from scipy.optimize import curve_fit


# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(num_it_2, bins=50, density=True, alpha=0.7, color='skyblue', edgecolor='black', label='Histogram')

# Fit a normal distribution
mu, std = norm.fit(num_it_1)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2, label=f'Normal Fit: $\mu={mu:.2f}$, $\sigma={std:.2f}$')

# Fit an exponential distribution
param_exp, _ = curve_fit(lambda t, l: expon.pdf(t, scale=1/l), number_list, num_it_2)
plt.plot(x, expon.pdf(x, scale=1/param_exp[0]), 'r--', label=f'Exponential Fit: $\lambda={param_exp[0]:.2f}$')

# Fit a gamma distribution with initial parameter guess
param_gamma_guess = [2, 0, 1]  # Initial guess for parameters (a, loc, scale)
param_gamma, _ = curve_fit(gamma.pdf, number_list, num_it_2, p0=param_gamma_guess)
plt.plot(x, gamma.pdf(x, *param_gamma), 'g--', label=f'Gamma Fit: $a={param_gamma[0]:.2f}$, $loc={param_gamma[1]:.2f}$, $scale={param_gamma[2]:.2f}$')

# Fit a log-normal distribution with initial parameter guess
param_lognorm_guess = [0.8, 0, 1]  # Initial guess for parameters (s, loc, scale)
param_lognorm, _ = curve_fit(lognorm.pdf, number_list, num_it_2, p0=param_lognorm_guess)
plt.plot(x, lognorm.pdf(x, *param_lognorm), 'm--', label=f'Log-Normal Fit: $\sigma={param_lognorm[0]:.2f}$, $\mu={param_lognorm[1]:.2f}$, $scale={param_lognorm[2]:.2f}$')

# Fit a chi-squared distribution with initial parameter guess
param_chi2_guess = [3, 0, 1]  # Initial guess for parameters (df, loc, scale)
param_chi2, _ = curve_fit(chi2.pdf, number_list, num_it_2, p0=param_chi2_guess)
plt.plot(x, chi2.pdf(x, *param_chi2), 'b--', label=f'Chi-Squared Fit: $df={param_chi2[0]:.2f}$, $loc={param_chi2[1]:.2f}$, $scale={param_chi2[2]:.2f}$')

plt.title('Histogram and Probability Distribution Fits')
plt.xlabel('Sequence Length')
plt.ylabel('Probability Density')
plt.legend()
plt.show()
