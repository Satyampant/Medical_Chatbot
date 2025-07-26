````markdown
# 🩺 AI-Powered Medical Chatbot

Welcome to the **AI-Powered Medical Chatbot** application! This project provides an intelligent conversational agent designed to offer general medical information, answer health-related queries, and act as a preliminary resource for common health concerns.

## 🌟 Overview

In an age where quick access to information is paramount, this chatbot aims to bridge the gap between users seeking health insights and reliable, AI-driven responses. Built to understand natural language, it leverages a large language model to process user queries and provide relevant, informative answers on a wide range of medical topics.

**Important Disclaimer:** This chatbot is intended for informational purposes only and should **NOT** be considered a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare professional for any health concerns or before making any decisions related to your health.

## ✨ Features

* **Natural Language Understanding:** Interprets user questions posed in everyday language.
* **Comprehensive Information Retrieval:** Provides answers on symptoms, common conditions, basic drug information, and general health advice.
* **Conversational Interface:** Designed for an intuitive and engaging user experience.
* **Scalable AI Backend:** Utilizes a powerful large language model (LLM) for robust and accurate responses.
* **Automated Deployment (CI/CD):** Streamlined deployment to AWS using GitHub Actions.

## ⚙️ Technologies Used

* **Python:** The core programming language for the application logic.
* **Groq API:** Powers the underlying large language model for generating responses.
* **`dotenv`:** For secure management of environment variables (like API keys).
* **Flask:** Web framework for building the application interface (if applicable).
* **Docker:** For containerizing the application for consistent deployment.
* **AWS (Amazon Web Services):**
    * **EC2 (Elastic Compute Cloud):** Virtual servers for hosting the application.
    * **ECR (Elastic Container Registry):** Secure Docker image repository.
* **GitHub Actions:** For Continuous Integration and Continuous Deployment (CI/CD) workflows.

## 🚀 Setup and Installation (Local)

Follow these steps to get the Medical Chatbot running on your local machine:

1.  **Clone the Repository:**
    Start by cloning this project to your local system:
    ```bash
    git clone [https://github.com/Satyampant/Medical_Chatbot.git](https://github.com/Satyampant/Medical_Chatbot.git)
    cd Medical_Chatbot
    ```

2.  **Set Up a Virtual Environment (Recommended):**
    It's good practice to create a virtual environment to manage project dependencies:
    ```bash
    python -m venv venv
    # On Windows:
    # .\venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate
    ```

3.  **Install Dependencies:**
    Install the necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```
    (Ensure you have a `requirements.txt` file listing `groq`, `python-dotenv`, `flask`, etc., as per your project's needs).

4.  **Configure Environment Variables:**
    This application requires an API key for the Groq service.
    * Create a file named `.env` in the root directory of your project (the same directory as this `README.md` file).
    * Obtain your Groq API Key from the [Groq website](https://console.groq.com/keys).
    * Add your API key to the `.env` file in the following format:
        ```
        GROQ_API_KEY="your_groq_api_key_here"
        ```
    * **Important Security Note:** The `.env` file is intentionally ignored by Git (via `.gitignore`) to prevent your sensitive API key from being pushed to public repositories. If you previously committed this file by mistake, please follow the instructions provided in the GitHub push protection error message to remove it from your Git history.

5.  **Run the Application:**
    Execute the main script to start the chatbot:
    ```bash
    python app.py
    ```
    (Replace `app.py` with the actual name of your main Python file if it's different, e.g., `chatbot.py`).

    Once running, you can typically access the web interface at `http://localhost:5000` (or the port your Flask app uses).

## 💬 Usage

Once the application is running, you can interact with the chatbot through its web interface. Simply type your medical queries and press Enter.

**Examples of questions you can ask:**

* "What are the symptoms of the common cold?"
* "Tell me about ibuprofen."
* "What is a balanced diet?"
* "How can I prevent flu?"

## ☁️ Deployment to AWS (CI/CD with GitHub Actions)

This project is configured for automated deployment to AWS using GitHub Actions, ensuring a seamless Continuous Integration and Continuous Deployment (CI/CD) pipeline.

### Deployment Workflow Overview

The CI/CD pipeline automates the following steps:
1.  **Build Docker Image:** The application's source code is containerized into a Docker image.
2.  **Push to ECR:** The Docker image is pushed to Amazon Elastic Container Registry (ECR).
3.  **Deploy to EC2:** The latest Docker image is pulled from ECR and launched on an Amazon EC2 instance.

### AWS Setup

Before setting up GitHub Actions, you need to configure your AWS environment:

1.  **Create IAM User for Deployment:**
    Create a dedicated IAM user with programmatic access. This user will be used by GitHub Actions to interact with your AWS resources. Grant this user the following policies:
    * `AmazonEC2ContainerRegistryFullAccess`: Allows pushing/pulling Docker images to/from ECR.
    * `AmazonEC2FullAccess`: Allows managing EC2 instances (e.g., pulling images, running containers).

2.  **Create ECR Repository:**
    Create a new private repository in Amazon ECR to store your Docker images. Note down the Repository URI, which will look something like:
    `[your_aws_account_id].dkr.ecr.[your_aws_region].amazonaws.com/medicalbot`
    (e.g., `315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot`).

3.  **Launch and Configure EC2 Instance (Ubuntu):**
    Launch an Ubuntu EC2 instance that will host your chatbot.
    * **Install Docker on EC2:** Connect to your EC2 instance via SSH and install Docker:
        ```bash
        sudo apt-get update -y
        sudo apt-get upgrade -y
        curl -fsSL [https://get.docker.com](https://get.docker.com) -o get-docker.sh
        sudo sh get-docker.sh
        sudo usermod -aG docker ubuntu
        newgrp docker # You might need to log out and log back in for this to take effect
        ```
    * Ensure your EC2 instance's security group allows inbound traffic on the port your Flask application runs on (e.g., port 5000 or 80).

### GitHub Actions Setup

To enable the CI/CD pipeline, you need to configure your GitHub repository:

1.  **Configure EC2 as a Self-Hosted Runner:**
    * In your GitHub repository, go to `Settings` > `Actions` > `Runners`.
    * Click `New self-hosted runner`.
    * Follow the on-screen instructions to set up your EC2 instance as a self-hosted runner. This involves running a series of commands on your EC2 instance to register it with GitHub.

2.  **Set Up GitHub Secrets:**
    Add the following environment variables as secrets in your GitHub repository (`Settings` > `Secrets` > `Actions` > `New repository secret`):
    * `AWS_ACCESS_KEY_ID`: Your AWS IAM user's access key ID.
    * `AWS_SECRET_ACCESS_KEY`: Your AWS IAM user's secret access key.
    * `AWS_DEFAULT_REGION`: The AWS region where your ECR and EC2 resources are located (e.g., `us-east-1`).
    * `ECR_REPO`: The full URI of your ECR repository (e.g., `315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot`).
    * `GROQ_API_KEY`: Your Groq API Key (same as in your local `.env` file).

### Running the Deployment

Once the AWS and GitHub configurations are complete, any push to the `main` branch (or as configured in your GitHub Actions workflow file, typically `.github/workflows/main.yml`) will trigger the CI/CD pipeline, building, pushing, and deploying your application automatically.

## 🤝 Contributing

We welcome contributions to improve this medical chatbot! If you have suggestions, bug reports, or want to contribute code, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add new feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
````