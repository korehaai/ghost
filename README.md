# GHOST

**Gathered History Of System Traces**

GHOST is a silent, local Python system-information collector. It gathers a small set of system and resource details in memory and displays a report only after collection is complete.

## Features

- Operating system and Python runtime details
- Machine architecture and hostname
- CPU logical-core count
- Home-directory disk capacity and usage
- A small allowlist of non-secret environment settings
- Collection start and finish timestamps
- Formatted terminal report after collection
- Automated tests
- Python standard library only

## Privacy

GHOST runs locally. It does not transmit collected data, inspect browser history, read personal documents, collect passwords or tokens, or scan the network. Environment collection is restricted to `LANG`, `LC_ALL`, `LC_CTYPE`, `TZ`, and `TERM`. The report is printed to the terminal after collection.

## Requirements

- Python 3.8 or newer
- No external dependencies

## Run

```bash
git clone https://github.com/YOUR-USERNAME/ghost.git
cd ghost
python main.py
```

Use `python3 main.py` on systems where Python is invoked that way.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
ghost/
├── main.py
├── ghost/
│   ├── __init__.py
│   ├── collector.py
│   └── report.py
├── tests/
│   ├── __init__.py
│   └── test_collector.py
├── README.md
└── LICENSE
```

## Design

The project separates collection from presentation. `GhostCollector` gathers information into a dictionary without printing. `print_report` is called only after collection finishes, so the terminal stays quiet during the collection phase.

## License

MIT
