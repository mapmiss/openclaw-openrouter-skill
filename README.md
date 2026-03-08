# OpenRouter Skill for OpenClaw

🦞 OpenClaw skill for calling LLMs via OpenRouter API.

## Features

- **24+ Free Models** - No payment required!
- **20+ Paid Models** - Claude, GPT-4o, Gemini, etc.
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
python3 scripts/openrouter_call.py llama-free "Hello!"
python3 scripts/openrouter_call.py qwen3-coder-free "Write a Python function"
python3 scripts/openrouter_call.py gemma-27b-free "Explain quantum computing"
```

## 🆓 Free Models (No Payment Required!)

| Alias | Model |
|-------|-------|
| `llama-free` | Meta Llama 3.3 70B |
| `qwen3-coder-free` | Qwen3 Coder 480B |
| `gemma-27b-free` | Google Gemma 3 27B |
| `mistral-24b-free` | Mistral Small 3.1 24B |
| `nemotron-9b-free` | NVIDIA Nemotron Nano 9B |
| `glm-free` | GLM 4.5 Air |
| `hermes-405b-free` | Nous Hermes 3 405B |

## 💰 Paid Models

| Alias | Model |
|-------|-------|
| `claude` | Claude 3.5 Sonnet |
| `gpt4o` | GPT-4o |
| `gemini` | Gemini Pro 1.5 |
| `deepseek` | DeepSeek Chat |

## Tips

- Free models may have rate limits
- Use full model ID if alias not available: `meta-llama/llama-3.3-70b-instruct:free`

## License

MIT
