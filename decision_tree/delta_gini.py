import math
from .helpers import get_field_counts, get_2d_count

def delta_gini(data, field, label_field):
    label_counts = get_field_counts(data, label_field)
    gini = 1
    for label in label_counts:
        gini += dg_helper(label_counts[label], len(data))

    # Compute the conditional probability
    conditional_prob = 0
    field_counts = get_field_counts(data, field)
    for field_value in field_counts:
        field_count = field_counts[field_value]
        total_count = len(data)
        temp_prob = 1
        for label in label_counts:
            temp_prob += dg_helper(get_2d_count(data, field, field_value, label_field, label), field_count)

        conditional_prob += ((field_count/total_count) * temp_prob)

    return gini - conditional_prob

def dg_helper(numerator, total):
    if numerator == 0:
        return 0
    return (-1 * math.pow(numerator/total, 2))


