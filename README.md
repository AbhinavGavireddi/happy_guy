# 🎉 Happy Guy - Your AI-Powered Message Composer

Welcome to Happy Guy, an intelligent multi-agent system designed to craft personalized, emotionally resonant messages for every occasion. Whether it's celebrating birthdays, marking work anniversaries, or bidding farewell to colleagues, Happy Guy brings together a crew of specialized AI agents to create the perfect message.

## ✨ Features

- **Smart Data Collection**: Automatically gathers relevant information about the person from various online sources
- **Personalized Content Creation**: Generates tailored messages that reflect individual achievements and personality
- **Professional Tone Adjustment**: Ensures the perfect balance of warmth and professionalism
- **Multiple Event Types**: Supports various occasions:
  - 🎂 Birthdays
  - 🌟 Work Anniversaries
  - 👋 Farewells
- **HTML Template Integration**: Automatically formats messages into beautiful HTML templates

## 🚀 Installation

### Prerequisites
- Python >=3.10 <=3.13

1. Clone the repository:
```bash
cd happy_guy
```

2. Set up your environment variables in `.env`:
```env
SERPER_API_KEY='your_serper_key'    # Used for web search capabilities
OPENAI_API_KEY='your_openai_key'    # Used for AI content generation
```

## 🎯 Usage

To generate a personalized message, run:

```bash
crewai run
```

The system will prompt you for:
- Person's name
- Event type (birthday/work anniversary/farewell)
- Event date

## 🤖 Understanding the Crew

Happy Guy employs three specialized AI agents working in harmony:

### 1. Data Collector Agent
- 🔍 Searches across various online sources
- 📊 Gathers professional achievements and milestones
- 💾 Stores findings in `data_collection.md`

### 2. Content Creator Agent
- ✍️ Crafts initial message content
- 🎯 Incorporates collected data meaningfully
- 📝 Outputs draft to `content.md`

### 3. Tone Expert Agent
- 🎨 Refines message tone and style
- 📏 Ensures consistent 1000-word length
- ✨ Produces final content in `tone.md`

## 📂 Output Files

Happy Guy generates several files during its operation:

| File | Description |
|------|-------------|
| `data_collection.md` | Raw data collected about the person |
| `content.md` | Initial message draft |
| `tone.md` | Tone-adjusted final content |
| `output.html` | Beautifully formatted final message |
| `output.pkl` | Serialized output data |
| `happy_guy.log` | Detailed operation logs |

## 🏗️ Project Structure

```
happy_guy/
├── src/
│   └── crew/
│       ├── __init__.py      # Core configurations and data structures
│       ├── crew.py          # Agent and task definitions
│       ├── main.py          # Main execution logic
│       └── utils.py         # Helper functions
├── html_templates/          # Event-specific HTML templates
├── outputs/                 # Generated files directory
├── config/                  # Agent and task configurations
├── pyproject.toml          # Poetry dependency configuration
└── poetry.lock            # Locked dependencies
```

## 🛠️ Configuration

The system uses YAML configuration files in the `config/` directory:

- `agents.yaml`: Defines agent roles, goals, and backstories
- `tasks.yaml`: Specifies task descriptions and expected outputs

## 🤝 Contributing

We welcome contributions! Whether it's adding new event types, improving agent capabilities, or enhancing templates, feel free to:

1. Fork the repository
2. Create your feature branch
3. Submit a pull request

---
Made with ❤️ by the Finance Analytics Team