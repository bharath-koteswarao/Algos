def rev(province_premier):
    # another dictionary to reversely map items
    rev_mapped = {}
    for province_name in province_premier:
        # Actual logic to reverse
        rev_mapped[province_premier[province_name]] = province_name
    return rev_mapped


# An example of how to use it

province_premier = {
    "hyderabad": "premier1",
    "mumbai": "premier2",
    "chennai": "premier3"
}

print(rev(province_premier))

# Output printed is {'premier1': 'hyderabad', 'premier2': 'mumbai', 'premier3': 'chennai'}