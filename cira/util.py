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
