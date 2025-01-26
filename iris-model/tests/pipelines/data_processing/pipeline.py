from kedro.pipeline import Pipeline, pipeline, node
from .nodes import view_info

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=view_info,
            inputs='iris',
            outputs=None,
            name='view_info_node'
        )
    ])