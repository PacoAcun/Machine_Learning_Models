"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.10
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import split_dataset, train_model, evaluate_model, train_model_with_gridsearch, train_random_forest, evaluate_random_forest



def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=split_dataset, inputs=['autodf_scaled', 'params:test_size'], outputs=['X_train', 'X_test', 'y_train', 'y_test'], name='split_datasetnode'),
        node(func=train_model,inputs=['X_train','y_train'],outputs='model',name='train_model_node'),
        node(func=evaluate_model, inputs=['model','X_test', 'y_test'], outputs=None, name='evaluate_model_node'),    
        node(func=train_model_with_gridsearch, inputs=['X_train', 'y_train'], outputs=['optimized_model', 'best_params'], name='train_optimized_model_node'),
        node(func=train_random_forest, inputs=['X_train', 'y_train'], outputs='rf_model', name='train_random_forest_node'),
        node(func=evaluate_random_forest, inputs=['optimized_model', 'X_test', 'y_test'], outputs='optimized_model_rmse', name='evaluate_optimized_model_node'),
    ])