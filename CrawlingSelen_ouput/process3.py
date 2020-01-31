import csv
from openpyxl import Workbook

INPUT_NAME = "pro2_SewSweetnessSewingPatterns.csv"
OUTPUT_NAME = "pro3_SewSweetnessSewingPatterns.xlsx"

f = open(INPUT_NAME, "r", encoding="utf-16")
rdr = csv.reader(f, delimiter=",")
write_wb = Workbook()
write_ws = write_wb.active
write_ws.append(["인덱스", "이름1", "이름2", "거주지", "부가정보들"])

for line in rdr:
    # print(line)
    if len(line) == 0:
        continue
    if len(line) == 1:
        continue
    if len(line) == 2:  # idx,이름뿐
        res = []
        name = line[1].split(" ", maxsplit=1)
        if len(name) == 1:
            name.append("")
        res.append(int(line[0]))
        res.extend(name)
        # print(res)
        write_ws.append(res)

    if len(line) >= 3:  # idx,이름,거주지, 외 추가 정보.
        res = []
        plusInfo = []
        # 이름정보 처리 ,
        name = line[1].split(" ", maxsplit=1)
        if len(name) == 1:
            name.append("")
        # 거주지 처리
        # 부가정보 처리
        for i in range(3, len(line) - 1):
            if "거주" in line[i]:
                continue
            plusInfo.append(line[i])
        res.append(int(line[0]))
        res.extend(name)
        res.append(line[2][0:-3])
        res.extend(plusInfo)
        # print(res)
        try:
            write_ws.append(res)
            pass
        except:
            print("Error: ", line[0])
            pass


write_wb.save(OUTPUT_NAME)
f.close()

