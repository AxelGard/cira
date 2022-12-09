from ..assets.asset import Asset


class Position:
    def __init__(self, alpc_position=None) -> None:
        self._alpc_position = alpc_position
        self._asset = None
        self._is_closed = True
        self.symbol: str = self._alpc_position.symbol
        self.quantity: int = int(self._alpc_position.qty)

    def asset(self) -> Asset:
        from ..assets.utils import cast_asset_class

        return cast_asset_class(self._alpc_position.assasset_class, self.symbol)

    def is_closed(self) -> bool:
        """returns if a position has been closed"""
        return self._is_closed

    def close(self) -> None:
        """close the position"""
        pass

    def to_dict(self) -> dict:
        """returns a dict with the atr of the position"""
        return {
            "asset": self._asset,
            "is_closed": self.is_closed(),
            "quantity": self.quantity,
        }
