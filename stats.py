import random
import statistics

# Generate random dataset
data = [random.randint(10, 100) for _ in range(20)]

# Calculate statistics
mean_value = statistics.mean(data)
variance_value = statistics.variance(data)
std_dev_value = statistics.stdev(data)

# Display results
print("Random Dataset:")
print(data)

print("\nDescriptive Statistics:")
print(f"Mean: {mean_value:.2f}")
print(f"Variance: {variance_value:.2f}")
print(f"Standard Deviation: {std_dev_value:.2f}")
