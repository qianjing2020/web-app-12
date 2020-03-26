import basilica
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")

def basilica_api_client():
    connection = basilica.Connection(API_KEY)
    return connection

if __name__ == "__main__":
    connection = basilica_api_client()
    with connection as c:
        # use "with connection_object as x" will automatically close the connection after the block
        sentences = ["hello", "how are you"]
        print(sentences)
        embeddings = c.embed_sentences(sentences)
        print(list(embeddings))
