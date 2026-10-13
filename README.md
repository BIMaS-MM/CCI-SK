# CCI-SK (Construction Classification International - Slovakia)

This repository hosts the machine-readable dataset for the Slovak implementation of the Construction Classification International (CCI). It provides a standardized framework for organizing information about the built environment, structured for seamless integration into BIM (Building Information Modeling) workflows and software applications.

## About the Dataset

The CCI-SK classification system is divided into six core classes:
* **CC** - Construction complex
* **CE** - Construction entity
* **CS** - Built space
* **CF** - Functional system
* **CT** - Techincal system
* **CO** - Construction component

The data is maintained in human-readable **YAML** format and automatically converted into machine-readable **JSON** distributions via a GitHub Actions CI/CD pipeline, ensuring the dataset is always up-to-date and ready for developer use.

---

## Repository Structure

```text
CCI-SK/
├── .github/workflows/         # Automation scripts (YAML to JSON compiler)
├── data/
│   ├── yaml/                  # 🟢 SOURCE OF TRUTH: Edit these YAML files
│   └── json/                  # 🔵 COMPILED DATA: Auto-generated JSON files
├── scripts/                   # Python build scripts
├── LICENSE.md                 # Licensing information
└── README.md                  # Documentation
```

---

## How to Access the Data

For integrations, API connections, or external software tools, use the auto-updating **Raw** links below. These links point to the `main` branch and will always serve the latest compiled version of the database.

**Aggregated Database (All Classes):**
* [CCI_Complete-SK.json](https://raw.githubusercontent.com/BIMaS-MM/CCI-SK/main/data/json/CCI_Complete-SK.json)

**Individual Class Datasets:**
* [CC.json](https://raw.githubusercontent.com/BIMaS-MM/CCI-SK/main/data/json/CC.json)
* [CE.json](https://raw.githubusercontent.com/BIMaS-MM/CCI-SK/main/data/json/CE.json)
* [CS.json](https://raw.githubusercontent.com/BIMaS-MM/CCI-SK/main/data/json/CS.json)
* [CF.json](https://raw.githubusercontent.com/BIMaS-MM/CCI-SK/main/data/json/CF.json)
* [CT.json](https://raw.githubusercontent.com/BIMaS-MM/CCI-SK/main/data/json/CT.json)
* [CO.json](https://raw.githubusercontent.com/BIMaS-MM/CCI-SK/main/data/json/CO.json)

> **Note on Versioning:** If you are citing this data for research or need a strictly locked version that will never change, navigate to the specific file on GitHub, press **`y`** to generate a permanent link (permalink), and use that URL instead.

---

## How to Update the Data

This repository utilizes an automated build system. **Never edit the JSON files directly.**

1. Navigate to the `data/yaml/` directory.
2. Edit or add classifications in the relevant `.yaml` file.
3. Commit and push your changes to the `main` branch.
4. The GitHub Action will automatically run, compile the YAML files, format them with Slovak diacritics support, and push the updated `.json` files to the `data/json/` directory.

## License

This dataset is distributed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. You are free to share and adapt the material for any purpose, even commercially, provided you give appropriate credit.
