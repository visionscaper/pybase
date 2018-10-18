import logging

logging.basicConfig(format='%(levelname)s: %(name)s::%(funcName)s : %(message)s')


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    return logger
