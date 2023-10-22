from file_monitor import FileMonitor

if __name__ == "__main__":
    folder_path = "testFolder"
    monitor = FileMonitor(folder_path)

    while True:
        user_input = input("Enter command (commit/info <filename>/status/exit): ").split()
        if user_input[0] == "commit":
            monitor.commit()
        elif user_input[0] == "info" and len(user_input) > 1:
            monitor.info(user_input[1])
        elif user_input[0] == "status":
            monitor.status()
        elif user_input[0] == "exit":
            break
        else:
            print("Invalid command. Please try again.")