# AI for Software Architecture

## Authors

- Casper Frøding
- Mads Nørklit Jensen

This is the repository supporting our Bachelor thesis on AI for Software Architecture.

## What This Project Does

This tool analyzes software repositories to detect violations of architectural principles using AI. Currently it uses Antropic API, and can only analyse code in regards to the Onion Architecture.
It can be run manually, or integrated with GitHub pipelines to automate architectural checks during development.

## Example output

When run, the tool outputs a list of architectural violations, in regards to the Onion Architecture, such as this example:

```txt
    1. ‘UserDTO‘ in Application layer directly references Domain entity (User) in its constructor, violating dependency rule as Application should not depend directly on concrete Domain entities.
    2. ‘SpecificationEvaluator‘ in Infrastructure layer uses Domain interfaces (‘IS-pecification‘) and models (‘BaseEntity‘), but is not implementing any Domain interface itself, making it an infrastructure concern that’s too tightly coupled to Domain.
    3. ‘UserService‘ in Application layer directly instantiates Domain entities(User), violating the dependency inversion principle. It should use a factory or mapper.
```

### Set Up

1. **Clone the Repository** (if applicable):

   ```bash
   git clone https://github.com/AIForSoftArchi/bachelor
   cd bachelor
   ```

2. **Create Virtual Environment** (if not already created):

   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**:

   - On **Windows**:

     ```bash
     .venv\Scripts\activate
     ```

   - On **macOS/Linux**:

     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Inputting secrets**:
   To input the key for Anthropic API, you should create a .env file, and in this file input your personal key:

   ```env
   ANTHROPIC_API_KEY= {YOUR ANTHROPIC API KEY HERE!}
   ```

### Running the Project manually

After activating the virtual environment and installing dependencies, the project can be manually run with the command:

```bash
python main.py
```

### integrating into a Github pipeline

To integrate into a pipeline, the project can be put in the same github repository as the code that should be analysed.
The project automaticcaly detects if it is run by a pipeline, or manually, so everything that is needed is to setup a yaml file, to make the analysis happen when desired.
Under here is an example of a yaml file, from a github repository that has saved our project in a folder called _.scripts_ , and the analysis is run on every push and pull request:

```yaml
name: Architecture checking prototype

on:
  push:
  pull_request:

jobs:
  check:
    runs-on: windows-latest
    env:
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
      PYTHONIOENCODING: utf-8

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: pip install -r .scripts/requirements.txt || true

      - name: Run architecture check
        run: python .scripts/main.py
```

**Notice** that you should not upload the Anthropic API key directly to a .env file in the repisitory, but instead go through Github's own secret integration, like in the above example

#### 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
