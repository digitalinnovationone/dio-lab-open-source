import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import scipy
# ==================================

from sklearn.model_selection import (train_test_split, KFold, StratifiedKFold, cross_validate,
                                     GridSearchCV, RandomizedSearchCV)

from sklearn.metrics import (r2_score, mean_absolute_error, mean_squared_error, mean_absolute_percentage_error,
                             ConfusionMatrixDisplay, classification_report, precision_recall_curve, 
                             PrecisionRecallDisplay, RocCurveDisplay,
                             recall_score, make_scorer, roc_auc_score)

from sklearn.preprocessing import MinMaxScaler, StandardScaler, PolynomialFeatures, OneHotEncoder, OrdinalEncoder

from sklearn.pipeline import Pipeline

from sklearn.decomposition import PCA

from sklearn.impute import SimpleImputer

from sklearn.compose import ColumnTransformer

from sklearn.base import BaseEstimator, TransformerMixin

# ==================================

from sklearn.linear_model import LogisticRegression

from sklearn.svm import SVC

from sklearn.neighbors import KNeighborsClassifier

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier, RandomForestClassifier

from xgboost import XGBClassifier

from lightgbm import LGBMClassifier

# ==================================

from sklearn.linear_model import LinearRegression, Lasso, Ridge

from sklearn.svm import SVR

from sklearn.neighbors import KNeighborsRegressor

from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import GradientBoostingRegressor, AdaBoostRegressor, RandomForestRegressor

from xgboost import XGBRegressor

from lightgbm import LGBMRegressor

# ================================================================================= #
# ================================================================================= #

def plot_scatter_real_pred(y_test, y_pred):
    
    x = np.linspace(0, y_test.max())
    y = x

    plt.title("Target real x target predito")
    
    plt.plot(x, y, color="red", ls=":")

    sns.scatterplot(x=y_test, y=y_pred)

    plt.xlabel("Real")
    plt.ylabel("Predito")

    plt.show()

def calc_r2_adj(r2, y, X):
    
    return 1 - (1-r2)*(len(y) - 1)/(len(y) - X.shape[1] - 1)


def calc_reg_metrics(model, X, y, label="", plot=False, dist_resids=True, print_stuff=True):
    
    y_pred = model.predict(X)

    if print_stuff:
        print(f"\nMétricas de avaliação (dados de {label}):\n")

    if plot:
        plot_scatter_real_pred(y, y_pred)

    r2 = r2_score(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    mape = mean_absolute_percentage_error(y, y_pred)

    if print_stuff:
        print(f"R^2: {r2:.2f}")
        print(f"MAE: {mae:.2f}")
        print(f"RMSE: {rmse:.2f}")
        print(f"MAPE: {mape:.2%}")

    if dist_resids:
        residuos = y - y_pred
        print(f"\nDistribuição dos resíduos de {label}:\n")
        print(pd.Series(residuos).describe())

    if plot:
        sns.histplot(residuos, kde=True)
        plt.show()
        
    # retorna um dicionário com as métricas
    metrics_dict = {"r2" : r2, 
                    "mae" : mae,
                    "rmse" : rmse,
                    "mape" : mape}
    
    return metrics_dict

def reg_metrics_train_test(model, X_train, y_train, X_test, y_test, 
                           plot=False, dist_resids=True, print_stuff=True):
    '''
    wrapper pras métricas de regressão, treino e teste
    '''
    
    dict_metrics_train = calc_reg_metrics(model, X_train, y_train, 
                                          label="treino", 
                                          plot=plot, dist_resids=dist_resids, print_stuff=print_stuff)

    print()
    print("#"*80)

    dict_metrics_test = calc_reg_metrics(model, X_test, y_test, 
                                         label="teste",
                                         plot=plot, dist_resids=dist_resids, print_stuff=print_stuff)

    return dict_metrics_train, dict_metrics_test
    

# ================================================================================= #
# ================================================================================= #

def reg_lin_pt1_pt2(X_train, y_train, X_test, y_test, 
                    plot=True, scale_mms=False, 
                    train_metrics=True, dist_resids=False):

    if scale_mms:

        mms = MinMaxScaler().fit(X_train)

        # passamos assim, pra carregar o nome das features, e ter o .feature_names_in_
        X_train = pd.DataFrame(mms.transform(X_train), columns=X_train.columns, index=X_train.index)
        X_test = pd.DataFrame(mms.transform(X_test), columns=X_test.columns, index=X_test.index)
    
    # ===============================
    # passo 1 - construção do modelo

    reglin = LinearRegression()

    reglin.fit(X_train, y_train)

    # ===============================
    # passo 2 - avaliação do modelo
    
    if train_metrics:
        _ = calc_reg_metrics(reglin, X_train, y_train, label="treino", 
                             plot=plot, dist_resids=dist_resids, print_stuff=True)
        print()
        print("#"*50)
        
    _ = calc_reg_metrics(reglin, X_test, y_test, label="teste", 
                         plot=plot, dist_resids=dist_resids, print_stuff=True)

    # new: returnando o objeto do modelo treinado!
    return reglin

# ================================================================================= #
# ================================================================================= #

def plot_reglin_model(modelo, X_train, y_train, X_test, y_test): 
    
    plt.title("Modelo de regressão linear")

    plt.scatter(X_train, y_train)
    plt.scatter(X_test, y_test, alpha=0.5)

    x_plot_modelo = np.linspace(X_train.min(), X_train.max(), 100000)

    # f_h = b0 + b1*x + b2*x^2 + ... + bn*x^n
    # aqui começamos com f_h = b0
    y_plot_modelo = modelo.intercept_ 

    # aqui vem o resto, b1*x + b2*x^2 + ... + bn*x^n
    for n, b_n in enumerate(modelo.coef_):

        y_plot_modelo = y_plot_modelo + b_n*(x_plot_modelo**(n+1))

    plt.plot(x_plot_modelo, y_plot_modelo, color="red")
    plt.show()

def reg_lin_poly_features(X_train, y_train, X_test, y_test, 
                          deg=1,
                          plot=True, scale_mms=False, 
                          train_metrics=True, 
                          dist_resids=True,
                          plot_model=False):
    
    # dimensão dos dados de input
    data_dim = X_train.shape[1]
    
    # é importante salvar os dados originais pra plotá-los!
    # isso é importante pra caso haja transformação no espaço de features
    X_train_orig = X_train.copy()
    X_test_orig = X_test.copy()
    
    if deg > 1:
        
        pf = PolynomialFeatures(degree=deg, include_bias=False).fit(X_train)
        
        X_train = pf.transform(X_train)
        X_test = pf.transform(X_test)
        
        print(f"Modelo com espaço de features transformado!\n")
        print(f"Número de features original: {pf.n_features_in_}")
        print(f"Número de features após o transformer: {pf.n_output_features_}\n")
        print("="*50)
        
    # é importante escalar depois!
    if scale_mms:

        mms = MinMaxScaler().fit(X_train)

        # não to trazendo o nome das colunas, então não vai mais ter o atributo feature_names_in_!
        # caso queira/precise, tem que alterar a função
        X_train = mms.transform(X_train)
        X_test = mms.transform(X_test)

    # ===============================
    # passo 1 - construção do modelo

    reglin = LinearRegression()

    reglin.fit(X_train, y_train)

    # ===============================
    # passo 2 - avaliação do modelo
    
    if train_metrics:
        metrics_train = calc_reg_metrics(reglin, X_train, y_train, label="treino", 
                                         plot=plot, dist_resids=dist_resids, print_stuff=True)
        print()
        print("#"*50)
    else:
        metrics_train = None
        
    metrics_test = calc_reg_metrics(reglin, X_test, y_test, label="teste",
                                     plot=plot, dist_resids=dist_resids, print_stuff=True)
    
    # só é possível quando temos uma única feature no espaço de features original!
    if plot_model and data_dim == 1:
        # note que passamos as features originais!!
        plot_reglin_model(reglin, X_train_orig, y_train, X_test_orig, y_test)

    # new: returnando o objeto do modelo treinado!
    return reglin, metrics_train, metrics_test

# ================================================================================= #
# ================================================================================= #

def reg_lin_poly_features_regularized(X_train, y_train, X_test, y_test, 
                                      deg=1,
                                      type_regularization=None, alpha=1, l1_ratio=0.5,
                                      iter_max=1000,
                                      plot=True, scale_mms=False, 
                                      train_metrics=True, 
                                      dist_resids=True,
                                      plot_model=False):
    '''
    docstring
    - type_regularization: None, "l1", "l2", "en"
    '''
    
    # dimensão dos dados de input
    data_dim = X_train.shape[1]
    
    # é importante salvar os dados originais pra plotá-los!
    # isso é importante pra caso haja transformação no espaço de features
    X_train_orig = X_train.copy()
    X_test_orig = X_test.copy()
    
    if deg > 1:
        
        pf = PolynomialFeatures(degree=deg, include_bias=False).fit(X_train)
        
        X_train = pf.transform(X_train)
        X_test = pf.transform(X_test)
        
        print(f"Modelo com espaço de features transformado!\n")
        print(f"Número de features original: {pf.n_features_in_}")
        print(f"Número de features após o transformer: {pf.n_output_features_}\n")
        print("="*50)
        
    # é importante escalar depois!
    # note que o "or type_regularization" garante que haja normalização 
    # se a regulatrização for usada, mesmo que "scale_mms" seja False ;)
    if scale_mms or type_regularization:

        mms = MinMaxScaler().fit(X_train)

        # não to trazendo o nome das colunas, então não vai mais ter o atributo feature_names_in_!
        # caso queira/precise, tem que alterar a função
        X_train = mms.transform(X_train)
        X_test = mms.transform(X_test)

    # ===============================
    # passo 1 - construção do modelo
    
    if type_regularization == "l1":
        
        model = Lasso(alpha=alpha, max_iter=iter_max).fit(X_train, y_train)
        
    elif type_regularization == "l2":
        
        model = Ridge(alpha=alpha, max_iter=iter_max).fit(X_train, y_train)
        
    elif type_regularization == "en":
        
        model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, max_iter=iter_max).fit(X_train, y_train)
        
    elif type_regularization == None:
    
        model = LinearRegression().fit(X_train, y_train)
        
    else:
        
        list_opcoes = ["l1", "l2", "en", None]
        raise ValueError(f"Opção de regularização indisponível!\nOpções aceitas: {list_opcoes}")


    # ===============================
    # passo 2 - avaliação do modelo
    
    if train_metrics:
        metrics_train = calc_reg_metrics(model, X_train, y_train, label="treino", 
                                         plot=plot, dist_resids=dist_resids, print_stuff=True)
        print()
        print("#"*50)
    else:
        metrics_train = None
        
    metrics_test = calc_reg_metrics(model, X_test, y_test, label="teste",
                                     plot=plot, dist_resids=dist_resids, print_stuff=True)
    
    # só é possível quando temos uma única feature no espaço de features original!
    if plot_model and data_dim == 1:
        # note que passamos as features originais!!
        plot_reglin_model(model, X_train_orig, y_train, X_test_orig, y_test)

    # new: returnando o objeto do modelo treinado!
    return model, metrics_train, metrics_test

# ================================================================================= #
# ================================================================================= #

def calc_f1_score(p, r):
    
    return 2/((1/p) + (1/r))

def plot_prec_rec_f1_curve(y_real, proba, pos_label=None):

    precisions, recalls, cutoffs = precision_recall_curve(y_real, proba, pos_label=pos_label)
    
    # ============================
    
    f1_scores = calc_f1_score(precisions[:-1], recalls[:-1])
    
    # ============================
    
    plt.title("Precision-recall tradeoff")

    plt.plot(cutoffs, precisions[:-1], label="precision")
    plt.plot(cutoffs, recalls[:-1], label="recall")
    plt.plot(cutoffs, f1_scores, label="f1 score")

    plt.xlabel("Cutoffs")

#     ponto_de_encontro = cutoffs[np.where(precisions == recalls)]
#     plt.axvline(x=ponto_de_encontro, ls=":", color="k")

    plt.legend()
    plt.show()

def clf_metrics(modelo, X, y, cutoff=0.5, label_metrica="", 
                print_plot=True, plot_conf_matrix=True, print_cr=True,
                plot_prc=False, plot_roc=False, pos_label=None):

    classes = modelo.classes_
        
    n_classes = len(classes)
    
    # pro caso binario
    if n_classes == 2:

        classes = modelo.classes_.tolist()

        # aqui eu identifico qual é a possição, na lista das classes, referente à classe positiva de interesse
        idx_classe_positiva = classes.index(pos_label)

        # pego a probabilidade de pertencimento à classe positiva (pelo indice, que é a variavel que criei acima)
        probas = modelo.predict_proba(X)[:, idx_classe_positiva]

        # pra facilitatr o y_pred abaixo, eu removo da lista de classes a minha classe de interesse (positiva)
        # ou seja, a unica coisa que sobra é a classe negativa!!
        classes.remove(pos_label)

        # a predição é o que esperávamos: predizemos a classe positiva se p >= cutoff
        # caso contrario, a classe negativa (que é a unica coisa que sobra na listsa "classes")
        y_pred = np.where(probas >= cutoff, pos_label, classes[0])
    
    # pro caso multiclasse
    else:
        # as probabilidades de todas as classes (pq aqui é multiclasse)
        probas_all = modelo.predict_proba(X)
        y_pred = classes[probas_all.argmax(axis=1)]
        
    if print_plot:
        
        if n_classes == 2:
            print(f"Métricas de avaliação de {label_metrica} - com cutoff = {cutoff:.2f}")
        
        # no caso multiclasse, o cutoff não é relevante
        else:
            print(f"Métricas de avaliação de {label_metrica}")
            
        if plot_conf_matrix:
            ConfusionMatrixDisplay.from_predictions(y, y_pred)
            plt.show()
    
        if print_cr:
            print(classification_report(y, y_pred))
        
        # apenas plotaremos as métricas que variam o cutoff pro caso binário!
        if n_classes == 2:
            
            if plot_prc or plot_roc:
                
                print("="*80)
                print("Abaixo, métricas que variam o cutoff".center(80))
                print(f"Classe positiva: {pos_label}".center(80))
                print("="*80)

            if plot_prc:
                PrecisionRecallDisplay.from_predictions(y, probas, pos_label=pos_label)
                plt.show()

                plot_prec_rec_f1_curve(y, probas, pos_label=pos_label)

            if plot_roc:
                disp = RocCurveDisplay.from_predictions(y, probas, pos_label=pos_label)
                disp.ax_.set_title(f"AUC: {roc_auc_score(y, probas):.3f}", fontsize=16)

                x = np.linspace(0, 1, 2)
                plt.plot(x, x, color="k", ls=":")

                plt.show()
    
    return classification_report(y, y_pred, output_dict=True)

def clf_metrics_train_test(modelo, X_train, y_train, X_test, y_test, cutoff=0.5, 
                           print_plot=True, plot_conf_matrix=True, print_cr=True,
                           plot_prc=False, plot_roc=False, pos_label=None):
    '''
    wrapper pra ambas as métricas de treino e teste
    '''
    
    cr_train = clf_metrics(modelo, X_train, y_train, cutoff=cutoff, label_metrica="treino", 
                           print_plot=print_plot, plot_conf_matrix=plot_conf_matrix, print_cr=print_cr,
                           plot_prc=plot_prc, plot_roc=plot_roc, pos_label=pos_label)

    print()
    print("#"*80)
    print()

    cr_test = clf_metrics(modelo, X_test, y_test, cutoff=cutoff, label_metrica="teste", 
                          print_plot=print_plot, plot_conf_matrix=plot_conf_matrix, print_cr=print_cr,
                          plot_prc=plot_prc, plot_roc=plot_roc, pos_label=pos_label)
    
    return cr_train, cr_test

# ================================================================================= #
# ================================================================================= #

def extrai_nome_metrica(str_metrica):
    '''
    - str_metrica: alguma string de metrica do sklearn, que sai do cross_validate com o prefixo "train_" ou "test_"
    (veja aqui os exemplos: https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter)
    
    - type_metric: "train_" ou "test_", dependendo do que temos
    '''
    
    type_metric = str_metrica.split("_")[0] + "_"
    
    return str_metrica.split(type_metric)[-1].replace("neg_", "").replace("_", " ")

def calc_cv(estimator, X, y, n_splits, scoring, n_jobs=-1, verbose=10, plot_distros=False, stratified=False):
    '''
    realiza a validação cruzada para um determinado estimador e conjunto de dados.
    pode receber várias métricas em `scoring`
    '''
    if stratified:
        kf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    else:
        kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    
    results_cv = cross_validate(estimator=estimator,
                                X=X, y=y,
                                cv=kf, scoring=scoring,
                                return_train_score=True,
                                n_jobs=n_jobs, 
                                verbose=verbose)

    # .abs() pra deixar as métricas positivas
    results_cv_df = pd.DataFrame(results_cv).abs()
    
    # ================================================
    
    colunas_metricas = results_cv_df.columns.tolist()[2:]

    for i in range(0, len(colunas_metricas), 2):

        # colunas de teste e treino
        col_test, col_train = colunas_metricas[i], colunas_metricas[i+1]

        # estrai o "test_", e dá apenas a string referente à metrica (sem o underline!!)
        str_metrica = extrai_nome_metrica(col_test)

        print(f"\nDistribuição da métrica de avaliação {str_metrica}:")

        display(results_cv_df[[col_test, col_train]].describe())
        
        # ================================================

        if plot_distros:
            
            print(f"\nDistribuição de {str_metrica} de treino")
            sns.histplot(data=results_cv_df, x=col_train, kde=True, color="orange")
            plt.show()

            print(f"\nDistribuição de {str_metrica} de teste")
            sns.histplot(data=results_cv_df, x=col_test, kde=True)
            plt.show()

            print("\nAs duas juntas (compara a variância!)")
            sns.histplot(data=results_cv_df, x=col_train, kde=True, color="orange", label="treino")
            sns.histplot(data=results_cv_df, x=col_test, kde=True, label="teste")
            plt.legend()
            plt.show()

        print("#"*80)
    
    # ================================================
    
    return results_cv_df

# ================================================================================= #
# ================================================================================= #

def calc_best_params_delta(grid, peso_delta=0.5, print_deltas=False):
    '''
    to-do: docsting
    
    - grid: é um objeto gridsearch já fitado!
    '''
    
    cv_results_df = pd.DataFrame(grid.cv_results_)

    aux = cv_results_df[['mean_train_score', 'mean_test_score']].copy()

    # esse será nosso novo critério: comparando treino e teste!!!
    # assim, evitamos overfitting!
    aux["delta"] = (aux["mean_train_score"] - aux["mean_test_score"]).abs()

    # vamos normalizar tanto as métricas quanto o delta pro intervalo (0.1, 0.9)
    # (nao deixei (0, 1) pra nao zerar as coisas)
    # com isso, podemos tratar de maneira unificada tanto problemas de regressão quanto classificação
    aux_norm = pd.DataFrame(MinMaxScaler((0.1, 0.9)).fit_transform(aux), 
                            columns=[f"{x}_norm" for x in aux.columns], index=aux.index)

    # considere:
    # - w: o peso que colocamos no delta (1-w, portanto, é o peso que colocamos na métrica de teste);
    # - d: delta;
    # - m: a métrica de teste;
    # a métrica final, que é MAXIMIZADA, é a seguinte:
    # (w*(1-d)) + ((1-w)*m)
    # quero maximizar essa métrica final, com o objetivo de MAXIMIZAR métrica de teste e ao mesmo tempo o MINIMIZAR o delta
    # pra esse fim, somo as duas contribuições, tomando a métrica em si, e o complementar do delta, ponderados respectivamente
    # com isso, consigo um ponto de equilibrio legal!
    aux_norm["metrica_criterio_final"] = (peso_delta*(1-aux_norm["delta_norm"])) + ((1-peso_delta)*aux_norm["mean_test_score_norm"])

    aux = pd.concat([aux, aux_norm], axis=1).sort_values("metrica_criterio_final", ascending=False)
    
    if print_deltas:
        display(aux)

    # esse é o indice correspondente à melhor métrica de critério final
    # (note que já ordenamos acima, então a melhor métrica é a primeira linha!)
    num_combinacao_melhor_delta = aux.iloc[0, :].name

    # isso dá os melhores parametros, segundo o critério do delta!!
    best_params_delta = cv_results_df.loc[num_combinacao_melhor_delta, "params"]

    return best_params_delta

# ================================================================================= #
# ================================================================================= #

def pca_eda(X, y, n_components):
    '''
    n_components: 2 ou 3
    '''
    
    pipe_pca = Pipeline([("ss", StandardScaler()),
                         ("pca", PCA(n_components=n_components))]).fit(X)

    X_pca = pd.DataFrame(pipe_pca.transform(X), index = X.index,
                         columns=[f"PC{i+1}" for i in range(n_components)])
    
    X_pca_y = pd.concat([X_pca, y], axis=1)
    
    target_name = y.name
    
    # =======================================

    if n_components == 2:
        
        g = sns.jointplot(data=X_pca_y, x="PC1", y="PC2", hue=target_name)
        
        g.fig.suptitle(f"Projeção dos dados nas 2 componentes principais", y=1.08)

        plt.show()
        
    elif n_components == 3:
        
        fig = plt.figure(figsize=(8, 8))

        ax = fig.add_subplot(111, projection='3d')
        ax.set_title(f"Projeção dos dados nas 3 componentes principais")

        for level in y.unique():

            X_level = X_pca_y.query(f"{target_name} == '{level}'")

            ax.scatter(X_level["PC1"], X_level["PC2"], X_level["PC3"], label=level)

        ax.legend()
        plt.show()
        
    else:
        
        print("Não é possível visualizar em mais de 3 dimensões!")

# ================================================================================= #
# ================================================================================= #


# ================================================================================= #
# ================================================================================= #


# ================================================================================= #
# ================================================================================= #


# ================================================================================= #
# ================================================================================= #


# ================================================================================= #
# ================================================================================= #
