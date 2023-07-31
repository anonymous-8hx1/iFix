# iFix
The source code and experiment scripts of the paper submitted to ICSE 2025

*Boosting User Trust in Automated Program Repair*.

## User Study

Please refer to [our website](https://sites.google.com/view/ifixuserstudy) for more details.

## Tutorial Video

[![iFix Tutorial](https://img.youtube.com/vi/QfkMG-E50g4/mqdefault.jpg)](http://www.youtube.com/watch?v=QfkMG-E50g4 "iFix Tutorial")

## Requirements

 - Linux or MacOS
 - JDK 8 (**Important**)
 - Visual Studio Code
 - Yarn

## Run iFix

1. Clone this repository

2. Run server
  ```
  cd iFix-server
  pip install -r requirements.txt
  hupper -m waitress --port=8000 ipr_server:server
  ```

 3. Run VS Code Extension
 - Configure environment
  ```
  cd iFix-extension
  yarn
  yarn watch
  ```
 - Unzip sample bugs
  ```
  unzip d4j-repo.zip
  ```

 - Open folder `iFix-extention` in VS Code

 - 'Run and Debug' -> 'Run Extension'

    <img width="350"  alt="Screenshot 2023-03-31 at 12 10 00 AM" src="https://user-images.githubusercontent.com/67893756/229020807-6adcd90f-d606-44c3-b6bb-7c598b1aa2a5.png">

 - In the new VS Code workspace, open sample buggy projects:
    `d4j-repo/Math_30`
    `d4j-repo/Lang_6`

 - You need to open the file with buggy code in the workspace to use the functionality of *iFix*:

     Math_30: `src/main/java/org/apache/commons/math3/stat/inference/MannWhitneyUTest.java`

     Lang_6: `src/main/java/org/apache/commons/lang3/text/translate/CharSequenceTranslator.java`

  4. Compile Runtime Comparison Backend
  ```
  cd iFix-extension/runtime-comp
  mvn clean package
  ```



 ## Quantitative Experiment
 ```
 cd experiments
 pip install -r requirements.txt
 python experiment.py
 ```

 The results are stored under `experiments/result`.

 
