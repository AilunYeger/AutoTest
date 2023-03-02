from utils.logger import logger
from configparser import ConfigParser
import yaml
import json
import os


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

class SourceLoad():

    def loadIni(self, path):
        logger.info(f'加载{path}文件..........')
        config = MyConfigParser()
        config.read(path, encoding='UTF-8')
        logger.info(f'{path}文件加载成功..........')
        return config._sections


    def loadJson(self, path, **kwargs):
        logger.info(f'加载{path}文件..........')
        with open(path, encoding='UTF-8') as f:
            data = json.load(f)
        logger.info(f'{path}文件加载成功..........')
        logger.info('替换指定参数..........')
        kwargs = dict(**kwargs)
        for k in kwargs:
            if k in data:
                data[k] = kwargs[k]
        return data


    def loadYaml(self, path):
        logger.info(f'加载{path}文件..........')
        with open(path, encoding='UTF-8') as f:
            data = yaml.safe_load(f)
        logger.info(f'{path}文件加载成功..........')
        return data

data = SourceLoad()

if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'source', 'test_data.yml')
    yaml_data = data.loadYaml(file_path)
    print(type(yaml_data))
    print(yaml_data)

