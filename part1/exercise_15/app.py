from datetime import datetime
import time
import sys

if __name__ == "__main__":
    while True:
        time.sleep(1)
        time_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #sys.stdout.write('\r{%s}' % time_string )
        print "%s" % time_string

