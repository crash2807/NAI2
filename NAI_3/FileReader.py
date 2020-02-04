import re


class FileReader:
    numberAtr = 0

    def get_numberAtr(self):
        return self.numberAtr

    def readLines(self, path):
        list = []
        with open(path, "r") as content:
            for line in content:
                line = line.replace("\n", "")
                line = line.replace(" ", "")
                line = line.replace(",", "")
                list.append(line)

        self.numberAtr = len(re.split("\s+", str(line))) - 1
        return list

    def readFromConsole(self):
        row = ""
        for i in range(0, self.numberAtr):
            row = row + str(input(str(i) + "/" + str(self.numberAtr))) + " "
        return row

