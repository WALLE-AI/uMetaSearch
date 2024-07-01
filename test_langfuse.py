from langfuse.decorators import observe
from langfuse.openai import openai # OpenAI integration

from langfuse import Langfuse

# LANGFUSE_SECRET_KEY="sk-lf-26c48eb9-56c2-4349-9b37-05a88ce75e19"
# LANGFUSE_PUBLIC_KEY="pk-lf-a6cee029-812e-4881-9bd7-dabe3154577c"
# LANGFUSE_HOST="https://us.cloud.langfuse.com"

# langfuse = Langfuse(
#   secret_key="sk-lf-26c48eb9-56c2-4349-9b37-05a88ce75e19",
#   public_key="pk-lf-a6cee029-812e-4881-9bd7-dabe3154577c",
#   host="https://us.cloud.langfuse.com" 
# )

 
@observe()
def story():
    return openai.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        messages=[
          {"role": "system", "content": "You are a great storyteller."},
          {"role": "user", "content": "你是谁"}
        ],
        metadata={"someMetadataKey": "someValue"},
    ).choices[0].message.content
 
@observe()
def main():
    return story()

if __name__ == "__main__":
    main()
 