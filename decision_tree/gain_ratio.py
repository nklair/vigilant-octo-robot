from .information_gain import information_gain, ig_helper
from .helpers import get_field_counts

def gain_ratio(data, field, label_field):
    intrinsicValue = splitInfo(data, field)
    if intrinsicValue == 0:
        return 0
    return information_gain(data, field, label_field)/splitInfo(data, field)

def splitInfo(data, field):
    result = 0
    field_counts = get_field_counts(data, field)
    for value in field_counts:
        result += ig_helper(field_counts[value], len(data))

    if result == 0:
        print(field_counts)
    return result
