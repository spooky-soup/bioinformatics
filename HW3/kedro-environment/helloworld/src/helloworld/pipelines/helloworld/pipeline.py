from kedro.pipeline import Pipeline, node

from .nodes import hello_world


def create_pipeline(**kwargs):
    return Pipeline([node(hello_world, inputs=None, outputs="hello-output")])
