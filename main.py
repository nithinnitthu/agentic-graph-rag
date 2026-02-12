from app.agent import run_agent

if __name__ == "__main__":
    query = input("Enter your query: ")
    result = run_agent(query)
    print(result)
