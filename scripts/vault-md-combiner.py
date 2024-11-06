import glob
import re
from datetime import datetime

mergedFile = open("mergedZolFile" + datetime.today().strftime('%Y-%m-%d') + ".txt", "x")

root_dir = "C:\\Users\\jaetu\\OneDrive\\Documents\\git\\zol\\content"
data = ""

for filename in glob.iglob(root_dir + '**/*.md', recursive=True):
    with open(filename, 'r') as file:
        fileData = file.read()
        # Accumulate Total String
        data += "Title: " + filename + "\n" + fileData + "\n\n"

mergedFile.write(data)
mergedFile.close()
print("Zol Vault Files Combined into: " + "mergedZolFile" + datetime.today().strftime('%Y-%m-%d') + ".txt")
