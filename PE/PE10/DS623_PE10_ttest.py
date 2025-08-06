
# Course: DS623
# Assignment: PE10 - One-Tailed T-Test from File Input
# Topic: Hypothesis Testing and Confidence Intervals
# Author: Verónica Elze (Assisted by OpenAI)

# Import necessary libraries (use of more libraries than minimal for demonstration)
import numpy as np
from scipy import stats
import pandas as pd
from pathlib import Path

# Task 1: Read input data
def read_input_file(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        confidence_level = float(lines[0].strip())
        data = list(map(float, lines[1:]))
        return confidence_level, np.array(data)
    except Exception as e:
        raise ValueError(f"Error reading file: {e}")

# Task 2: Perform t-test computations
def compute_statistics(confidence_level, data, test_type='greater', popmean=None):
    n = len(data)
    df = n - 1
    sample_mean = np.mean(data)
    sample_std = np.std(data, ddof=1)

    if popmean is None:
        popmean = 0  # For demonstration, we assume testing if mean > 0
        
    # Calculate standard error and t-statistic
    se = sample_std / np.sqrt(n)
    t_stat = (sample_mean - popmean) / se

    # Calculate p-value and critical value based on test type
    if test_type == 'greater':
        p_value = 1 - stats.t.cdf(t_stat, df)
        crit_val = stats.t.ppf(confidence_level, df)
        margin_error = crit_val * se
        ci_lower = sample_mean - margin_error
        ci_upper = float('inf')
    elif test_type == 'less':
        p_value = stats.t.cdf(t_stat, df)
        crit_val = stats.t.ppf(1 - confidence_level, df)
        margin_error = -crit_val * se
        ci_lower = float('-inf')
        ci_upper = sample_mean + margin_error
    else:
        raise ValueError("Unsupported test_type")

    # Return results
    return {
        "Sample Mean": sample_mean,
        "Sample Std Dev": sample_std,
        "Degrees of Freedom": df,
        "T-Statistic": t_stat,
        "P-Value": p_value,
        "Confidence Interval": (ci_lower, ci_upper),
        "Critical Value": crit_val
    }

# Task 3: Load input and run stats on both files
file_paths = {
    "Not Reject": "PE10 input - not reject.txt",
    "Reject": "PE10 input - reject.txt"
}

# Store results in a dictionary
results = {}
for label, path in file_paths.items():
    conf_level, data = read_input_file(path)
    stats_result = compute_statistics(conf_level, data, test_type='greater', popmean=82)
    results[label] = stats_result

# Format for display
df_results = pd.DataFrame(results).T
print(df_results)

# REFERENCE:
# OpenAI. (2025). ChatGPT’s assistance with hypothesis testing in Python for DS623 PE10 [Large language model]. https://openai.com/chatgpt
