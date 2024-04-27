import glob
import re

root_dir = "C:\\Users\\jaetu\\OneDrive\\Documents\\Obsidian Vaults\\Zol\\"

data = ""
empties = []
nonEmpties = []
numFiles = 0

for filename in glob.iglob(root_dir + '**/*.md', recursive=True):
    numFiles += 1 # Sum File Count
    with open(filename, 'r') as file:
        fileData = file.read()
        parseFiledName = str(filename)
        parseFiledName = "https://jakeabetes.github.io/zol/" + parseFiledName[parseFiledName.rfind('\\')+1:-3].replace(',', '').replace(' ', '-')
        # Track Empty Files
        if (fileData == ""):
            empties.append(parseFiledName)
        else:
            nonEmpties.append(parseFiledName)
        # Accumulate Total String
        data += fileData + " "

# Process File Info
print("========== Start Content Files ==========")
for nonEmpty in nonEmpties:
    print(nonEmpty)
print("=========== End Content Files ===========\n")

if (len(empties) > 0):
    print("========== Start Empty Files ==========")
    for empty in empties:
        print(empty)
    print("=========== End Empty Files ===========\n")
    print("Number of Empty Files: " + str(len(empties)))

print("Number of Content Files: " + str(numFiles - len(empties)))
print("Number of Total Files: " + str(numFiles))

# Process word Count By Removing Symbols and Spaces
data = re.sub(r'[^\w]', ' ', data)
data = re.sub(' +', ' ', data)
print("Word Count: " + str(len(data.split())))
