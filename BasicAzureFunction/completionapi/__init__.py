import logging
import openai
import azure.functions as func

secret_key = "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"

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # give open ai our secret key to authenticate
    openai.api_key = secret_key
    # get variable from the http body
    req_body = req.get_json()
    # call the openAI API
    output = openai.Completion.create(
        model = req_body['model'],
        prompt = req_body['prompt'],
        max_token = req_body['max_tokens'],
        temperature = ["temperature"]

    )
    # format the response
    output_text = output['choices'][0]['text']
    
    return func.HttpResponse(output_text, status_code = 200)