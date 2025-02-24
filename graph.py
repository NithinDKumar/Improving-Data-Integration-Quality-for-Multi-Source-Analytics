import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Sample Data Generator
def generate_error_rate_data(n=100):
    np.random.seed(42)
    before_errors = np.random.uniform(10, 30, n)  # Higher error rate before
    after_errors = before_errors * np.random.uniform(0.2, 0.5, n)  # Reduce errors
    return before_errors, after_errors

def generate_completeness_data(rows=10, cols=10):
    np.random.seed(42)
    before_missing = np.random.randint(0, 2, (rows, cols))  # 0: missing, 1: present
    after_missing = before_missing.copy()
    mask = np.random.choice([0, 1], size=(rows, cols), p=[0.3, 0.7])  # Simulate improvement
    after_missing[mask == 1] = 1  # Fill missing data
    return before_missing, after_missing

def generate_confusion_matrix_data():
    np.random.seed(42)
    y_true = np.random.choice([0, 1], size=100, p=[0.6, 0.4])  # Ground truth
    y_pred = y_true.copy()
    
    # Introduce some misclassifications
    flip_idx = np.random.choice(len(y_true), size=15, replace=False)
    y_pred[flip_idx] = 1 - y_pred[flip_idx]
    
    cm = confusion_matrix(y_true, y_pred)
    return cm

# 1. Error Rate Reduction Graph
def plot_error_rate_graph():
    before_errors, after_errors = generate_error_rate_data()
    
    plt.figure(figsize=(10, 5))
    plt.plot(before_errors, label="Before Model", color='red', alpha=0.7)
    plt.plot(after_errors, label="After Model", color='green', alpha=0.7)
    plt.xlabel("Sample Index")
    plt.ylabel("Error Rate (%)")
    plt.title("Error Rate Reduction Before and After Model Integration")
    plt.legend()
    plt.grid()
    plt.show()

# 2. Data Completeness Heatmap
def plot_completeness_heatmap():
    before_missing, after_missing = generate_completeness_data()
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    sns.heatmap(before_missing, cmap="Reds", ax=axes[0], cbar=False)
    axes[0].set_title("Missing Data Before Integration")
    
    sns.heatmap(after_missing, cmap="Greens", ax=axes[1], cbar=False)
    axes[1].set_title("Missing Data After Integration")
    
    plt.suptitle("Data Completeness Improvement")
    plt.show()

# 3. Confusion Matrix
def plot_confusion_matrix():
    cm = generate_confusion_matrix_data()
    
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", xticklabels=["Negative", "Positive"], yticklabels=["Negative", "Positive"])
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.title("Confusion Matrix for Data Validation")
    plt.show()

# Execute visualizations
plot_error_rate_graph()
plot_completeness_heatmap()
plot_confusion_matrix()
