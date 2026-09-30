# Task Manager CLI

A simple command-line application for managing tasks efficiently from the terminal.

<img width="306" height="230" alt="Screenshot From 2026-09-30 11-53-15" src="https://github.com/user-attachments/assets/def31885-3378-4bfd-affe-5ead9330be02" />


## Features

- Add a new task
- View all tasks
- Mark a task as complete
- Delete a task
- Exit the application

## Prerequisites

- Python 3.x installed on your system
- Git (optional, for cloning the repository)

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/galib-ds/Task-Manager-CLI.git
```

```bash
cd Task-Manager-CLI
```

### 2. Create and activate a virtual environment

#### Linux / macOS

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

#### Windows

```powershell
python -m venv .venv
```

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

## Run the application

```bash
python3 -m app.main
```

If you are using Windows, you can also run:

```powershell
python -m app.main
```

## Deactivate the virtual environment

```bash
deactivate
```

## Notes

This project is designed as a lightweight CLI task manager and is ideal for learning Python application structure and terminal-based project workflows.
