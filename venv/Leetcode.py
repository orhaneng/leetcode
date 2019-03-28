from ExcelOperations import *
import pandas as pd

excelfilecompany= "/Users/omerorhan/Desktop/UCSC/resume/leetcode/leetcode/venv/leetcodeCompany.xlsx"
excelfiletopic= "/Users/omerorhan/Desktop/UCSC/resume/leetcode/leetcode/venv/leetcodeByTopics.xlsx"
excelfilemain= "/Users/omerorhan/Desktop/UCSC/resume/leetcode/leetcode/venv/LeetCodemixed.xlsx"

#main file
def getmainFile():
    sheetnames = getSheetNames(excelfilemain)
    for sheet in sheetnames:
        #print(sheet)
        pass

    datamain = readExcelRange(excelfilemain,"all questions by frequency",2,1015,1,6)

    datamain = pd.DataFrame({'LeetcodeId':datamain[:,1],
                            'Title':datamain[:,2],'Acceptance':datamain[:,3],'Difficulty':datamain[:,4],'Frequency':datamain[:,5]})
    return datamain
datamain =getmainFile()

#############

def getTopicFile(datamain):
    sheetnames = getSheetNames(excelfiletopic)
    dftopics = pd.DataFrame(columns=list(['LeetcodeId', 'Topic']))
    for sheet in sheetnames:
        datatopic = readExcelRange(excelfiletopic,sheet,2,200,1,1)
        datatopic =  pd.DataFrame({'LeetcodeId':datatopic[:,0]})
        for topicid in datatopic["LeetcodeId"]:
            dftopics = dftopics.append({'LeetcodeId': topicid, "Topic":sheet}, ignore_index=True)
    dict = {};
    for item in dftopics.iterrows():
        if item[1][0] in dict:
            text = dict.get(item[1][0])
            text = text + "|" + item[1][1]
            dict.update({item[1][0]: text})
        else:
            dict.update({item[1][0]: item[1][1]})
    for item in datamain["LeetcodeId"]:
        if item in dict:
            datamain.loc[datamain["LeetcodeId"]==item,"Topic"] = dict.get(item)
    datamain.to_csv("/Users/omerorhan/Desktop/UCSC/resume/leetcode/leetcode/venv/leetcoderesult.csv",index=False)
    return datamain

def getCompanyFile():
    datamain = pd.read_csv("/Users/omerorhan/Desktop/UCSC/resume/leetcode/leetcode/venv/leetcoderesult.csv", engine='python',
                        index_col=False)
    sheetnames = getSheetNames(excelfilecompany)
    dfCompany = pd.DataFrame(columns=list(['LeetcodeId', 'Company']))
    for sheet in sheetnames:
        datacompany = readExcelRange(excelfilecompany,sheet,2,1000,1,1)
        datatopic =  pd.DataFrame({'LeetcodeId':datacompany[:,0]})
        for topicid in datatopic["LeetcodeId"]:
            dfCompany = dfCompany.append({'LeetcodeId': topicid, "Company":sheet}, ignore_index=True)
    dict = {};

    for item in dfCompany.iterrows():
        if item[1][0] in dict:
            text = dict.get(item[1][0])
            text = text + "|" + item[1][1]
            dict.update({item[1][0]: text})
        else:
            dict.update({item[1][0]: item[1][1]})
    print(dict)
    for item in datamain["LeetcodeId"]:
        if int(item) in dict:
            datamain.loc[datamain["LeetcodeId"]==item,"Company"] = dict.get(item)
    print(datamain)
    datamain.to_csv("/Users/omerorhan/Desktop/UCSC/resume/leetcode/leetcode/venv/leetcoderesult.csv",index=False)
    return datamain
getCompanyFile()
#dftopics = getTopicFile(datamain)
#dataset = pd.read_csv("/Users/omerorhan/Desktop/UCSC/resume/leetcode/leetcode/venv/leetcoderesult.csv", engine='python',
#                     index_col=False)
#print(dataset)
#dict = {};
#for item in dataset.iterrows():
#    if item[1][0] in dict:
#        text = dict.get(item[1][0])
#        text = text+"|"+item[1][1]
#        dict.update({item[1][0]:text})
#    else:
#        dict.update({item[1][0]:item[1][1]})
#print(dict)
#    #print(str(item[1][0])+"-"+item[1][1])