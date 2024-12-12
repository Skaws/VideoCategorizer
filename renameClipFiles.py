from cgitb import text
from fileinput import filename
import fnmatch
import os
from tabnanny import check

#general vid file folder
projectFolder = "H:/YTVids [ext drive]/Free For Alls THREE/Da Replays/"
#path to the testclips folder
clip_path="E:/Documents/SMASH/YTVids/Free For ALLS TWO/DA REPLAYS/25th Nov/"
#path to the text files folder
textpath="E:/Documents/SMASH/YTVids/Free For ALLS TWO/textFiles/Clips from sampleClips.txt"
#gets the list of files and stores them in clip_list

def createClipDict(txtpath,reversed):
    splitkey = " - "
    if reversed == True:
        splitkey = " : "
    textfile=open(txtpath,"r")
    clipDictionary= {}
    for line in textfile:
        print("\n This is the line: ", line)
        if line!="\n":
            splitLine = line.split(splitkey)
            print("This is the list: ",splitLine)
            fileID=splitLine[0]
            print("This is the file ID: ", fileID)
            fileNamed=splitLine[1].strip()
        #print("This is the file name: ", fileNamed)
        #print("file name length: ", len(fileNamed))
        clipDictionary[fileID] = fileNamed

    print(clipDictionary)
    return clipDictionary

#check if the revert file is vaild
def checkRevertFile(clipPath):
    print("\n called check revert file")
    print("current path: ", clipPath)
    print("overall project path: ", projectFolder)
    #get the current reversion text file
    inputPath = clipPath.replace(projectFolder,"")
    inputPath = inputPath.strip("/")
    print("input path is: ", inputPath)
    revertTextPath = clipPath + "Reversion text for "+ inputPath + ".txt"
    #put the current reversion text file into a dictionary
    prevDict = createClipDict(revertTextPath,True)
    #get all files in the current folder
    file_list=os.listdir(clipPath)
    #for each original shadowplay file name in the dictionary
    for newName in prevDict:
        print("evaluating: ", newName, " and it's original name ", prevDict[newName])
        #if any of NEW file names are in the list of files, return a value of true to show the file is valid
        if newName in file_list:
            print("Valid Revert File")
            return True
    return False


def createrRevertFile(revertDict,clipPath):
    
    inputPath = clipPath.replace(projectFolder,"")
    inputPath = inputPath.strip("/")
    revertTextPath = clipPath + "Reversion text for "+ inputPath + ".txt"
    #print("this is the input folder: ", inputPath)
    print("this is the reverted texts path, ", revertTextPath)
    validRevertFile=False
    revertString=""
    #if the revert file exists then this can be evaluated
    if os.path.isfile(revertTextPath):
        #check if the revert file is valid. If it is append to it otherwise overwrite data in it
        validRevertFile = checkRevertFile(clipPath)
        revertTextFile = open(revertTextPath,"r")
        revertString = revertTextFile.read()
        revertTextFile.close()
        print(revertString)
    
    if validRevertFile==True:
        textfile=open(revertTextPath,"a")
    else:
        textfile=open(revertTextPath,"w")
    for oldName in revertDict:
        revertline = revertDict[oldName] + " : " + oldName + "\n"
        print("file's new name: " + revertDict[oldName] )
        print("file's original name: " + oldName )
        if(revertline in revertString):
            print("this line is already in here: ", revertline)
        else:
            textfile.write(revertline)
    textfile.close()

def revertFile(clip_list,clipPath):
    inputPath = clipPath.replace(projectFolder,"")
    inputPath = inputPath.strip("/")
    revertTextPath = clipPath + "Reversion text for "+ inputPath + ".txt"
    #print("this is the input folder: ", inputPath)
    print("this is the reverted texts path, ", revertTextPath)
    revertDict = createClipDict(revertTextPath,True)
    for newName in revertDict:
        print("New name: ", newName, " and the old name: ", revertDict[newName])
        if newName in clip_list:
            print("the renamed file exists")
            renamedFilePath = clipPath + newName
            revertedFilePath = clipPath + revertDict[newName]
            print("renamed file path is '",renamedFilePath)
            print("reverted file path is '",revertedFilePath)
            os.rename(renamedFilePath,revertedFilePath)
        else:
            print("renamed file does not exist! ")



def revertMain(clipPath):
    clip_list=os.listdir(clipPath)

    print("Files and directories in '", clipPath, "' :")

    print(clip_list)

    revertFile(clip_list,clipPath)

def renameFiles(clipDict,clip_list,clipPath):
    doubleNameDict = {}
    for fileName in clip_list:
        nameSplitList = fileName.split(" - ")
        print("this is the name list: ",nameSplitList)
        vidTimeStamp = nameSplitList[1]
        print("this is the vids timestamp: ",vidTimeStamp)
        vidID=vidTimeStamp[0:8]
        print(vidID)
        clipName = clipDict.get(vidID)
        #print("this is the clip name's length: ", len(clipName), ".")
        if clipDict.get(vidID) is None:
            print("file does not have a name associated")

        elif len(clipName)==0:
            print("file exists but has no name")
        else:
            print("file has a name associated")
            newFileName = clipDict.get(vidID) + ".mp4"
            print("file name is '",newFileName,"' .")
            oldFilePath = clipPath + fileName
            newFilePath = clipPath + newFileName
            doubleNameDict[fileName] = newFileName
            print("original file path is '",oldFilePath,"' .")
            print("new file path is '",newFilePath,"' .")
            os.rename(oldFilePath,newFilePath)
    dictLen = len(doubleNameDict)
    print("reverse Dictionary size: ", dictLen)
    if dictLen!=0:
        createrRevertFile(doubleNameDict,clipPath)
        print("creating reversion file")

#removes non mp4 files from the list of files
def checkFiles(fileList):
    print("This is the input fileList to the function: ", fileList)
    clip_list=[]
    for fileName in fileList:
        print("\n this is the filename: ", fileName)
        if fileName.endswith(".mp4"):
            print(fileName, " is a clip file")
            print("clip detected")
            clip_list.append(fileName)
        else:
            print(fileName, " is not a clip file")
    print("this is the resulting list: ", clip_list)
    return clip_list

def renameMain(clipPath,textFileDir):
    breakLoop = False
    #loop that asks how many clips should be renamed and only breaks when an integer is used
    while breakLoop==False:
        print("How many clips would you like to rename")
        try:
            clipnumber = int(input())
        except ValueError:
            print("that's not a number, try again")
        else:
            print("Number accepted as ", clipnumber)
            breakLoop=True

    #gets the list of clips in clipPath
    file_list=os.listdir(clipPath)
    print("Files and directories in '", clipPath, "' :")
    print(file_list)

    clip_list = checkFiles(file_list)

    clip_list.sort()

    print("this is the sorted list", clip_list)

    vidDict = createClipDict(textFileDir,False)

    print("this is the number input", clipnumber)
    inputClipList = clip_list[0:clipnumber]
    print(inputClipList)
    renameFiles(vidDict,inputClipList,clipPath)

def getFileDir():
    closeProgram = False

    while closeProgram == False:

        print("\nChoose a directory of clips to rename/revert")
        inputDir = input()
        if(inputDir=="exit"):
            closeProgram=True
        else:
            clipDir = projectFolder + inputDir
            print("this is the directory: ", clipDir)
            if(os.path.isdir(clipDir)):
                print("directory exists!")
                closeProgram=True
            else:
                print("invalid directory")
    return inputDir

def main():
    inDir = getFileDir()
    if inDir=="exit":
        return
    textFileName = "Clips from " + inDir + ".txt"
    clipDir = projectFolder + inDir + "/"
    clip_path=clipDir
    textFileDir = projectFolder + "Text Files/" + textFileName
    print("this is the clip folder: ", clip_path)
    print("this is the text folder: ", textFileDir)
    txtFilesExist = os.path.isfile(textFileDir)
    print("Does the folder have a respective text file generated? ",txtFilesExist)
    if txtFilesExist==False:
        return
    breakClause = False
    while breakClause==False:
        print("\nWould you like to rename files or revert them to the shadowplay original names \nType 'rename' or revert' (or 'exit' to escape) ")
        answer = input()
        if answer == "exit":
            breakClause=True
        elif answer == "revert":
            revertMain(clipDir)
        elif answer == "rename":
            renameMain(clipDir,textFileDir)
        else:
            print("Invalid answer")

main()
    
