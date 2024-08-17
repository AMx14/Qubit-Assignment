def filter_data(data):
    filtered_data = {k: v for k, v in data.items() if 'affiliatedOrganizations' not in k and 'locations' not in k and 'similarOrganizations' not in k}
    return filtered_data
