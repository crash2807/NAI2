from FileReader import FileReader
from Perceptron import Perceptron

reader = FileReader()
listtest = reader.readLines("iris_test.txt")
listtraing = reader.readLines("iris_training.txt")
perceptron = Perceptron(reader, listtraing, listtest)
perceptron.learn(listtraing)
perceptron.test()
line = reader.readFromConsole()
print(line)
if perceptron.calculateNet(line):
    print("Setosa")
else:
    print("not setosa")


