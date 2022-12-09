def reformat_position(position):
    """reformat position to be float values"""
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


def bars_to_dict(bars):
    result = []
    for bar in bars:
        result.append(
            {
                "open": float(bar.open),
                "high": float(bar.high),
                "low": float(bar.low),
                "close": float(bar.close),
                "time": bar.timestamp.strftime("%Y-%m-%d, %H:%M:%S"),
                "time_zone": str(bar.timestamp.tzinfo),
                "volume": float(bar.volume),
            }
        )
    return result


def date_to_days_back(date: str):
    pass
