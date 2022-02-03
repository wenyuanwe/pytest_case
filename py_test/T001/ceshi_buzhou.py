import pytest
import allure


@allure.step('第一步：用户登录login')
def login():
    print('这是登录')


@allure.step('第二步： 添加商品add')
def add():
    print('添加商品')


@allure.step('第三步：获取商品get')
def gets():
    print('获取商品')