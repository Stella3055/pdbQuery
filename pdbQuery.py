import requests
import urllib
import json
import os
import wget
import re

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
    for idX in idList:
        wget.download(DOWNLOAD_URL+idX+".pdb", out="PDBs")
    return

def getMetaData(idList):
    # RegEx Patterns
    patternDesc = re.compile(r"TITLE.*")
    patternChain = re.compile(r"COMPND.*CHAIN: .*;")
    patternChainDesc = re.compile(r"TITLE.*")
    patternRange = re.compile(r"COMPND.*MOLECULE: [.\n]*;")
    patternRes = re.compile(r'REMARK.*RESOLUTION.\s*[\d"."]*\s*ANGSTROMS.')

    pdbList = list(map(lambda x: "PDBs/%s.pdb" %x.lower(), idList))
    for pdbX in pdbList:
        with open(pdbX, "r") as pdbFile:
            pdbContent = pdbFile.read()
            desc = (re.sub(r"\s*TITLE\s*\d*\s*", " ", "".join(patternDesc.findall(pdbContent))).strip())
            print(desc)
            chains = (re.sub(r"COMPND.*CHAIN:\s*", " ", "".join(patternChain.findall(pdbContent))).strip().replace(";", ""))
            print(chains)
            chainsDesc = (re.sub(r"COMPND.*CHAIN:\s*", " ", "".join(patternChain.findall(pdbContent))).strip().replace(";", ""))
            print("_____________")



if __name__ == "__main__":
    TARGET = "P60484"
    # idList = getPdbList(TARGET)
    idList = ['2KYL', '1D5R', '4O1V', '5BUG', '5BZX', '5BZZ']
    getMetaData(idList)
    # batchQueryPdb(idList)
