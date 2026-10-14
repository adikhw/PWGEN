from cli import show_menu_and_run

def main():
    """Run the application and handle unexpected interruptions or errors."""
    try:
        show_menu_and_run()
    except (KeyboardInterrupt, EOFError):
        print()
        print("Goodbye")

    except Exception:
        print()
        print("Unexpected error occured, please try again later")

if __name__ == "__main__":
    main()