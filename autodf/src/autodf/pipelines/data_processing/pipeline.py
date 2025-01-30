"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.10
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import process_data, add_volume, scale_features


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=process_data, inputs='autodf_raw', outputs='autodf_intermediate', name='process_data_node'),
        node(func=add_volume, inputs='autodf_intermediate', outputs='autodf', name='add_volume_node'),
        node(func=scale_features, inputs='autodf', outputs='autodf_scaled', name='scale_feature_node'), 
    ])