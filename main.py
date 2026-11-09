from ghost.collector import GhostCollector
from ghost.report import print_report


def main():
    collector = GhostCollector()
    collector.collect()
    print_report(collector.data)


if __name__ == "__main__":
    main()
