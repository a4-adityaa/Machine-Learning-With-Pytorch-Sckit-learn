<a id="top"></a>

<div align="center">

# 🧠 Machine Learning with PyTorch and Scikit-Learn
### My learning journey through the book by Raschka, Liu & Mirjalili

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-deep%20learning-EE4C2C?logo=pytorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-classical%20ML-F7931E?logo=scikitlearn&logoColor=white)

**[Book](#book-info) · [Objectives](#objectives) · [Roadmap](#roadmap) · [Chapters](#chapters) · [Cross-Cutting Topics](#cross-cutting) · [Structure](#structure) · [Workflow](#workflow) · [Philosophy](#philosophy) · [Progress](#progress)**

</div>

---

## 📌 Introduction

This repository is a **public learning log** for *Machine Learning with PyTorch and Scikit-Learn*. I am working through the book chapter by chapter and recording what I actually understand: my own explanations, my own implementations, and my own experiments.

It is organized as a **navigation hub and roadmap**. Every chapter has a dedicated folder with three parts:

| Folder | Purpose |
|:--|:--|
| 📝 `notes/` | Detailed explanations in my own words: intuition, math, pitfalls |
| 💻 `code/` | Implementations: from-scratch versions and library versions |
| 🧪 `experiments/` | Things I tried beyond the book, with hypotheses and observations |

> ⚠️ **Status:** Just started. Every checkbox in this README is intentionally **unchecked**. Boxes get ticked only when the corresponding notes, code, and experiments exist in this repo.

> 📚 **Copyright note:** This repository does not reproduce the book's text, figures, or code. Everything here is written independently. To follow along properly, please get the book and use the authors' official code repository, linked below.

<p align="right"><a href="#top">⬆ back to top</a></p>

---

<a id="book-info"></a>
## 📖 About the Book

| | |
|:--|:--|
| **Title** | *Machine Learning with PyTorch and Scikit-Learn: Develop machine learning and deep learning models with Python* |
| **Authors** | Sebastian Raschka, Yuxi (Hayden) Liu, Vahid Mirjalili |
| **Foreword** | Dmytro Dzhulgakov |
| **Publisher** | Packt Publishing |
| **Published** | February 25, 2022 (1st edition) |
| **Length** | 774 pages (per Packt) |
| **ISBN-13** | 978-1801819312 |
| **Chapters** | 19 |
| **Prerequisites** | Python basics, plus a working grasp of calculus and linear algebra (as stated by the publisher) |

**Official links**
- 🔗 [Authors' code repository (`rasbt/machine-learning-book`)](https://github.com/rasbt/machine-learning-book)
- 🔗 [Packt book page and table of contents](https://www.packtpub.com/en-us/product/machine-learning-with-pytorch-and-scikit-learn-9781801819312)
- 🔗 [Sebastian Raschka's blog post on what is new in this book](https://sebastianraschka.com/blog/2022/ml-pytorch-book.html)

**How the author describes the structure:** the first ten chapters teach machine learning with scikit-learn, Chapter 11 is the turning point where a neural network is built from scratch in NumPy, and the second half focuses on deep learning with PyTorch, closing with reinforcement learning. The book began as a planned 4th edition of *Python Machine Learning* but was rewritten enough to get a new title, with the deep learning code moved from TensorFlow to PyTorch and with new chapters on transformers and graph neural networks.

**Software the book was written with:** Python 3.9, NumPy 1.21.2, SciPy 1.7.0, scikit-learn 1.0, Matplotlib 3.4.3, pandas 1.3.2. I will use current versions where possible and record any breaking differences I run into in the relevant notes.

<p align="right"><a href="#top">⬆ back to top</a></p>

---

<a id="objectives"></a>
## 🎯 Learning Objectives

By the end of this journey I want to be able to:

- [ ] Explain the three learning paradigms (supervised, unsupervised, reinforcement) and pick the right one for a problem
- [ ] Implement the perceptron, Adaline, logistic regression, and linear regression from scratch, and explain the gradient-based learning behind them
- [ ] Build clean, leak-free scikit-learn workflows: preprocessing, pipelines, cross-validation, and hyperparameter search
- [ ] Choose and interpret evaluation metrics correctly, including for imbalanced data
- [ ] Derive and implement backpropagation for a multilayer network in plain NumPy
- [ ] Use PyTorch confidently: tensors, autograd, `Dataset`/`DataLoader`, `nn.Module`, optimizers, and PyTorch Lightning
- [ ] Build and train CNNs, RNNs/LSTMs, transformers, GANs, and graph neural networks
- [ ] Explain self-attention and the transformer architecture, and fine-tune a pre-trained language model
- [ ] Understand the core reinforcement learning ideas (MDPs, Bellman equations, Q-learning, DQN)
- [ ] Run my own small experiments, record the results honestly, and reason about *why* things behaved as they did

<p align="right"><a href="#top">⬆ back to top</a></p>

---

<a id="roadmap"></a>
## 🗺️ Roadmap at a Glance

I group the 19 chapters into three study phases. This grouping is mine, based on the author's own description of the book's structure.

| Phase | Chapters | Theme | Main tools |
|:--|:--|:--|:--|
| 🟦 **Phase 1: Foundations & classical ML** | 1 – 10 | Learning paradigms, classifiers, preprocessing, evaluation, ensembles, text, regression, clustering | NumPy, scikit-learn, pandas, Matplotlib |
| 🟧 **Phase 2: Neural networks, from scratch to PyTorch** | 11 – 13 | Backpropagation by hand, then PyTorch training and internals | NumPy, PyTorch, PyTorch Lightning |
| 🟥 **Phase 3: Advanced deep learning & RL** | 14 – 19 | CNNs, RNNs, transformers, GANs, GNNs, reinforcement learning | PyTorch, Hugging Face Transformers, PyTorch Geometric, Gym |

### Chapter index

| # | Chapter | Focus | Folder |
|:-:|:--|:--|:--|
| 1 | [Giving Computers the Ability to Learn from Data](#ch01) | Big picture, terminology, workflow | [`ch01`](chapters/ch01-intro-to-ml/) |
| 2 | [Training Simple Machine Learning Algorithms for Classification](#ch02) | Perceptron, Adaline, gradient descent | [`ch02`](chapters/ch02-simple-classification-algorithms/) |
| 3 | [A Tour of Machine Learning Classifiers Using Scikit-Learn](#ch03) | Logistic regression, SVM, trees, KNN | [`ch03`](chapters/ch03-sklearn-classifiers-tour/) |
| 4 | [Building Good Training Datasets – Data Preprocessing](#ch04) | Missing data, encoding, scaling, feature selection | [`ch04`](chapters/ch04-data-preprocessing/) |
| 5 | [Compressing Data via Dimensionality Reduction](#ch05) | PCA, LDA, t-SNE | [`ch05`](chapters/ch05-dimensionality-reduction/) |
| 6 | [Learning Best Practices for Model Evaluation and Hyperparameter Tuning](#ch06) | Pipelines, CV, curves, grid search, metrics | [`ch06`](chapters/ch06-model-evaluation-and-tuning/) |
| 7 | [Combining Different Models for Ensemble Learning](#ch07) | Voting, bagging, boosting | [`ch07`](chapters/ch07-ensemble-learning/) |
| 8 | [Applying Machine Learning to Sentiment Analysis](#ch08) | Text processing, bag-of-words, topic modeling | [`ch08`](chapters/ch08-sentiment-analysis/) |
| 9 | [Predicting Continuous Target Variables with Regression Analysis](#ch09) | Linear, robust, regularized, nonlinear regression | [`ch09`](chapters/ch09-regression-analysis/) |
| 10 | [Working with Unlabeled Data – Clustering Analysis](#ch10) | k-means, hierarchical, DBSCAN | [`ch10`](chapters/ch10-clustering/) |
| 11 | [Implementing a Multilayer Artificial Neural Network from Scratch](#ch11) | MLP and backpropagation in NumPy | [`ch11`](chapters/ch11-neural-network-from-scratch/) |
| 12 | [Parallelizing Neural Network Training with PyTorch](#ch12) | Tensors, data pipelines, first PyTorch models | [`ch12`](chapters/ch12-pytorch-training/) |
| 13 | [Going Deeper – The Mechanics of PyTorch](#ch13) | Graphs, autograd, `torch.nn`, Lightning | [`ch13`](chapters/ch13-pytorch-mechanics/) |
| 14 | [Classifying Images with Deep Convolutional Neural Networks](#ch14) | Convolutions, CNNs, image classification | [`ch14`](chapters/ch14-deep-cnns/) |
| 15 | [Modeling Sequential Data Using Recurrent Neural Networks](#ch15) | RNNs, LSTMs, sequence tasks | [`ch15`](chapters/ch15-rnns/) |
| 16 | [Transformers – Improving Natural Language Processing with Attention Mechanisms](#ch16) | Attention, transformers, GPT/BERT/BART | [`ch16`](chapters/ch16-transformers/) |
| 17 | [Generative Adversarial Networks for Synthesizing New Data](#ch17) | GANs, DCGAN, Wasserstein GAN | [`ch17`](chapters/ch17-gans/) |
| 18 | [Graph Neural Networks for Capturing Dependencies in Graph Structured Data](#ch18) | Graph convolutions, GNNs | [`ch18`](chapters/ch18-graph-neural-networks/) |
| 19 | [Reinforcement Learning for Decision Making in Complex Environments](#ch19) | MDPs, Q-learning, deep Q-learning | [`ch19`](chapters/ch19-reinforcement-learning/) |

<p align="right"><a href="#top">⬆ back to top</a></p>

---

<a id="chapters"></a>
## 📚 Chapter-by-Chapter Roadmap

Each chapter below lists the book's major sections as checkboxes, plus a map of concepts, algorithms, math, and tooling. Expand a chapter with the ▶ arrow. Section titles follow the publisher's table of contents; the descriptions are my own summaries.

---

# 🟦 Phase 1: Foundations & Classical ML (Chapters 1–10)

<a id="ch01"></a>
### Chapter 1: Giving Computers the Ability to Learn from Data
> Sets the stage: what machine learning is, the three learning types, notation, and the general workflow for building a predictive system.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] Building intelligent machines to transform data into knowledge
- [ ] The three different types of machine learning
- [ ] Introduction to the basic terminology and notations
- [ ] A roadmap for building machine learning systems
- [ ] Using Python for machine learning

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | Supervised, unsupervised, and reinforcement learning; classification vs. regression; clustering; dimensionality reduction; features/targets/examples; the predictive-modeling workflow (preprocess, train and select, evaluate, predict); Python environment setup |
| 🤖 Algorithms / models | None implemented; conceptual overview only |
| ➗ Mathematics | Feature-matrix and vector notation, basic linear-algebra conventions used throughout the book |
| 🧰 scikit-learn | Introduced as the main library for the following chapters; setup only |
| 🔥 PyTorch | Not yet (installation is covered in Chapter 12) |
| 🛠️ From scratch | None |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch01-intro-to-ml/notes/) · `[ ]` 💻 [code](chapters/ch01-intro-to-ml/code/) · `[ ]` 🧪 [experiments](chapters/ch01-intro-to-ml/experiments/)

</details>

<a id="ch02"></a>
### Chapter 2: Training Simple Machine Learning Algorithms for Classification
> Builds the earliest learning algorithms by hand and introduces gradient descent as the core optimization idea.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] Artificial neurons – a brief glimpse into the early history of machine learning
- [ ] Implementing a perceptron learning algorithm in Python
- [ ] Adaptive linear neurons and the convergence of learning

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | Artificial neuron model, net input and thresholding, perceptron learning rule, linear separability and convergence, learning rate, cost-function minimization, feature standardization, batch vs. stochastic gradient descent |
| 🤖 Algorithms / models | Perceptron, Adaline (adaptive linear neuron) |
| ➗ Mathematics | Dot products, weight-update rules, sum-of-squared-errors cost, partial derivatives, gradient descent, standardization |
| 🧰 scikit-learn | None (introduced in Chapter 3) |
| 🔥 PyTorch | None |
| 🛠️ From scratch | Perceptron and Adaline (gradient descent and stochastic variant) with NumPy |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch02-simple-classification-algorithms/notes/) · `[ ]` 💻 [code](chapters/ch02-simple-classification-algorithms/code/) · `[ ]` 🧪 [experiments](chapters/ch02-simple-classification-algorithms/experiments/)

</details>

<a id="ch03"></a>
### Chapter 3: A Tour of Machine Learning Classifiers Using Scikit-Learn
> A guided tour of the main classical classifiers and when each one is a reasonable choice.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] Choosing a classification algorithm
- [ ] First steps with scikit-learn – training a perceptron
- [ ] Modeling class probabilities via logistic regression
- [ ] Maximum margin classification with support vector machines
- [ ] Solving nonlinear problems using a kernel SVM
- [ ] Decision tree learning
- [ ] K-nearest neighbors – a lazy learning algorithm

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | No single best classifier; the scikit-learn fit/predict workflow; class probabilities; overfitting, underfitting, and regularization strength; margin maximization and slack; the kernel trick; impurity and information gain; lazy learning and distance metrics; the curse of dimensionality |
| 🤖 Algorithms / models | Perceptron, logistic regression, linear SVM, kernel SVM (RBF), decision tree, random forest, k-nearest neighbors |
| ➗ Mathematics | Sigmoid, logit and odds, log-likelihood and logistic loss, L2 regularization, margin and separating hyperplane, RBF kernel, entropy / Gini impurity / classification error, Minkowski and Euclidean distance |
| 🧰 scikit-learn | `Perceptron`, `LogisticRegression`, `SVC`, `DecisionTreeClassifier`, `RandomForestClassifier`, `KNeighborsClassifier`, `train_test_split`, `StandardScaler`, accuracy metrics, decision-region plots |
| 🔥 PyTorch | None |
| 🛠️ From scratch | Logistic regression trained with gradient descent, adapted from the Adaline implementation |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch03-sklearn-classifiers-tour/notes/) · `[ ]` 💻 [code](chapters/ch03-sklearn-classifiers-tour/code/) · `[ ]` 🧪 [experiments](chapters/ch03-sklearn-classifiers-tour/experiments/)

</details>

<a id="ch04"></a>
### Chapter 4: Building Good Training Datasets – Data Preprocessing
> Data quality drives model quality: cleaning, encoding, scaling, and choosing informative features.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] Dealing with missing data
- [ ] Handling categorical data
- [ ] Partitioning a dataset into separate training and test datasets
- [ ] Bringing features onto the same scale
- [ ] Selecting meaningful features
- [ ] Assessing feature importance with random forests

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | Detecting, removing, and imputing missing values; nominal vs. ordinal features; label mapping and one-hot encoding; train/test partitioning; normalization vs. standardization; overfitting and sparsity via L1; feature selection vs. feature extraction; feature importance |
| 🤖 Algorithms / models | Imputation, one-hot encoding, min-max scaling, standardization, L1-regularized logistic regression, sequential backward selection, random-forest feature importance |
| ➗ Mathematics | Min-max and z-score formulas, L1 vs. L2 penalty behavior |
| 🧰 scikit-learn | `SimpleImputer`, `LabelEncoder`, `OneHotEncoder`, `train_test_split`, `MinMaxScaler`, `StandardScaler`, L1 `LogisticRegression`, `RandomForestClassifier` (with pandas for inspection and cleaning) |
| 🔥 PyTorch | None |
| 🛠️ From scratch | Sequential backward selection (SBS) |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch04-data-preprocessing/notes/) · `[ ]` 💻 [code](chapters/ch04-data-preprocessing/code/) · `[ ]` 🧪 [experiments](chapters/ch04-data-preprocessing/experiments/)

</details>

<a id="ch05"></a>
### Chapter 5: Compressing Data via Dimensionality Reduction
> Reducing the number of features, both for compression and for visualization.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] Unsupervised dimensionality reduction via principal component analysis
- [ ] Supervised data compression via linear discriminant analysis
- [ ] Nonlinear dimensionality reduction and visualization

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | Feature extraction vs. selection; variance and covariance; PCA step by step; explained variance and feature transformation; PCA factor loadings; LDA and class separability; nonlinear structure and 2D visualization |
| 🤖 Algorithms / models | PCA, LDA, t-SNE |
| ➗ Mathematics | Covariance matrix, eigenvalues and eigenvectors, explained-variance ratio, within-class and between-class scatter matrices |
| 🧰 scikit-learn | `PCA`, `LinearDiscriminantAnalysis`, `TSNE`, plus a downstream classifier to judge the compressed features |
| 🔥 PyTorch | None |
| 🛠️ From scratch | PCA and LDA via NumPy eigendecomposition |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch05-dimensionality-reduction/notes/) · `[ ]` 💻 [code](chapters/ch05-dimensionality-reduction/code/) · `[ ]` 🧪 [experiments](chapters/ch05-dimensionality-reduction/experiments/)

</details>

<a id="ch06"></a>
### Chapter 6: Learning Best Practices for Model Evaluation and Hyperparameter Tuning
> How to estimate real-world performance honestly and tune models without fooling yourself.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] Streamlining workflows with pipelines
- [ ] Using k-fold cross-validation to assess model performance
- [ ] Debugging algorithms with learning and validation curves
- [ ] Fine-tuning machine learning models via grid search
- [ ] Looking at different performance evaluation metrics

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | Pipelines and leakage prevention; holdout vs. k-fold and stratified k-fold; diagnosing bias and variance with learning/validation curves; grid search and randomized search; nested cross-validation for model selection; confusion matrix; precision, recall, F1; ROC and AUC; multiclass averaging; class imbalance |
| 🤖 Algorithms / models | Scaler + PCA + classifier pipelines, tuned SVMs |
| ➗ Mathematics | Error and accuracy, precision, recall, F1, true/false-positive rates, area under the ROC curve |
| 🧰 scikit-learn | `Pipeline`/`make_pipeline`, `StratifiedKFold`, `cross_val_score`, `learning_curve`, `validation_curve`, `GridSearchCV`, `RandomizedSearchCV`, `confusion_matrix`, `precision_score`, `recall_score`, `f1_score`, `make_scorer`, `roc_curve`, `auc`, `resample` |
| 🔥 PyTorch | None |
| 🛠️ From scratch | None |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch06-model-evaluation-and-tuning/notes/) · `[ ]` 💻 [code](chapters/ch06-model-evaluation-and-tuning/code/) · `[ ]` 🧪 [experiments](chapters/ch06-model-evaluation-and-tuning/experiments/)

</details>

<a id="ch07"></a>
### Chapter 7: Combining Different Models for Ensemble Learning
> Why combining several models often beats a single one, and the main ways to do it.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] Learning with ensembles
- [ ] Combining classifiers via majority vote
- [ ] Bagging – building an ensemble of classifiers from bootstrap samples
- [ ] Leveraging weak learners via adaptive boosting
- [ ] Gradient boosting – training an ensemble based on loss gradients

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | Why ensembles reduce error; plurality and weighted majority voting; bootstrap sampling; bagging vs. boosting; weak learners; AdaBoost reweighting; gradient boosting for classification; brief coverage of XGBoost |
| 🤖 Algorithms / models | Majority-vote ensemble, bagging, AdaBoost, gradient boosting, XGBoost |
| ➗ Mathematics | Ensemble error as a binomial probability, weighted voting, sample-weight updates, loss gradients / residuals |
| 🧰 scikit-learn | `BaggingClassifier`, `AdaBoostClassifier`, `GradientBoostingClassifier`, estimator base classes for custom models, `GridSearchCV` for ensembles (plus the `xgboost` library) |
| 🔥 PyTorch | None |
| 🛠️ From scratch | A scikit-learn-compatible majority-vote classifier |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch07-ensemble-learning/notes/) · `[ ]` 💻 [code](chapters/ch07-ensemble-learning/code/) · `[ ]` 🧪 [experiments](chapters/ch07-ensemble-learning/experiments/)

</details>

<a id="ch08"></a>
### Chapter 8: Applying Machine Learning to Sentiment Analysis
> A first end-to-end text project: turning movie reviews into features and classifying their sentiment.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] Preparing the IMDb movie review data for text processing
- [ ] Introducing the bag-of-words model
- [ ] Training a logistic regression model for document classification
- [ ] Working with bigger data – online algorithms and out-of-core learning
- [ ] Topic modeling with latent Dirichlet allocation

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | Text cleaning and tokenization; stop words and stemming; bag-of-words; term frequency and TF-IDF; document classification; online learning and out-of-core training; topic modeling |
| 🤖 Algorithms / models | Logistic regression on text features, stochastic-gradient-based online learning, latent Dirichlet allocation (LDA) |
| ➗ Mathematics | Term frequency and TF-IDF, the probabilistic idea behind topic models |
| 🧰 scikit-learn | `CountVectorizer`, TF-IDF transformers, `HashingVectorizer`, `SGDClassifier` with `partial_fit`, `LatentDirichletAllocation`, grid search over a text pipeline (with NLTK for stop words and stemming) |
| 🔥 PyTorch | None |
| 🛠️ From scratch | A hand-written text preprocessing routine |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch08-sentiment-analysis/notes/) · `[ ]` 💻 [code](chapters/ch08-sentiment-analysis/code/) · `[ ]` 🧪 [experiments](chapters/ch08-sentiment-analysis/experiments/)

</details>

<a id="ch09"></a>
### Chapter 9: Predicting Continuous Target Variables with Regression Analysis
> From a straight-line fit to regularized and nonlinear regression models.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] Introducing linear regression
- [ ] Exploring the Ames Housing dataset
- [ ] Implementing an ordinary least squares linear regression model
- [ ] Fitting a robust regression model using RANSAC
- [ ] Evaluating the performance of linear regression models
- [ ] Using regularized methods for regression
- [ ] Turning a linear regression model into a curve – polynomial regression
- [ ] Dealing with nonlinear relationships using random forests

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | Simple and multiple linear regression; exploratory analysis (scatterplot matrix, correlations); least squares; closed-form vs. gradient-based fitting; outliers and robust fitting; residual plots; regularization; polynomial features; tree-based regression |
| 🤖 Algorithms / models | OLS linear regression, RANSAC, Ridge, LASSO, Elastic Net, polynomial regression, decision-tree and random-forest regression |
| ➗ Mathematics | Least-squares cost, normal equation, MSE, R², L1/L2 penalties |
| 🧰 scikit-learn | `LinearRegression`, `RANSACRegressor`, `Ridge`, `Lasso`, `ElasticNet`, `PolynomialFeatures`, `DecisionTreeRegressor`, `RandomForestRegressor`, `mean_squared_error`, `r2_score` |
| 🔥 PyTorch | None |
| 🛠️ From scratch | Linear regression via gradient descent, plus the closed-form solution |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch09-regression-analysis/notes/) · `[ ]` 💻 [code](chapters/ch09-regression-analysis/code/) · `[ ]` 🧪 [experiments](chapters/ch09-regression-analysis/experiments/)

</details>

<a id="ch10"></a>
### Chapter 10: Working with Unlabeled Data – Clustering Analysis
> Finding structure in data when there are no labels.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] Grouping objects by similarity using k-means
- [ ] Organizing clusters as a hierarchical tree
- [ ] Locating regions of high density via DBSCAN

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | Prototype-based, hierarchical, and density-based clustering; k-means iterations and k-means++ initialization; choosing the number of clusters (elbow method); silhouette analysis; dendrograms and linkage; core, border, and noise points; where each method breaks down |
| 🤖 Algorithms / models | k-means, k-means++, agglomerative hierarchical clustering, DBSCAN |
| ➗ Mathematics | Euclidean distance, within-cluster sum of squared errors, silhouette coefficient, linkage criteria, density neighborhoods |
| 🧰 scikit-learn | `KMeans`, `AgglomerativeClustering`, `DBSCAN`, silhouette utilities (with SciPy for dendrograms) |
| 🔥 PyTorch | None |
| 🛠️ From scratch | None |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch10-clustering/notes/) · `[ ]` 💻 [code](chapters/ch10-clustering/code/) · `[ ]` 🧪 [experiments](chapters/ch10-clustering/experiments/)

</details>

---

# 🟧 Phase 2: Neural Networks, from Scratch to PyTorch (Chapters 11–13)

<a id="ch11"></a>
### Chapter 11: Implementing a Multilayer Artificial Neural Network from Scratch
> The turning point of the book: a full neural network in NumPy, with backpropagation explained step by step.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] Modeling complex functions with artificial neural networks
- [ ] Classifying handwritten digits
- [ ] Training an artificial neural network
- [ ] About convergence in neural networks
- [ ] A few last words about the neural network implementation

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | Why multiple layers; MLP architecture and forward propagation; one-hot targets; handwritten-digit classification; backpropagation; mini-batch training; convergence behavior and monitoring training |
| 🤖 Algorithms / models | Multilayer perceptron trained with backpropagation |
| ➗ Mathematics | Chain rule, matrix-form gradients, sigmoid activation, loss functions, one-hot encoding |
| 🧰 scikit-learn | Only for loading data and splitting it |
| 🔥 PyTorch | None (deliberately; this chapter motivates it) |
| 🛠️ From scratch | Complete MLP with backpropagation in NumPy |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch11-neural-network-from-scratch/notes/) · `[ ]` 💻 [code](chapters/ch11-neural-network-from-scratch/code/) · `[ ]` 🧪 [experiments](chapters/ch11-neural-network-from-scratch/experiments/)

</details>

<a id="ch12"></a>
### Chapter 12: Parallelizing Neural Network Training with PyTorch
> First contact with PyTorch: tensors, input pipelines, and building and training models.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] PyTorch and training performance
- [ ] First steps with PyTorch
- [ ] Building input pipelines in PyTorch
- [ ] Building an NN model in PyTorch
- [ ] Choosing activation functions for multilayer neural networks

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | What PyTorch is and why it speeds up training; creating and manipulating tensors; `Dataset` and `DataLoader`; shuffling and batching; built-in datasets; `nn.Module` and `nn.Sequential`; loss functions and optimizers; saving and loading models; activation-function choices |
| 🤖 Algorithms / models | Linear regression in PyTorch, MLP classifier (Iris), activation functions (logistic, softmax, tanh, ReLU and relatives) |
| ➗ Mathematics | Softmax, tanh, ReLU, cross-entropy |
| 🧰 scikit-learn | Data loading and splitting only |
| 🔥 PyTorch | Tensors, `Dataset`/`DataLoader`, `torch.nn`, `torch.optim`, model saving/loading |
| 🛠️ From scratch | Small custom `nn.Module` models |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch12-pytorch-training/notes/) · `[ ]` 💻 [code](chapters/ch12-pytorch-training/code/) · `[ ]` 🧪 [experiments](chapters/ch12-pytorch-training/experiments/)

</details>

<a id="ch13"></a>
### Chapter 13: Going Deeper – The Mechanics of PyTorch
> How PyTorch works under the hood, then two projects and a first look at PyTorch Lightning.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] The key features of PyTorch
- [ ] PyTorch's computation graphs
- [ ] PyTorch tensor objects for storing and updating model parameters
- [ ] Computing gradients via automatic differentiation
- [ ] Simplifying implementations of common architectures via the `torch.nn` module
- [ ] Project one – predicting the fuel efficiency of a car
- [ ] Project two – classifying MNIST handwritten digits
- [ ] Higher-level PyTorch APIs: a short introduction to PyTorch-Lightning

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | Dynamic computation graphs; tensors as trainable parameters; automatic differentiation; building models by composing layers or subclassing `nn.Module`; an end-to-end regression project; an end-to-end image-classification project; organizing training code with Lightning |
| 🤖 Algorithms / models | Deep regression network (fuel efficiency), MLP on MNIST, Lightning-based training |
| ➗ Mathematics | Gradients via autodiff (chain rule in practice), MSE and cross-entropy losses |
| 🧰 scikit-learn | Incidental preprocessing and splitting |
| 🔥 PyTorch | Computation graphs, `nn.Parameter`, autograd, `torch.nn`, `torch.optim`, PyTorch Lightning |
| 🛠️ From scratch | Hand-managed parameters and gradients, to compare against autograd |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch13-pytorch-mechanics/notes/) · `[ ]` 💻 [code](chapters/ch13-pytorch-mechanics/code/) · `[ ]` 🧪 [experiments](chapters/ch13-pytorch-mechanics/experiments/)

</details>

---

# 🟥 Phase 3: Advanced Deep Learning & Reinforcement Learning (Chapters 14–19)

<a id="ch14"></a>
### Chapter 14: Classifying Images with Deep Convolutional Neural Networks
> How convolutional networks learn visual features, culminating in a face-image classification project.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] The building blocks of CNNs
- [ ] Putting everything together – implementing a CNN
- [ ] Implementing a deep CNN using PyTorch
- [ ] Smile classification from face images using a CNN

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | Feature hierarchies; local connectivity and parameter sharing; 1D/2D discrete convolution; padding and stride; pooling; multichannel inputs; dropout and L2 regularization; classification losses; data augmentation |
| 🤖 Algorithms / models | CNN for digit classification, deeper CNN in PyTorch, CNN for smile classification on face images |
| ➗ Mathematics | Discrete convolution, output-size calculations, cross-entropy |
| 🧰 scikit-learn | None |
| 🔥 PyTorch | `nn.Conv2d`, pooling layers, `nn.Dropout`, torchvision datasets and transforms, GPU training |
| 🛠️ From scratch | Naive 1D and 2D convolution implementations |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch14-deep-cnns/notes/) · `[ ]` 💻 [code](chapters/ch14-deep-cnns/code/) · `[ ]` 🧪 [experiments](chapters/ch14-deep-cnns/experiments/)

</details>

<a id="ch15"></a>
### Chapter 15: Modeling Sequential Data Using Recurrent Neural Networks
> Neural networks for ordered data such as text, with two hands-on sequence projects.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] Introducing sequential data
- [ ] RNNs for modeling sequences
- [ ] Implementing RNNs for sequence modeling in PyTorch

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | What makes data sequential; sequence-modeling task types (many-to-one, many-to-many, and so on); recurrent hidden state; backpropagation through time; vanishing and exploding gradients; LSTM gating; text embeddings; a sentiment-analysis project; a character-level language-modeling project |
| 🤖 Algorithms / models | RNN, LSTM, bidirectional recurrent layers, character-level language model |
| ➗ Mathematics | Recurrent state updates, backpropagation through time, LSTM gate equations |
| 🧰 scikit-learn | None |
| 🔥 PyTorch | `nn.Embedding`, recurrent layers (`nn.RNN`, `nn.LSTM`, `nn.GRU`), sequence padding, text data pipelines |
| 🛠️ From scratch | None beyond custom model classes |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch15-rnns/notes/) · `[ ]` 💻 [code](chapters/ch15-rnns/code/) · `[ ]` 🧪 [experiments](chapters/ch15-rnns/experiments/)

</details>

<a id="ch16"></a>
### Chapter 16: Transformers – Improving Natural Language Processing with Attention Mechanisms
> From attention added to RNNs, to self-attention, to the transformer and today's large pre-trained language models.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] Adding an attention mechanism to RNNs
- [ ] Introducing the self-attention mechanism
- [ ] Attention is all we need: introducing the original transformer architecture
- [ ] Building large-scale language models by leveraging unlabeled data
- [ ] Fine-tuning a BERT model in PyTorch

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | Why plain RNN sequence models struggle; attention over encoder states; self-attention and query/key/value; multi-head attention; the encoder-decoder transformer; positional information; pre-training on unlabeled text and then fine-tuning; decoder-style (GPT) vs. encoder-style (BERT) models, plus BART; using pre-trained models rather than training from zero |
| 🤖 Algorithms / models | Attention-augmented RNN, self-attention, original transformer, GPT-style, BERT-style, and BART-style models, fine-tuned BERT-family classifier |
| ➗ Mathematics | Attention weights via softmax over similarity scores, scaled dot-product attention, query/key/value projections, positional encodings |
| 🧰 scikit-learn | None |
| 🔥 PyTorch | Attention computed with raw tensors; Hugging Face Transformers for loading and fine-tuning pre-trained models |
| 🛠️ From scratch | Basic self-attention and scaled dot-product attention with tensor operations |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch16-transformers/notes/) · `[ ]` 💻 [code](chapters/ch16-transformers/code/) · `[ ]` 🧪 [experiments](chapters/ch16-transformers/experiments/)

</details>

<a id="ch17"></a>
### Chapter 17: Generative Adversarial Networks for Synthesizing New Data
> Models that learn to generate new samples through an adversarial two-network game.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] Introducing generative adversarial networks
- [ ] Implementing a GAN from scratch
- [ ] Improving the quality of synthesized images using a convolutional and Wasserstein GAN
- [ ] Other GAN applications

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | Autoencoders as a starting point; generative models; generator vs. discriminator; adversarial training and the two loss functions; transposed convolutions and batch normalization; training instability and mode collapse; Wasserstein distance and the gradient penalty; other GAN applications |
| 🤖 Algorithms / models | Fully connected GAN, convolutional GAN (DCGAN-style), Wasserstein GAN with gradient penalty |
| ➗ Mathematics | Minimax objective, binary cross-entropy for both networks, transposed-convolution output size, Wasserstein (earth-mover) distance, Lipschitz constraint and gradient penalty |
| 🧰 scikit-learn | None |
| 🔥 PyTorch | `nn.ConvTranspose2d`, batch normalization, custom training loops with two optimizers, gradient computation for the penalty term |
| 🛠️ From scratch | GAN, convolutional GAN, and WGAN-GP training loops |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch17-gans/notes/) · `[ ]` 💻 [code](chapters/ch17-gans/code/) · `[ ]` 🧪 [experiments](chapters/ch17-gans/experiments/)

</details>

<a id="ch18"></a>
### Chapter 18: Graph Neural Networks for Capturing Dependencies in Graph Structured Data
> Deep learning on graph-structured inputs such as molecules and networks.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] Introduction to graph data
- [ ] Understanding graph convolutions
- [ ] Implementing a GNN in PyTorch from scratch
- [ ] Implementing a GNN using the PyTorch Geometric library
- [ ] Other GNN layers and recent developments

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | Graph types and representations (adjacency matrices, node and edge features); molecules as graphs; why graph convolutions are needed; neighborhood aggregation; graph-level readout; batching graphs; molecular property prediction; other layer types and recent directions |
| 🤖 Algorithms / models | Graph convolutional network written from scratch, GNN built with PyTorch Geometric |
| ➗ Mathematics | Adjacency and degree matrices, matrix form of graph convolution, permutation invariance of readout |
| 🧰 scikit-learn | None |
| 🔥 PyTorch | Custom graph-convolution `nn.Module`, PyTorch Geometric data objects, loaders, and layers |
| 🛠️ From scratch | A GNN layer and model in plain PyTorch |

**My deliverables:** `[ ]` 📝 [notes](chapters/ch18-graph-neural-networks/notes/) · `[ ]` 💻 [code](chapters/ch18-graph-neural-networks/code/) · `[ ]` 🧪 [experiments](chapters/ch18-graph-neural-networks/experiments/)

</details>

<a id="ch19"></a>
### Chapter 19: Reinforcement Learning for Decision Making in Complex Environments
> Learning from interaction and reward: the theory, a tabular agent, and a first deep RL algorithm.

<details>
<summary><b>▶ Open chapter map</b></summary>

**Major sections**
- [ ] Introduction – learning from experience
- [ ] The theoretical foundations of RL
- [ ] Reinforcement learning algorithms
- [ ] Implementing our first RL algorithm
- [ ] A glance at deep Q-learning

| Aspect | Details |
|:--|:--|
| 🧠 Key concepts | Agent, environment, reward; Markov decision processes; episodic vs. continuing tasks; return and discounting; policies and value functions; dynamic programming, Monte Carlo, and temporal-difference approaches; exploration vs. exploitation; a custom grid-world environment; deep Q-learning |
| 🤖 Algorithms / models | Dynamic-programming methods, Monte Carlo and TD methods, Q-learning, deep Q-network (DQN) |
| ➗ Mathematics | MDP formalism, discounted return, Bellman equations, TD and Q-learning update rules |
| 🧰 scikit-learn | None |
| 🔥 PyTorch | Q-network, experience replay, DQN training loop |
| 🛠️ From scratch | Grid-world environment and tabular Q-learning agent; DQN |

> 📝 The book uses the OpenAI Gym toolkit for environments; that project is now maintained as Gymnasium, so expect small API differences.

**My deliverables:** `[ ]` 📝 [notes](chapters/ch19-reinforcement-learning/notes/) · `[ ]` 💻 [code](chapters/ch19-reinforcement-learning/code/) · `[ ]` 🧪 [experiments](chapters/ch19-reinforcement-learning/experiments/)

</details>

<p align="right"><a href="#top">⬆ back to top</a></p>

---

<a id="cross-cutting"></a>
## 🔀 Cross-Cutting Views

The same material sliced by theme, handy for revision and for spotting connections between chapters.

### ➗ Mathematics covered

| Theme | Where it appears |
|:--|:--|
| Linear algebra notation, dot products, matrices | Ch 1, 2, 5, 11 |
| Gradient descent and partial derivatives | Ch 2, 3, 9, 11, 13 |
| Probability and likelihood (sigmoid, logistic loss, softmax) | Ch 3, 8, 12, 17 |
| Regularization (L1 / L2) | Ch 3, 4, 9, 14 |
| Impurity measures and information gain | Ch 3, 4, 7, 9 |
| Eigendecomposition, covariance, scatter matrices | Ch 5 |
| Evaluation metrics (precision, recall, F1, ROC/AUC, MSE, R²) | Ch 6, 9 |
| Ensemble error, weighted voting, boosting updates | Ch 7 |
| TF-IDF and topic-model intuition | Ch 8 |
| Distances, silhouette, density neighborhoods | Ch 10 |
| Chain rule and backpropagation | Ch 11, 13 |
| Convolution arithmetic | Ch 14, 17 |
| Backpropagation through time, gating | Ch 15 |
| Attention (softmax weights, scaled dot-product, Q/K/V) | Ch 16 |
| Adversarial objectives, Wasserstein distance | Ch 17 |
| Adjacency and degree matrices, message passing | Ch 18 |
| MDPs, returns, Bellman equations, Q-learning updates | Ch 19 |

### 🧰 scikit-learn topics

- [ ] Estimator API, `train_test_split`, scaling, plotting decision regions (Ch 3)
- [ ] Linear and kernel classifiers: `Perceptron`, `LogisticRegression`, `SVC` (Ch 3)
- [ ] Trees, forests, and KNN (Ch 3)
- [ ] Imputation, encoding, and scaling (Ch 4)
- [ ] Feature selection and forest-based importance (Ch 4)
- [ ] `PCA`, `LinearDiscriminantAnalysis`, `TSNE` (Ch 5)
- [ ] Pipelines, cross-validation, learning and validation curves (Ch 6)
- [ ] Grid search, randomized search, nested cross-validation (Ch 6)
- [ ] Metrics: confusion matrix, precision/recall/F1, ROC/AUC, imbalance handling (Ch 6)
- [ ] Bagging, AdaBoost, gradient boosting, custom ensemble estimator (Ch 7)
- [ ] Text vectorizers, online learning, LDA topic modeling (Ch 8)
- [ ] Linear, robust, regularized, polynomial, and tree-based regression (Ch 9)
- [ ] `KMeans`, `AgglomerativeClustering`, `DBSCAN`, silhouette analysis (Ch 10)

### 🔥 PyTorch topics

- [ ] Tensors: creation, dtypes, manipulation (Ch 12)
- [ ] `Dataset` and `DataLoader`, shuffling and batching (Ch 12)
- [ ] `nn.Module`, `nn.Sequential`, losses, optimizers, saving/loading (Ch 12)
- [ ] Computation graphs and automatic differentiation (Ch 13)
- [ ] `nn.Parameter` and manual parameter updates (Ch 13)
- [ ] The `torch.nn` module for common architectures (Ch 13)
- [ ] PyTorch Lightning basics (Ch 13)
- [ ] Convolution, pooling, dropout, torchvision datasets and transforms, GPU training (Ch 14)
- [ ] Embeddings and recurrent layers for text and sequences (Ch 15)
- [ ] Attention with raw tensors; Hugging Face Transformers fine-tuning (Ch 16)
- [ ] Transposed convolutions, multi-optimizer GAN training, gradient penalty (Ch 17)
- [ ] Custom graph layers and PyTorch Geometric (Ch 18)
- [ ] Deep Q-network and experience replay (Ch 19)

### 🛠️ From-scratch implementations

Writing these myself is the point of the exercise; each one gets a matching note on how it differs from the library version.

- [ ] Perceptron (Ch 2)
- [ ] Adaline with batch and stochastic gradient descent (Ch 2)
- [ ] Logistic regression via gradient descent (Ch 3)
- [ ] Sequential backward selection (Ch 4)
- [ ] PCA via eigendecomposition (Ch 5)
- [ ] LDA via scatter matrices (Ch 5)
- [ ] Majority-vote ensemble classifier (Ch 7)
- [ ] Linear regression via gradient descent and closed form (Ch 9)
- [ ] Multilayer perceptron with backpropagation in NumPy (Ch 11)
- [ ] 1D and 2D convolution (Ch 14)
- [ ] Self-attention with tensor operations (Ch 16)
- [ ] GAN, convolutional GAN, and WGAN-GP training loops (Ch 17)
- [ ] Graph neural network layer and model in PyTorch (Ch 18)
- [ ] Grid-world environment with tabular Q-learning (Ch 19)
- [ ] Deep Q-network (Ch 19)

<p align="right"><a href="#top">⬆ back to top</a></p>

---

<a id="structure"></a>
## 🗂️ Repository Structure

```text
.
├── README.md                      ← you are here: the master hub
├── requirements.txt               ← pinned package versions I actually use
├── chapters/
│   ├── ch01-intro-to-ml/
│   │   ├── notes/                 ← my explanations (markdown)
│   │   ├── code/                  ← notebooks and .py implementations
│   │   └── experiments/           ← my own experiments and observations
│   ├── ch02-simple-classification-algorithms/
│   ├── ch03-sklearn-classifiers-tour/
│   ├── ch04-data-preprocessing/
│   ├── ch05-dimensionality-reduction/
│   ├── ch06-model-evaluation-and-tuning/
│   ├── ch07-ensemble-learning/
│   ├── ch08-sentiment-analysis/
│   ├── ch09-regression-analysis/
│   ├── ch10-clustering/
│   ├── ch11-neural-network-from-scratch/
│   ├── ch12-pytorch-training/
│   ├── ch13-pytorch-mechanics/
│   ├── ch14-deep-cnns/
│   ├── ch15-rnns/
│   ├── ch16-transformers/
│   ├── ch17-gans/
│   ├── ch18-graph-neural-networks/
│   └── ch19-reinforcement-learning/
└── resources/                     ← glossary, cheat sheets, useful references
```

Every chapter folder follows the same `notes/ code/ experiments/` layout, so any link in this README resolves the same way.

**Create the folder skeleton in one go** (the `.gitkeep` files make Git track empty folders so the links above work immediately):

```bash
for d in ch01-intro-to-ml ch02-simple-classification-algorithms ch03-sklearn-classifiers-tour \
         ch04-data-preprocessing ch05-dimensionality-reduction ch06-model-evaluation-and-tuning \
         ch07-ensemble-learning ch08-sentiment-analysis ch09-regression-analysis ch10-clustering \
         ch11-neural-network-from-scratch ch12-pytorch-training ch13-pytorch-mechanics \
         ch14-deep-cnns ch15-rnns ch16-transformers ch17-gans ch18-graph-neural-networks \
         ch19-reinforcement-learning; do
  for sub in notes code experiments; do
    mkdir -p "chapters/$d/$sub" && touch "chapters/$d/$sub/.gitkeep"
  done
done
mkdir -p resources
```

<p align="right"><a href="#top">⬆ back to top</a></p>

---

<a id="workflow"></a>
## 🧭 How Notes, Code, and Experiments Are Organized

### 📝 `notes/`: explain it to my future self
One markdown file per book section, named `NN-section-slug.md` (for example `03-logistic-regression.md`). Each note follows the same skeleton:

1. **The idea in a paragraph:** what problem this solves and why anyone cares
2. **Intuition:** a picture, an analogy, or a tiny numeric example
3. **The math:** derived step by step, not just quoted
4. **Implementation notes:** how it maps to code, plus library behavior and defaults worth knowing
5. **Pitfalls:** where it breaks or misleads
6. **Open questions:** things I still do not fully get

### 💻 `code/`: implementations I can run
- **Notebooks (`.ipynb`)** for exploration and plots
- **Python modules (`.py`)** for reusable from-scratch implementations, so later chapters can import them
- Where both exist, I implement the **from-scratch version first**, then the **library version**, and compare outputs
- Fixed random seeds and a short header cell stating the library versions used

### 🧪 `experiments/`: questions the book did not ask
One file or notebook per experiment, named `exp-NN-short-title`. Each records:

- **Question and hypothesis:** what I expect and why
- **Setup:** data, model, hyperparameters, seed
- **Result:** numbers and plots
- **Takeaway:** what I learned, including when the hypothesis was wrong

### ✅ Definition of "done" for a section
A box is ticked only when all of these are true:

- [ ] I can explain the idea without looking at the book
- [ ] My note exists and includes the derivation or reasoning
- [ ] The code runs end to end from a clean environment
- [ ] I have run at least one change of my own and recorded what happened

<p align="right"><a href="#top">⬆ back to top</a></p>

---

<a id="philosophy"></a>
## 💡 Learning Philosophy: Understanding over Memorization

Memorizing an API fades within weeks, while understanding why an algorithm behaves the way it does lasts. The rules I follow:

- **Derive before you import.** Work out the update rule, then write the code, then compare to the library.
- **Predict, then run.** Write down what I expect a change to do before executing it. The surprises are where the learning is.
- **Break things on purpose.** Remove the scaling step, shrink the data, crank the learning rate, and see what fails and why.
- **Explain it in my own words.** If I cannot write it down plainly, I do not understand it yet.
- **Small and from scratch first.** A 30-line NumPy version teaches more than a 3-line library call, and the library call then makes sense.
- **Record failures honestly.** An experiment that disproved my hypothesis is worth more than one that confirmed it.
- **Revisit.** Later chapters reuse earlier ideas (gradient descent, regularization, softmax, attention); I go back and strengthen the earlier notes when that happens.
- **Check against the source.** When my understanding conflicts with the book, I investigate before assuming either of us is right, and the authors' errata and discussion forum are fair game.

<p align="right"><a href="#top">⬆ back to top</a></p>

---

<a id="progress"></a>
## 📈 Final Progress Tracker

Update this section as work lands in the repo. Everything starts at zero on purpose.

### Overall

| Metric | Count |
|:--|:--:|
| Chapters completed | 0 / 19 |
| Major book sections completed | 0 / 94 |
| From-scratch implementations finished | 0 / 15 |

### By phase

| Phase | Chapters | Sections done |
|:--|:--:|:--:|
| 🟦 Foundations & classical ML | 1 – 10 | 0 / 50 |
| 🟧 Neural networks, scratch to PyTorch | 11 – 13 | 0 / 18 |
| 🟥 Advanced deep learning & RL | 14 – 19 | 0 / 26 |

### By chapter

| Ch | Title | 📝 Notes | 💻 Code | 🧪 Experiments | Done |
|:-:|:--|:-:|:-:|:-:|:-:|
| 1 | [Giving Computers the Ability to Learn from Data](#ch01) | ⬜ | ⬜ | ⬜ | ⬜ |
| 2 | [Training Simple ML Algorithms for Classification](#ch02) | ⬜ | ⬜ | ⬜ | ⬜ |
| 3 | [A Tour of ML Classifiers Using Scikit-Learn](#ch03) | ⬜ | ⬜ | ⬜ | ⬜ |
| 4 | [Building Good Training Datasets – Data Preprocessing](#ch04) | ⬜ | ⬜ | ⬜ | ⬜ |
| 5 | [Compressing Data via Dimensionality Reduction](#ch05) | ⬜ | ⬜ | ⬜ | ⬜ |
| 6 | [Model Evaluation and Hyperparameter Tuning](#ch06) | ⬜ | ⬜ | ⬜ | ⬜ |
| 7 | [Combining Different Models for Ensemble Learning](#ch07) | ⬜ | ⬜ | ⬜ | ⬜ |
| 8 | [Applying ML to Sentiment Analysis](#ch08) | ⬜ | ⬜ | ⬜ | ⬜ |
| 9 | [Regression Analysis](#ch09) | ⬜ | ⬜ | ⬜ | ⬜ |
| 10 | [Working with Unlabeled Data – Clustering Analysis](#ch10) | ⬜ | ⬜ | ⬜ | ⬜ |
| 11 | [Multilayer Neural Network from Scratch](#ch11) | ⬜ | ⬜ | ⬜ | ⬜ |
| 12 | [Parallelizing Neural Network Training with PyTorch](#ch12) | ⬜ | ⬜ | ⬜ | ⬜ |
| 13 | [Going Deeper – The Mechanics of PyTorch](#ch13) | ⬜ | ⬜ | ⬜ | ⬜ |
| 14 | [Deep Convolutional Neural Networks](#ch14) | ⬜ | ⬜ | ⬜ | ⬜ |
| 15 | [Recurrent Neural Networks](#ch15) | ⬜ | ⬜ | ⬜ | ⬜ |
| 16 | [Transformers](#ch16) | ⬜ | ⬜ | ⬜ | ⬜ |
| 17 | [Generative Adversarial Networks](#ch17) | ⬜ | ⬜ | ⬜ | ⬜ |
| 18 | [Graph Neural Networks](#ch18) | ⬜ | ⬜ | ⬜ | ⬜ |
| 19 | [Reinforcement Learning](#ch19) | ⬜ | ⬜ | ⬜ | ⬜ |

*Legend: ⬜ not started · 🟨 in progress · ✅ complete*

---

## 🙏 Credits & Disclaimer

All credit for the book goes to **Sebastian Raschka, Yuxi (Hayden) Liu, and Vahid Mirjalili**. This repository is an independent, unofficial study log. It is not affiliated with or endorsed by the authors or Packt Publishing, and it contains my own summaries, notes, and code only. For the original text, figures, and official code notebooks, please use the book and the [authors' repository](https://github.com/rasbt/machine-learning-book).

<p align="center"><i>Learning in public, one chapter at a time. 🚀</i></p>
