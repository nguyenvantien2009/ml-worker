class BaseModel(object):
    def __init__(self, config):
        self.config = config
        self.model = None

    def save(self, checkpoint_path):
        if self.model is None:
            raise Exception("Your mode is None. So can not load now.")

        self.model.save_weight(checkpoint_path)

    def load(self, checkpoint_path):
        if self.model is None:
            raise Exception("Your mode is None. So can not load now.")
        self.model.load_weights(checkpoint_path)

    def build_model(self):
        raise NotImplementedError
