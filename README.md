# CCI-SK (Construction Classification International - Slovakia)
![Slovakia](https://flagcdn.com/w40/sk.png)

Tento repozitár slúži ako úložisko pre strojovo čitateľný dataset slovenskej implementácie CCI. Poskytuje štandardizovaný rámec na organizáciu informácií o vystavanom prostredí, štruktúrovaný pre bezproblémovú integráciu do BIM (Building Information Modeling) pracovných postupov a softvérových aplikácií.

## O datasete

Klasifikačný systém CCI-SK je rozdelený do šiestich základných tried:
- **CC** - Stavebný komplex (Construction complex)
- **CE** - Stavebná entita (Construction entity)
- **CS** - Vystavaný priestor (Built space)
- **CF** - Funkčný systém (Functional system)
- **CT** - Technický systém (Technical system)
- **CO** - Stavebný komponent (Construction component)

Dáta sú spravované v ľudsky čitateľnom formáte **YAML** a automaticky konvertované do strojovo čitateľných **JSON** formátov prostredníctvom CI/CD pipeline v GitHub Actions. Tým je zabezpečené, že dataset je vždy aktuálny a pripravený pre vývojárov.

## Štruktúra repozitára

```text
CCI-SK/
├── .github/workflows/         # Automatizačné skripty (YAML to JSON kompilátor)
├── data/
│   ├── yaml/                  # 🟢 ZDROJ PRAVDY: Upravujte tieto YAML súbory
│   └── json/                  # 🔵 KOMPILOVANÉ DÁTA: Automaticky generované JSON súbory
├── scripts/                   # Python build skripty
├── LICENSE.md                 # Informácie o licencii
└── README.md                  # Dokumentácia
```

## Ako získať prístup k dátam

Pre integrácie, API pripojenia alebo externé softvérové nástroje použite nižšie uvedené automaticky sa aktualizujúce **Raw** odkazy. Tieto odkazy smerujú na vetvu `main` a vždy poskytnú najnovšiu skompilovanú verziu databázy.

**Agregovaná databáza (Všetky triedy):**
- [CCI_Complete-SK.json](https://raw.githubusercontent.com/MartinMisun-BIMaS/CCI-SK/main/data/json/CCI_Complete-SK.json)

**Datasety jednotlivých tried:**
- [CC.json](https://raw.githubusercontent.com/MartinMisun-BIMaS/CCI-SK/main/data/json/CC.json)
- [CE.json](https://raw.githubusercontent.com/MartinMisun-BIMaS/CCI-SK/main/data/json/CE.json)
- [CS.json](https://raw.githubusercontent.com/MartinMisun-BIMaS/CCI-SK/main/data/json/CS.json)
- [CF.json](https://raw.githubusercontent.com/MartinMisun-BIMaS/CCI-SK/main/data/json/CF.json)
- [CT.json](https://raw.githubusercontent.com/MartinMisun-BIMaS/CCI-SK/main/data/json/CT.json)
- [CO.json](https://raw.githubusercontent.com/MartinMisun-BIMaS/CCI-SK/main/data/json/CO.json)

> **Poznámka k verziovaniu:** Ak tieto dáta citujete na výskumné účely alebo potrebujete striktne uzamknutú verziu, ktorá sa nikdy nezmení, prejdite na konkrétny súbor na GitHub-e, stlačte kláves **`y`** pre vygenerovanie trvalého odkazu (permalink) a namiesto neho použite túto URL adresu.

## Ako aktualizovať dáta

Tento repozitár využíva automatizovaný systém zostavovania (build system). **Nikdy neupravujte JSON súbory priamo.**

1. Prejdite do adresára `data/yaml/`.
2. Upravte alebo pridajte klasifikácie v príslušnom `.yaml` súbore.
3. Vykonajte commit a push vašich zmien do vetvy `main`.
4. GitHub Action sa automaticky spustí, skompiluje YAML súbory, naformátuje ich s podporou slovenskej diakritiky a nahrá (push) aktualizované `.json` súbory do adresára `data/json/`.

## Licencia

Tento dataset je distribuovaný pod licenciou **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Materiál môžete voľne zdieľať a upravovať na akýkoľvek účel, a to aj komerčne, za predpokladu, že uvediete príslušné uvedenie autora (kredit).

[Originálne tabuľky CCI Core Tables](https://cci-collaboration.org/the-standard/)


<br><br><br><br><br><br>
---

![UK](https://flagcdn.com/w40/gb.png)

This repository hosts the machine-readable dataset for the Slovak implementation of the Construction Classification International (CCI). It provides a standardized framework for organizing information about the built environment, structured for seamless integration into BIM (Building Information Modeling) workflows and software applications.

## About the Dataset

The CCI-SK classification system is divided into six core classes:
- **CC** - Construction complex
- **CE** - Construction entity
- **CS** - Built space
- **CF** - Functional system
- **CT** - Technical system
- **CO** - Construction component

The data is maintained in human-readable **YAML** format and automatically converted into machine-readable **JSON** distributions via a GitHub Actions CI/CD pipeline, ensuring the dataset is always up-to-date and ready for developer use.

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

## How to Access the Data

For integrations, API connections, or external software tools, use the auto-updating **Raw** links below. These links point to the `main` branch and will always serve the latest compiled version of the database.

**Aggregated Database (All Classes):**
- [CCI_Complete-SK.json](https://raw.githubusercontent.com/MartinMisun-BIMaS/CCI-SK/main/data/json/CCI_Complete-SK.json)

**Individual Class Datasets:**
- [CC.json](https://raw.githubusercontent.com/MartinMisun-BIMaS/CCI-SK/main/data/json/CC.json)
- [CE.json](https://raw.githubusercontent.com/MartinMisun-BIMaS/CCI-SK/main/data/json/CE.json)
- [CS.json](https://raw.githubusercontent.com/MartinMisun-BIMaS/CCI-SK/main/data/json/CS.json)
- [CF.json](https://raw.githubusercontent.com/MartinMisun-BIMaS/CCI-SK/main/data/json/CF.json)
- [CT.json](https://raw.githubusercontent.com/MartinMisun-BIMaS/CCI-SK/main/data/json/CT.json)
- [CO.json](https://raw.githubusercontent.com/MartinMisun-BIMaS/CCI-SK/main/data/json/CO.json)

> **Note on Versioning:** If you are citing this data for research or need a strictly locked version that will never change, navigate to the specific file on GitHub, press **`y`** to generate a permanent link (permalink), and use that URL instead.

## How to Update the Data

This repository utilizes an automated build system. **Never edit the JSON files directly.**

1. Navigate to the `data/yaml/` directory.
2. Edit or add classifications in the relevant `.yaml` file.
3. Commit and push your changes to the `main` branch.
4. The GitHub Action will automatically run, compile the YAML files, format them with Slovak diacritics support, and push the updated `.json` files to the `data/json/`.

## License

This dataset is distributed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. You are free to share and adapt the material for any purpose, even commercially, provided you give appropriate credit.

[Original CCI Core Tables](https://cci-collaboration.org/the-standard/)
