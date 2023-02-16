import logging
import openai
import azure.functions as func

# sample request
# {"model":"text-davinci-003","prompt":"give me a slogan for a cookie company", "max_tokens":200,"temperature":0} 

secret_key = "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"

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # give open ai our secret key to authenticate
    openai.api_key = secret_key
    # get variable from the http body
    req_body = req.get_json()
    logging.info(type(req_body))
    # call the openAI API
    output = openai.Completion.create(
        model = req_body['model'],
        prompt = req_body['prompt'],
        max_tokens = req_body['max_tokens'],
        temperature = req_body["temperature"]

    )
    # format the response
    output_text = output['choices'][0]['text']
    
    return func.HttpResponse(output_text, status_code = 200)