import os

year = "2025"
nbday = 12
os.mkdir(year)

for d in range(1,nbday+1):


    pathdays = f"{str(d).zfill(len(str(nbday)))}-day"

    dospath = f"{year}/{pathdays}"

    os.mkdir(dospath)



    p1 = open(f"{dospath}/part1.py","w")
    p2 = open(f"{dospath}/part2.py","w")
    open(f"{dospath}/inputExemple.txt","w")
    open(f"{dospath}/input.txt","w")

    startcode = "file = open(\"inputExemple.txt\",\"r\")\n#file = open(\"input.txt\",\"r\")\ndata = file.read()\n\ndatalist = data.split(\"\\n\")\n\n\n\n"

    p1.write(f"#parti1\n\n{startcode}")
    p2.write(f"#parti2\n\n{startcode}")

    p1.close()
    p2.close()

print("ok")

