# export fprocess="python /Users/gaozhe/GolandProjects/vpnbook/dev/of-watchdog/test/index.py"
# export mode=serializing
import logging
import sys

logging.basicConfig(level=logging.DEBUG)


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    # print(req, "222")
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

    # logging.debug("This is a debug log.")
    # logging.info("This is a info log.")
    # logging.warning("This is a warning log.")
    # logging.error("This is a error log.")
    # logging.critical("This is a critical log.")
    print("1")
    # time.sleep(2)
    return req


def get_stdin():
    buf = ""
    while (True):
        line = sys.stdin.readline()
        buf += line
        if line == "":
            break
    return buf


if __name__ == "__main__":
    st = get_stdin()
    ret = handle(st)
    if ret != None:
        print(ret)
