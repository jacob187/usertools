import os, argparse


def create_directories(class_name, base_name, num_directories):
    for i in range(1, num_directories + 1):
        dir_name = f"{base_name}{i}"
        os.makedirs(os.path.join(class_name, dir_name))
        print(f"Created directory: {os.path.join(class_name, dir_name)}")


def add_common_folder(folder_name):
    for class_dir in os.listdir("."):
        if os.path.isdir(class_dir):
            os.makedirs(os.path.join(class_dir, folder_name))
            print(f"Added folder {folder_name} to {class_dir}")


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
        print(f"Creating directories for class: {class_name}")

        base_name = input(f"Enter the base name for {class_name} directories: ")

        while True:
            num_directories_str = input(
                f"Enter the number of directories to create for {class_name} (or leave empty to skip): "
            )
            if not num_directories_str:
                num_directories = 0
                break
            try:
                num_directories = int(num_directories_str)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number or leave it empty.")

        if num_directories > 0:
            create_directories(
                os.path.join(parent_dir, class_name), base_name, num_directories
            )
    add_folder_response = input(
        "Do you want to add a common folder to all classes? (yes/no): "
    )
    if add_folder_response.lower() == "yes":
        common_folder_name = input("Enter the name of the common folder to add: ")
        add_common_folder(common_folder_name)

    print("All directories created successfully.")


if __name__ == "__main__":
    main()
