


import logging

LOGGER_NAME = "meme"

def init_logging(level: int=logging.INFO):
  
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(level)

    console_handler = logging.StreamHandler()

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)


logger = logging.getLogger(LOGGER_NAME)


# end
