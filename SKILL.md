---
name: openrouter
description: >
  Invoke various LLMs (Claude, GPT-4, Gemini, DeepSeek, Llama, etc.) via OpenRouter API 
  to save main agent tokens and leverage specialized model capabilities. 
  Supports 24+ free models with no payment required.
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

### 查看可用模型
```bash
python3 scripts/openrouter_call.py list
```

### 调用模型
```bash
python3 scripts/openrouter_call.py <model_alias> "<prompt>"
```

## 免费模型别名 (FREE)
- `llama-free`, `qwen3-coder-free`, `gemma-27b-free`, `mistral-24b-free`
- `nemotron-9b-free`, `glm-free`, `hermes-405b-free`

## 付费模型别名
- `claude`, `gpt4o`, `gemini`, `deepseek`, `llama`, `qwen`

## Integration with OpenClaw
Add to your `MEMORY.md`:
```markdown
## OpenRouter Skill
- **默认模型：** `llama-free`
- **API Key：** 已配置在 `~/.bashrc`
- **脚本路径：** `skills/openrouter/scripts/openrouter_call.py`
```
