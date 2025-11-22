import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/Khadar190798/Mlops_Project.mlflow/')
dagshub.init(repo_owner='Khadar190798', repo_name='Mlops_Project', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)