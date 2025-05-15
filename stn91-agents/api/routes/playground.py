from os import getenv

from agno.playground import Playground

from agents.sage import get_sage
from agents.scholar import get_scholar
from workspace.dev_resources import dev_fastapi

######################################################
## Router for the Playground Interface
######################################################

sage_agent = get_sage(debug_mode=True)
scholar_agent = get_scholar(debug_mode=True)
email_agent = get_scholar(debug_mode=True)

# Create a playground instance
playground = Playground(agents=[sage_agent, scholar_agent, email_agent])

# Register the endpoint where playground routes are served with agno.com
if getenv("RUNTIME_ENV") == "dev":
    endpoint = f"http://localhost:{dev_fastapi.host_port}"
    print(f"Registering playground endpoint at: {endpoint}")
    playground.create_endpoint(endpoint)

playground_router = playground.get_async_router()
