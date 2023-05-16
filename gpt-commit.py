#!/usr/bin/env python3

import openai
import os
import argparse
from git import Repo
from git.exc import GitCommandError
import sys

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Get the diff from your git repository
repo = Repo('.')
try:
    diff = repo.git.diff('HEAD~1')
except GitCommandError:
    print("There's only one commit or none in this repository. Please make more commits before using this tool.")
    sys.exit(1)  # Exit the program with a non-zero status to indicate an error

# Argument parser
parser = argparse.ArgumentParser(description="Generate commit messages or Agile stories with AI.")
parser.add_argument('--output_type', choices=['detailed_commit', 'brief_commit', 'story'], default='brief_commit')
args = parser.parse_args()

# Use OpenAI to get a commit message or Agile story for the diff
if args.output_type == 'detailed_commit':
    prompt = f'Please suggest a detailed commit message for this change. The message should contain point-by-point changes made in the diff:\n\n{diff}'
elif args.output_type == 'brief_commit':
    prompt = f'Please suggest a commit message for this change:\n\n{diff}'
else:  # args.output_type == 'story'
    prompt = f'Please write an Agile user story that reflects the changes made in this diff:\n\n{diff}'

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0.3,  # you can experiment with this value
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

# Print out the assistant's response
print(response['choices'][0]['message']['content'])

