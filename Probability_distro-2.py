import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, expon, gamma, lognorm, chi2, beta
from scipy.stats import kstest

# Assuming you have already computed and stored 'num_it_1'

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.hist(num_it_2, bins=50, density=True, alpha=0.7, color='skyblue', edgecolor='black', label='Histogram')

# Define candidate distributions
distributions = [
    norm,  # Normal distribution
    expon,  # Exponential distribution
    gamma,  # Gamma distribution
    lognorm,  # Log-normal distribution
    chi2,  # Chi-squared distribution
    beta,  # Beta distribution (you can add more as needed)
]

best_fit_name = ""
best_fit_params = None
best_fit_ks = np.inf

# Fit each distribution and compare KS values
for distribution in distributions:
    # Fit the distribution to the data
    params = distribution.fit(num_it_2)

    # Calculate KS statistic
    ks_statistic, _ = kstest(num_it_2, distribution.cdf, args=params)

    # Update best fit if current distribution has lower KS
    if ks_statistic < best_fit_ks:
        best_fit_name = distribution.name
        best_fit_params = params
        best_fit_ks = ks_statistic

        # Plot the best-fit distribution
        x = np.linspace(min(num_it_2), max(num_it_2), 100)
        y = distribution.pdf(x, *params[:-2], loc=params[-2], scale=params[-1])
        plt.plot(x, y, label=f'{distribution.name} Fit')

# Add labels and legend
plt.title('Histogram and Best-fit Distributions')
plt.xlabel('Values')
plt.ylabel('Probability Density')
plt.legend()

# Print the best-fit distribution and its parameters
print(f"Best-fit distribution: {best_fit_name}")
print(f"Best-fit parameters: {best_fit_params}")
print(f"Kolmogorov-Smirnov (KS) Statistic: {best_fit_ks}")

# Show the plot
plt.show()
