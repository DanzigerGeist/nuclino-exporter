import os
import shutil
import argparse
from nuclino import Nuclino
from nuclino.objects import Collection, Item


def export_all_workspaces(client, output_dir):
    workspaces = client.get_workspaces()
    workspaces = workspaces if isinstance(workspaces, list) else [workspaces]

    if not workspaces:
        print("❌ No workspaces found.")
        return

    print(f"🚀 Found {len(workspaces)} workspaces. Exporting to '{
          output_dir}'...")

    for workspace in workspaces:
        workspace_name = sanitize_filename(workspace.name)
        workspace_path = os.path.join(output_dir, workspace_name)
        os.makedirs(workspace_path, exist_ok=True)
        print(f"\n📚 Exporting workspace: {workspace.name}")
        traverse_items(workspace.get_children(), workspace_path)

    print(f"\n✅ All workspaces exported! Check the '{output_dir}' folder.")


def traverse_items(items, current_path):
    for item in items:
        if isinstance(item, Collection):
            collection_path = os.path.join(
                current_path, sanitize_filename(item.title))
            os.makedirs(collection_path, exist_ok=True)
            print(f"📂 Created folder: {collection_path}")
            traverse_items(item.get_children(), collection_path)

        elif isinstance(item, Item):
            content = getattr(item, "content", "").strip()
            if content:
                file_name = f"{sanitize_filename(item.title)}.md"
                file_path = os.path.join(current_path, file_name)
                with open(file_path, "w", encoding="utf-8") as md_file:
                    md_file.write(content)
                print(f"📝 Exported document: {file_path}")


def sanitize_filename(name):
    return "".join(c if c.isalnum() or c in (" ", "-", "_") else "_" for c in name).strip()


def main():
    parser = argparse.ArgumentParser(
        description="Export Nuclino workspaces to a local directory.")
    parser.add_argument("--outputDir", type=str, default="./export",
                        help="Output directory for exported files.")
    parser.add_argument("--apiKey", type=str, required=True,
                        help="Nuclino API key (required).")

    args = parser.parse_args()
    output_dir = os.path.abspath(args.outputDir)

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)  # Clean up previous exports
    os.makedirs(output_dir, exist_ok=True)

    client = Nuclino(args.apiKey)
    export_all_workspaces(client, output_dir)


if __name__ == "__main__":
    main()
