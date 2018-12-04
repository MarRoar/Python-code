''''
实现一个通用装饰器，实现打印日志功能
'''

import logging
import logging.handlers

def logger(fn):
    def inner():
        LOG_FILE = 'tst.log'

        handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)
        fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)

        logger = logging.getLogger('tst')
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)

        logger.info('input message... ')

        fn()
    return inner

@logger
def test():
    print("test")

test()