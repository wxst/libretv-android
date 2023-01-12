def find_value(db, column, value):
    """ Function to get a row in a data frame
    db: dataframe
    value: value to find
    column: id where value is located

    return: dict
    """

    # Find the item in the df
    db.loc[db[column] == value]
    # Because to_dict return a dict_values cast to list and get the values
    row = list(db.T.to_dict().values())[0]
    return row
