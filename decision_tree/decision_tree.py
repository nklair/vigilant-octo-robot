import sys
import math
import copy

from .information_gain import information_gain
from .gain_ratio import gain_ratio
from .delta_gini import delta_gini
from .helpers import get_field_counts

class DecisionTreeNode:
    def __init__(self):
        self.field_number = -1
        self.decision_label = None
        self.children = {}

    def test(self, data):
        if self.decision_label:
            return self.decision_label

        try:
            next_node = self.children[data[self.field_number]]
            return next_node.test(data)
        except:
            return None

def build_tree(data, available_choices, value_function, label_field):
    if len(available_choices) == 0 or all_one_label(data, label_field):
        current_node = DecisionTreeNode()
        current_node.decision_label = get_decision_value(data, label_field)
        return current_node

    # Determine best field
    best_field = -1
    best_field_value = -1
    for field in available_choices:
        value = value_function(data, field, label_field)
        if value > best_field_value:
            best_field = field
            best_field_value = value

    # Split the data along the best field
    new_data = split_data(data, best_field)

    # For each set of data in the new data, recurse
    current_node = DecisionTreeNode()
    current_node.field_number = best_field
    for decision_label in new_data:
        new_dataset = new_data[decision_label]
        current_node.children[decision_label] = build_tree(new_dataset, available_choices - {best_field}, value_function, label_field)

    return current_node

def print_decision(value, level):
    for x in range(level):
        sys.stdout.write('\t')

    sys.stdout.write(str(value) + '\n')
    sys.stdout.flush()

def all_one_label(data, label_field):
    result = None
    for val in data:
        curr_result = val[label_field]
        if result == None:
            result = curr_result
        elif curr_result != result:
            return False
    return True

def get_decision_value(data, label_field_num):
    counts = get_field_counts(data, label_field_num)
    maxCount = -1
    maxLabel = None
    for label in counts:
        if counts[label] > maxCount:
            maxCount = counts[label]
            maxLabel = label
    return maxLabel

def split_data(data, field_num):
    data_dict = {}
    for row in data:
        field_val = row[field_num]
        if field_val not in data_dict:
            data_dict[field_val] = []
        data_dict[field_val].append(row)

    return copy.deepcopy(data_dict)

