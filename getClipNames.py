from fileinput import filename
import fnmatch
import os
#general vid file folder
projectFolder = "H:/YTVids [ext drive]/Free For Alls THREE/Da Replays/"
#path to the testclips folder
clip_path="E:/Documents/SMASH/YTVids/Free For ALLS TWO/DA REPLAYS/25th Nov/"
#path to the text files folder
textpath="E:/Documents/SMASH/YTVids/Free For ALLS TWO/textFiles/Clips from sampleClips.txt"
#checks if text file has data in it
def overwriteTextFile(txtpath):
    breakCase=False
    filesize=os.stat(txtpath).st_size
    print("this is the text file's path: ", txtpath)
    print("this is the file's size: ", filesize)
    # if the file has data in it
    if filesize!=0:
        while breakCase==False:
            print("-------------------------------\n")
            print("Text file already has data. \nWould you like to overwrite the text data (yes/no)")
            overwriteInput = input()
            if overwriteInput=="yes":
                print("Overwriting file")
                return True
            elif overwriteInput=="no":
                print("Leaving file")
                return False
            else:
                print("Invalid input")
    #if the file doesn't exist
    else:
        return True


def createTextFile(vid_path,txtpath):
    clip_list=os.listdir(vid_path)
    #print("Files and directories in '", vid_path, "' :")
    #print(clip_list)
    if os.path.isfile(txtpath):
        print("checking if text file is empty")
        #ask the user if we want to overwrite the text file
        writeTxt = overwriteTextFile(txtpath)
        #if they do not want to overwrite, exit the function (and thus program)
        if writeTxt == False:
            print("Text Data detected. Not overwriting")
            return  
    sorted_clip_list = clip_list.sort()
    textfile=open(txtpath,"w")
    count = 0
    for fileName in clip_list:
        if fileName.endswith(".mp4"):
            count+=1
            nameSplitList = fileName.split(" ")
            print("this is the name list: ",nameSplitList)
            vidTimeStamp = nameSplitList[2]
            print("this is the vids timestamp: ",vidTimeStamp)
            vidID=vidTimeStamp[0:8]
            print("this is the vidID: ",vidID)
            vidLine = vidID + " : \n"
            if count == 20:
                vidLine += "\n"
                print("resetting count")
                count=0
                print(count)
            print(vidLine) 
            textfile.write(vidLine)
        else:
            print(fileName, " is not a clip file")
    textfile.close()

def main():
    closeProgram = False
    #While the program is running
    while closeProgram == False:
        #ask for the directory as a string input
        print("\nChoose a directory of clips to generate a text file for")
        inputDir = input()
        if(inputDir=="exit"):
            closeProgram=True
        #if they choose not to exit
        else:
            dirDataTxtFile = open("H:/YTVids [ext drive]/Free For Alls THREE/DirectoryData.txt", "w")

            #combine the project folder with the date folder (e.g. 2nd July) to get the clip directory
            clipDir = projectFolder + inputDir
            print("this is the directory: ", clipDir)
            #if the clip directory exists
            if(os.path.isdir(clipDir)):
                #set the txt file's name to "Clips from [insert date].txt"
                textFileName = "Clips from " + inputDir + ".txt"
                #set the file's location to 'projectfolder/Text Files/{Clips from [insert date].txt}'
                textFileDir = projectFolder + "/Text Files/" + textFileName
                print("directory exists!")
                print("to be created: ", textFileName)
                #call the createTextFile function
                createTextFile(clipDir,textFileDir)
                closeProgram=True
            else:
                print("invalid directory")
main()


    
    