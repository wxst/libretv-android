def find_value(db, column, value):
    """ Function to get a row in a data frame
    db: dataframe
    value: value to find
    column: id where value is located

    return: dict
    """

    # Find the item in the df
    db = db.loc[db[column] == value]
    # Because to_dict return a dict_values cast to list and get the values
    indexes = db.index
    values = list(db.T.to_dict().values())
    if len(values) > 0:
        value = values[0]
        value["indexes"] = indexes
        return value
    return None
