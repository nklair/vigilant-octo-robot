def get_field_counts(data, field):
    counts = {}
    for row in data:
        value = row[field]
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1

    return counts

# Return the number of rows with the given values in the given fields
def get_2d_count(data, field1, value1, field2, value2):
    count = 0
    for row in data:
        if row[field1] == value1 and row[field2] == value2:
            count += 1
    return count


