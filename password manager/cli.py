import argparse
from password_manager.manager import PasswordManager

def main():
    parser = argparse.ArgumentParser(description="Password Manager CLI")
    parser.add_argument("action", choices=["store", "retrieve"], help="Action to perform")
    parser.add_argument("--service", required=True, help="Service name (e.g., Gmail, Facebook)")
    parser.add_argument("--username", help="Username for the service")
    parser.add_argument("--password", help="Password for the service (only for store)")

    args = parser.parse_args()
    manager = PasswordManager()

    if args.action == "store":
        if not args.password or not args.username:
            print("For storing a password, both username and password are required.")
            return
        manager.store_password(args.service, args.username, args.password)
        print(f"Password stored for service: {args.service}")
    elif args.action == "retrieve":
        credentials = manager.retrieve_password(args.service)
        if credentials:
            print(f"Service: {args.service}")
            print(f"Username: {credentials['username']}")
            print(f"Password: {credentials['password']}")
        else:
            print(f"No credentials found for service: {args.service}")

if __name__ == "__main__":
    main()
