import time
import os
import base64


class Task:

    def __init__(self, platform, extension):
        self.taskID = ""
        self.platform = platform
        self.timestamp = str(time.time() * 1000000).split('.')[0]
        self.name = "{0}.{1}".format(self.timestamp, extension)
        self.folder = os.path.dirname(os.path.realpath(__file__)) + "/{0}/{1}/".format(platform, self.timestamp)
        # self.folder = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\{0}\\{1}\\".format(platform, self.timestamp)
        # self.folder = "./{0}/{1}/".format(platform, self.timestamp)
        self.logName = "{0}.{1}.log".format(self.timestamp, platform)
        self.outName = "{0}.{1}.out".format(self.timestamp, platform)
        self.createDir()
        self.result = {
            "platform": platform,
            "folder": self.timestamp,
            "status": {},
            "log": {},
            "out": {},
            "image": {}
        }

    def getFolder(self):
        return os.path.dirname(os.path.realpath(__file__)) + "/{0}/{1}/".format(self.platform, self.timestamp)

    def createDir(self):
        os.mkdir(self.folder)

    def getScriptPath(self):
        return self.folder + self.name

    def getLogPath(self):
        return self.folder + self.logName

    def getOutPath(self):
        return self.folder + self.outName

    def getname(self):
        return self.name

    def setTaskID(self, ID):
        self.taskID = ID

    def getTaskID(self):
        return self.taskID

    def readLog(self):
        # TODO: Add logic to check if file is there
        file = self.getLogPath()
        log = open(file, "r")
        self.result["log"] = log.read()
        log.close()

    def readOut2(self):
        # TODO: Add logic to check if file is there
        file = self.getOutPath()
        out = open(file, "r")
        self.result["out"] = out.read()
        out.close()

    def readOut(self):
        outs = []
        for file in os.listdir(self.folder):
            if file.endswith(".out"):
                outs.append(file)
        for f in outs:
            path = self.folder + "/" + f
            with open (path, "r") as out_file:
                out = out_file.read()
                self.result["out"] = out

    def readImage(self):
        # check if file is there, convert to base 64, put to result

        images = self.findImages()
        if len(images) != 0:
            for i in images:
                path = self.folder + "/" + i
                with open(path, "rb") as image_file:
                    image = image_file.read()
                    encoded_image = str(base64.b64encode(image))
                    data = encoded_image[2:-3]
                    header = 'data:image/png;base64,'
                    result = header + data
                    self.result['image'] = result
                    image_file.close()

    def findImages(self):
        images = []
        for file in os.listdir(self.folder):
            if file.endswith(".png"):
                images.append(file)
            if file.endswith(".jpg"):
                images.append(file)
        return images
