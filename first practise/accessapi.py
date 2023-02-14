secret_key = "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"
prompt = "Give a slogan for kids shopping website within 50 words"

import openai
openai.api_key = secret_key

output = openai.Completion.create(
    model = 'text-davinci-003',
    prompt = prompt,
    max_tokens = 200,
    temperature = 0
)

output_text = output['choices'][0]['text']


print(output_text)