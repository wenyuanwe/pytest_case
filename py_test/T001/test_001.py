import pytest
import data.data as data
import allure

@pytest.mark.parametrize("input",[
                            2,3,6,9
])

@pytest.mark.fang
def test_02(input):
    print(input)

@allure.story('算术加法')
@allure.severity('blocker')
@pytest.mark.parametrize("input,expect,title_desc",data.data())
@pytest.mark.che
def test_03(input,expect,title_desc):
    allure.dynamic.title(title_desc)
    data.result_data(input,expect,eval(input),expect==eval(input))
    assert eval(input)==int(expect)

def teardown_module():
    data.csv_excel()








