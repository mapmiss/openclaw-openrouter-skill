#!/usr/bin/env python3
"""
OpenRouter API 调用脚本
参考 nim_call.py 风格实现
"""

import urllib.request
import json
import ssl
import sys
import os

# 模型别名映射表
MODEL_MAP = {
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
    "gemini-flash": "google/gemini-2.0-flash-exp:free",
    
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
    
    # --- 免费模型 ---
    "llama-free": "meta-llama/llama-3.2-3b-instruct:free",
    "gemini-free": "google/gemini-2.0-flash-exp:free",
    "deepseek-free": "deepseek/deepseek-r1:free",
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
    except Exception as e:
        return f"Error: {str(e)}"

def list_models():
    print("\n--- OpenRouter 可用模型别名列表 ---")
    print(f"{'别名':<18} | {'模型 ID'}")
    print("-" * 60)
    for alias, mid in sorted(MODEL_MAP.items()):
        print(f"{alias:<18} | {mid}")
    print("-" * 60)
    print("提示: 你也可以直接使用 OpenRouter 支持的完整模型 ID。\n")

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
