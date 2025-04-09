
# Text Summarizer Project

## Overview

The Text Summarizer Project is designed to automatically generate concise summaries from longer text documents. Utilizing Natural Language Processing (NLP) techniques and transformer-based models, this project aims to provide accurate and meaningful text condensations.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Training and Evaluation](#training-and-evaluation)
- [API Deployment](#api-deployment)
- [License](#license)

## Project Structure

The repository is organized as follows:

- `.github/workflows/`: Contains GitHub Actions workflows for Continuous Integration and Deployment (CI/CD).
- `config/`: Houses configuration files for model training and evaluation.
- `research/`: Includes Jupyter notebooks for exploratory data analysis and experimentation.
- `src/text_summarizer/`: Contains the core source code for the text summarization model and related utilities.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `Dockerfile`: Defines the Docker image for containerizing the application.
- `LICENSE`: The MIT License for the project.
- `README.md`: This document.
- `app.py`: A Flask application for serving the text summarization model via an API.
- `main.py`: The main script to initiate model training and evaluation.
- `params.yaml`: A YAML file containing hyperparameters and configurations for training.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `setup.py`: The setup script for packaging the project.
- `template.py`: A template script for initializing new components or modules.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hyrun2005/text_summarizer_project.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd text_summarizer_project
   ```

3. **Create a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training the Model

To train the text summarization model, execute the `main.py` script:

```bash
python main.py
```

This script will load the data, preprocess it, and train the model based on the configurations specified in `params.yaml`.

## Configuration

Hyperparameters and other configurations for training and evaluation are managed in the `params.yaml` file. Adjust these settings as needed to optimize model performance.

## Training and Evaluation

The `research/` directory contains Jupyter notebooks that provide insights into the data exploration, model training processes, and evaluation metrics. These notebooks serve as a guide for understanding the model's performance and for further experimentation.

## API Deployment

The project includes a REST API built with FastAPI. It exposes the following endpoints:

### **GET /** – Index
- **Endpoint**: `/`
- **Description**: Basic index route to verify that the API is running.

### **GET /train** – Training
- **Endpoint**: `/train`
- **Description**: Starts the training process for the model.

### **POST /predict** – Predict Route
- **Endpoint**: `/predict`
- **Description**: Accepts raw text and returns a summarized version.
- **Request Example**:
  ```json
  {
    "text": "This is a very long article that needs to be summarized..."
  }
  ```
- **Response Example**:
  ```json
  {
    "summary": "A brief summary of the article."
  }
  ```

### Schemas

- **HTTPValidationError** – Returned if the input doesn't meet schema requirements.
- **ValidationError** – General validation issues during request processing.

To start the API, run:
```bash
uvicorn app:app --reload
```

Then open your browser at `http://127.0.0.1:8000/docs` to access the interactive Swagger UI.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
