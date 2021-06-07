from subprocess import check_output
from os import listdir
from sys import argv

unified_log = ""
for filename in sorted(listdir(".")):
    if filename.endswith(".log.gz"):
        unified_log = unified_log+"=== "+filename+" ===\n"+check_output(["gunzip", "-c", filename]).decode("utf-8")

unified_log = unified_log + check_output(["cat", "latest.log"]).decode("utf-8")

if "-o" in argv:
    if argv.index("-o") == len(argv) - 1:
        print(unified_log)
    else:
        output = open(argv[argv.index("-o")+1], "w")
        output.write(unified_log)
        output.close()
else:
    print(unified_log)
