import glob

import pandas as pd
import folium
import webbrowser
import openpyxl

logPrint = True

clinic = pd.read_excel('./resources/선별진료소_20211102115541.xls',
                    header=0)
if logPrint:
    print(f'CB : {clinic.head()}')

addr = []

for address in clinic.주소:
    addr.append(str(address).split())

if logPrint:
    print(f'addr : {addr}')

addr2 = []

for i in range(len(addr)):
    if addr[i][0] == "서울":
        addr[i][0] = "서울특별시"
    elif addr[i][0] == "서울시":
        addr[i][0] = "서울특별시"
    elif addr[i][0] == "부산시":
        addr[i][0] = "부산광역시"
    elif addr[i][0] == "부산":
        addr[i][0] = "부산광역시"
    elif addr[i][0] == "대구":
        addr[i][0] = "대구광역시"
    elif addr[i][0] == "인천":
        addr[i][0] = "인천광역시"
    elif addr[i][0] == "광주":
        addr[i][0] = "광주광역시"
    elif addr[i][0] == "대전시":
        addr[i][0] = "대전광역시"
    elif addr[i][0] == "대전":
        addr[i][0] = "대전광역시"
    elif addr[i][0] == "울산시":
        addr[i][0] = "울산광역시"
    elif addr[i][0] == "울산":
        addr[i][0] = "울산광역시"
    elif addr[i][0] == "세종시":
        addr[i][0] = "세종특별자치시"
    elif addr[i][0] == "경기":
        addr[i][0] = "경기도"
    elif addr[i][0] == "강원":
        addr[i][0] = "강원도"
    elif addr[i][0] == "충북":
        addr[i][0] = "충청북도"
    elif addr[i][0] == "충남":
        addr[i][0] = "충청남도"
    elif addr[i][0] == "전북":
        addr[i][0] = "전라북도"
    elif addr[i][0] == "전남":
        addr[i][0] = "전라남도"
    elif addr[i][0] == "경북":
        addr[i][0] = "경상북도"
    elif addr[i][0] == "경남":
        addr[i][0] = "경상남도"
    elif addr[i][0] == "제주":
        addr[i][0] = "제주특별자치도"
    elif addr[i][0] == "제주도":
        addr[i][0] = "제주특별자치도"
    elif addr[i][0] == "제주시":
        addr[i][0] = "제주특별자치도"

    addr2.append(' '.join(addr[i]))

if logPrint:
    print(f'addr2 : {addr2}')

# addr2 = pd.DataFrame(addr2, columns= ['address2'])
#
# clinic2 = pd.concat([clinic, addr2], axis=1)
#
# clinic2.to_csv('./resources/clinicList.csv', encoding='CP949', index=False)
#
# if logPrint:
#     print(f'clinic2 : {clinic2.head()}')



# updateAddress = pd.DataFrame(addr2, columns=['주소 업데이트'])
#
# updateAddress.to_excel('./resources/clinic2.xls', encoding='cp949', index=False)
#
# excel_names = ['선별진료소_20211102115541.xls', 'clinic2.xls']
# excels = [pd.ExcelFile(name) for name in excel_names]
# frames = [x.parse(x.sheet_names[0], header=None, index_col=None) for x in excels]
# frames[1:] = [df[1:] for df in frames[1:]]
# combined = pd.concat(frames)
#
# combined.to_csv('./resources/clinicGeoMap.csv', header=0, encoding='cp949', index=False)

all_data = pd.DataFrame

for f in glob.glob('./resources/clinic.csv'):

    data = pd.read_excel(f)

    columns = ['의료기관명', '관할보건소 전화번호', 'address2']
    df = pd.DataFrame(data, columns=columns)

    all_data = all_data.append(df, ignore_index=True)

    all_data.to_csv('./resources/clinicList2.csv', header=True, index=False, encoding='cp949')


# print(all_data.shape)
#
# # print(all_data.head())




