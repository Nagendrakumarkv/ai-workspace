from tools.datetime_tool import DateTimeTool


def test_datetime_tool():

    tool = DateTimeTool()

    result = tool.execute()

    assert "date" in result

    assert "time" in result

    assert "datetime" in result