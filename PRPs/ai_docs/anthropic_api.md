# Anthropic Messages API Documentation

## Key API Endpoint

- POST `/v1/messages`
- Base URL: `https://api.anthropic.com/v1/messages`

## Required Request Parameters

- `model`: Specify Claude model (e.g., "claude-sonnet-4-20250514")
- `messages`: Conversation history as an array of message objects
- `max_tokens`: Maximum tokens for response generation
- `x-api-key`: Authentication token
- `anthropic-version`: API version header

## Sample Request for Sentiment Analysis

```json
{
  "model": "claude-sonnet-4-20250514",
  "max_tokens": 1024,
  "messages": [
    {
      "role": "user",
      "content": "Analyze the sentiment of this customer review: [Review Text]"
    }
  ]
}
```

## Response Structure

- `content`: Generated analysis
- `id`: Unique message identifier
- `stop_reason`: Reason for response termination
- `usage`: Token consumption details

## Important Considerations

- Supports multi-turn conversations
- Can include text and image content
- Offers configurable parameters like temperature and tools
- Provides detailed usage metrics

## Sentiment Analysis Use Case

Recommended for sentiment analysis by leveraging Claude's contextual understanding and nuanced response generation.
