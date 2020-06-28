import requests
import urllib
import json
import os
import wget
import re
import getopt
import sys

def getPdbList(uniprotId):
    # https://search.rcsb.org/index.html#search-services
    API_URL = "https://search.rcsb.org/rcsbsearch/v1/query?json="
    SEARCH ='''{"query": {"node_id": 0,"type": "terminal","service": "text","parameters": {"value": "%s"}},"return_type": "entry"}''' % uniprotId
    req = requests.get(url=API_URL+urllib.parse.quote(SEARCH.replace(" ", ""), safe=':",'))
    req_json = json.loads(req.text)
    idList = list(map(lambda x: x["identifier"], req_json["result_set"]))
    print("%d PDB structure(s) found: %s" % (len(idList), ",".join(idList)))
    return idList

def batchQueryPdb(idList):
    DOWNLOAD_URL = "http://files.rcsb.org/download/"
    if not os.path.exists("PDBs"):
        os.mkdir("PDBs")
    else:
        print("Warning: directory PDBs has existed")
    for indX, idX in enumerate(idList):
        print("Downloading PDB structure %s (%d/%d)" %(idX, indX+1, len(idList)))
        wget.download(DOWNLOAD_URL+idX+".pdb", out="PDBs", bar=None)
    return

def getMetaData(idList):
    # RegEx Patterns
    patternDesc = re.compile(r"TITLE.*")
    patternChain = re.compile(r"COMPND.*CHAIN: .*;")
    # patternChainDesc = re.compile(r"TITLE.*")
    patternRange = re.compile(r"COMPND.*FRAGMENT: RESIDUES \d*-\d*;")
    patternRes = re.compile(r'REMARK.*RESOLUTION.\s*[\d"."]*\s*ANGSTROMS.')
    pdbList = list(map(lambda x: "PDBs/%s.pdb" %x.lower(), idList))
    with open("PDB.metadata.txt", "w") as out_meta:
        for indX, pdbX in enumerate(pdbList):
            print("Extracting metadata from %s (%d/%d)" %(idList[indX], indX+1, len(pdbList)))
            with open(pdbX, "r") as pdbFile:
                pdbContent = pdbFile.read()
                desc = (re.sub(r"\s*TITLE\s*\d*\s*", " ", "".join(patternDesc.findall(pdbContent))).strip())
                chains = (re.sub(r"COMPND.*CHAIN:\s*", " ", "".join(patternChain.findall(pdbContent))).strip().replace(";", ""))
                # chainsDesc = (re.sub(r"COMPND.*CHAIN:\s*", " ", "".join(patternChainDesc.findall(pdbContent))).strip().replace(";", ""))
                ranges = (re.sub(r"COMPND.*FRAGMENT: RESIDUES\s*", " ", "".join(patternRange.findall(pdbContent))).strip().replace(";", ""))
                res = (re.sub(r"REMARK.*RESOLUTION.", " ", "".join(patternRes.findall(pdbContent))).replace("ANGSTROMS.", "").strip())

                out_meta.write("\t".join([
                    idList[indX],
                    chains,
                    ranges,
                    res,
                    desc
                ])+"\n")
    return

def main(uniprotId):
    idList = getPdbList(uniprotId)
    batchQueryPdb(idList)
    getMetaData(idList)
    return

if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] in ["-h", "--help"]:
        print('''
---------------------------
pdbQuery: fetch PDB structures related to a certain UniprotID or Keyword and extract their metadata.
Usage:
# Deploy environment
[PYTHON_ENV] python -m pip install -r ./requirements.txt
# Download and analyze
[PYTHON_ENV] python ./pdbQuery.py [UNIPROT_ID]
# e.g.
python ./pdbQuery.py P60484
---------------------------
        ''')
    else:
        main(str(sys.argv[1]))
