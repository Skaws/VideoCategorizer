# Creation and Purpose

This project was made to significantly speed up the video editing footage categorisation process by searching for and renaming footage in bulk simultaneously. 

This is rather useful as recording software will generate file names based on time such as "Replay 2022-12-17 22-47-32", but video editors constantly have to rename said files to keep track of the content the footage contains.

# How to Run
The Video Categorizer consists of two main programs: getClipNames and renameClipFiles. The former aims to get all source footage file names into an orderly text file, such that each video file can be easily renamed in said text file. For Example:

Replay 2022-12-17 22-47-32 : [insert your desired clip name here]

## getClipNames.py
This getClipNames program must first be provided with the video project directory in line 5. Subsequently the program will ask which folder in the directory has the batch of clips to be organised. It will then gather every mp4 file in the directory and store its name in the Text File

e.g. given a folder of files:  Replay 2022-12-17 22-47-32, Replay 2022-12-17 22-53-48, Replay 2022-12-17 23-14-25, the resulting text file will look like

2022-12-17 22-47-32 : [insert your desired clip name here]

2022-12-17 22-53-48 : [insert your desired clip name here]

2022-12-17 23-14-25 : [insert your desired clip name here]

## renameClipFiles.py
The user can then desired names for each clip in the [] listed above. Once the files are named, the second program - renameClipFiles, can be run. This program will rename the original footage files to the desired name, whilst keeping track of the original file names. Thanks to this feature, if footage has been incorrectly renamed, it can be reverted back to the original source file name in bulk.
