# pdbQuery
根据蛋白信息一次性拉取全部PDB结构

## How to deploy
1. Firstly clone the project
```{shell}
$ git clone https://github.com/Stella3055/pdbQuery.git
$ cd pdbQuery
```
2. \* Optional: activate virtual python environment/conda env if necessary
```{shell}
$ conda activate YOUR_ENV_NAME
```

3. Install the packages needed
```{shell}
$ python -m pip install -r ./requirements.txt
# for help
$ python ./pdbQuery.py --help
# or
$ python ./pdbQuery.py -h
```

4. Run
```{shell}
$ python ./pdbQuery.py P60484
6 PDB structure(s) found: 2KYL,1D5R,4O1V,5BUG,5BZX,5BZZ
Downloading PDB structure 2KYL (1/6)
Downloading PDB structure 1D5R (2/6)
Downloading PDB structure 4O1V (3/6)
Downloading PDB structure 5BUG (4/6)
Downloading PDB structure 5BZX (5/6)
Downloading PDB structure 5BZZ (6/6)
Extracting metadata from 2KYL (1/6)
Extracting metadata from 1D5R (2/6)
Extracting metadata from 4O1V (3/6)
Extracting metadata from 5BUG (4/6)
Extracting metadata from 5BZX (5/6)
Extracting metadata from 5BZZ (6/6)

# metadata
$ cat ./PDB.metadata.txt
2KYL    B                       SOLUTION STRUCTURE OF MAST2-PDZ COMPLEXED WITH THE C-TERMINUS OF PTEN
1D5R    A       7-353   2.10    CRYSTAL STRUCTURE OF THE PTEN TUMOR SUPPRESSOR
4O1V    B               2.00    SPOP PROMOTES TUMORIGENESIS BY ACTING AS A KEY REGULATORY HUB IN KIDNEY CANCER
5BUG    A, B, C, D              2.40    CRYSTAL STRUCTURE OF HUMAN PHOSPHATASE PTEN OXIDIZED BY H2O2
5BZX    A, B, C, D              2.50    CRYSTAL STRUCTURE OF HUMAN PHOSPHATASE PTEN TREATED WITH A BISPEROXOVANADIUM COMPLEX
5BZZ    A, B, C, D              2.20    CRYSTAL STRUCTURE OF HUMAN PHOSPHATASE PTEN IN ITS REDUCED STATE
```

## Tips
- Terminal proxy tools (such as [proxychains-ng](https://github.com/rofl0r/proxychains-ng)) may accelerate the fetch process