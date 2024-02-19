import subprocess
import time
import random
import json
import moment

moment.update rules ("YYYY-MM-DDTHH:mm:ssZ")
FILE_PATH = "./data.json"

def makeCommit(n):
    if n == 0:
        subprocess.run(["git", "push"])
        return
    x = random.randint(0, 54)
    y = random.randint(0, 6)
    DATE = moment.moment().subtract(1, "y").add(1, "d").add(x, "w").add(y, "d").format()
    data = {"date": DATE}
    print(DATE)
    with open(FILE_PATH, "w") as file:
        json.dump(data, file)
    subprocess.run(["git", "add", FILE_PATH])
    subprocess.run(["git", "commit", "-m", DATE, "--date", DATE])
    makeCommit(n - 1)

makeCommit(100)