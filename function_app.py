import azure.functions as func
import logging

app = func.FunctionApp()
@app.function_name(name="openai_app")
@app.route(route="openai_function",auth_level=func.Auth_Level.ANONYMOUS)
def openai_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed so  successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
        
        # //git@github.com:Git-hubTeam/trappus-openaiapp.git