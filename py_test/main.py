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

if __name__ == '__main__':
    che()

