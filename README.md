# 📚 Nuclino Workspace Exporter

This Python script exports all Nuclino workspaces into a local folder, preserving the hierarchy of collections (folders) and items (documents). Documents are saved as Markdown (`.md`) files.

---

## 🚀 Features
- Exports all workspaces under the Nuclino account.
- Creates folder structures for collections.
- Saves documents as `.md` files, named by their titles.

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/DanzigerGeist/nuclino-exporter.git
cd nuclino-exporter
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

## 📝 Usage

Run the script with the required --apiKey argument:
```bash
python export_nuclino.py --apiKey YOUR_NUCLINO_API_KEY
```

Optional: Specify a custom output directory:
```bash
python export_nuclino.py --apiKey YOUR_NUCLINO_API_KEY --outputDir ./my_exports
```

## 🛠️ CLI Options

| **Argument**  | **Required** | **Default**  | **Description**                |
|--------------|-------------|--------------|--------------------------------|
| `--apiKey`   | ✅ Yes      | N/A          | Your Nuclino API key            |
| `--outputDir`| ❌ No       | `./export`   | Directory to store exported files |

## ⚖️ License

This project is licensed under the MIT License. See the LICENSE file for details.
