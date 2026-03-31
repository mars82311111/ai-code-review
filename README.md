# ai-code-review

**AI-powered code review in one command**

## Usage

```bash
# Review a diff file
python3 ai_code_review.py changes.diff

# Pipe git diff directly
git diff | python3 ai_code_review.py -

# Review specific file
git diff main.py > changes.diff
python3 ai_code_review.py changes.diff
```

## Features

- 🔍 Security scanning (credentials, API keys)
- 🐛 Debug code detection
- 📝 Code quality checks
- ⚡ Zero config, runs locally

## Install

```bash
pip install openai anthropic
export OPENAI_API_KEY=your_key
```

## License

MIT
