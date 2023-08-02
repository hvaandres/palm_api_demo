
from dotenv import load_dotenv
import os
import google.generativeai as palm
load_dotenv()

palm_api_key = os.getenv("Palm_API")

# Testing connection to PALM API
palm.configure(api_key=palm_api_key)

# Testing the API

model_list = [_ for _ in palm.list_models()]
for model in model_list:
    print(model.name)


# Some text generation

model_id = 'models/text-bison-001'
prompt = '''
Write a professional summary for my resume as a DevOps. Limit the proposal to 100 words. 
'''

completion = palm.generate_text(
    # model_id - The model to use for generation
    model=model_id,
    # prompt - The text to start the generation from
    prompt=prompt,
    # Random sampling - Creativity of the output which can go for 0 to 1
    temperature=0.9,
    # max_output_tokens - Number of tokens to generate
    max_output_tokens=800,
    # We can also use candidate_count to get more diverse results
    candidate_count=2
)
# Returns the first result
completion.result
completion.candidates[0]['output']

outputs = [output['output'] for output in completion.candidates]
for output in outputs:
    print(output)
    print('-'*50)
