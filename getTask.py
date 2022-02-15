import json

def getTask(id=1):
    fileObject = open("tasks.json", "r", encoding="UTF-8")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    str1 = aList[id]['task']
    ans=aList[id]['ans']
    task=""
    with open(str1, "r", encoding="UTF-8") as file:
        task = file.read()
    return task, ans

if __name__ == '__main__':
    task, ans = getTask(3)
    print(task)
    print(ans)