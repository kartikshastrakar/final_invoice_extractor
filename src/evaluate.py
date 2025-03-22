from sklearn.metrics import f1_score

def evaluate_extraction(y_true, y_pred):
    """
    Evaluate extraction accuracy using precision.
    """
    if not y_true or not y_pred or len(y_true[0]) != len(y_pred[0]):
        return 0.0  # Return 0 if empty or mismatched

    num_fields = len(y_true[0])
    precisions = []

    for i in range(num_fields):
        # Handle potential index errors if lengths are mismatched
        true_values = [item[i] if i < len(item) else "" for item in y_true]
        pred_values = [item[i] if i < len(item) else "" for item in y_pred]

        # Convert to binary: 1 if correct, 0 if incorrect
        binary_true = [1 if str(true_values[j]) == str(pred_values[j]) else 0 for j in range(len(true_values))]
        binary_pred = [1 for _ in range(len(true_values))]  # All predicted as positive

        # Calculate precision safely
        precision = sum(binary_true) / sum(binary_pred) if sum(binary_pred) != 0 else 0.0
        precisions.append(precision)

    return sum(precisions) / num_fields


def evaluate_summary(ground_truth, summary):
    """
    Evaluate summary quality using F1 score.
    """
    if not ground_truth or not summary:
        return 0.0

    # F1 score to compare summary quality
    f1 = f1_score([ground_truth], [summary], average='weighted')
    return f1
