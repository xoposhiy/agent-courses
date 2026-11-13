# Project code: stanford-oval/genie-worksheets: web/docs/installation/index.html

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/web/docs/installation/index.html) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/web/docs/installation/index.html)

Retrieved: 2026-11-13T17:06:24.900930+00:00

# Installation

## 🛠️ Prerequisites

We recommend using [uv](https://github.com/astral-sh/uv) as the package installer for GenieWorksheets. UV is a fast, reliable Python package installer and resolver.

Why UV?

UV offers significantly faster installation times and more reliable dependency resolution compared to pip. It's especially helpful when working with complex Python projects.

## 📦 Installation Steps

1. First, install UV by following the [UV installation guide](https://github.com/astral-sh/uv#installation)
2. Clone the GenieWorksheets repository:

   ```
   git clone https://github.com/stanford-oval/worksheets.git
   ```
3. Navigate to the project directory:

   ```
   cd worksheets
   ```
4. Install the dependencies:

   ```
   uv venv
   ```
5. Activate the virtual environment:

   ```
   source .venv/bin/activate
   ```
6. Sync the dependencies:

   ```
   uv sync
   ```

## ❓ Issues?

If you encounter any issues, please refer to the Troubleshooting (source archive omits `troubleshooting.md`) guide.

Or, if you're stuck, please [open an issue](https://github.com/stanford-oval/worksheets/issues/new) and we'll do our best to help you out.

Back to top
