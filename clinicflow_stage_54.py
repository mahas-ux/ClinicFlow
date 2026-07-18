# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: ClinicFlow
def colorize(text, style):
    codes = {
        'red': '\033[91m', 'green': '\033[92m', 'yellow': '\033[93m',
        'blue': '\033[94m', 'cyan': '\033[96m', 'bold': '\033[1m',
        'dim': '\033[2m', 'reset': '\033[0m'
    }
    return codes.get(style, '') + text + codes['reset']

def print_report(visitor):
    name = colorize(visitor.name, 'bold')
    pri = colorize(f"Priority: {visitor.priority}", 'cyan')
    status = colorize(f"Status: {visitor.status}", 'green' if visitor.status == 'seen' else 'yellow')
    print(f"{name} | {pri} | {status}")

if __name__ == '__main__':
    v1 = Visit(name='Alice', priority=2, status='seen')
    v2 = Visit(name='Bob', priority=5, status='waiting')
    print_report(v1)
    print_report(v2)
