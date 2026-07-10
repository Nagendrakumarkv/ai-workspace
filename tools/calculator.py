import ast
import operator
import logging

from tools.base import BaseTool


class CalculatorTool(BaseTool):
    """
    Tool for performing safe mathematical calculations.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Mod: operator.mod,
            ast.Pow: operator.pow,
        }

    @property
    def name(self) -> str:
        return "calculator"

    @property
    def description(self) -> str:
        return "Performs mathematical calculations."

    def execute(self, **kwargs):

        expression = kwargs.get("expression")

        if expression is None:
            raise ValueError("Expression is required.")

        self.logger.info(f"Calculating: {expression}")

        result = self._evaluate(expression)

        self.logger.info(f"Result: {result}")

        return result

    def _evaluate(self, expression: str):

        tree = ast.parse(expression, mode="eval")

        return self._visit(tree.body)

    def _visit(self, node):

        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.BinOp):

            left = self._visit(node.left)

            right = self._visit(node.right)

            operation = self.operators[type(node.op)]

            return operation(left, right)

        raise ValueError("Unsupported expression.")