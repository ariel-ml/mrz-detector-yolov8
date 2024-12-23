import os


def find_project_root(start_dir):
    """
    Find the project root directory by looking for a specific marker file or folder.
    """
    current_dir = start_dir
    while current_dir != "/":  # Stop when reaching the filesystem root
        if any(
            item in os.listdir(current_dir) for item in [".git", "requirements.txt"]
        ):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    return None


# Find the project root starting from the current working directory
def cwd_to_root():
    project_root = find_project_root(os.getcwd())

    if project_root:
        # Change the current working directory to the project root
        os.chdir(project_root)
        print(f"Current working directory set to project root: {project_root}")
    else:
        print("Project root not found.")
