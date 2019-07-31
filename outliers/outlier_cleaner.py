#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    for x in range(90):
        cleaned_data.append((ages[x], net_worths[x], pow(predictions[x] - net_worths[x], 2)))

    cleaned_data.sort(key=lambda x: x[2], reverse=True)

    del cleaned_data[:9]

    return cleaned_data
