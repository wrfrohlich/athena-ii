#---------------------------------------------------------------------------------------
#
#       Name: Eng. William da Rosa Frohlich
#
#       Project: ATHENA I - Processing (Filters)
#
#       Date: 2021.10.16
#
#       Update: 2021.10.17
#
#---------------------------------------------------------------------------------------

import logging

from datetime import datetime


class Logs():
    def __init__(self):
        logging.basicConfig(level=logging.INFO,
                            filename="/home/athena/ftp/files/athena-ii/athena-i.log",
                            filemode="a+",
                            format="%(asctime)-15s :: %(message)s")


    def log_out(self, service, msg, level):
        message = "%s: %s" % (service, msg)
        if level == "INFO":
            logging.info(message)
        if level == "WARNING":
            logging.warning(message)
        if level == "ERROR":
            logging.error(message)
        if level == "CRITICAL":
            logging.critical(message)


    def alert(message, participant):
        with open("/home/athena/ftp/files/athena-ii/alerts/%s.log" % participant, "a+") as f:
            for index in range(0, len(message), 30):
                f.write("%s - %s\n" % (datetime.now(), message[index:index+30]))
