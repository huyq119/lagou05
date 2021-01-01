import pytest
import yaml

from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        # 实例化类,生成类的对象
        self.calc = Calculator()

    def teardown_class(self):
        print("\n所有用例完成")

    def setup_method(self):
        print("\n开始计算")

    def teardown_method(self):
        print("\n结束计算")

    #  使用参数化
    @pytest.mark.parametrize("a,b,expect", [(3, 5, 8), (-1, -2, -3), (10000, 10000, 20000)])
    # 测试add函数
    def test_add(self, a, b, expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.add(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", yaml.safe_load(open("./sub_param.yml")))
    # 测试sub函数
    def test_sub(self, a, b, expect):
        # 调用sub函数，返回的结果保存在result里面
        print("减法函数")
        result = self.calc.sub(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", yaml.safe_load(open("./mul_param.yml")))
    # 测试mul函数
    def test_mul(self, a, b, expect):
        # 调用mul函数，返回的结果保存在result里面
        print("乘法函数")
        result = self.calc.mul(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", yaml.safe_load(open("./div_param.yml")))
    def test_div(self, a, b, expect):
        # 调用mul函数，返回的结果保存在result里面
        print("除法函数")
        result = self.calc.div(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect
