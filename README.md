# OpenRouter Skill for OpenClaw

🦞 OpenClaw skill for calling LLMs via OpenRouter API.

## Features

- Support for 20+ popular models (Claude, GPT-4, Gemini, DeepSeek, etc.)
- Free models available
- Simple command-line interface
- Compatible with NIM skill style

## Installation

```bash
# Clone to OpenClaw skills directory
git clone https://github.com/mapmiss/openclaw-openrouter-skill.git
cp -r openclaw-openrouter-skill/* ~/.nvm/versions/node/v24.14.0/lib/node_modules/openclaw/skills/openrouter/
```

## Setup

1. Get your API key from [openrouter.ai](https://openrouter.ai)
2. Set environment variable:
   ```bash
   export OPENROUTER_API_KEY="your_api_key_here"
   ```

## Usage

```bash
# List available models
python3 scripts/openrouter_call.py list

# Call a model
python3 scripts/openrouter_call.py claude "Hello!"
python3 scripts/openrouter_call.py gpt4o "Write a poem"
python3 scripts/openrouter_call.py deepseek "Explain quantum computing"
```

## Supported Models

| Alias | Model |
|-------|-------|
| `claude` | Claude 3.5 Sonnet |
| `gpt4o` | GPT-4o |
| `gemini` | Gemini Pro 1.5 |
| `deepseek` | DeepSeek Chat |
| `llama` | Llama 3.1 70B |
| `qwq` | QwQ 32B |

Free models: `llama-free`, `gemini-free`, `deepseek-free`

## License

MIT
