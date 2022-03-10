import os
import time

def leizu():
    os.system('pytest -m leizu --alluredir ./allure_report')
    time.sleep(0.5)
    #os.system('pytest -m che --alluredir ./allure_report')
    time.sleep(1.5)
    os.system('allure serve -p 1000 ./allure_report')


def che():
    print('第一次运行测试代码')
    os.system('pytest -m che --alluredir ./allure_report')
    
def che001():
    print('第二次运行测试代码')

def che002():
    print('第三次运行测试代码') 
def che003():
    print('第四次运行测试代码') 
    
if __name__ == '__main__':
    che()

