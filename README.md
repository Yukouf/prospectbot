# ProspectBot

<p align="center">
  <a href="README.md">English</a> &bull;
  <a href="README_fr.md">Français</a>
</p>

Generates in bulk personalized prospecting messages for local businesses, from a local LLM (Ollama). The idea: produce short, natural and non-pushy messages, with no data leaving the machine.

## What it does

1. You enter businesses (name, address, phone number) or paste a list.
2. For each business, ProspectBot calls a small local model (`phi3:3.8b` via Ollama) to draft a prospecting message of 2 sentences max.
3. The generated messages are displayed for copy and paste, and exported to a CSV.

The model is configured to:
- stay natural, like a real private message (not corporate)
- offer help with a modern website
- end with a simple question
- not mention prices, nor be pushy or sales-oriented

## Prerequisites

- Python 3
- [Ollama](https://ollama.com/) installed and running
- The local model `phi3:3.8b` (`ollama pull phi3:3.8b`)
- The `requests` package

## Usage

```bash
python3 prospectbot.py
```

Follow the prompts:
- leave blank to finish the entry
- no entry -> it uses demonstration examples
- valid messages are copied in the terminal, everything is exported to `prospects.csv`

## Data files

The files `prospects.csv`, `prospects.json` and `scraped.json` contain real prospecting data (names, addresses, phone numbers). They are **excluded from the repository** via `.gitignore` so as not to distribute personal information or canvassing data.

## Limits and ethics

- Demonstration tool: to be adapted to comply with the rules (GDPR, opt-out, prospecting practices) depending on the context of use.
- The local model produces text; always check the content before an actual send.
- No data leaves your machine when you use Ollama locally.

## Author

Created by [Youssef Guerniou](https://github.com/Yukouf), for prospecting local businesses without leaving the machine.
