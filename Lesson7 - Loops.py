from xml.dom.minidom import ProcessingInstruction

for x in range (200 ):
    print ("**********")
    print ("{{}{}}}{}{}{}{{}{}")
for y in range (0, 200 + 1, 2):
    print (y)
for c in range (0, 200 + 1, 2):
    print ("Number c = " + str(c))

for d in range (200, 10, -2):
    print ("Number d = " + str(d))
    if d == 100:
        break
print("___________EOF_____________")

x = 0
while True:
    print (x)
    x = x + 100 - 99
    if x == 2000 + 1:
        break
