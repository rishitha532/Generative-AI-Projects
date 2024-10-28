from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

completion = client.chat.completions.create(
  model="meta/llama-3.1-70b-instruct",
  messages=[{"role":"user","content":"Provide me an article on Transformer architecture in NLP"}],
  temperature=0.8,
  top_p=0.7,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

