import logging

class log_generator_class:

    @staticmethod
    def log_gen_method():
        logger = logging.getLogger()
        log_file = logging.FileHandler(".\\logs\\Credkart.log")
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - lineno - %(message)s')
        log_file.setFormatter(log_format)
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger
