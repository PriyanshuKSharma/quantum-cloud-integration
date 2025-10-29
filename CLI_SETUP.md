# CLI Setup Guide

## Virtual Environment Setup

```bash
# Create virtual environment
python -m venv quantum-env

# Activate (Windows)
quantum-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## AWS CLI Configuration

```bash
# Configure AWS credentials
aws configure
```

Enter:
- AWS Access Key ID: `your_access_key`
- AWS Secret Access Key: `your_secret_key`
- Default region: `us-east-1`
- Default output format: `json`

## Environment Variables

```bash
# Windows Command Prompt
set AWS_ACCESS_KEY_ID=your_access_key
set AWS_SECRET_ACCESS_KEY=your_secret_key
set AWS_DEFAULT_REGION=us-east-1

# Windows PowerShell
$env:AWS_ACCESS_KEY_ID="your_access_key"
$env:AWS_SECRET_ACCESS_KEY="your_secret_key"
$env:AWS_DEFAULT_REGION="us-east-1"
```

## Running Scripts

### Local Simulator
```bash
python src/quantum_experiment.py
```

### AWS Braket (requires service role)
```bash
python src/aws_braket.py
```

### Docker
```bash
docker-compose up --build
```

## AWS Braket Service Role

For AWS Braket access:
1. Visit: https://console.aws.amazon.com/braket/home#/permissions?tab=executionRoles
2. Create `AWSServiceRoleForAmazonBraket` role