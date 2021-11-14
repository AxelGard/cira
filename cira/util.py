def reformat_position(position):
    """ reformat position to be float values """
    raw_position = vars(position)["_raw"]
    position_dict = {}
    for key, value in raw_position.items():
        try:
            if isinstance(value, str):
                if "." in value:
                    position_dict[key] = float(value)
                else:
                    position_dict[key] = int(value)
        except ValueError:
            continue
    return position_dict
