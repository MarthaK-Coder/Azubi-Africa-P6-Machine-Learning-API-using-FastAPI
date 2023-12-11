# Predicting Sepsis Onset with FastAPI: A Dockerized Machine Learning Approach

<div align="center">

[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0-blue?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8.5-green?style=flat-square&logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Latest-blue?style=flat-square&logo=docker)](https://www.docker.com/)

</div>

## Table of Contents
1. [Introduction](#introduction)
2. [Business Understanding](#business-understanding)
   - [Formulating Hypotheses and Questions](#formulating-hypotheses-and-questions)
3. [Data Understanding](#data-understanding)
   - [Loading Datasets and Exploratory Data Analysis (EDA)](#loading-datasets-and-exploratory-data-analysis-eda)
4. [Data Preparation](#data-preparation)
   - [Data Splitting and Balancing Classes](#data-splitting-and-balancing-classes)
   - [Creating a Preprocessing Pipeline](#creating-a-preprocessing-pipeline)
5. [Model Training and Evaluation](#model-training-and-evaluation)
   - [Selecting and Training Models](#selecting-and-training-models)
   - [Model Evaluation](#model-evaluation)
   - [Hyperparameter Tuning](#hyperparameter-tuning)
   - [Model Persistence](#model-persistence)
6. [FastAPI and Dockerization](#fastapi-and-dockerization)
   - [Building a FastAPI](#building-a-fastapi)
   - [Docker Containerization](#docker-containerization)
   - [Pushing to Docker Hub](#pushing-to-docker-hub)
7. [Conclusion](#conclusion)

## Introduction
Timely prediction of sepsis onset is crucial for enhancing patient outcomes in healthcare. This project explores the application of machine learning classification models to predict sepsis, encapsulating the solution within a Docker container and exposing it through FastAPI for seamless deployment.

## Business Understanding
### Formulating Hypotheses and Questions
**Hypothesis:** Early sepsis detection can significantly improve patient outcomes.
**Question:** Can machine learning models accurately predict sepsis onset based on patient data?

## Data Understanding
### Loading Datasets and Exploratory Data Analysis (EDA)
Initiating the project with loading datasets and conducting exploratory data analysis (EDA) to gain insights:
- What features are available in the dataset?
- How should missing values be handled?
- What is the distribution of sepsis cases in the dataset?

## Data Preparation
### Data Splitting and Balancing Classes
Addressing class imbalance by splitting data into training and testing sets and employing techniques such as oversampling or undersampling.
### Creating a Preprocessing Pipeline
Developing a preprocessing pipeline to streamline tasks like imputing missing values, scaling features, and encoding categorical variables.

## Model Training and Evaluation
### Selecting and Training Models
Experimenting with classification models (Random Forest, Logistic Regression, Gradient Boosting) to identify well-performing models for sepsis prediction.
### Model Evaluation
Utilizing metrics like precision, recall, and F1 score with a focus on sensitivity for effective sepsis case capture.
### Hyperparameter Tuning
Achieving optimal model performance through hyperparameter tuning using techniques like grid search or random search.
### Model Persistence
Persisting selected models for easy deployment, eliminating the need for retraining.

## FastAPI and Dockerization
### Building a FastAPI
FastAPI serves as the foundation for our API, designed to take patient data as input and return the predicted likelihood of sepsis onset.

#### Screenshots
![FastAPI Screenshots](screenshots/fastapi.jpg)

### Docker Containerization
Encapsulating the solution within a Docker container to ensure consistency and eliminate dependency issues across different environments.

#### Screenshots
![Docker Screenshots](screenshots/docker.jpg)

### Pushing to Docker Hub
Pushing the Docker image to Docker Hub, facilitating accessibility and deployment on various platforms.

## Conclusion
By combining machine learning, FastAPI, and Docker, we create a robust solution for predicting sepsis onset. The seamless integration of predictive analytics and healthcare demonstrates the potential for early intervention and improved patient outcomes. The titled approach, "Predicting Sepsis Onset using FastAPI: A Dockerized Machine Learning Approach," underscores the intersection of technology and healthcare for impactful predictive analytics.