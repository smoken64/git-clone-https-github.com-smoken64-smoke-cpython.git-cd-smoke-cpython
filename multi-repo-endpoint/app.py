import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/repositories', methods=['POST'])
def handle_repositories():
    data = request.get_json()
    repositories = data.get('repositories', [])
    
    results = []
    for repo in repositories:
        repo_name = repo.split('/')[-1].replace('.git', '')
        try:
            # Clone the repository
            subprocess.run(['git', 'clone', repo], check=True)
            
            # Perform analysis (example: count files in the repo)
            file_count = len(os.listdir(repo_name))
            
            # Clean up by removing the cloned repository
            subprocess.run(['rm', '-rf', repo_name])
            
            results.append({'repository': repo, 'status': 'processed', 'file_count': file_count})
        except subprocess.CalledProcessError as e:
            results.append({'repository': repo, 'status': 'error', 'message': str(e)})
    
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True)
