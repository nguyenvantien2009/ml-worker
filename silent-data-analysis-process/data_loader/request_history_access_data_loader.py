from base.base_data_loader import BaseDataLoader


class RequestHistoryAccessDataLoader(BaseDataLoader):

    def __init__(self, config):
        super(RequestHistoryAccessDataLoader, self).__init__(config)
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

    def get_train_data(self):
        return self.X_train, self.y_train

    def get_test_data(self):
        return self.X_test, self.y_test
