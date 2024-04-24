{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8c9cb1d9",
   "metadata": {
    "papermill": {
     "duration": 0.005341,
     "end_time": "2024-04-20T14:45:26.178287",
     "exception": false,
     "start_time": "2024-04-20T14:45:26.172946",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Documentação\n",
    "1. O foco será na aplicação de modelos combinamos afim de obter consitência nas previsões ao invés de uma posição atraente no `lb`.\n",
    "\n",
    "2. A abordagem será data-centric\n",
    "\n",
    "3. Este notebook será atualizado vagasoramente em ordem de melhorar o resultado final\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f93a3e0e",
   "metadata": {
    "papermill": {
     "duration": 0.003502,
     "end_time": "2024-04-20T14:45:26.185707",
     "exception": false,
     "start_time": "2024-04-20T14:45:26.182205",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Modelos\n",
    "\n",
    "1. XGBOOST: \n",
    "- Tem um problema que precisa subtrair '-1' da coluna y, para contagem começar no zero."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "98ba16ac",
   "metadata": {
    "papermill": {
     "duration": 0.003387,
     "end_time": "2024-04-20T14:45:26.192833",
     "exception": false,
     "start_time": "2024-04-20T14:45:26.189446",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Pipeline\n",
    "1. Numérico\n",
    "- StandardScaler()\n",
    "\n",
    "2. Categórico\n",
    "- OneHotEncoder"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0434d711",
   "metadata": {
    "papermill": {
     "duration": 0.003312,
     "end_time": "2024-04-20T14:45:26.199753",
     "exception": false,
     "start_time": "2024-04-20T14:45:26.196441",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## GridSearch\n",
    "1. Cross-Validation\n",
    "- Kfold: 5 pastas"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7cb5326b",
   "metadata": {
    "papermill": {
     "duration": 0.003272,
     "end_time": "2024-04-20T14:45:26.206558",
     "exception": false,
     "start_time": "2024-04-20T14:45:26.203286",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Código\n",
    "Estrutura para encontrar padrões nos dados para previsão da coluna `damage_grade`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2dad3ff3",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-04-20T14:45:26.215915Z",
     "iopub.status.busy": "2024-04-20T14:45:26.215233Z",
     "iopub.status.idle": "2024-04-20T14:45:29.185942Z",
     "shell.execute_reply": "2024-04-20T14:45:29.184696Z"
    },
    "papermill": {
     "duration": 2.978534,
     "end_time": "2024-04-20T14:45:29.188702",
     "exception": false,
     "start_time": "2024-04-20T14:45:26.210168",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "import seaborn as sns\n",
    "sns.set_style('whitegrid')\n",
    "plt.rcParams['figure.figsize'] = 10, 4\n",
    "plt.rcParams['font.size'] = 12\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "import xgboost as xgb\n",
    "\n",
    "from sklearn.feature_selection import SelectKBest, chi2\n",
    "from sklearn.preprocessing import OneHotEncoder, StandardScaler\n",
    "from sklearn.compose import ColumnTransformer\n",
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.model_selection import KFold, GridSearchCV\n",
    "from sklearn.metrics import roc_auc_score, make_scorer\n",
    "\n",
    "from sklearn.metrics import classification_report\n",
    "\n",
    "\n",
    "URL_TRAIN = '/kaggle/input/ml-olympiad-predicting-earthquake-damage/train.csv'\n",
    "URL_SAMPLE = '/kaggle/input/ml-olympiad-predicting-earthquake-damage/sample_submission.csv'\n",
    "URL_TEST = '/kaggle/input/ml-olympiad-predicting-earthquake-damage/test.csv'\n",
    "\n",
    "N_SAMPLE = 0\n",
    "TARGET = 'damage_grade'\n",
    "SEED = 101"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2196b701",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-04-20T14:45:29.197939Z",
     "iopub.status.busy": "2024-04-20T14:45:29.197346Z",
     "iopub.status.idle": "2024-04-20T14:45:33.282107Z",
     "shell.execute_reply": "2024-04-20T14:45:33.281059Z"
    },
    "papermill": {
     "duration": 4.092573,
     "end_time": "2024-04-20T14:45:33.285062",
     "exception": false,
     "start_time": "2024-04-20T14:45:29.192489",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/lib/python3.10/site-packages/sklearn/model_selection/_validation.py:778: UserWarning: Scoring failed. The score on this train-test partition for these parameters will be set to nan. Details: \n",
      "Traceback (most recent call last):\n",
      "  File \"/opt/conda/lib/python3.10/site-packages/sklearn/model_selection/_validation.py\", line 767, in _score\n",
      "    scores = scorer(estimator, X_test, y_test)\n",
      "  File \"/opt/conda/lib/python3.10/site-packages/sklearn/metrics/_scorer.py\", line 444, in _passthrough_scorer\n",
      "    return estimator.score(*args, **kwargs)\n",
      "  File \"/opt/conda/lib/python3.10/site-packages/sklearn/pipeline.py\", line 718, in score\n",
      "    Xt = transform.transform(Xt)\n",
      "  File \"/opt/conda/lib/python3.10/site-packages/sklearn/utils/_set_output.py\", line 140, in wrapped\n",
      "    data_to_wrap = f(self, X, *args, **kwargs)\n",
      "  File \"/opt/conda/lib/python3.10/site-packages/sklearn/compose/_column_transformer.py\", line 800, in transform\n",
      "    Xs = self._fit_transform(\n",
      "  File \"/opt/conda/lib/python3.10/site-packages/sklearn/compose/_column_transformer.py\", line 658, in _fit_transform\n",
      "    return Parallel(n_jobs=self.n_jobs)(\n",
      "  File \"/opt/conda/lib/python3.10/site-packages/sklearn/utils/parallel.py\", line 63, in __call__\n",
      "    return super().__call__(iterable_with_config)\n",
      "  File \"/opt/conda/lib/python3.10/site-packages/joblib/parallel.py\", line 1918, in __call__\n",
      "    return output if self.return_generator else list(output)\n",
      "  File \"/opt/conda/lib/python3.10/site-packages/joblib/parallel.py\", line 1847, in _get_sequential_output\n",
      "    res = func(*args, **kwargs)\n",
      "  File \"/opt/conda/lib/python3.10/site-packages/sklearn/utils/parallel.py\", line 123, in __call__\n",
      "    return self.function(*args, **kwargs)\n",
      "  File \"/opt/conda/lib/python3.10/site-packages/sklearn/pipeline.py\", line 876, in _transform_one\n",
      "    res = transformer.transform(X)\n",
      "  File \"/opt/conda/lib/python3.10/site-packages/sklearn/pipeline.py\", line 658, in transform\n",
      "    Xt = transform.transform(Xt)\n",
      "  File \"/opt/conda/lib/python3.10/site-packages/sklearn/utils/_set_output.py\", line 140, in wrapped\n",
      "    data_to_wrap = f(self, X, *args, **kwargs)\n",
      "  File \"/opt/conda/lib/python3.10/site-packages/sklearn/preprocessing/_encoders.py\", line 917, in transform\n",
      "    X_int, X_mask = self._transform(\n",
      "  File \"/opt/conda/lib/python3.10/site-packages/sklearn/preprocessing/_encoders.py\", line 174, in _transform\n",
      "    raise ValueError(msg)\n",
      "ValueError: Found unknown categories ['f'] in column 6 during transform\n",
      "\n",
      "  warnings.warn(\n",
      "/opt/conda/lib/python3.10/site-packages/sklearn/model_selection/_search.py:952: UserWarning: One or more of the test scores are non-finite: [nan]\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CPU times: user 13.6 s, sys: 155 ms, total: 13.8 s\n",
      "Wall time: 4.07 s\n"
     ]
    }
   ],
   "source": [
    "%%time\n",
    "\n",
    "# Carregar dados\n",
    "train = pd.read_csv(URL_TRAIN) \n",
    "\n",
    "# Separar dados de treino e teste\n",
    "X, y = train.drop(TARGET, axis=1), train[TARGET] - 1\n",
    "X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)\n",
    "\n",
    "# Parâmetros para o XGBOOST\n",
    "params =  {\n",
    "    \n",
    "    #\"classifier__booster\":['dart', 'gbtree', 'gblinear'], # Booster\n",
    "    #\"classifier__eta\": np.logspace(0, -2, num=2), # Learning rate\n",
    "    #\"classifier__max_depth\": np.arange(1, 100, 10) # Profundidade\n",
    "}\n",
    "\n",
    "# Modelo\n",
    "base_classifier = xgb.XGBClassifier(device=\"cpu\")\n",
    "\n",
    "# Definir transformações nos dados\n",
    "numeric_features = X.select_dtypes(exclude=['object']).columns\n",
    "numeric_transformer = Pipeline( # <- Aplicar Scaling aos dados\n",
    "        steps=[(\"scaler\", StandardScaler())]) \n",
    "\n",
    "categorical_features = X.select_dtypes(include=['object']).columns\n",
    "categorical_transformer = Pipeline(# <- Codificar as variáveis categóricas\n",
    "        steps=[(\"encoder\", OneHotEncoder(handle_unknown='error'))]) \n",
    "\n",
    "preprocessor = ColumnTransformer( # <- Combinar as transformações\n",
    "        transformers=[\n",
    "            (\"num\", numeric_transformer, numeric_features),\n",
    "            ('cat', categorical_transformer, categorical_features)])\n",
    "\n",
    "clf = Pipeline( # <- Combinar transformações e modelo escolhido\n",
    "        steps=[\n",
    "            (\"preprocessor\", preprocessor),\n",
    "            (\"classifier\", base_classifier)])\n",
    "\n",
    "# Método de validação cruzada\n",
    "kfold = KFold(n_splits=5) # <- Cinco pastas\n",
    "\n",
    "# Busca pelos melhores parâmetros\n",
    "grid = GridSearchCV( \n",
    "        clf,\n",
    "        param_grid={})\n",
    "\n",
    "model = grid.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2ff4232f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-04-20T14:45:33.295754Z",
     "iopub.status.busy": "2024-04-20T14:45:33.295354Z",
     "iopub.status.idle": "2024-04-20T14:45:33.347696Z",
     "shell.execute_reply": "2024-04-20T14:45:33.346495Z"
    },
    "papermill": {
     "duration": 0.060846,
     "end_time": "2024-04-20T14:45:33.350510",
     "exception": false,
     "start_time": "2024-04-20T14:45:33.289664",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.99      0.94      0.96       581\n",
      "           1       0.95      0.97      0.96      1590\n",
      "           2       0.96      0.94      0.95      1029\n",
      "\n",
      "    accuracy                           0.96      3200\n",
      "   macro avg       0.96      0.95      0.96      3200\n",
      "weighted avg       0.96      0.96      0.96      3200\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Avaliar em dados de treino\n",
    "y_hat_train = model.predict(X_train)\n",
    "report_train = classification_report(y_train, y_hat_train)\n",
    "print(report_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "310ac5ff",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-04-20T14:45:33.361011Z",
     "iopub.status.busy": "2024-04-20T14:45:33.360365Z",
     "iopub.status.idle": "2024-04-20T14:45:33.394304Z",
     "shell.execute_reply": "2024-04-20T14:45:33.393359Z"
    },
    "papermill": {
     "duration": 0.042128,
     "end_time": "2024-04-20T14:45:33.396888",
     "exception": false,
     "start_time": "2024-04-20T14:45:33.354760",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.65      0.52      0.58       148\n",
      "           1       0.50      0.59      0.54       378\n",
      "           2       0.44      0.38      0.41       274\n",
      "\n",
      "    accuracy                           0.51       800\n",
      "   macro avg       0.53      0.50      0.51       800\n",
      "weighted avg       0.51      0.51      0.50       800\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Avaliar em dados de teste\n",
    "y_hat_test = model.predict(X_val)\n",
    "report_train = classification_report(y_val, y_hat_test)\n",
    "print(report_train)"
   ]
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [
    {
     "databundleVersionId": 7801946,
     "sourceId": 71128,
     "sourceType": "competition"
    }
   ],
   "dockerImageVersionId": 30699,
   "isGpuEnabled": false,
   "isInternetEnabled": true,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 11.087424,
   "end_time": "2024-04-20T14:45:34.123774",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2024-04-20T14:45:23.036350",
   "version": "2.5.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
