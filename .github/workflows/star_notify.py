"""..."""
import sys

import yagmail

if __name__ == '__main__':
    yag = yagmail.SMTP(sys.argv[1], sys.argv[2], 'smtp.qq.com', 465)
    yag.send(sys.argv[3], 'github aligo started', 'github aligo started\n' + sys.argv[4])
