from tools.registry import ToolRegistry
from tools.calculator import CalculatorTool


def test_registry():

    registry = ToolRegistry()

    registry.register(
        CalculatorTool()
    )

    assert "calculator" in registry.list_tools()

    result = registry.execute(
        "calculator",
        expression="5+5"
    )

    assert result == 10