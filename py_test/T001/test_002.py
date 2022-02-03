import pytest
import allure
import T001.ceshi_buzhou as ceshi



@allure.feature('添加商品')
@pytest.mark.leizu
class TestGoods:
    @allure.epic('我是一个标签')
    @allure.story('测试添加商品接口')
    @allure.title('添加商品-动态步骤方式1----')
    @allure.testcase('这是一个测试的链接')
    @allure.severity('critical')
    def test_good_1(self):
        ceshi.login()
        ceshi.add()
        ceshi.gets()
        print('添加成功')

    @allure.epic('我是一个标签')
    @allure.story('测试添加商品接口')
    @allure.title('添加商品-动态步骤方式2----')

    def test_good_2(self):
        with allure.step('步骤1.....'):
            step_01()
        with allure.step('步骤2.....'):
            step_02()

        print('重复添加')

def step_01():
    print('000011111')


def step_02():
    print('00002222')