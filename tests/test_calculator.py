from tools.calculator import CalculatorTool


def test_addition():

    tool = CalculatorTool()

    assert tool.execute(expression="10+20") == 30


def test_power():

    tool = CalculatorTool()

    assert tool.execute(expression="2**5") == 32