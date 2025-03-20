from openai import OpenAI
from os import getenv
from decouple import config


OPENAI_API_KEY = config("DEEPSEEL_R1")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=OPENAI_API_KEY,
)

try:
  completion = client.chat.completions.create(
    extra_headers={
      # "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
      # "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="deepseek/deepseek-r1",
    messages=[
      {
        "role": "user",
        "content": "Why Listening is important?"
      }
    ]
  )
  print(completion.choices[0].message.content)

except Exception as e:
  print(e)
