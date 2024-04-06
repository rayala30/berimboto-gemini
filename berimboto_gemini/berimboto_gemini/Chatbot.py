
from google.cloud import aiplatform
import prompts

def interact_with_chatbot(user_input):
    # Set up the client (replace with endpoint and region)

    # TODO
    # client_options = {"api_endpoint": "us-central1-aiplatform.googleapis.com"}
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

    # Create the prompt
    prompt = prompts.GoogleAIPrompt(text=user_input)
    prompt_dict = prompt.to_dict()

    # Send the request to the LLM
    response = client.predict(
        endpoint="your-endpoint-id", instances=[prompt_dict]
    )

    # Process the response
    chatbot_response = response.predictions[0]
    return chatbot_response

def main():
    while True:
        user_input = input("You: ")
        chatbot_response = interact_with_chatbot(user_input)
        print("Berimboto:", chatbot_response)


if __name__ == "__main__":
    main()

