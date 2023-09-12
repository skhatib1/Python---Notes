from pathlib import Path
import re

HOME = Path.home()
MOVIES = HOME / "Videos" / "Movies"
SUBTITLES = MOVIES / "Videos" / "Subtitles"


def perform_scan(path, search):

    return path.rglob(search)


def check_paths():
    """Validate given paths."""

    print("\nValidating paths:")

    path_list = [HOME, MOVIES, SUBTITLES]

    for path in path_list:
        print(f"- {path}")
        if not Path(path).exists():
            return f"ERROR: Invalid Path: {path}"

    print("\nPath validation passed.\n")



def remove_junk():
    """Removes unecessary files like images, text and executable files."""

    print("\nRemoving junk files...")

    counter = 0

    for item in perform_scan(MOVIES, "*"):
        if item.is_file() and item.suffix not in [".mp4", ".mkv"]:
            print("- " + item.name)
            item.unlink()
            counter += 1

    print(f"\nJunk files removed: {counter}\n")


def rename_directories():
    """Rename directories to correct standard."""

    print("\nRenaming directories...")

    counter = 0

    for item in perform_scan(MOVIES, "*"):
        if item.is_dir():
            non_standard_name = re.search(r"\[.*]", item.name)
            if non_standard_name:
                new_dir_name = re.sub(r"\[.*]", "", item.name)
                new_dir_path = item.with_name(new_dir_name)
                print(f"- Rename: {item.name} --> {new_dir_name}")
                item.rename(new_dir_path)
                counter += 1


    print(f"\nDirectories renamed: {counter}\n")


def rename_movies():
    """Rename files to correct standard."""

    print("\nRenaming files...")

    counter = 0

    for item in perform_scan(MOVIES, "*"):
        if item.is_file() and item.suffix in [".mp4", ".mkv"]:
            non_standard_name = re.search(r"\[.*]|BluRay|YIFY|x264", item.name)
            if non_standard_name:

                new_stem = " ".join(item.stem.split("."))
                new_stem = re.sub(r"\s1080p.*", "", new_stem)
                new_stem = re.sub(r"\s720p.*", "", new_stem)
                new_stem = re.sub(r"\sBluRay", "", new_stem)
                year = re.search(r"\d{4}", new_stem)
                if year:
                    new_stem = re.sub(r"\d{4}", f"({year.group(0)})", new_stem)

                print(f"- Renaming: {item.name} --> {new_stem}{item.suffix}")
                new_file_path = item.with_stem(new_stem)
                try:
                    item.rename(new_file_path)
                    counter += 1
                except FileExistsError:
                    print(f"ERROR: File already exists: {new_file_path}")
                    print(f"FIX: Deleting duplicate file: {item}")
                    item.unlink()

    print(f"\nFiles renamed: {counter}\n")


def move_movies():
    """Move movies to movies directory"""

    print("\nMoving movie files...")

    counter = 0

    for item in perform_scan(MOVIES, "*"):
        if item.is_file() and item.suffix in [".mp4", ".mkv"]:
            if item.parent != MOVIES:
                new_path = MOVIES / item.name
                try:
                    item.rename(new_path)
                    counter += 1
                except FileExistsError:
                    print(f"ERROR: File already exists: {new_path}")
                    print(f"FIX: Deleting duplicate file: {item}")
                    item.unlink()

    print(f"\nMovie files moved: {counter}\n")


def main():

    check_paths()
    remove_junk()
    rename_movies()
    move_movies()


if __name__== "__main__":
    main()

