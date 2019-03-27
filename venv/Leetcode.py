from ExcelOperations import *
import pandas as pd

excelfilecompany= "/Users/omerorhan/Desktop/UCSC/resume/leetcode/leetcode/venv/leetcodeCompany.xlsx"
excelfiletopic= "/Users/omerorhan/Desktop/UCSC/resume/leetcode/leetcode/venv/leetcodeByTopics.xlsx"
excelfilemain= "/Users/omerorhan/Desktop/UCSC/resume/leetcode/leetcode/venv/LeetCodemixed.xlsx"

#main file
def getmainFile():
    sheetnames = getSheetNames(excelfilemain)
    for sheet in sheetnames:
        print(sheet)

    datamain = readExcelRange(excelfilemain,"all questions by frequency",2,1015,1,6)

    datamain = pd.DataFrame({'Index':datamain[:,0],'LeetcodeId':datamain[:,1],
                            'Title':datamain[:,2],'Acceptance':datamain[:,3],'Difficulty':datamain[:,4],'Frequency':datamain[:,5]})
    return datamain
datamain =getmainFile()
#############

def getTopicFile():
    sheetnames = getSheetNames(excelfiletopic)
    for sheet in sheetnames:
        datatopic = readExcelRange(excelfiletopic,sheet,2,200,1,1)
        datatopic =  pd.DataFrame({'LeetcodeId':datatopic[:,0]})
        for topicid in datatopic["LeetcodeId"]:
            for dmain in datamain.iterrows():
                print((dmain[1]))
                break

                #if(topicid["LeetcodeId"]==main["LeetcodeId"]):
                #    print(main["Title"])

        break

    #dataset = pd.DataFrame({'Index':data[:,0],'LeetcodeId':data[:,1],
    #                        'Title':data[:,2],'Acceptance':data[:,3],'Difficulty':data[:,4],'Frequency':data[:,5]})
getTopicFile()
