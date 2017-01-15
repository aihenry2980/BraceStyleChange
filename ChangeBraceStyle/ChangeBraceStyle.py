import os
import string
import sys

def isSupportedFileType(fileExt):
    extensions = ['.c', '.cpp', '.h', '.java', '.cs', '.C' ]
    return fileExt in extensions

def DealWtihFile(filename, bReplaceOriginalFile):
    if os.path.exists(filename)==False:
        return

    filenameNoExt, file_extension = os.path.splitext(filename)
    if isSupportedFileType(file_extension)==False:
        return

    outFileName = filename.replace(filenameNoExt, filenameNoExt+"_bs")
    if  os.path.exists(outFileName)==True:
        print(outFileName  +  " already exists!")
        return

    inf = open(filename, "r")
    otf = open(outFileName, "w")
    lines = inf.readlines()
    row = len(lines)
    i=0
    for line in lines:
        linestrip = line.strip()
        if linestrip.endswith("{"):
            indent = len(line)-len(line.lstrip())
            strIndent = line[:indent]
            lineWithoutBrace = line.rstrip()[:-1]
            if lineWithoutBrace.rstrip().endswith("else"):
                otf.write(lineWithoutBrace.rstrip()[:-4] + "\n")
                otf.write(strIndent  + "else\n")
            else:
                otf.write(lineWithoutBrace + "\n")
            otf.write(strIndent + "{\n")
        else:
            otf.write(line)

    inf.close()
    otf.close()

    if bReplaceOriginalFile==True:
        os.remove(filename)
        os.rename(outFileName, filename)


if len(sys.argv)==2:
    if os.path.isfile(sys.argv[1])==True:
        DealWtihFile(sys.argv[1], False)  #create a new file



