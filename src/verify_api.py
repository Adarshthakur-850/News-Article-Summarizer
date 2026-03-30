import requests
import sys

def test_api():
    base_url = "http://127.0.0.1:8000"
    
    # 1. Health Check
    try:
        resp = requests.get(f"{base_url}/health")
        print(f"Health Response: {resp.json()}")
    except Exception as e:
        print(f"Health check failed: {e}")
        sys.exit(1)

    # 2. Summarization
    text = """
    SpaceX is an American aerospace manufacturer, a provider of space transportation services, and a communications corporation headquartered in Hawthorne, California. 
    It was founded in 2002 by Elon Musk with the goal of reducing space transportation costs to enable the colonization of Mars. 
    SpaceX manufactures the Falcon 9 and Falcon Heavy launch vehicles, several rocket engines, Cargo Dragon, crew spacecraft, and Starlink communications satellites.
    """
    
    payload = {"text": text}
    
    try:
        print("Sending summarization request (this may take time for first load)...")
        resp = requests.post(f"{base_url}/summarize", json=payload)
        if resp.status_code == 200:
            print(f"Summary: {resp.json()['summary']}")
        else:
            print(f"Summarization failed ({resp.status_code}): {resp.text}")
            sys.exit(1)
    except Exception as e:
        print(f"Request failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_api()
