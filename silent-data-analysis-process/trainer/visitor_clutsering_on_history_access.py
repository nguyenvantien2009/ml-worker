from base.base_trainer import BaseTrainer


class VisitorClusteringOnHistoryAccess(BaseTrainer):

    def __init__(self, model, data, config):
        super(VisitorClusteringOnHistoryAccess, self)\
            .__init__(model, data, config)

    def init_callbacks(self):
        raise NotImplementedError

    def train(self):
        raise NotImplementedError
