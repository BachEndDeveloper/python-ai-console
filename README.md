# Python AI Console

A smart home assistant powered by Azure OpenAI and Semantic Kernel that can control lights through natural language commands.

## Features

- Natural language processing for smart home control
- Light control functionality (turn on/off lights in specific rooms)
- Conversational AI interface using Azure OpenAI
- Function calling capabilities with Semantic Kernel

## Prerequisites

- Python 3.8 or higher
- Azure OpenAI account and API key
- pip (Python package installer)

## Quick Setup

### 1. Clone the repository
```bash
git clone https://github.com/BachEndDeveloper/python-ai-console.git
cd python-ai-console
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
```bash
cp .env.example .env
```

Edit the `.env` file with your Azure OpenAI credentials:
- `AZURE_OPENAI_API_KEY`: Your Azure OpenAI API key
- `AZURE_OPENAI_ENDPOINT`: Your Azure OpenAI endpoint URL
- `AZURE_OPENAI_DEPLOYMENT_NAME`: Your deployment name (e.g., "gpt-4")

### 5. Run the application
```bash
python main.py
```

## Usage

Once the application is running, you can interact with it using natural language:

```
User > Turn on the lights in the living room
Assistant > The lights in the living room have been turned on.

User > Turn off the bedroom lights
Assistant > The lights in the bedroom have been turned off.

User > exit
```

## Project Structure

```
python-ai-console/
├── main.py              # Main application entry point
├── requirements.txt     # Python dependencies
├── .env.example        # Environment variables template
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Development

### Code Style
This project uses:
- `black` for code formatting
- `flake8` for linting
- `isort` for import sorting

Run formatting:
```bash
black main.py
isort main.py
flake8 main.py
```

### Testing
Run tests using pytest:
```bash
pytest
```

## Configuration

The application can be configured through environment variables or by directly editing the configuration in `main.py`.

### Key Configuration Options
- **Azure OpenAI Deployment**: Change the `deployment_name` parameter
- **Logging Level**: Modify the logging configuration in the `main()` function
- **Plugin Functions**: Add new functions to the `LightsPlugin` class

## Troubleshooting

### Common Issues

1. **Authentication Error**: Ensure your Azure OpenAI API key and endpoint are correct
2. **Module Not Found**: Make sure you've activated your virtual environment and installed dependencies
3. **Connection Error**: Check your internet connection and Azure service status

### Getting Help

- Check the [Semantic Kernel documentation](https://learn.microsoft.com/en-us/semantic-kernel/)
- Review Azure OpenAI service documentation
- Create an issue in this repository

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.