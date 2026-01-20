1. Structure folder for docs
2. Dann Framework
3. Created Version/Readme.md
   - this is where the summary of the project for the future
   - changelog README
4. Fill up the Dann Framework
   - Concern about how user experience
   - What AWS Service to use and cost of prototype
   - Compare Version/Readme.md and DannFramework_docs if there are contradictions.
   - Use gemini flash openrouter, pasted prompt to look for improvement and contradiction on my documentation
5. Created new Branch named v1
6. Use the prompt from DannFramework to generate todo task. Note use Openrouter: Gemini Flash for planning Version
7. Create .env.example file for environment variables
8. Created IAM Account dedicated to the project
   - Check marked to generate custom password
   - Permission to: AWS-FullStack-Deployment (Ive built this months ago suitable for this project)
   - 
9. AWS Cognito, we didnt use (Google OAuth via ) since you need GCP here, we want to stick in AWS
   - Create user pool > Copy paste the form in AWS and ask AI the appropriate to answer 
   - Add a return url: http://localhost:3000 for prototype and change this later for production
10. Backend Setup
    ```
    mkdir backend && cd backend && python -m venv venv && source venv/bin/activate && pip install fastapi uvicorn sqlalchemy psycopg2-binary boto3 "python-jose[cryptography]" "pydantic[email]
    ```

    requirements.txt (Inside backend/backend, run this)
    ```
    pip freeze > requirements.txt
    ```
    - Set Up Database Models (models.py)

11. 
