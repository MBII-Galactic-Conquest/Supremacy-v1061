# Supremacy-v1061

## Installation & Setup

Follow these steps to install and configure **Supremacy** with Rock the Era (RTE) scripts:

---

### 1. Extract Godfinger
- Download **godfingerv102.zip**
- Extract it into your `gamedata/` folder
- Make sure **Python 3.12.7** is installed on your system

> `SupremacyTools.zip` will have a binary installer for the exact python version that ran Supremacy official servers.

---

### 2. Configure Godfinger
- Follow the configuration instructions in the [Godfinger README](https://github.com/MBII-Galactic-Conquest/godfinger)

---

### 3. Add RTE Scripts
- *(RTE = Rock the Era, including Rock the Bonus scripts)*
- Download one of the following:
  - `rte-campaignstable.zip` (campaign version), **OR**
  - `rte-stable.zip` (stable version)
- Extract into: `godfinger/update/deploy`

> `rte-campaignstable` - version of Supremacy that limited excessive script use, highly recommended
> `rte-stable` - version of Supremacy that showcased godfinger capabilities and the scripts have minor cooldowns

---

### 4. Configure Supremacy Scripts
- Read the [Deploying Private Codebases guide](https://github.com/MBII-Galactic-Conquest/godfinger?tab=readme-ov-file#deploying-private-codebases)
- Follow the instructions on setting up **Supremacy scripts** through nested git repositories

---

### 5. Add campaignfiles
- Extract the contents from `./campaignfiles` and place them in **GameData/MBII**
- Supremacy will not run without the **.mbcr** & **.mb2c** files necessary to function

---

### 6. First time startup
- If you have not created your **virtual environment** in godfinger yet, do so now by running `prepare/OS/prepare.bat/sh`
- Run to generate first time errors and configs, this will be important as you will have to edit in necessary information needed
- Afterwards, modify sensitive information such as RCON passwords, dirpathing, etcetera, as requested in config files in order for Supremacy to function

---

> ✅ After completing these steps, your Supremacy setup will be ready with Godfinger & RTE integration

You may run Supremacy scripts by running `./quickstart_win.bat` or `./quickstart_linuxMacOS.sh` depending on OS