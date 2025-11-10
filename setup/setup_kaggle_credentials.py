"""
Simple Kaggle API Setup
"""

import os
import json

def create_kaggle_json():
    """Create kaggle.json with your credentials"""
    
    print("Kaggle API Setup")
    print("=" * 16)
    
    # Use provided credentials
    username = "priyanshuksharma"
    key = "183d115db4781f73be654efdaa2b23dc"
    
    # Create kaggle directory
    kaggle_dir = os.path.expanduser("~/.kaggle")
    os.makedirs(kaggle_dir, exist_ok=True)
    
    # Create kaggle.json
    kaggle_config = {
        "username": username,
        "key": key
    }
    
    kaggle_file = os.path.join(kaggle_dir, "kaggle.json")
    
    with open(kaggle_file, 'w') as f:
        json.dump(kaggle_config, f)
    
    # Set permissions (Unix/Linux/Mac)
    try:
        os.chmod(kaggle_file, 0o600)
    except:
        pass  # Windows doesn't need this
    
    print(f"Created {kaggle_file}")
    return True

def test_kaggle_connection():
    """Test Kaggle API connection"""
    try:
        import kaggle
        kaggle.api.authenticate()
        print("Kaggle API working!")
        return True
    except Exception as e:
        print(f"Kaggle API failed: {e}")
        return False

if __name__ == "__main__":
    if create_kaggle_json():
        test_kaggle_connection()