def stop_handler(signum, frame, done):
    done = False
    print("signum {}, frame: {}".format(signum, frame))
    return done