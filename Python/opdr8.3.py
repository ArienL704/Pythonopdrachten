vakkenlijst = ["JavaScript", "Python", "HTML", "CSS", "LiveScript", "PHP", "EcmaScript"]
print(vakkenlijst)

cnt = len(vakkenlijst)
print(cnt)

print(vakkenlijst[1])

vakkenlijst.sort()
print(vakkenlijst)

vakkenlijst.pop( 4 )
vakkenlijst.pop( 4 )
print(vakkenlijst)

for a in range(len(vakkenlijst)):
    if vakkenlijst[a] == "EcmaScript":
        vakkenlijst[a] = "ES6"

print(vakkenlijst)

vakkenlijst = vakkenlijst[:2] + vakkenlijst[4:]
print(vakkenlijst)

l = [s.lower() for s in vakkenlijst]
print(l)