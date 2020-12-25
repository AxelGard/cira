def reformat_position(position):
    """ reformat position to be float values """
    raw_position = vars(position)["_raw"]
    position_dict = {}
    for key in raw_position.keys():
        try:
            position_dict[key] = float(raw_position[key])
        except ValueError:
            continue
    return position_dict
