def past_verb(s):
    irregular = {
        "go": "gone",
        "put": "put",
        "write": "written",
        "find": "found",
        "read": "read",
        }
    c = ["a", "i", "u", "e", "o"]

    if s in irregular:
        return irregular[s]
    if s[-1] == "c":
        return s + "ked"
    if s[-1] == "e":
        return s + "d"
    if s[-1] == "y":
        if not s[-2] in c:
            return s[:-1] + "ied"
        else:
            return s + "ed"
    if not s[-1] in c and s[-2] in c and not s[-3] in c:
        return s + s[-1] + "ed"
    return s + "ed"
  
print(past_verb("play"))
print(past_verb("like"))
print(past_verb("try"))
print(past_verb("stop"))
print(past_verb("heat"))
print(past_verb("picnic"))
print(past_verb("go"))
print(past_verb("put"))
print(past_verb("refer"))
print(past_verb("omit"))
print(past_verb("rain"))
print(past_verb("need"))
print(past_verb("look"))