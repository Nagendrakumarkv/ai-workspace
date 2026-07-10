from tools.random_tool import RandomTool


def test_random_tool():

    tool = RandomTool()

    value = tool.execute(start=1, end=100)

    assert 1 <= value <= 100