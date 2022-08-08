import logging

logging.basicConfig(filename="versionautomation_log.log", format='%(asctime)s - %(levelname)s  - %(message)s',
                    filemode='a',datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)