from base.base_model import BaseModel


class RequestHistoryAccessModel(BaseModel):
    def __init__(self, config):
        super(RequestHistoryAccessModel, self).__init__(self, config)
        self.build_model()

    def build_model(self):
        raise NotImplementedError
