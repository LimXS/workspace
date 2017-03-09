#coding=utf-8
import logging.handlers
def addlogmes(logType,cases,message):
    LOG_FILE='C:\\workspace\\nufeeb.button\\data\\assertlog'
    #LOG_FILE='D:\\testCase.log'
    handler=logging.handlers.RotatingFileHandler(LOG_FILE,maxBytes=1024*1024,backupCount=5)
    #fmt='%(asctime)s - %(filename)s:%(filename)s-%(funcName)s-%(lineno)s - %(name)s - %(levelname)s - %(message)s'
    fmt='%(asctime)s  - %(name)s - %(levelname)s - %(message)s'
    formatter=logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger=logging.getLogger(cases)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    if logType == 'info':
        logger.info(message)
    elif logType == 'debug':
        logger.debug(message)
    elif logType == 'error':
        logger.error(message)
    elif logType == 'warning':
        logger.warning(message)
    elif logType == 'critical':
        logger.critical(message)
    logger.removeHandler(handler)
