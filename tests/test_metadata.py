from tools.registry import ToolRegistry
from tools.calculator import CalculatorTool


def test_metadata():

    registry = ToolRegistry()

    registry.register(CalculatorTool())

    metadata = registry.metadata()

    assert len(metadata) == 1

    assert metadata[0].name == "calculator"

    assert "calculation" in metadata[0].description.lower()