import random
import re


class Perceptron:
    listOfWeights = []
    teta = 1  # x * W' = x*W = X1 * (W +/- (d-y)(alpha)X)
    alpha = 1
    listtest = []
    listtraining = []

    def __init__(self, reader, listtraining, listtest): #konstruktor
        self.reader = reader
        self.listtest = listtest
        self.listtraining = listtraining
        for i in range(0, self.reader.get_numberAtr()):
            self.listOfWeights.append(float(random.uniform(0.0, 1.0)))
            print(self.listOfWeights[i])

    def calculateNet(self, vector):
        net = 0
        listOfAtr = re.split("\s+", str(vector))
        listOfAtr.pop()
        for j in range(0, self.reader.get_numberAtr()):
            net += float(self.listOfWeights[j]) * float(listOfAtr[j])
        print("net value = " + str(net))
        return net >= self.teta

    def getAtr(self, line, idx):
        return re.split("\s+", line)[int(idx)]

    def learn(self, traininglist):
        successes = 0
        count = 0
        while successes < len(traininglist):
            successes = 0
            for vec in traininglist:
                if self.calculateNet(vec) and not self.getAtr(vec, self.reader.get_numberAtr()).__eq__("Iris-setosa"):
                    for i in range(0, self.reader.get_numberAtr()):
                        self.listOfWeights[i] = self.listOfWeights[i] + (-1) * int(self.alpha) * float(self.getAtr(vec, i))
                elif not self.calculateNet(vec) and self.getAtr(vec, self.reader.get_numberAtr()).__eq__("Iris-setosa"):
                    for i in range(0, self.reader.get_numberAtr()):
                        self.listOfWeights[i] = self.listOfWeights[i] + int(self.alpha) * float(self.getAtr(vec, i))
                else:
                    successes = successes + 1

            count = count + 1
            print("Iteracja : " + str(count) + "successes: [" + str(successes) + "/" + str(len(traininglist)) + "]")

    def test(self):
        successes = 0
        for line in self.listtest:
            if self.calculateNet(line) and self.getAtr(line, self.reader.get_numberAtr()).__eq__("Iris-setosa"):
                successes = successes + 1
            elif not self.calculateNet(line) and not self.getAtr(line, self.reader.get_numberAtr()).__eq__("Iris-setosa"):
                print("netVlue dla nie setosa = " + str(self.calculateNet(line)))
                successes = successes + 1

        print("successes = " + str(successes) + "/" + str(len(self.listtest)))

