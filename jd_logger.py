import logging
import logging.handlers

'''
日志模块
'''
LOG_FILENAME = 'jd_seckill.log'
logger = logging.getLogger()


def set_logger():
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(threadName)s  %(levelname)s - ''%(filename)s[%(lineno)d] - %(message)s')
    # formatter = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - ''%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)
    # 10mb 大小
    file_handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=10485760, backupCount=3, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


set_logger()
