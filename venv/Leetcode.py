from ExcelOperations import *
import pandas

excelfilecompany= "/Users/omerorhan/Desktop/UCSC/resume/leetcode/leetcode/venv/leetcodeCompany.xlsx"
excelfilecompany= "/Users/omerorhan/Desktop/UCSC/resume/leetcode/leetcode/venv/leetcodeByTopics.xlsx"
excelfilemain= "/Users/omerorhan/Desktop/UCSC/resume/leetcode/leetcode/venv/LeetCodemixed.xlsx"


sheetnames = getSheetNames(excelfilemain)


for sheet in sheetnames:
    print(sheet)
