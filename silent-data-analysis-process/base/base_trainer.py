class BaseTrainer(object):
    def __init__(self, model, data, config):
        self.model = model
        self.data = data
        self.config = config

    def train(self):
        raise NotImplementedError

    def save_trained_model(self, model_trained):
        """dump model trained to save database. will will used it to predict"""
        raise NotImplementedError
