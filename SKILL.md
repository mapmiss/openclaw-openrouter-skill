---
name: openrouter
description: >
  Invoke various LLMs (Claude, GPT-4, Gemini, DeepSeek, etc.) via OpenRouter API 
  to save main agent tokens and leverage specialized model capabilities.
---

# OpenRouter Skill for OpenClaw

This skill allows OpenClaw to delegate tasks to external models hosted on the OpenRouter platform.

## Setup

1. **Get API Key**: Register at [openrouter.ai](https://openrouter.ai) and get your API key.
2. **Set Environment Variable**:
   ```bash
   export OPENROUTER_API_KEY="your_api_key_here"
   ```

## Usage

### List Available Models
```bash
python3 scripts/openrouter_call.py list
```

### Call a Model
```bash
python3 scripts/openrouter_call.py <model_alias> "<prompt>"
```

## Supported Model Aliases

| Alias | Model ID |
|-------|----------|
| `claude` | anthropic/claude-3.5-sonnet |
| `claude-opus` | anthropic/claude-3-opus |
| `gpt4` | openai/gpt-4-turbo |
| `gpt4o` | openai/gpt-4o |
| `gemini` | google/gemini-pro-1.5 |
| `llama` | meta-llama/llama-3.1-70b-instruct |
| `deepseek` | deepseek/deepseek-chat |
| `deepseek-r1` | deepseek/deepseek-r1 |
| `qwen` | qwen/qwen-2.5-72b-instruct |
| `qwq` | qwen/qwq-32b-preview |
| `mistral` | mistralai/mistral-large |

### Free Models
| Alias | Model ID |
|-------|----------|
| `llama-free` | meta-llama/llama-3.2-3b-instruct:free |
| `gemini-free` | google/gemini-2.0-flash-exp:free |
| `deepseek-free` | deepseek/deepseek-r1:free |

## Integration with OpenClaw

Add to your `MEMORY.md`:
```markdown
## OpenRouter Skill
- **默认模型：** `claude`
- **API Key：** 已配置在 `~/.bashrc`
- **脚本路径：** `skills/openrouter/scripts/openrouter_call.py`
```
