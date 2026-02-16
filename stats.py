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


median_value = statistics.median(data)
min_value = min(data)
max_value = max(data)
count_value = len(data)

print(f"Count: {count_value}")
print(f"Min: {min_value}")
print(f"Max: {max_value}")
print(f"Median: {median_value:.2f}")

range_value = max(data) - min(data)
total_value = sum(data)

print(f"Range: {range_value}")
print(f"Total: {total_value:.2f}")

### now I need to visualize the descriptive statistics 
