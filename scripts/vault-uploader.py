import glob
import re
import os
import shutil


root_dir = "C:\\Users\\jaetu\\OneDrive\\Documents\\Obsidian Vaults\\Zol\\"
dest_dir = "C:\\Users\\jaetu\\OneDrive\\Documents\\git\\zol\\content"

textFileTypes = ['md']
imgFileTypes = ['png', 'jpg']

# empty content for copy
files = glob.glob(dest_dir + "\\*")
for f in files:
    os.remove(f)

for ft in textFileTypes + imgFileTypes:
    for filename in glob.iglob(root_dir + '**/*.' + ft, recursive=True):
        if ft in imgFileTypes:
            # if it is an image file we just copy no questions asked
            shutil.copy(filename, dest_dir)
        else:
            # if it is a text file don't copy if blank
            with open(filename, 'r') as file:
                fileData = file.read()
                # Track Empty Files
                if (fileData != ""):
                    # Add YAML front matter for Hugo .Title value to be used for page title
                    fileData = "---\ntitle: " + "\"" + os.path.basename(filename).replace('.md', '') + "\"\n---\n" + fileData

                    # Due to a weird bug with quartz, we have to remove the ' character from filenames
                    destFilename = dest_dir + "\\" + os.path.basename(filename).replace("\'", "")

                    # Make new file at dest folder (new instead of copy for front matter and possible new filename)
                    with open(destFilename, 'w') as f:
                        f.write(fileData)
