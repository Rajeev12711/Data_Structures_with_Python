string= ["flower", "flow", "flight"]
def per_fix(strs):

    if strs == "":
        return ""
    check =  strs[0]
    for i in strs[1:]:
        while not i.startswith(check):
            check = check[:-1]
            if check == "":
                return ""
    return check

print(per_fix(string))