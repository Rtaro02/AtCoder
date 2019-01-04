import re
import copy

def getDevidedString(S):
    s = copy.deepcopy(S)
    regExDream = "^(.*)dream$"
    if re.match(regExDream, s):
        return re.sub(regExDream, "\\2", s)
    regExDreamer = "^(.*)dreamer$"
    if re.match(regExDreamer, s):
        return re.sub(regExDreamer, "\\1", s)
    regExErase = "^(.*)erase$"
    if re.match(regExErase, s):
        return re.sub(regExErase, "\\1", s)
    regExEraser = "^(.*)eraser$"
    if re.match(regExEraser, s):
        return re.sub(regExEraser, "\\1", s)
    return s

S = input()

while len(S) != 0:
    tmp = getDevidedString(S)
    if len(S) != len(tmp):
        S = tmp
    else:
        break

if len(S)== 0:
    print("YES")
else:
    print("NO")