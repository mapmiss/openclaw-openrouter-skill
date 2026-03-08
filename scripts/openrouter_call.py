#!/usr/bin/env python3
"""
OpenRouter API 调用脚本
支持 20+ 模型别名，包含多个免费模型
"""

import urllib.request
import json
import ssl
import sys
import os

# 模型别名映射表
MODEL_MAP = {
    # ============ 免费模型 (FREE) ============
    # Meta Llama
    "llama-free": "meta-llama/llama-3.3-70b-instruct:free",
    "llama3-70b-free": "meta-llama/llama-3.3-70b-instruct:free",
    "llama3-3b-free": "meta-llama/llama-3.2-3b-instruct:free",
    
    # Qwen
    "qwen3-coder-free": "qwen/qwen3-coder:free",
    "qwen3-4b-free": "qwen/qwen3-4b:free",
    "qwen3-80b-free": "qwen/qwen3-next-80b-a3b-instruct:free",
    
    # Google Gemma
    "gemma-27b-free": "google/gemma-3-27b-it:free",
    "gemma-12b-free": "google/gemma-3-12b-it:free",
    "gemma-4b-free": "google/gemma-3-4b-it:free",
    "gemma-2b-free": "google/gemma-3n-e2b-it:free",
    
    # NVIDIA Nemotron
    "nemotron-9b-free": "nvidia/nemotron-nano-9b-v2:free",
    "nemotron-12b-free": "nvidia/nemotron-nano-12b-v2-vl:free",
    "nemotron-30b-free": "nvidia/nemotron-3-nano-30b-a3b:free",
    
    # Mistral
    "mistral-24b-free": "mistralai/mistral-small-3.1-24b-instruct:free",
    
    # OpenAI OSS
    "gpt-oss-120b-free": "openai/gpt-oss-120b:free",
    "gpt-oss-20b-free": "openai/gpt-oss-20b:free",
    
    # GLM
    "glm-free": "z-ai/glm-4.5-air:free",
    
    # Nous Hermes
    "hermes-405b-free": "nousresearch/hermes-3-llama-3.1-405b:free",
    
    # 其他
    "dolphin-free": "cognitivecomputations/dolphin-mistral-24b-venice-edition:free",
    "step-free": "stepfun/step-3.5-flash:free",
    "trinity-free": "arcee-ai/trinity-large-preview:free",
    
    # ============ 付费模型 ============
    # --- Anthropic ---
    "claude": "anthropic/claude-3.5-sonnet",
    "claude-opus": "anthropic/claude-3-opus",
    "claude-haiku": "anthropic/claude-3-haiku",
    
    # --- OpenAI ---
    "gpt4": "openai/gpt-4-turbo",
    "gpt4o": "openai/gpt-4o",
    "gpt4o-mini": "openai/gpt-4o-mini",
    "o1": "openai/o1-preview",
    
    # --- Google ---
    "gemini": "google/gemini-pro-1.5",
    
    # --- Meta ---
    "llama": "meta-llama/llama-3.1-70b-instruct",
    "llama405b": "meta-llama/llama-3.1-405b-instruct",
    
    # --- DeepSeek ---
    "deepseek": "deepseek/deepseek-chat",
    "deepseek-r1": "deepseek/deepseek-r1",
    
    # --- Qwen ---
    "qwen": "qwen/qwen-2.5-72b-instruct",
    "qwq": "qwen/qwq-32b-preview",
    
    # --- Mistral ---
    "mistral": "mistralai/mistral-large",
    "mixtral": "mistralai/mixtral-8x22b-instruct",
}

def call_openrouter(model_alias, prompt):
    model_id = MODEL_MAP.get(model_alias.lower(), model_alias)
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return "Error: OPENROUTER_API_KEY not found in environment."
        
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://openclaw.ai",
        "X-Title": "OpenClaw"
    }
    data = {
        "model": model_id,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 2048
    }
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    try:
        req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=120) as response:
            result = json.loads(response.read().decode())
            return result['choices'][0]['message']['content']
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        try:
            error_json = json.loads(error_body)
            return f"Error: {error_json.get('error', {}).get('message', str(e))}"
        except:
            return f"Error: HTTP {e.code} - {e.reason}"
    except Exception as e:
        return f"Error: {str(e)}"

def list_models():
    print("\n" + "=" * 70)
    print("  OpenRouter 可用模型别名列表")
    print("=" * 70)
    
    print("\n🆓 免费模型 (FREE):")
    print("-" * 70)
    print(f"{'别名':<22} | {'模型名称'}")
    print("-" * 70)
    free_models = [
        ("llama-free", "Meta Llama 3.3 70B"),
        ("llama3-3b-free", "Meta Llama 3.2 3B"),
        ("qwen3-coder-free", "Qwen3 Coder 480B"),
        ("qwen3-4b-free", "Qwen3 4B"),
        ("qwen3-80b-free", "Qwen3 Next 80B"),
        ("gemma-27b-free", "Google Gemma 3 27B"),
        ("gemma-12b-free", "Google Gemma 3 12B"),
        ("gemma-4b-free", "Google Gemma 3 4B"),
        ("nemotron-9b-free", "NVIDIA Nemotron Nano 9B"),
        ("mistral-24b-free", "Mistral Small 3.1 24B"),
        ("glm-free", "GLM 4.5 Air"),
        ("hermes-405b-free", "Nous Hermes 3 405B"),
        ("gpt-oss-120b-free", "OpenAI GPT-OSS 120B"),
    ]
    for alias, name in free_models:
        print(f"{alias:<22} | {name}")
    
    print("\n💰 付费模型 (需要充值):")
    print("-" * 70)
    print(f"{'别名':<22} | {'模型名称'}")
    print("-" * 70)
    paid_models = [
        ("claude", "Anthropic Claude 3.5 Sonnet"),
        ("gpt4o", "OpenAI GPT-4o"),
        ("gemini", "Google Gemini Pro 1.5"),
        ("deepseek", "DeepSeek Chat"),
        ("llama", "Meta Llama 3.1 70B"),
        ("qwen", "Qwen 2.5 72B"),
    ]
    for alias, name in paid_models:
        print(f"{alias:<22} | {name}")
    
    print("\n💡 提示: 你也可以直接使用 OpenRouter 支持的完整模型 ID")
    print("   例如: meta-llama/llama-3.3-70b-instruct:free\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 openrouter_call.py <alias|list> [prompt]")
    elif sys.argv[1].lower() == "list":
        list_models()
    elif len(sys.argv) >= 3:
        alias = sys.argv[1]
        task = " ".join(sys.argv[2:])
        print(call_openrouter(alias, task))
    else:
        print("错误: 缺少任务内容。如果是查看模型列表，请用 'list'。")
