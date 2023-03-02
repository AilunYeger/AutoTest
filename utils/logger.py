import logging
import os
import datetime
import time

log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'log')
if not os.path.exists(log_path):
    os.mkdir(log_path)

class Logger():
    def __init__(self):
        self.log_name = os.path.join(log_path, f'{time.strftime("%Y%m%d")}.log')
        self.logger = logging.getLogger('Log')
        self.logger.setLevel(logging.DEBUG)

        self.formate = logging.Formatter('[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')
        self.handler = logging.FileHandler(self.log_name, mode='a', encoding='UTF-8')
        self.handler.setFormatter(self.formate)
        self.handler.setLevel(logging.DEBUG)

        self.consloe = logging.StreamHandler()
        self.consloe.setFormatter(self.formate)
        self.consloe.setLevel(logging.DEBUG)

        self.logger.addHandler(self.handler)
        self.logger.addHandler(self.consloe)

logger = Logger().logger


if __name__ == '__main__':
    logger.debug('this is a debug')
    logger.error('this is a error')