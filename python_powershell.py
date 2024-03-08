import subprocess

def main():
    while True:
        # Get user input
        command = input("Enter a PowerShell command (or 'exit' to quit): ")

        if command.lower() == 'exit':
            break

        try:
            # Execute the command in PowerShell
            result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)

            # Print the output of the command
            print("Output:")
            print(result.stdout)

            # Print any errors
            if result.stderr:
                print("Errors:")
                print(result.stderr)

        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
