# T5-SQL Generator

## Project Overview
The T5-SQL Generator is a deep learning-based tool that converts natural language queries into SQL queries using a pre-trained T5 model. This project fine-tunes the T5 model for the task of translating English queries into SQL commands.

## Features
- **Natural Language to SQL Translation**: Converts user input in natural language to SQL commands.
- **Fine-Tuning of T5**: Fine-tunes a pre-trained T5 model using a custom dataset for SQL query generation.
- **Interactive Command-Line Interface**: Allows users to input natural language queries and receive the corresponding SQL queries interactively.

## Technologies Used
- **Transformers**: Hugging Face library for handling transformer models.
- **PyTorch**: Deep learning framework for model training and inference.
- **scikit-learn**: For dataset splitting and evaluation.
- **matplotlib**: For visualizing model performance and outputs.
- **seaborn**: For generating heatmaps and other visualizations.

### Setup and Installation

## 1. Clone the Repository

Clone the repository to your local machine using the following command:

bash
git clone https://github.com/your-username/t5-sql-generator.git


## 2. Install Dependencies
install the required libraries:

transformers
datasets
torch
scikit-learn
matplotlib
seaborn

## 3. Dataset Preparation
Ensure that your dataset is in the correct format with two columns:
text_query (Natural Language query)
sql_command (Corresponding SQL query)

## 4. Training the Model:
Run the following Python script to train the model:
python train_model.py

## 5. Running the Model :
Once the model is trained, run the following script to interactively generate SQL queries from natural language input:
python generate_sql.py

## 6. Acknowledgments
Hugging Face for the transformers library.
PyTorch for the deep learning framework.
The Spider dataset for text-to-SQL tasks.


## Summary of this project-
The T5-SQL Generator project leverages the power of the T5 (Text-to-Text Transfer Transformer) model to translate natural language queries into SQL queries. By fine-tuning the pre-trained T5 model on a custom dataset containing natural language queries paired with their corresponding SQL commands, the system enables accurate and efficient translation from English to SQL. The project is implemented using the Hugging Face transformers library along with PyTorch for model training and inference. It offers an interactive command-line interface, where users can input natural language queries, and the system returns the generated SQL queries. The model is trained using a dataset with columns for natural language queries (text_query) and their corresponding SQL statements (sql_command). After training, users can run the model to generate SQL queries from input queries and evaluate the model’s performance through visualization tools such as accuracy plots, SQL query length distributions, and attention heatmaps. The project also includes the necessary scripts for training the model, generating SQL queries, and visualizing results, making it a comprehensive solution for automated text-to-SQL conversion.







