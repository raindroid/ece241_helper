class LogicSignal(object):

    """
        default signal is 0
        >>> t = LogicSignal()
        >>> t.get_signal()
        0
    """

    def __init__(self, sig: int = 0):
        if sig != 1 and sig != 0:
            raise Exception("Error Signal!")
        self.__sig = sig

    def __str__(self):
        return str(self.__sig)

    def __repr__(self):
        return str(self.__sig)

    def get_signal(self) -> int:
        return self.__sig

    def __mul__(self, other):
        """
            AND operation
            >>> t1 = LogicSignal(1)
            >>> t2 = LogicSignal(1)
            >>> (t1 + t2).get_signal()
            1
        """
        if not isinstance(other, LogicSignal):
            raise Exception("Type Error!")
        t = 1 if self.__sig == 1 and other.__sig == 1 else 0
        ans = LogicSignal(t)
        return ans

    def __and__(self, other):
        """
            AND operation
            >>> t1 = LogicSignal()
            >>> t2 = LogicSignal(1)
            >>> (t1 & t2).get_signal()
            0
        """
        return self.__mul__(other)

    def __add__(self, other):
        """
            OR operation
            >>> t1 = LogicSignal(1)
            >>> t2 = LogicSignal(0)
            >>> (t1 * t2).get_signal()
            1
        """
        if not isinstance(other, LogicSignal):
            raise Exception("Type Error!")
        t = 1 if self.__sig == 1 or other.__sig == 1 else 0
        ans = LogicSignal(t)
        return ans

    def __or__(self, other):
        """
            OR operation
            >>> t1 = LogicSignal(1)
            >>> t2 = LogicSignal()
            >>> (t1 | t2).get_signal()
            1
        """
        return self.__add__(other)

    def __invert__(self):
        """
            NOT operation
            >>> t = LogicSignal(1)
            >>> (~t).get_signal()
            0
            >>> not t.get_signal()
            0
        """
        ans = LogicSignal(1 - self.__sig)
        return ans


if __name__ == '__main__':
    a = LogicSignal()
    print(a)