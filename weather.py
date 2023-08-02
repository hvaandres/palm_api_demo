from dotenv import load_dotenv
import os
import google.generativeai as palm
load_dotenv()

palm_api_key = os.getenv("Palm_API")

# Testing connection to PALM API
palm.configure(api_key=palm_api_key)

defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.3,
    'candidate_count': 3,
    'max_output_tokens': 100,

}

prompt = '''
Come up with a research about how the weather will look in 10 years, taking into a count all the truobles that we are facing right now.
'''

response = palm.generate_text(
    **defaults,
    prompt=prompt,
)
print(response.result)