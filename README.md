# gpt-commit

gpt-commit is a tool that leverages OpenAI's language model to automatically generate commit messages or Agile stories from your git diffs. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install and use gpt-commit, you need to have Python 3 and Git installed in your environment. 

1. Clone this repository
```bash
git clone https://github.com/yourusername/gpt-commit.git
cd gpt-commit
```

2. Install the required Python libraries
```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key as an environment variable.
```bash
export OPENAI_API_KEY=yourapikey
```

## Usage
The script requires an argument to determine the type of output. The choices are 'detailed_commit', 'brief_commit', and 'story'. If no argument is provided, it defaults to 'brief_commit'.

To use gpt-commit in your terminal, navigate to the directory of the git repository you want to generate a commit message or Agile story for and run the script.

```bash
gpt-commit.py --output_type output_type
```

Replace output_type with one of the following:

- 'detailed_commit' for a detailed commit message.
- 'brief_commit' for a brief commit message.
- 'story' for an Agile user story.

## Contributing
Yo! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

### Fork the Project
- Create your Feature Branch (git checkout -b feature/AmazingFeature)
- Commit your Changes (git commit -m 'Add some AmazingFeature')
- Push to the Branch (git push origin feature/AmazingFeature)
- Open a Pull Request




