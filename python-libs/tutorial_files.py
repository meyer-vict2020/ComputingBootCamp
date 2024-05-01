#with open("example_data.csv") as f:
 #   for line in f:
  #      print(line)

import requests

r = requests.get("https://byu-cpe.github.io/ComputingBootCamp/media/example_data.csv")

print(r.text)