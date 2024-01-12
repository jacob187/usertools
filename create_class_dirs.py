import os, argparse


def create_directories(class_name, base_name, num_directories):
    for i in range(1, num_directories + 1):
        dir_name = f"{base_name}{i}"
        os.makedirs(os.path.join(class_name, dir_name))
        print(f"Created directory: {os.path.join(class_name, dir_name)}")


def add_common_folder(parent_dir, common_folder_name):
    for class_dir in os.listdir(parent_dir):
        full_path = os.path.join(parent_dir, class_dir)
        if os.path.isdir(full_path):
            os.makedirs(os.path.join(full_path, common_folder_name), exist_ok=True)
            print(f"Added folder {common_folder_name} to {class_dir}")


def main():
    parser = argparse.ArgumentParser(description="Create class directories.")
    parser.add_argument(
        "parent_dir", type=str, help="Parent directory for the class directories."
    )
    args = parser.parse_args()

    parent_dir = args.parent_dir

    class_names = input(
        "Enter the names of the classes (separated by spaces): "
    ).split()

    for class_name in class_names:
        class_dir = os.path.join(parent_dir, class_name)
        os.makedirs(class_dir, exist_ok=True)
        print(f"Created directory: {class_dir}")

        base_name = input(f"Enter the base name for {class_name} directories: ")

        while True:
            num_directories_str = input(
                f"Enter the number of directories to create for {class_name} (or leave empty to skip): "
            )
            if not num_directories_str:
                break
            try:
                num_directories = int(num_directories_str)
                create_directories(class_dir, base_name, num_directories)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number or leave it empty.")

    common_folder_name = input(
        "Enter a common folder name to add to all class directories: "
    )
    if common_folder_name:
        add_common_folder(parent_dir, common_folder_name)

    print("All directories created successfully.")


if __name__ == "__main__":
    main()
