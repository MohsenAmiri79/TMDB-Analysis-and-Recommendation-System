# TMDB 5k Dataset Analysis

This project presents an in-depth analysis of the TMDB Movie Dataset, available on Kaggle. The dataset comprises several thousand films, providing data on the plot, cast, crew, budget, and revenues. The primary aim of this project is to gain insights about the data for further modeling to investigate the profitability of the movies.

## Table of Contents
- [Introduction](#introduction)
- [Overview](#overview)
- [Preprocessing](#preprocessing)
- [Data Analysis](#data-analysis)
- [Predictive Modeling](#predictive-modeling)

## Introduction
This report presents an in-depth analysis of the TMDB Movie Dataset, available on Kaggle. The dataset comprises several thousand films, providing data on the plot, cast, crew, budget, and revenues. The primary aim of this project is to gain insights about the data for further modeling to investigate the profitability of the movies.

## Overview
The dataset is sourced from Kaggle and contains comprehensive information and statistics about roughly 5000 movies. This dataset provides a wealth of information for analyzing and understanding trends in the movie industry.

## Preprocessing
The preprocessing process of the data involved cleaning, reforming and adding features to the dataset and saving the result. The cleaned and preprocessed dataset is saved to a CSV file for future use. This new CSV file can be accessed in the data directory with the name of “movies_data.csv”.

## Data Analysis
In this section we will explore the dataset using visualization along with statistical methods to find patterns and intuitions into how different factors affect a movie’s success.

## Predictive Modeling
The modeling phase involves defining a target based on the profit column to indicate whether a movie has been profitable or not. Feature engineering is performed to select a subset of useful features for training a model. The models used for prediction include Logistic Regression, Decision Tree, Random Forest, and XGBoost. Each model’s performance is evaluated using four metrics: Accuracy, Precision, Recall, and F1-Score. Additionally, the ROC-AUC plot for each model is generated for a more visual comparison.

## Author
- Mohsen Amiri Amjad

## Dataset
- [TMDB 5000 Movie Dataset | Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata)

## GitHub
- [TMDB Exploratory and Predictive Analysis](https://github.com/MohsenAmiri79/TMDB-Analysis-and-Recommendation-System)
