import yaml
import os
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def getEnv(env_name):
    """Get the value of an environment variable."""
    try:
        return os.environ[env_name]
    except KeyError:
        raise ValueError(f"Environment variable {env_name} not found")


def getConfig():
    curPath = os.path.dirname(os.path.realpath(__file__))
    configPath = os.path.join(curPath, "../config/config.yaml")
    configFile = open(configPath, "r", encoding="utf-8")
    configDict = yaml.load(configFile.read(), Loader=yaml.FullLoader)
    return configDict

def getSecret():
    curPath = os.path.dirname(os.path.realpath(__file__))
    configPath = os.path.join(curPath, "../config/secret.yaml")
    configFile = open(configPath, "r", encoding="utf-8")
    configDict = yaml.load(configFile.read(), Loader=yaml.FullLoader)
    return configDict

def getReceiveEmail():
    return getSecret()["receives"]


def getSendEmail():
    SenderEmail = getSecret()["send"]["email"]
    SenderSmtpPwd = getSecret()["send"]["smtp_pwd"]
    SenderSmtpServer = getSecret()["send"]["smtp_server"].split(":")
    if len(SenderSmtpServer) == 1:
        SenderSmtpServer.append("465")
    return [{"Email": SenderEmail, "SMTPPwd": SenderSmtpPwd, "SMTPServer": SenderSmtpServer}]


def formatAddress(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, "utf-8").encode(), addr))


class SendMail:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.sendEmail(title, text)

    def sendEmail(self, title, text):
        for sendEmail in getSendEmail():
            server = smtplib.SMTP_SSL(sendEmail["SMTPServer"][0], int(sendEmail["SMTPServer"][1]))  # 25 is default smtp port, check mail setting
            # server.set_debuglevel(1)
            server.login(sendEmail["Email"], sendEmail["SMTPPwd"])

            msg = MIMEText(self.text, "plain", "utf-8")
            msg["From"] = formatAddress("Birthday Reminder Service<%s>" % sendEmail["Email"])
            msg["Subject"] = Header(self.title, "utf-8").encode()
            for ta in getReceiveEmail():
                msg["To"] = formatAddress("SiteGroup<%s>" % ta)
                server.sendmail(sendEmail["Email"], ta, msg.as_string())
            server.quit()


if __name__ == "__main__":
    SendMail("Hello", "Hello")
