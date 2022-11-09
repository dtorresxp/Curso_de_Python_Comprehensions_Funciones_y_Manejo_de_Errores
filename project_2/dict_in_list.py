def dict_in_list(data):
    
    labels = [item['Country/Territory'] for item in data]
    values = [item['World Population Percentage'] for item in data]
    
    return labels, values
