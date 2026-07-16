def check_duplicates(items):
    duplicates = []

    for item in items:
        if items.count(item) > 1 and item not in duplicates:
            duplicates.append(item)

    if duplicates:
        return duplicates
    return "No duplicates"