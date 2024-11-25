from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
from fastapi.responses import RedirectResponse
from markdown import markdown
from langchain.schema import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

app = FastAPI()

# Setup for LangChain's Google Generative AI
GEMINI_API_KEY = "AIzaSyC2ONnLcokJ0awQLYF24A966Hgv7E8hIsA"  # Replace with your actual API key
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    api_key=GEMINI_API_KEY,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

templates = Jinja2Templates(directory="templates")

# Function to fetch GitHub details
def account_detail_fetching(username: str):
    github_username = username
    github_api_url = f"https://api.github.com/users/{github_username}"

    headers = {
        'User-Agent': 'PythonApp',
        'Accept': 'application/vnd.github.v3+json'
    }

    user_data = None
    repos_data = []

    try:
        # Fetch user details
        user_response = requests.get(github_api_url, headers=headers, timeout=10)
        if user_response.status_code == 200:
            user_data = user_response.json()

            # Fetch repository details
            repos_api_url = user_data.get("repos_url")
            repos_response = requests.get(repos_api_url, headers=headers, timeout=10)
            if repos_response.status_code == 200:
                repos_data = repos_response.json()
            else:
                print("Failed to fetch repository information.")
        else:
            print(f"Failed to fetch user information for {github_username}")
    except Exception as e:
        print(f"Error occurred: {e}")

    return user_data, repos_data


# Generate summary function
def Generate_summary(username: str):
    user_data, repos_data = account_detail_fetching(username)
    if not user_data:
        return "User data could not be fetched. No user exist with this Username"

    user_info = f"""
    GitHub User: {user_data.get('login')} ({user_data.get('name')})
    Bio: {user_data.get('bio')}
    Location: {user_data.get('location')}
    Public Repositories: {user_data.get('public_repos')}
    Followers: {user_data.get('followers')}
    Following: {user_data.get('following')}
    Profile URL: {user_data.get('html_url')}
    """

    repositories_info = "\n".join([
        f"""
    Repository Name: {repo.get('name')}
    Description: {repo.get('description')}
    Stars: {repo.get('stargazers_count')}
    Forks: {repo.get('forks_count')}
    Repository URL: {repo.get('html_url')}
    """
        for repo in repos_data
    ])

    # Template for prompt
    template = """You are a very good assistant that summarizes GitHub profiles.

    Here's the GitHub profile and repositories you want to summarize.

    ==================
    User Information:
    {user_info}

    Repositories:
    {repositories_info}
    ==================

    Write a summary of the GitHub profile and repositories.
    """

    # Format the prompt
    prompt = template.format(user_info=user_info, repositories_info=repositories_info)

    # Create messages for LangChain pipeline
    messages = [HumanMessage(content=prompt)]
    summary = llm.invoke(messages)

    # Template for bulleted list
    template = """You are an advanced AI assistant that summarizes GitHub profiles into concise, bulleted lists 
    also at last you suggest user how to improve thier github profile by observing the limitation in current profile.

    Here's the GitHub profile summary you need to summarize.

    ==================
    {github_profile_summary}
    ==================

    Now, provide a summarized version of the profile in a concise, bulleted list format.
    """

    # Format prompt for summary generation
    prompt = template.format(github_profile_summary=summary.content)

    # Generate summary in bulleted format
    final_summary = llm.invoke([HumanMessage(content=prompt)])
    # print(final_summary.content)
    return final_summary.content


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "username": "", "summary": ""})

@app.post("/search", response_class=HTMLResponse)
async def search(request: Request, username: str = Form(...)):
    # Generate the summary and convert it to HTML using markdown
    summary = Generate_summary(username)
    summary_html = markdown(summary)
    return templates.TemplateResponse("index.html", {"request": request, "username": username, "summary": summary_html})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
