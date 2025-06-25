import argparse
import os

def get_current_version(version_file, tag_prefix):
    if os.path.exists(version_file):
        with open(version_file, 'r') as f:
            return f.read().strip().lstrip(tag_prefix)
    return "0.0.0"

def increment_version(version, bump_type):
    major, minor, patch = map(int, version.split('.'))
    if bump_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif bump_type == 'minor':
        minor += 1
        patch = 0
    elif bump_type == 'patch':
        patch += 1
    return f"{major}.{minor}.{patch}"

def main():
    parser = argparse.ArgumentParser(description="Manage semantic versioning.")
    parser.add_argument('bump_type', choices=['major', 'minor', 'patch'], help="Type of version bump.")
    parser.add_argument('--version-file', default='VERSION', help="Path to the version file.")
    parser.add_argument('--tag-prefix', default='', help="Prefix for the git tag.")
    args = parser.parse_args()

    current_version = get_current_version(args.version_file, args.tag_prefix)
    new_version = increment_version(current_version, args.bump_type)

    with open(args.version_file, 'w') as f:
        f.write(args.tag_prefix + new_version)

    print(f"Version bumped from {current_version} to {new_version}")
    print(f"::set-output name=new_version::{args.tag_prefix}{new_version}")

if __name__ == "__main__":
    main() 