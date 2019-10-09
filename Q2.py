def mark_3rd(s):
    if len(s) < 3: return s
    s2 = s.replace(s[2], "*")
    return s2[:2] + s[2] + s2[3:]

print(mark_3rd("logging"))
print(mark_3rd("apple"))
print(mark_3rd("orange"))
print(mark_3rd("gooooogle"))
print(mark_3rd("i"))

