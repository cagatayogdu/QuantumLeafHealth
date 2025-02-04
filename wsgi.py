from waitress import serve
from app import app

def print_intro():
    print("\n" + "=" * 40)
    print(" " * 10 + "█████████████████")
    print(" " * 10 + "█               █")
    print(" " * 10 + "█   2   QUBIT   █")
    print(" " * 10 + "█               █")
    print(" " * 10 + "█████████████████")
    print("=" * 40 + "\n")
    print('[SYSTEM] System yapılandırılması tamamlandı.')

if __name__ == "__main__":
    print_intro()
    serve(
        app, 
          host='localhost', 
          port=8080,
          threads=4
          )