### HNG Stage 1 Task - User Information API
A FastAPI application that serves user information including email, current datetime, and GitHub URL. This API was developed as part of the HNG Internship Stage 1 task.

## Features
- Returns registered email address used for HNG12 Slack workspace
- Provides current datetime in ISO 8601 format (UTC)
- Returns GitHub repository URL
- Handles CORS (Cross-Origin Resource Sharing)
- Returns JSON formatted responses

## Technology Stack
- Python 3.8+
- FastAPI
- Uvicorn (ASGI server)
- Pyenv to create the virual environment

### Local Development Setup
##### Clone the repository:
```bash
git clone https://github.com/Marlinekhavele/HNG1
cd HNG1
```

##### Create and activate a virtual environment:
```bash
pyenv virtualenv env
pyenv activate env
```
##### Alternatively, using Python's built-in venv:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
##### Install dependencies:
```bash
pip install -r requirements.txt
```
##### Create a .env file in the root directory and add your configuration:
```bash
EMAIL=your-email@example.com
GITHUB_URL=https://github.com/yourusername/your-repo
```
##### Run the application:
```bash
uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000/docs
```
##### API Endpoint
**Method:** GET  
**Path:** `/`  
**Description:** Returns basic user information 
##### Example Request:
```bash
curl -X GET http://127.0.0.1:8000/
```
##### Response Format:
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```
##### Status Codes  
- **200 OK** – Successful request  
- **500 Internal Server Error** – An unexpected issue occurred  

##### Deployment
[https://hng1-production.up.railway.app/docs](https://hng1-production.up.railway.app/docs)

##### [https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)
