# Quantum Cloud Integration: Potential Impact of Quantum Computing on Cloud Storage

## Overview

This repository presents the research and practical implementation of hybrid cloud-quantum systems. The project focuses on exploring the **potential impact of quantum computing on cloud storage**, specifically using **AWS**, **IBM Quantum**, and **GitHub** for version control. 

The goal is to investigate how integrating quantum computing into traditional cloud environments can revolutionize storage systems by enhancing speed, security, and computational power.

## Project Structure

```bash
quantum-cloud-integration/
│
├── Dockerfile                  # Container configuration for setting up the environment
├── requirements.txt            # Python dependencies for the project
├── src/                        # Source code for the hybrid cloud-quantum integration
│   ├── quantum_cloud.py        # Main script for handling quantum and cloud interaction
│   └── aws_storage.py          # AWS integration for cloud storage
│
├── docs/                       # Documentation for the project
│   └── research_paper.md       # Research findings and literature review
│
├── notebooks/                  # Jupyter notebooks for quantum simulations
│   └── quantum_experiments.ipynb # IBM Quantum experiments and test results
│
├── .gitignore                  # Files and directories to ignore in version control
├── README.md                   # Project overview and documentation (this file)
└── LICENSE                     # Licensing information
```

## Installation

### Prerequisites

To run this project, you need the following installed on your local machine:

- **Docker** (to containerize and run the project)
- **Python 3.x** (for executing scripts)
- **IBM Quantum Experience Account** (for running quantum experiments)
- **AWS Account** (for cloud storage integration)

### Steps to Set Up

1. **Clone the repository**:
   ```bash
   git clone https://github.com/PriyanshuKSharma/quantum-cloud-integration.git
   cd quantum-cloud-integration
   ```

2. **Install dependencies** using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Docker**:
   If you prefer using Docker to run the project in a containerized environment, follow these steps:
   
   - Build the Docker image:
     ```bash
     docker build -t quantum-cloud .
     ```
   - Run the Docker container:
     ```bash
     docker run -it quantum-cloud
     ```

4. **Configure AWS CLI**:
   ```bash
   aws configure
   ```
   Enter your AWS credentials:
   - AWS Access Key ID
   - AWS Secret Access Key
   - Default region: `us-east-1` (recommended for Braket)
   - Default output format: `json`

5. **AWS Braket Service Role Setup**:
   For AWS Braket access, create the service role:
   - Visit: https://console.aws.amazon.com/braket/home#/permissions?tab=executionRoles
   - Create `AWSServiceRoleForAmazonBraket` role
   
   **Alternative - Local Simulator**:
   The project includes local quantum simulation that works without AWS setup.

## Dockerfile

The Dockerfile sets up a containerized environment with all the necessary dependencies. It installs Python, Docker CLI, and libraries required for AWS and IBM Quantum integration.

```dockerfile
# Use official Python base image
FROM python:3.9-slim

# Set up working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Install Docker CLI (needed for cloud interaction)
RUN apt-get update && apt-get install -y docker.io

# Set entry point
CMD ["python", "src/quantum_cloud.py"]
```

## requirements.txt

This file lists all the Python libraries and packages required to run the project.

```txt
qiskit==0.36.2
boto3==1.24.28
flask==2.1.1
numpy==1.22.4
pandas==1.4.2
```

## Features

- **Hybrid Cloud-Quantum Systems**: The integration of cloud storage using AWS with quantum computing via IBM Quantum.
- **Quantum Simulation**: Use of quantum algorithms to test cloud storage encryption.
- **Dockerized Environment**: Run the project in a container for easier setup and scalability.

## Usage

**For detailed CLI setup instructions, see [CLI_SETUP.md](CLI_SETUP.md)**

Once you have set up the environment, you can start interacting with the hybrid system using the provided Python scripts. Here’s how to run a basic experiment:

```bash
python src/quantum_cloud.py
```

The script will simulate a quantum computing task and integrate it with AWS cloud storage, showcasing the potential applications of quantum computing in cloud environments.

## Contributions

Feel free to submit issues or pull requests if you find bugs or have suggestions for improvements.

## License

This project is for research purposes.
