from abc import ABCMeta


class TAEvaluator:
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()
        self.data = None
        self.config = None

    def set_data(self, data):
        self.data = data

    def set_config(self, config):
        self.config = config


class MomentumEvaluator(TAEvaluator):
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()


class OrderBookEvaluator(TAEvaluator):
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()


class VolatilityEvaluator(TAEvaluator):
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()


class TrendEvaluator(TAEvaluator):
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()
