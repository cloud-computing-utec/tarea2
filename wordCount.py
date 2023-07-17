from pyspark import SparkContext
import sys

reload(sys)
sys.setdefaultencoding('utf8')

input_name = "input_file.txt"
output_name = "output_file.txt"

sc = SparkContext(appName="Cloud Computing!")

text_file = sc.textFile(input_name)
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
output = sorted(counts.collect(), key=lambda tup: tup[1], reverse=True)
with open(output_name, "w") as file:
    for word, count in output:
        file.write("%s: %i\n" % (word, count))

sc.stop()