import matplotlib.pyplot as plt
from scipy.stats import binom
import numpy as np

# Parameters
n_required = 25              # Number of working channels needed
p_success = 0.89              # Probability that a single channel works
max_redundant_channels = 25  # Maximum number of redundant channels to sweep

# Prepare data
redundant_range = np.arange(0, max_redundant_channels + 1)
total_channels = n_required + redundant_range
yield_probabilities = []

for n_total in total_channels:
    prob = sum(binom.pmf(k, n_total, p_success) for k in range(n_required, n_total + 1))
    yield_probabilities.append(prob)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(redundant_range, yield_probabilities, marker='o')
plt.xlabel("Number of Redundant Channels")
plt.ylabel("Probability of System Success")
plt.grid(True)
plt.tight_layout()

# Save the figure
plt.savefig("yield_vs_redundancy.png", dpi=300)

plt.show()
