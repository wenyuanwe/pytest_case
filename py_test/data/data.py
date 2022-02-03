import pandas as pd



def data():
    data_list=[]
    data = pd.read_excel('C:\\Users\\yuanwe\\Desktop\\test.xlsx')

    for index,row in data.iterrows():
        input=str(row['input1'])+'+'+str(row['input2'])
        expect=str(row['result'])
        title_desc=str('计算:'+input)
        data_list.append([input,expect,title_desc])

    return data_list


def result_data(input,expect,ac_result,data_result):
    with open('C:\\Users\\yuanwe\\Desktop\\result.txt',mode='a+') as wf:
        wf.write(str(input)+' '+str(expect)+' '+str(ac_result)+' '+str(data_result)+'\n')



def csv_excel():
    data = pd.read_csv('C:\\Users\\yuanwe\\Desktop\\result.txt', sep=' ',names=['算式','期望结果','实际结果','对比结果'])
    data.to_excel('C:\\Users\\yuanwe\\Desktop\\result.xlsx',index=False)


if __name__ == '__main__':
    print(data())