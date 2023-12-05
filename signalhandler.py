from loggerhandlers import logger
def stop_handler(signum, frame, done):
    done = False
    logger.warn("signum {}, frame: {}".format(signum, frame))
    return done