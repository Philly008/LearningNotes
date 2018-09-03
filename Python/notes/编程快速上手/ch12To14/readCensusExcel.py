# -*- coding:utf-8 -*-
# Tabulates population and number of census tracts for each county.
# 第 1 步：读取电子表格数据
import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
# 新版本 openpyxl 直接用 wb['']，而不用wb.get_sheet_by_name('')
# sheet = wb.get_sheet_by_name('Population by Census Tract')
sheet = wb['Population by Census Tract']
countyData = {}
# Fill in countyData with each county's population and tracts.
print('Reading rows...')
# 新版本openpyxl 不支持get_highest_row()，引入 max_row, max_column 属性替代。
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
# 第 2 步：填充数据结构
    # Make sure the key for this state exists.
    countyData.setdefault(state, {})
    # Make sure the key for this county in this state exists.
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    # Each row represents one census tract, so increment by one
    countyData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract.
    countyData[state][county]['pop'] += int(pop)

# 第 3 步：将结果写入文件
# Open a new text file and write the contents of countyData to it.
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
