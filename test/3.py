#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/21 14:36
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : 3.py

k = [
    {
        "pdb_code": "5WB1",
        "ligands": [],
        "species": "Human cytomegalovirus",
        "publication_date": "2018-06-13",
        "family": "001_011_001_001",
        "preferred_chain": "A",
        "protein": "q80km9_hcmv",
        "state": "Active",
        "publication": "http://dx.doi.org/10.7554/ELIFE.35850",
        "resolution": 3.51,
        "distance": 9.12,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6M9T",
        "ligands": [
            {
                "name": "misoprostol-FA",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-12-05",
        "family": "001_004_008_005",
        "preferred_chain": "A",
        "protein": "pe2r3_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/S41589-018-0160-Y",
        "resolution": 2.5,
        "distance": 7.11,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5NX2",
        "ligands": [
            {
                "name": "truncated protein agonist",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-06-14",
        "family": "002_001_003_003",
        "preferred_chain": "A",
        "protein": "glp1r_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NATURE22800",
        "resolution": 3.7,
        "distance": 4.86,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5WS3",
        "ligands": [
            {
                "name": "EMPA",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-12-13",
        "family": "001_002_023_002",
        "preferred_chain": "A",
        "protein": "ox2r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2017.11.005",
        "resolution": 2.3,
        "distance": -1.13,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5X93",
        "ligands": [
            {
                "name": "K-8794",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-08-16",
        "family": "001_002_007_002",
        "preferred_chain": "A",
        "protein": "ednrb_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NSMB.3450",
        "resolution": 2.2,
        "distance": -0.68,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5G53",
        "ligands": [
            {
                "name": "NECA",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-08-03",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE18966",
        "resolution": 3.4,
        "distance": 9.79,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5CXV",
        "ligands": [
            {
                "name": "CHEMBL258622",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-03-09",
        "family": "001_001_002_001",
        "preferred_chain": "A",
        "protein": "acm1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE17188",
        "resolution": 2.7,
        "distance": 0.64,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6E3Y",
        "ligands": [
            {
                "name": "Calcitonin gene-related peptide",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-09-19",
        "family": "002_001_001_005",
        "preferred_chain": "R",
        "protein": "calrl_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/S41586-018-0535-Y",
        "resolution": 3.3,
        "distance": 6.86,
        "type": "Electron microscopy"
    },
    {
        "pdb_code": "4XNW",
        "ligands": [
            {
                "name": "MRS2500",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2015-04-01",
        "family": "001_006_002_001",
        "preferred_chain": "A",
        "protein": "p2ry1_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NATURE14287",
        "resolution": 2.7,
        "distance": 5.2,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5T04",
        "ligands": [
            {
                "name": "CHEMBL342252",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Rattus norvegicus",
        "publication_date": "2016-12-21",
        "family": "001_002_021_001",
        "preferred_chain": "A",
        "protein": "ntr1_rat",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/SREP38564",
        "resolution": 3.3,
        "distance": 8.26,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3VW7",
        "ligands": [
            {
                "name": "Vorapaxar",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2012-12-12",
        "family": "001_002_026_001",
        "preferred_chain": "A",
        "protein": "par1_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NATURE11701",
        "resolution": 2.2,
        "distance": 6.18,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5JQH",
        "ligands": [
            {
                "name": "Carazolol",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-07-13",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE18636",
        "resolution": 3.2,
        "distance": -1.07,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5TUD",
        "ligands": [
            {
                "name": "Ergotamine",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-07-26",
        "family": "001_001_001_007",
        "preferred_chain": "D",
        "protein": "5ht2b_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1073/PNAS.1700891114",
        "resolution": 3,
        "distance": 8.66,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4N6H",
        "ligands": [
            {
                "name": "Naltrindole",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2013-12-25",
        "family": "001_002_022_001",
        "preferred_chain": "A",
        "protein": "oprd_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE12944",
        "resolution": 1.8,
        "distance": -1.54,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5L7D",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2016-07-20",
        "family": "005_001_001_011",
        "preferred_chain": "B",
        "protein": "smo_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE18934",
        "resolution": 3.2,
        "distance": -1.98,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5TGZ",
        "ligands": [
            {
                "name": "SCHEMBL662960",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-11-02",
        "family": "001_004_005_001",
        "preferred_chain": "A",
        "protein": "cnr1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2016.10.004",
        "resolution": 2.8,
        "distance": -0.85,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6G79",
        "ligands": [
            {
                "name": "Donitriptan",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-06-20",
        "family": "001_001_001_002",
        "preferred_chain": "S",
        "protein": "5ht1b_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/S41586-018-0241-9",
        "resolution": 3.78,
        "distance": 8.9,
        "type": "Electron microscopy"
    },
    {
        "pdb_code": "6NIY",
        "ligands": [
            {
                "name": "PEP",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2019-01-23",
        "family": "002_001_001_001",
        "preferred_chain": "R",
        "protein": "calcr_human",
        "state": "Active",
        "publication": None,
        "resolution": 3.34,
        "distance": 7.8,
        "type": "Electron microscopy"
    },
    {
        "pdb_code": "6A94",
        "ligands": [
            {
                "name": "Zotepine",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2019-02-13",
        "family": "001_001_001_006",
        "preferred_chain": "A",
        "protein": "5ht2a_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41594-018-0180-Z",
        "resolution": 2.9,
        "distance": -0.82,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5X33",
        "ligands": [
            {
                "name": "BIIL-260",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Cavia porcellus",
        "publication_date": "2018-01-03",
        "family": "001_004_002_001",
        "preferred_chain": "A",
        "protein": "q9wtk1_cavpo",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NCHEMBIO.2547",
        "resolution": 3.7,
        "distance": -1.53,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4OO9",
        "ligands": [
            {
                "name": "Mavoglurant",
                "type": "small molecule",
                "function": "NAM"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2014-07-02",
        "family": "004_002_002_005",
        "preferred_chain": "A",
        "protein": "grm5_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE13396",
        "resolution": 2.6,
        "distance": 3.98,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5C1M",
        "ligands": [
            {
                "name": "BU72",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Mus musculus",
        "publication_date": "2015-08-05",
        "family": "001_002_022_003",
        "preferred_chain": "A",
        "protein": "oprm_mouse",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE14886",
        "resolution": 2.1,
        "distance": 10.99,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5XSZ",
        "ligands": [],
        "species": "Danio rerio",
        "publication_date": "2017-08-16",
        "family": "001_004_003_006",
        "preferred_chain": "A",
        "protein": "q08bg4_danre",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE23448",
        "resolution": 3.2,
        "distance": 9.96,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6BQH",
        "ligands": [
            {
                "name": "Ritanserin",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-02-14",
        "family": "001_001_001_008",
        "preferred_chain": "A",
        "protein": "5ht2c_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2018.01.001",
        "resolution": 2.7,
        "distance": 0.08,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4MQT",
        "ligands": [
            {
                "name": "LY2119620",
                "type": "small molecule",
                "function": "PAM"
            },
            {
                "name": "iperoxo",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2013-11-27",
        "family": "001_001_002_002",
        "preferred_chain": "A",
        "protein": "acm2_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE12735",
        "resolution": 3.7,
        "distance": 8.74,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6HLP",
        "ligands": [
            {
                "name": "Netupitant",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2019-01-16",
        "family": "001_002_029_001",
        "preferred_chain": "A",
        "protein": "nk1r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41467-018-07939-8",
        "resolution": 2.2,
        "distance": 0.8,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5TZY",
        "ligands": [
            {
                "name": "(2s,3r)-3-Cyclopropyl-3-[(2r)-2-(1-{(1s)-1-[5-Fluoro-2-(Trifluoromethoxy)phenyl]ethyl}piperidin-4-Yl)-3,4-Dihydro-2h-1-Benzopyran-7-Yl]-2-Methylpropanoic Acid",
                "type": "small molecule",
                "function": "Agonist"
            },
            {
                "name": "UNII-11612L5SPI",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-06-07",
        "family": "001_004_001_001",
        "preferred_chain": "A",
        "protein": "ffar1_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NSMB.3417",
        "resolution": 3.22,
        "distance": 3.21,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5ZBH",
        "ligands": [
            {
                "name": "BMS-193885",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-04-25",
        "family": "001_002_020_001",
        "preferred_chain": "A",
        "protein": "npy1r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41586-018-0046-X",
        "resolution": 3,
        "distance": -0.68,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6CM4",
        "ligands": [
            {
                "name": "Risperidone",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-03-14",
        "family": "001_001_004_002",
        "preferred_chain": "A",
        "protein": "drd2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE25758",
        "resolution": 2.87,
        "distance": -1.8,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5ZTY",
        "ligands": [
            {
                "name": "AM10257",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2019-01-30",
        "family": "001_004_005_002",
        "preferred_chain": "A",
        "protein": "cnr2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2018.12.011",
        "resolution": 2.8,
        "distance": -0.5,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5UNG",
        "ligands": [
            {
                "name": "CHEMBL289472",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-04-05",
        "family": "001_002_001_002",
        "preferred_chain": "B",
        "protein": "agtr2_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE22035",
        "resolution": 2.8,
        "distance": 8.46,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6IIV",
        "ligands": [
            {
                "name": "Daltroban",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-12-19",
        "family": "001_004_008_009",
        "preferred_chain": "A",
        "protein": "ta2r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41589-018-0170-9",
        "resolution": 3,
        "distance": 1,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4DJH",
        "ligands": [
            {
                "name": "JDTic",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2012-03-21",
        "family": "001_002_022_002",
        "preferred_chain": "A",
        "protein": "oprk_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE10939",
        "resolution": 2.9,
        "distance": -1.29,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5DSG",
        "ligands": [
            {
                "name": "Tiotropium",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-03-16",
        "family": "001_001_002_004",
        "preferred_chain": "B",
        "protein": "acm4_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE17188",
        "resolution": 2.6,
        "distance": 0.28,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5ZKP",
        "ligands": [
            {
                "name": "Foropafant",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-06-20",
        "family": "001_004_007_001",
        "preferred_chain": "A",
        "protein": "ptafr_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/S41594-018-0068-Y",
        "resolution": 2.81,
        "distance": 15.31,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3RZE",
        "ligands": [
            {
                "name": "doxepin",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2011-06-15",
        "family": "001_001_005_001",
        "preferred_chain": "A",
        "protein": "hrh1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE10236",
        "resolution": 3.1,
        "distance": 0.45,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5DHG",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2015-10-21",
        "family": "001_002_022_004",
        "preferred_chain": "A",
        "protein": "oprx_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2015.07.024",
        "resolution": 3,
        "distance": -1.28,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5ZKC",
        "ligands": [
            {
                "name": "N-methyl scopolamine",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-11-21",
        "family": "001_001_002_002",
        "preferred_chain": "A",
        "protein": "acm2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41589-018-0152-Y",
        "resolution": 2.3,
        "distance": 0.83,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5LWE",
        "ligands": [
            {
                "name": "Vercirnon",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-12-07",
        "family": "001_003_002_009",
        "preferred_chain": "B",
        "protein": "ccr9_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE20606",
        "resolution": 2.8,
        "distance": 0.09,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5NDD",
        "ligands": [
            {
                "name": "GTPL9585",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-05-03",
        "family": "001_002_026_002",
        "preferred_chain": "A",
        "protein": "par2_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NATURE22309",
        "resolution": 2.8,
        "distance": 7.07,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4UHR",
        "ligands": [
            {
                "name": "Cgs 21680",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2015-04-08",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1124/MOL.114.097360",
        "resolution": 2.6,
        "distance": 6.28,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5T1A",
        "ligands": [
            {
                "name": "CCR2-RA-[R]",
                "type": "small molecule",
                "function": "Antagonist"
            },
            {
                "name": "CHEMBL3577945",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-12-14",
        "family": "001_003_002_002",
        "preferred_chain": "A",
        "protein": "ccr2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE20605",
        "resolution": 2.81,
        "distance": 1.66,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4U15",
        "ligands": [
            {
                "name": "Tiotropium",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Rattus norvegicus",
        "publication_date": "2014-11-26",
        "family": "001_001_002_003",
        "preferred_chain": "B",
        "protein": "acm3_rat",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2014.08.022",
        "resolution": 2.8,
        "distance": 0.5,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6B73",
        "ligands": [
            {
                "name": "MP1104",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-01-17",
        "family": "001_002_022_002",
        "preferred_chain": "A",
        "protein": "oprk_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2017.12.011",
        "resolution": 3.1,
        "distance": 9.71,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2Z73",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Todarodes pacificus",
        "publication_date": "2008-05-13",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_todpa",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE06925",
        "resolution": 2.5,
        "distance": -0.27,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6D32",
        "ligands": [
            {
                "name": "Cyclopamine",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Xenopus laevis",
        "publication_date": "2018-05-23",
        "family": "005_001_001_011",
        "preferred_chain": "A",
        "protein": "q98sw5_xenla",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2018.04.029",
        "resolution": 3.75,
        "distance": -2.2,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6AK3",
        "ligands": [
            {
                "name": "Prostaglandin E2",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-12-05",
        "family": "001_004_008_005",
        "preferred_chain": "B",
        "protein": "pe2r3_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/S41589-018-0171-8",
        "resolution": 2.9,
        "distance": 7.57,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5DYS",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2016-08-10",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.15252/EMBR.201642671",
        "resolution": 2.3,
        "distance": 7.7,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5VAI",
        "ligands": [
            {
                "name": "GLP-1",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Oryctolagus cuniculus",
        "publication_date": "2017-05-24",
        "family": "002_001_003_003",
        "preferred_chain": "R",
        "protein": "g1sgd4_rabit",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE22394",
        "resolution": 4.1,
        "distance": 6.89,
        "type": "Electron microscopy"
    },
    {
        "pdb_code": "5VEW",
        "ligands": [
            {
                "name": "97Y",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-05-24",
        "family": "002_001_003_003",
        "preferred_chain": "A",
        "protein": "glp1r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE22378",
        "resolution": 2.7,
        "distance": -5.1,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5YWY",
        "ligands": [
            {
                "name": "ONO-AE3-208",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-12-05",
        "family": "001_004_008_006",
        "preferred_chain": "A",
        "protein": "pe2r4_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41589-018-0131-3",
        "resolution": 3.2,
        "distance": -0.97,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5UEN",
        "ligands": [
            {
                "name": "CHEMBL144360",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-03-01",
        "family": "001_006_001_001",
        "preferred_chain": "B",
        "protein": "aa1r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2017.01.042",
        "resolution": 3.2,
        "distance": -1.06,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4Z35",
        "ligands": [
            {
                "name": "ONO-9910539",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2015-06-03",
        "family": "001_004_003_001",
        "preferred_chain": "A",
        "protein": "lpar1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2015.06.002",
        "resolution": 2.9,
        "distance": -1.3,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3ODU",
        "ligands": [
            {
                "name": "IT1t",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2010-10-27",
        "family": "001_003_002_014",
        "preferred_chain": "A",
        "protein": "cxcr4_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1194396",
        "resolution": 2.5,
        "distance": -1.34,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5O9H",
        "ligands": [
            {
                "name": "NDT 9513727",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-01-10",
        "family": "001_002_006_002",
        "preferred_chain": "A",
        "protein": "c5ar1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE25025",
        "resolution": 2.7,
        "distance": -1.46,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3PBL",
        "ligands": [
            {
                "name": "Eticlopride",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2010-11-03",
        "family": "001_001_004_003",
        "preferred_chain": "A",
        "protein": "drd3_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1197410",
        "resolution": 2.89,
        "distance": -0.43,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5XEZ",
        "ligands": [
            {
                "name": "4-{[(4-Cyclohexylphenyl){[3-(Methylsulfonyl)phenyl]carbamoyl}amino]methyl}-N-(1h-Tetrazol-5-Yl)benzamide",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-05-24",
        "family": "002_001_003_005",
        "preferred_chain": "B",
        "protein": "glr_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE22363",
        "resolution": 3,
        "distance": -4.53,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5VBL",
        "ligands": [
            {
                "name": "AMG3054",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-05-31",
        "family": "001_002_002_001",
        "preferred_chain": "B",
        "protein": "apj_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2017.04.008",
        "resolution": 2.6,
        "distance": -0.37,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4Z9G",
        "ligands": [
            {
                "name": "CP-376395",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-06-29",
        "family": "002_001_002_001",
        "preferred_chain": "A",
        "protein": "crfr1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.2174/1874467210666170110114727",
        "resolution": 3.18,
        "distance": -0.98,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5WIV",
        "ligands": [
            {
                "name": "Nemonapride",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-10-18",
        "family": "001_001_004_004",
        "preferred_chain": "A",
        "protein": "drd4_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.AAN5468",
        "resolution": 2.14,
        "distance": -0.93,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3SN6",
        "ligands": [
            {
                "name": "BI-167107",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2011-07-20",
        "family": "001_001_003_008",
        "preferred_chain": "R",
        "protein": "adrb2_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE10361",
        "resolution": 3.2,
        "distance": 9.96,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6N4B",
        "ligands": [
            {
                "name": "Fub-mdmb",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2019-01-30",
        "family": "001_004_005_001",
        "preferred_chain": "R",
        "protein": "cnr1_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2018.11.040",
        "resolution": 3,
        "distance": 8.26,
        "type": "Electron microscopy"
    },
    {
        "pdb_code": "6B3J",
        "ligands": [
            {
                "name": "Exendin-P5",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-02-21",
        "family": "002_001_003_003",
        "preferred_chain": "R",
        "protein": "glp1r_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE25773",
        "resolution": 3.3,
        "distance": 6.78,
        "type": "Electron microscopy"
    },
    {
        "pdb_code": "4NTJ",
        "ligands": [
            {
                "name": "AZD1283",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2014-03-26",
        "family": "001_006_002_006",
        "preferred_chain": "A",
        "protein": "p2y12_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NATURE13083",
        "resolution": 2.62,
        "distance": 4.74,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4ZJ8",
        "ligands": [
            {
                "name": "Suvorexant",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-03-09",
        "family": "001_002_023_001",
        "preferred_chain": "A",
        "protein": "ox1r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NSMB.3183",
        "resolution": 2.75,
        "distance": -0.47,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6FJ3",
        "ligands": [
            {
                "name": "ePTH",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-11-21",
        "family": "002_001_004_001",
        "preferred_chain": "A",
        "protein": "pth1r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41594-018-0151-4",
        "resolution": 2.5,
        "distance": -19.28,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4XES",
        "ligands": [
            {
                "name": "CHEMBL342252",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Rattus norvegicus",
        "publication_date": "2015-07-29",
        "family": "001_002_021_001",
        "preferred_chain": "A",
        "protein": "ntr1_rat",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NCOMMS8895",
        "resolution": 2.6,
        "distance": 6.03,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6BD4",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2018-08-22",
        "family": "005_001_001_004",
        "preferred_chain": "A",
        "protein": "fzd4_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41586-018-0447-X",
        "resolution": 2.4,
        "distance": -4.31,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4ZUD",
        "ligands": [
            {
                "name": "OLM",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2015-10-07",
        "family": "001_002_001_001",
        "preferred_chain": "A",
        "protein": "agtr1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1074/JBC.M115.689000",
        "resolution": 2.8,
        "distance": -0.93,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4BUO",
        "ligands": [
            {
                "name": "CHEMBL342252",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Rattus norvegicus",
        "publication_date": "2014-01-29",
        "family": "001_002_021_001",
        "preferred_chain": "A",
        "protein": "ntr1_rat",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1073/PNAS.1317903111",
        "resolution": 2.75,
        "distance": 0.57,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4EJ4",
        "ligands": [
            {
                "name": "Naltrindole",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Mus musculus",
        "publication_date": "2012-05-16",
        "family": "001_002_022_001",
        "preferred_chain": "A",
        "protein": "oprd_mouse",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE11111",
        "resolution": 3.4,
        "distance": -1.23,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "1GZM",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2003-11-20",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.JMB.2004.08.090",
        "resolution": 2.65,
        "distance": 0.06,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5UIW",
        "ligands": [
            {
                "name": "5P7-CCL5",
                "type": "peptide",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-06-28",
        "family": "001_003_002_005",
        "preferred_chain": "A",
        "protein": "ccr5_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.IMMUNI.2017.05.002",
        "resolution": 2.2,
        "distance": 1.02,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5ZKQ",
        "ligands": [
            {
                "name": "ABT-491",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-06-20",
        "family": "001_004_007_001",
        "preferred_chain": "B",
        "protein": "ptafr_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/S41594-018-0068-Y",
        "resolution": 2.9,
        "distance": 4.76,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4XT1",
        "ligands": [
            {
                "name": "CX3CL1",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Human cytomegalovirus",
        "publication_date": "2015-03-04",
        "family": "001_011_001_001",
        "preferred_chain": "A",
        "protein": "us28_hcmva",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.AAA5026",
        "resolution": 2.89,
        "distance": 9.02,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3V2Y",
        "ligands": [
            {
                "name": "W146",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2012-02-15",
        "family": "001_004_004_001",
        "preferred_chain": "A",
        "protein": "s1pr1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1215904",
        "resolution": 2.8,
        "distance": -0.61,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4IB4",
        "ligands": [
            {
                "name": "ERGOTAMINE",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2013-03-13",
        "family": "001_001_001_007",
        "preferred_chain": "A",
        "protein": "5ht2b_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1232808",
        "resolution": 2.7,
        "distance": 3.08,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4OR2",
        "ligands": [
            {
                "name": "FITM",
                "type": "small molecule",
                "function": "NAM"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2014-03-19",
        "family": "004_002_002_001",
        "preferred_chain": "A,B",
        "protein": "grm1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1249489",
        "resolution": 2.8,
        "distance": 4,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6D9H",
        "ligands": [
            {
                "name": "Adenosine",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-06-20",
        "family": "001_006_001_001",
        "preferred_chain": "R",
        "protein": "aa1r_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/S41586-018-0236-6",
        "resolution": 3.6,
        "distance": 9.23,
        "type": "Electron microscopy"
    },
    {
        "pdb_code": "4ZWJ",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2015-07-29",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE14656",
        "resolution": 3.3,
        "distance": 8.61,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3VG9",
        "ligands": [
            {
                "name": "ZM241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2012-02-01",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE10750",
        "resolution": 2.7,
        "distance": -1.2,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4DKL",
        "ligands": [
            {
                "name": "BF0",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Mus musculus",
        "publication_date": "2012-03-21",
        "family": "001_002_022_003",
        "preferred_chain": "A",
        "protein": "oprm_mouse",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE10954",
        "resolution": 2.8,
        "distance": -1.44,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6H7N",
        "ligands": [
            {
                "name": "Xamoterol",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2018-10-17",
        "family": "001_001_003_007",
        "preferred_chain": "A",
        "protein": "adrb1_melga",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1101/436212",
        "resolution": 2.5,
        "distance": 9.29,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4AMJ",
        "ligands": [
            {
                "name": "(S)-Carvedilol",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2012-05-23",
        "family": "001_001_003_007",
        "preferred_chain": "B",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2012.03.014",
        "resolution": 2.3,
        "distance": -1.01,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4IAQ",
        "ligands": [
            {
                "name": "dihydroergotamine",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2013-03-13",
        "family": "001_001_001_002",
        "preferred_chain": "A",
        "protein": "5ht1b_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1232807",
        "resolution": 2.8,
        "distance": 2.79,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5WQC",
        "ligands": [
            {
                "name": "EMPA",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-11-29",
        "family": "001_002_023_002",
        "preferred_chain": "A",
        "protein": "ox2r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2017.11.005",
        "resolution": 1.96,
        "distance": -0.99,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "1L9H",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2002-05-15",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1073/PNAS.082666399",
        "resolution": 2.6,
        "distance": -0.45,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "1HZX",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2001-07-04",
        "family": "001_009_001_001",
        "preferred_chain": "A,B",
        "protein": "opsd_bovin",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/BI0155091",
        "resolution": 2.8,
        "distance": -0.02,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2PED",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2007-10-30",
        "family": "001_009_001_001",
        "preferred_chain": "A,B",
        "protein": "opsd_bovin",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1529/BIOPHYSJ.107.108225",
        "resolution": 2.95,
        "distance": 0.24,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5XRA",
        "ligands": [
            {
                "name": "CHEMBL1683648",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-07-12",
        "family": "001_004_005_001",
        "preferred_chain": "A",
        "protein": "cnr1_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE23272",
        "resolution": 2.8,
        "distance": 7.95,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2Y04",
        "ligands": [
            {
                "name": "Levalbuterol",
                "type": "small molecule",
                "function": "Agonist (partial)"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2011-01-12",
        "family": "001_001_003_007",
        "preferred_chain": "B",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE09746",
        "resolution": 3.05,
        "distance": -1.14,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6AKX",
        "ligands": [
            {
                "name": "N-[(1S)-3-{(3-exo)-3-[3-methyl-5-(propan-2-yl)-4H-1,2,4-triazol-4-yl]-8-azabicyclo[3.2.1]octan-8-yl}-1-(thiophen-2-yl)propyl]cyclopentanecarboxamide",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-10-24",
        "family": "001_003_002_005",
        "preferred_chain": "B",
        "protein": "ccr5_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/ACS.JMEDCHEM.8B01077",
        "resolution": 2.8,
        "distance": 0.71,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3PDS",
        "ligands": [
            {
                "name": "FAUC50",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2011-01-12",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE09665",
        "resolution": 3.5,
        "distance": -0.96,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3NY8",
        "ligands": [
            {
                "name": "AC1NSK5N",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2010-08-11",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/JA105108Q",
        "resolution": 2.84,
        "distance": -1.26,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6AQF",
        "ligands": [
            {
                "name": "ZM241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-01-10",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2017.12.004",
        "resolution": 2.51,
        "distance": -0.44,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5OLO",
        "ligands": [
            {
                "name": "Tozadenant",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-01-17",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41598-017-18570-W",
        "resolution": 3.1,
        "distance": -0.69,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6IGL",
        "ligands": [
            {
                "name": "IRL1620",
                "type": "peptide",
                "function": "Partial agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-11-21",
        "family": "001_002_007_002",
        "preferred_chain": "A",
        "protein": "ednrb_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41467-018-07094-0",
        "resolution": 2.7,
        "distance": 0.16,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6D26",
        "ligands": [
            {
                "name": "fevipiprant",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-10-03",
        "family": "001_004_008_002",
        "preferred_chain": "A",
        "protein": "pd2r2_human",
        "state": "Inactive",
        "publication": None,
        "resolution": 2.8,
        "distance": -1.4,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6GPX",
        "ligands": [
            {
                "name": "MK-0812",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2019-01-02",
        "family": "001_003_002_002",
        "preferred_chain": "B",
        "protein": "ccr2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2018.10.027",
        "resolution": 2.7,
        "distance": 0.58,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5IUB",
        "ligands": [
            {
                "name": "CHEMBL184061",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-06-29",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/ACS.JMEDCHEM.6B00653",
        "resolution": 2.1,
        "distance": -0.87,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5IU8",
        "ligands": [
            {
                "name": "CHEMBL3934661",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-06-29",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": None,
        "resolution": 2,
        "distance": -0.82,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5VRA",
        "ligands": [
            {
                "name": "ZM241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-12-13",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NPROT.2017.135",
        "resolution": 2.35,
        "distance": -0.39,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4RWD",
        "ligands": [
            {
                "name": "DIPP-NH2",
                "type": "peptide-like",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2015-01-14",
        "family": "001_002_022_001",
        "preferred_chain": "A,B",
        "protein": "oprd_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NSMB.2965",
        "resolution": 2.7,
        "distance": -0.83,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5K2C",
        "ligands": [
            {
                "name": "ZM241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-09-21",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIADV.1600292",
        "resolution": 1.9,
        "distance": -0.67,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6H7J",
        "ligands": [
            {
                "name": "ISOPRENALINE",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2018-10-17",
        "family": "001_001_003_007",
        "preferred_chain": "A",
        "protein": "adrb1_melga",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1101/436212",
        "resolution": 2.8,
        "distance": 9.27,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2RH1",
        "ligands": [
            {
                "name": "Carazolol",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2007-10-30",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1150577",
        "resolution": 2.4,
        "distance": -0.82,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6MXT",
        "ligands": [
            {
                "name": "Salmeterol",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-11-14",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/S41589-018-0145-X",
        "resolution": 2.96,
        "distance": 8.22,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5YC8",
        "ligands": [
            {
                "name": "N-methyl scopolamine",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-11-21",
        "family": "001_001_002_002",
        "preferred_chain": "A",
        "protein": "acm2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41589-018-0152-Y",
        "resolution": 2.5,
        "distance": 1.05,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2Y00",
        "ligands": [
            {
                "name": "Dobutamine",
                "type": "small molecule",
                "function": "Agonist (partial)"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2011-01-12",
        "family": "001_001_003_007",
        "preferred_chain": "B",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE09746",
        "resolution": 2.5,
        "distance": -1.22,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3UZC",
        "ligands": [
            {
                "name": "T4E",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2012-03-21",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/JM201376W",
        "resolution": 3.34,
        "distance": -0.5,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4J4Q",
        "ligands": [],
        "species": "Bos taurus",
        "publication_date": "2013-10-30",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1002/ANIE.201302374",
        "resolution": 2.65,
        "distance": 8.54,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5L7I",
        "ligands": [
            {
                "name": "Vismodegib",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-07-20",
        "family": "005_001_001_011",
        "preferred_chain": "B",
        "protein": "smo_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE18934",
        "resolution": 3.3,
        "distance": -2.33,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3ZEV",
        "ligands": [
            {
                "name": "CHEMBL342252",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Rattus norvegicus",
        "publication_date": "2014-01-29",
        "family": "001_002_021_001",
        "preferred_chain": "A",
        "protein": "ntr1_rat",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1073/PNAS.1317903111",
        "resolution": 3,
        "distance": 0.45,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5TE3",
        "ligands": [],
        "species": "Bos taurus",
        "publication_date": "2017-03-15",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1073/PNAS.1617446114",
        "resolution": 2.7,
        "distance": 7.98,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6HLO",
        "ligands": [
            {
                "name": "Aprepitant",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2019-01-16",
        "family": "001_002_029_001",
        "preferred_chain": "A",
        "protein": "nk1r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41467-018-07939-8",
        "resolution": 2.4,
        "distance": 0.68,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5N2R",
        "ligands": [
            {
                "name": "PSB36",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-07-26",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2017.06.012",
        "resolution": 2.8,
        "distance": -0.73,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2Y03",
        "ligands": [
            {
                "name": "LEVISOPRENALINE",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2011-01-12",
        "family": "001_001_003_007",
        "preferred_chain": "B",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE09746",
        "resolution": 2.85,
        "distance": -1.2,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6J20",
        "ligands": [
            {
                "name": "Aprepitant",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2019-03-06",
        "family": "001_002_029_001",
        "preferred_chain": "A",
        "protein": "nk1r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41467-019-08568-5",
        "resolution": 2.7,
        "distance": 0.21,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4EIY",
        "ligands": [
            {
                "name": "ZM241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2012-07-25",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1219218",
        "resolution": 1.8,
        "distance": -0.55,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5V56",
        "ligands": [
            {
                "name": "N-methyl-N-[1-[4-(2-methylpyrazol-3-yl)phthalazin-1-yl]piperidin-4-yl]-4-nitro-2-(trifluoromethyl)benzamide",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-05-24",
        "family": "005_001_001_011",
        "preferred_chain": "B",
        "protein": "smo_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NCOMMS15383",
        "resolution": 2.9,
        "distance": -1.89,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3AYM",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Todarodes pacificus",
        "publication_date": "2011-08-17",
        "family": "001_009_001_001",
        "preferred_chain": "A,B",
        "protein": "opsd_todpa",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.JMB.2011.08.044",
        "resolution": 2.8,
        "distance": -0.22,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2YCX",
        "ligands": [
            {
                "name": "(S)-Cyanopindolol",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2011-06-01",
        "family": "001_001_003_007",
        "preferred_chain": "A",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1073/PNAS.1100185108",
        "resolution": 3.25,
        "distance": -1.64,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5D5A",
        "ligands": [
            {
                "name": "Carazolol",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-01-13",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1107/S2059798315021683",
        "resolution": 2.48,
        "distance": -1.14,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4K5Y",
        "ligands": [
            {
                "name": "CP-376395",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2013-07-17",
        "family": "002_001_002_001",
        "preferred_chain": "C",
        "protein": "crfr1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE12357",
        "resolution": 2.98,
        "distance": -2.02,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5OLH",
        "ligands": [
            {
                "name": "Vipadenant",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-01-17",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41598-017-18570-W",
        "resolution": 2.6,
        "distance": -0.7,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5F8U",
        "ligands": [
            {
                "name": "(S)-Cyanopindolol",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2015-12-23",
        "family": "001_001_003_007",
        "preferred_chain": "A",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NSMB.3130",
        "resolution": 3.35,
        "distance": -0.51,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5XR8",
        "ligands": [
            {
                "name": "8D0",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-07-12",
        "family": "001_004_005_001",
        "preferred_chain": "A",
        "protein": "cnr1_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE23272",
        "resolution": 2.95,
        "distance": 7.9,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2YDV",
        "ligands": [
            {
                "name": "NECA",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2011-05-18",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NATURE10136",
        "resolution": 2.6,
        "distance": 6.21,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6DRX",
        "ligands": [
            {
                "name": "Lisuride",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-08-29",
        "family": "001_001_001_007",
        "preferred_chain": "A",
        "protein": "5ht2b_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/S41594-018-0116-7",
        "resolution": 3.1,
        "distance": 2.67,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6FK7",
        "ligands": [
            {
                "name": "(2~{R},3~{R})-2-(4-chlorophenyl)-3-oxidanyl-1-spiro[1,3-benzodioxole-2,4'-piperidine]-1'-yl-butan-1-one",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2018-04-04",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1073/PNAS.1718084115",
        "resolution": 2.62,
        "distance": 7.68,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6FK6",
        "ligands": [
            {
                "name": "(2~{S})-2-(4-chlorophenyl)-3-methyl-1-spiro[1,3-benzodioxole-2,4'-piperidine]-1'-yl-butan-1-one",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2018-04-04",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": None,
        "resolution": 2.36,
        "distance": 7.85,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2VT4",
        "ligands": [
            {
                "name": "(S)-Cyanopindolol",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2008-06-24",
        "family": "001_001_003_007",
        "preferred_chain": "B",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE07101",
        "resolution": 2.7,
        "distance": -1.55,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3REY",
        "ligands": [
            {
                "name": "Xanthine amine congener",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2011-09-07",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2011.06.014",
        "resolution": 3.31,
        "distance": -0.38,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4AMI",
        "ligands": [
            {
                "name": "bucindolol",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2012-05-23",
        "family": "001_001_003_007",
        "preferred_chain": "A",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2012.03.014",
        "resolution": 3.2,
        "distance": -1.16,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4PY0",
        "ligands": [
            {
                "name": "2-Mesatp",
                "type": "small molecule",
                "function": "Agonist (partial)"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2014-04-30",
        "family": "001_006_002_006",
        "preferred_chain": "A",
        "protein": "p2y12_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NATURE13288",
        "resolution": 3.1,
        "distance": 3.81,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3OE9",
        "ligands": [
            {
                "name": "IT1t",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2010-10-27",
        "family": "001_003_002_014",
        "preferred_chain": "A",
        "protein": "cxcr4_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1194396",
        "resolution": 3.1,
        "distance": -0.65,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2R4R",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2007-11-06",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE06325",
        "resolution": 3.4,
        "distance": -2.8,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4LDE",
        "ligands": [
            {
                "name": "BI167107",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2013-09-25",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE12572",
        "resolution": 2.79,
        "distance": 9.4,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5JTB",
        "ligands": [
            {
                "name": "ZM241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-05-31",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIADV.1602952",
        "resolution": 2.8,
        "distance": -0.46,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5MZJ",
        "ligands": [
            {
                "name": "Theophylline",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-07-26",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2017.06.012",
        "resolution": 2,
        "distance": -0.54,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4PXF",
        "ligands": [],
        "species": "Bos taurus",
        "publication_date": "2014-09-17",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NCOMMS5801",
        "resolution": 2.75,
        "distance": 8.58,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4L6R",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2013-07-24",
        "family": "002_001_003_005",
        "preferred_chain": "A",
        "protein": "glr_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE12393",
        "resolution": 3.3,
        "distance": -4.62,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5MZP",
        "ligands": [
            {
                "name": "Caffeine",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-07-26",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2017.06.012",
        "resolution": 2.1,
        "distance": -0.75,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3OAX",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2011-01-19",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.BPJ.2010.08.003",
        "resolution": 2.6,
        "distance": 0.02,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4WW3",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Todarodes pacificus",
        "publication_date": "2015-06-17",
        "family": "001_009_001_001",
        "preferred_chain": "A, B",
        "protein": "opsd_todpa",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1371/JOURNAL.PONE.0126970",
        "resolution": 2.8,
        "distance": 0.1,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2YDO",
        "ligands": [
            {
                "name": "adenosine",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2011-05-18",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NATURE10136",
        "resolution": 3,
        "distance": 6.28,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6HLL",
        "ligands": [
            {
                "name": "CP-99,994",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2019-01-16",
        "family": "001_002_029_001",
        "preferred_chain": "A",
        "protein": "nk1r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41467-018-07939-8",
        "resolution": 3.27,
        "distance": 1.05,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3UON",
        "ligands": [
            {
                "name": "62869-69-6",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2012-02-01",
        "family": "001_001_002_002",
        "preferred_chain": "A",
        "protein": "acm2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE10753",
        "resolution": 3,
        "distance": -1.5,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3PQR",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2011-03-09",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE09789",
        "resolution": 2.85,
        "distance": 8.57,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4BEZ",
        "ligands": [],
        "species": "Bos taurus",
        "publication_date": "2013-04-24",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/EMBOR.2013.44",
        "resolution": 3.3,
        "distance": 8.33,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5IUA",
        "ligands": [
            {
                "name": "2-(Furan-2-Yl)-N~5~-[3-(4-Phenylpiperazin-1-Yl)propyl][1,2,4]triazolo[1,5-A][1,3,5]triazine-5,7-Diamine",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-06-29",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/ACS.JMEDCHEM.6B00653",
        "resolution": 2.2,
        "distance": -0.68,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3NYA",
        "ligands": [
            {
                "name": "(-)-Alprenolol",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2010-08-11",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/JA105108Q",
        "resolution": 3.16,
        "distance": -1.28,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2I35",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2006-10-17",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1073/PNAS.0608022103",
        "resolution": 3.8,
        "distance": -0.33,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4MQS",
        "ligands": [
            {
                "name": "iperoxo",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2013-11-27",
        "family": "001_001_002_002",
        "preferred_chain": "A",
        "protein": "acm2_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE12735",
        "resolution": 3.5,
        "distance": 9.14,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4U14",
        "ligands": [
            {
                "name": "Tiotropium",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Rattus norvegicus",
        "publication_date": "2014-11-26",
        "family": "001_001_002_003",
        "preferred_chain": "A",
        "protein": "acm3_rat",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2014.08.022",
        "resolution": 3.57,
        "distance": 0.52,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3VGA",
        "ligands": [
            {
                "name": "ZM241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2012-02-01",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE10750",
        "resolution": 3.1,
        "distance": -1.4,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4QKX",
        "ligands": [
            {
                "name": "35V",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2014-07-23",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1073/PNAS.1410415111",
        "resolution": 3.3,
        "distance": 9.44,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5WIU",
        "ligands": [
            {
                "name": "Nemonapride",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-10-18",
        "family": "001_001_004_004",
        "preferred_chain": "A",
        "protein": "drd4_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.AAN5468",
        "resolution": 1.96,
        "distance": -0.97,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6N52",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2019-01-23",
        "family": "004_002_002_005",
        "preferred_chain": "A",
        "protein": "grm5_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41586-019-0881-4",
        "resolution": 4,
        "distance": 4.14,
        "type": "Electron microscopy"
    },
    {
        "pdb_code": "2G87",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2006-09-02",
        "family": "001_009_001_001",
        "preferred_chain": "A,B",
        "protein": "opsd_bovin",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1002/ANIE.200600595",
        "resolution": 2.6,
        "distance": -0.18,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3EML",
        "ligands": [
            {
                "name": "ZM241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2008-10-14",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1164772",
        "resolution": 2.6,
        "distance": -1.16,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4GRV",
        "ligands": [
            {
                "name": "Neurotensin(8-13)",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Rattus norvegicus",
        "publication_date": "2012-10-17",
        "family": "001_002_021_001",
        "preferred_chain": "A",
        "protein": "ntr1_rat",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NATURE11558",
        "resolution": 2.8,
        "distance": 7.34,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6FUF",
        "ligands": [
            {
                "name": "Retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2018-10-03",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1126/SCIADV.AAT7052",
        "resolution": 3.12,
        "distance": 8.28,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6DDF",
        "ligands": [
            {
                "name": "DAMGO",
                "type": "peptide-like",
                "function": "Agonist"
            }
        ],
        "species": "Mus musculus",
        "publication_date": "2018-06-13",
        "family": "001_002_022_003",
        "preferred_chain": "R",
        "protein": "oprm_mouse",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/S41586-018-0219-7",
        "resolution": 3.5,
        "distance": 7.85,
        "type": "Electron microscopy"
    },
    {
        "pdb_code": "4XT3",
        "ligands": [
            {
                "name": "Fractalkine",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Human cytomegalovirus",
        "publication_date": "2015-03-04",
        "family": "001_011_001_001",
        "preferred_chain": "A",
        "protein": "us28_hcmva",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.AAA5026",
        "resolution": 3.8,
        "distance": 8.85,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6C1R",
        "ligands": [
            {
                "name": "PMX53",
                "type": "peptide",
                "function": "Antagonist"
            },
            {
                "name": "Avacopan",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-05-30",
        "family": "001_002_006_002",
        "preferred_chain": "B",
        "protein": "c5ar1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41594-018-0067-Z",
        "resolution": 2.2,
        "distance": -1.37,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6J21",
        "ligands": [
            {
                "name": "Aprepitant",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2019-03-06",
        "family": "001_002_029_001",
        "preferred_chain": "A",
        "protein": "nk1r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41467-019-08568-5",
        "resolution": 3.2,
        "distance": 0.35,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6IIU",
        "ligands": [
            {
                "name": "Ramatroban",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-12-19",
        "family": "001_004_008_009",
        "preferred_chain": "A",
        "protein": "ta2r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41589-018-0170-9",
        "resolution": 2.5,
        "distance": 1.01,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6BQG",
        "ligands": [
            {
                "name": "Ergotamine",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-02-14",
        "family": "001_001_001_008",
        "preferred_chain": "A",
        "protein": "5ht2c_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2018.01.001",
        "resolution": 3,
        "distance": 7.92,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3D4S",
        "ligands": [
            {
                "name": "timolol",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2008-06-17",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2008.05.001",
        "resolution": 2.8,
        "distance": -1.53,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5YQZ",
        "ligands": [
            {
                "name": "NNC1702",
                "type": "peptide",
                "function": "Partial agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-01-17",
        "family": "002_001_003_005",
        "preferred_chain": "R",
        "protein": "glr_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE25153",
        "resolution": 3,
        "distance": -4.97,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5K2B",
        "ligands": [
            {
                "name": "ZM241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-09-21",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIADV.1600292",
        "resolution": 2.5,
        "distance": -0.63,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3UZA",
        "ligands": [
            {
                "name": "CHEMBL2024115",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2012-03-21",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/JM201376W",
        "resolution": 3.27,
        "distance": -0.56,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6H7L",
        "ligands": [
            {
                "name": "DOBUTAMINE",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2018-10-17",
        "family": "001_001_003_007",
        "preferred_chain": "A",
        "protein": "adrb1_melga",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1101/436212",
        "resolution": 2.7,
        "distance": 9.24,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5W0P",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2017-08-09",
        "family": "001_009_001_001",
        "preferred_chain": "D",
        "protein": "opsd_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2017.07.002",
        "resolution": 3.01,
        "distance": 8.63,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4RWA",
        "ligands": [
            {
                "name": "DIPP-NH2",
                "type": "peptide-like",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2015-01-14",
        "family": "001_002_022_001",
        "preferred_chain": "A,B",
        "protein": "oprd_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NSMB.2965",
        "resolution": 3.28,
        "distance": -1.2,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4XNV",
        "ligands": [
            {
                "name": "BPTU",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2015-04-01",
        "family": "001_006_002_001",
        "preferred_chain": "A",
        "protein": "p2ry1_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NATURE14287",
        "resolution": 2.2,
        "distance": 5.58,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4Z34",
        "ligands": [
            {
                "name": "ONO-9780307",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2015-06-03",
        "family": "001_004_003_001",
        "preferred_chain": "A",
        "protein": "lpar1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2015.06.002",
        "resolution": 3,
        "distance": -1.3,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4BEY",
        "ligands": [],
        "species": "Bos taurus",
        "publication_date": "2013-05-08",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/EMBOR.2013.44",
        "resolution": 2.9,
        "distance": 8.38,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5GLH",
        "ligands": [
            {
                "name": "Et 1",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-09-07",
        "family": "001_002_007_002",
        "preferred_chain": "A",
        "protein": "ednrb_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE19319",
        "resolution": 2.8,
        "distance": -0.17,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2ZIY",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Todarodes pacificus",
        "publication_date": "2008-05-06",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_todpa",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1074/JBC.C800040200",
        "resolution": 3.7,
        "distance": -0.28,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2HPY",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2006-08-22",
        "family": "001_009_001_001",
        "preferred_chain": "A,B",
        "protein": "opsd_bovin",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1073/PNAS.0601765103",
        "resolution": 2.8,
        "distance": 0.33,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5XJM",
        "ligands": [
            {
                "name": "(Sar1,Ile8)-angiontensin II",
                "type": "peptide-like",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-07-11",
        "family": "001_002_001_002",
        "preferred_chain": "A",
        "protein": "agtr2_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/S41594-018-0079-8",
        "resolution": 3.2,
        "distance": 7.86,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6MET",
        "ligands": [
            {
                "name": "Envelope glycoprotein gp160",
                "type": "peptide",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-12-12",
        "family": "001_003_002_005",
        "preferred_chain": "B",
        "protein": "ccr5_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41586-018-0804-9",
        "resolution": 4.5,
        "distance": 0.7,
        "type": "Electron microscopy"
    },
    {
        "pdb_code": "3V2W",
        "ligands": [
            {
                "name": "W146",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2012-02-15",
        "family": "001_004_004_001",
        "preferred_chain": "A",
        "protein": "s1pr1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1215904",
        "resolution": 3.35,
        "distance": -1.48,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2J4Y",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2007-09-25",
        "family": "001_009_001_001",
        "preferred_chain": "A,B",
        "protein": "opsd_bovin",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.JMB.2007.03.007",
        "resolution": 3.4,
        "distance": -0.41,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4PHU",
        "ligands": [
            {
                "name": "TAK-875",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2014-07-16",
        "family": "001_004_001_001",
        "preferred_chain": "A",
        "protein": "ffar1_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NATURE13494",
        "resolution": 2.33,
        "distance": 3.58,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4MBS",
        "ligands": [
            {
                "name": "Maraviroc",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2013-09-11",
        "family": "001_003_002_005",
        "preferred_chain": "A",
        "protein": "ccr5_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1241475",
        "resolution": 2.71,
        "distance": 0.46,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5NJ6",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2017-05-03",
        "family": "001_002_026_002",
        "preferred_chain": "A",
        "protein": "par2_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NATURE22309",
        "resolution": 4,
        "distance": 7.1,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5IU4",
        "ligands": [
            {
                "name": "ZM241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-06-29",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/ACS.JMEDCHEM.6B00653",
        "resolution": 1.72,
        "distance": -0.76,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4Z36",
        "ligands": [
            {
                "name": "ONO-3080573",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2015-06-03",
        "family": "001_004_003_001",
        "preferred_chain": "A",
        "protein": "lpar1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2015.06.002",
        "resolution": 2.9,
        "distance": -1.22,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "1F88",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2000-08-04",
        "family": "001_009_001_001",
        "preferred_chain": "A,B",
        "protein": "opsd_bovin",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.289.5480.739",
        "resolution": 2.8,
        "distance": -0.5,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2YCY",
        "ligands": [
            {
                "name": "(S)-Cyanopindolol",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2011-06-08",
        "family": "001_001_003_007",
        "preferred_chain": "A",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1073/PNAS.1100185108",
        "resolution": 3.15,
        "distance": -1.62,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5WF5",
        "ligands": [
            {
                "name": "UK-432,097",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-02-21",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1016/J.STR.2017.12.013",
        "resolution": 2.6,
        "distance": 5.91,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6E59",
        "ligands": [
            {
                "name": "L760735",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-12-12",
        "family": "001_002_029_001",
        "preferred_chain": "A",
        "protein": "nk1r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1073/PNAS.1812717115",
        "resolution": 3.4,
        "distance": -0.46,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5TZR",
        "ligands": [
            {
                "name": "UNII-11612L5SPI",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-06-07",
        "family": "001_004_001_001",
        "preferred_chain": "A",
        "protein": "ffar1_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NSMB.3417",
        "resolution": 2.2,
        "distance": 3.69,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5CGC",
        "ligands": [
            {
                "name": "CHEMBL3603915",
                "type": "small molecule",
                "function": "NAM"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2015-08-12",
        "family": "004_002_002_005",
        "preferred_chain": "A",
        "protein": "grm5_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/ACS.JMEDCHEM.5B00892",
        "resolution": 3.1,
        "distance": 4.25,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3QAK",
        "ligands": [
            {
                "name": "UK-432097",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2011-03-09",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1202793",
        "resolution": 2.71,
        "distance": 6.12,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6H7M",
        "ligands": [
            {
                "name": "SALBUTAMOL",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2018-10-17",
        "family": "001_001_003_007",
        "preferred_chain": "A",
        "protein": "adrb1_melga",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1101/436212",
        "resolution": 2.76,
        "distance": 9.3,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5WB2",
        "ligands": [
            {
                "name": "CX3CL1",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Human cytomegalovirus",
        "publication_date": "2018-06-13",
        "family": "001_011_001_001",
        "preferred_chain": "A",
        "protein": "q80km9_hcmv",
        "state": "Active",
        "publication": "http://dx.doi.org/10.7554/ELIFE.35850",
        "resolution": 3.5,
        "distance": 8.86,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6IGK",
        "ligands": [
            {
                "name": "Endothelin-3",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-11-21",
        "family": "001_002_007_002",
        "preferred_chain": "A",
        "protein": "ednrb_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/S41467-018-07094-0",
        "resolution": 2,
        "distance": 2.18,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5D6L",
        "ligands": [
            {
                "name": "Carazolol",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-08-17",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NPROT.2017.057",
        "resolution": 3.2,
        "distance": -0.99,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5NDZ",
        "ligands": [
            {
                "name": "AZ3451",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-05-03",
        "family": "001_002_026_002",
        "preferred_chain": "A",
        "protein": "par2_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NATURE22309",
        "resolution": 3.6,
        "distance": 6.87,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5OLV",
        "ligands": [
            {
                "name": "CHEMBL1671936",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-01-17",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41598-017-18570-W",
        "resolution": 2,
        "distance": -0.56,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6CMO",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2018-06-20",
        "family": "001_009_001_001",
        "preferred_chain": "R",
        "protein": "opsd_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/S41586-018-0215-Y",
        "resolution": 4.5,
        "distance": 9.4,
        "type": "Electron microscopy"
    },
    {
        "pdb_code": "6D35",
        "ligands": [],
        "species": "Xenopus laevis",
        "publication_date": "2018-05-23",
        "family": "005_001_001_011",
        "preferred_chain": "A",
        "protein": "q98sw5_xenla",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2018.04.029",
        "resolution": 3.9,
        "distance": -2.2,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6DRZ",
        "ligands": [
            {
                "name": "Methysergide",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-08-29",
        "family": "001_001_001_007",
        "preferred_chain": "A",
        "protein": "5ht2b_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/S41594-018-0116-7",
        "resolution": 3.1,
        "distance": 4.19,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3PWH",
        "ligands": [
            {
                "name": "ZM241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2011-09-07",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2011.06.014",
        "resolution": 3.3,
        "distance": -0.67,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6FFI",
        "ligands": [
            {
                "name": "2-[2-(3-methoxyphenyl)ethynyl]-6-methyl-pyridine",
                "type": "small molecule",
                "function": "NAM"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-03-07",
        "family": "004_002_002_005",
        "preferred_chain": "A",
        "protein": "grm5_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/ACS.JMEDCHEM.7B01722",
        "resolution": 2.2,
        "distance": 4.49,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5NLX",
        "ligands": [
            {
                "name": "ZM 241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-09-27",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41467-017-00630-4",
        "resolution": 2.14,
        "distance": -0.71,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6GDG",
        "ligands": [
            {
                "name": "NECA",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-05-16",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.7554/ELIFE.35946",
        "resolution": 4.11,
        "distance": 10.41,
        "type": "Electron microscopy"
    },
    {
        "pdb_code": "5OM1",
        "ligands": [
            {
                "name": "4-(3-amino-5-phenyl-1,2,4-triazin-6-yl)-2-chlorophenol",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-01-17",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41598-017-18570-W",
        "resolution": 2.1,
        "distance": -0.69,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5UNF",
        "ligands": [
            {
                "name": "CHEMBL289472",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-04-05",
        "family": "001_002_001_002",
        "preferred_chain": "A",
        "protein": "agtr2_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE22035",
        "resolution": 2.8,
        "distance": 8.94,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4JKV",
        "ligands": [
            {
                "name": "LY2940680",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2013-04-24",
        "family": "005_001_001_011",
        "preferred_chain": "A",
        "protein": "smo_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE12167",
        "resolution": 2.45,
        "distance": -2.2,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6H7O",
        "ligands": [
            {
                "name": "4-{[(2S)-3-(tert-butylamino)-2-hydroxypropyl]oxy}-3H-indole-2-carbonitrile",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2018-10-17",
        "family": "001_001_003_007",
        "preferred_chain": "A",
        "protein": "adrb1_melga",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1101/436212",
        "resolution": 2.8,
        "distance": 9.29,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5XF1",
        "ligands": [
            {
                "name": "4-{[(4-Cyclohexylphenyl){[3-(Methylsulfonyl)phenyl]carbamoyl}amino]methyl}-N-(1h-Tetrazol-5-Yl)benzamide",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-05-24",
        "family": "002_001_003_005",
        "preferred_chain": "B",
        "protein": "glr_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE22363",
        "resolution": 3.19,
        "distance": -4.75,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3P0G",
        "ligands": [
            {
                "name": "BI-167107",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2011-01-19",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE09648",
        "resolution": 3.5,
        "distance": 9.03,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2Y02",
        "ligands": [
            {
                "name": "Carmoterol",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2011-01-12",
        "family": "001_001_003_007",
        "preferred_chain": "B",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE09746",
        "resolution": 2.6,
        "distance": -1.15,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5D5B",
        "ligands": [
            {
                "name": "Carazolol",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-01-13",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1107/S2059798315021683",
        "resolution": 3.8,
        "distance": -1.06,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5WKT",
        "ligands": [],
        "species": "Bos taurus",
        "publication_date": "2017-12-13",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NPROT.2017.135",
        "resolution": 3.2,
        "distance": 7.98,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6C1Q",
        "ligands": [
            {
                "name": "PMX53",
                "type": "peptide",
                "function": "Antagonist"
            },
            {
                "name": "H94Wrl71FP",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-05-30",
        "family": "001_002_006_002",
        "preferred_chain": "B",
        "protein": "c5ar1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41594-018-0067-Z",
        "resolution": 2.9,
        "distance": -1.37,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6FFH",
        "ligands": [
            {
                "name": "Fenobam",
                "type": "small molecule",
                "function": "NAM"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-03-07",
        "family": "004_002_002_005",
        "preferred_chain": "A",
        "protein": "grm5_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/ACS.JMEDCHEM.7B01722",
        "resolution": 2.65,
        "distance": 4.08,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5CGD",
        "ligands": [
            {
                "name": "CHEMBL3603923",
                "type": "small molecule",
                "function": "NAM"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2015-08-12",
        "family": "004_002_002_005",
        "preferred_chain": "A",
        "protein": "grm5_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/ACS.JMEDCHEM.5B00892",
        "resolution": 2.6,
        "distance": 4.13,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5DGY",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2016-03-23",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/SDATA.2016.21",
        "resolution": 7.7,
        "distance": 8.61,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4NC3",
        "ligands": [
            {
                "name": "ERGOTAMINE",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2013-12-18",
        "family": "001_001_001_007",
        "preferred_chain": "A",
        "protein": "5ht2b_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1244142",
        "resolution": 2.8,
        "distance": 3.09,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6N51",
        "ligands": [
            {
                "name": "Quisqualic acid",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2019-01-23",
        "family": "004_002_002_005",
        "preferred_chain": "B",
        "protein": "grm5_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/S41586-019-0881-4",
        "resolution": 4,
        "distance": 5.53,
        "type": "Electron microscopy"
    },
    {
        "pdb_code": "3OE0",
        "ligands": [
            {
                "name": "CVX15",
                "type": "peptide",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2010-10-27",
        "family": "001_003_002_014",
        "preferred_chain": "A",
        "protein": "cxcr4_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1194396",
        "resolution": 2.9,
        "distance": -1.45,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6FK8",
        "ligands": [
            {
                "name": "(2~{R},3~{S})-3-azanyl-2-(4-chlorophenyl)-1-spiro[1,3-benzodioxole-2,4'-piperidine]-1'-yl-butan-1-one",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2018-04-04",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1073/PNAS.1718084115",
        "resolution": 2.87,
        "distance": 7.94,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2I37",
        "ligands": [],
        "species": "Bos taurus",
        "publication_date": "2006-10-17",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1073/PNAS.0608022103",
        "resolution": 4.15,
        "distance": -1.63,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3OE8",
        "ligands": [
            {
                "name": "IT1t",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2010-10-27",
        "family": "001_003_002_014",
        "preferred_chain": "A",
        "protein": "cxcr4_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1194396",
        "resolution": 3.1,
        "distance": -1.28,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5OLG",
        "ligands": [
            {
                "name": "ZM241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-01-17",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41598-017-18570-W",
        "resolution": 1.87,
        "distance": -0.73,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5TVN",
        "ligands": [
            {
                "name": "Lysergide",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-02-01",
        "family": "001_001_001_007",
        "preferred_chain": "A",
        "protein": "5ht2b_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2016.12.033",
        "resolution": 2.9,
        "distance": 4.46,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6MEO",
        "ligands": [
            {
                "name": "Envelope glycoprotein gp160",
                "type": "peptide",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-12-12",
        "family": "001_003_002_005",
        "preferred_chain": "B",
        "protein": "ccr5_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41586-018-0804-9",
        "resolution": 3.9,
        "distance": 0.7,
        "type": "Electron microscopy"
    },
    {
        "pdb_code": "4X1H",
        "ligands": [
            {
                "name": "69984-73-2",
                "type": "N/A",
                "function": "Inverse agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2015-11-04",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1016/J.STR.2015.09.015",
        "resolution": 2.29,
        "distance": 8.24,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4BWB",
        "ligands": [
            {
                "name": "CHEMBL342252",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Rattus norvegicus",
        "publication_date": "2014-01-29",
        "family": "001_002_021_001",
        "preferred_chain": "A",
        "protein": "ntr1_rat",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1073/PNAS.1317903111",
        "resolution": 3.57,
        "distance": 1.53,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6FKB",
        "ligands": [
            {
                "name": "2-(4-chlorophenyl)-1-spiro[1,3-benzodioxole-2,4'-piperidine]-1'-yl-ethanone",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2018-04-04",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1073/PNAS.1718084115",
        "resolution": 3.03,
        "distance": 7.93,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5TE5",
        "ligands": [
            {
                "name": "10,20-Methanoretinal",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2017-03-15",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1073/PNAS.1617446114",
        "resolution": 4.01,
        "distance": -0.47,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5WF6",
        "ligands": [
            {
                "name": "UK-432,097",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-02-21",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1016/J.STR.2017.12.013",
        "resolution": 2.9,
        "distance": 5.83,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2X72",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2011-03-16",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE09795",
        "resolution": 3,
        "distance": 8.34,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6FKA",
        "ligands": [
            {
                "name": "(2~{S})-2-(3,4-dichlorophenyl)-3-methyl-1-spiro[1,3-benzodioxole-2,4'-piperidine]-1'-yl-butan-1-one",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2018-04-04",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1073/PNAS.1718084115",
        "resolution": 2.7,
        "distance": 7.99,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2YCW",
        "ligands": [
            {
                "name": "timolol",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2011-06-01",
        "family": "001_001_003_007",
        "preferred_chain": "A",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1073/PNAS.1100185108",
        "resolution": 3,
        "distance": -1.08,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5ZK3",
        "ligands": [
            {
                "name": "Quinuclidinyl benzilate",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-11-21",
        "family": "001_001_002_002",
        "preferred_chain": "A",
        "protein": "acm2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41589-018-0152-Y",
        "resolution": 2.6,
        "distance": 0.58,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5K2A",
        "ligands": [
            {
                "name": "ZM241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-09-21",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIADV.1600292",
        "resolution": 2.5,
        "distance": -0.71,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6DRY",
        "ligands": [
            {
                "name": "Methylergonovine",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-08-29",
        "family": "001_001_001_007",
        "preferred_chain": "A",
        "protein": "5ht2b_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/S41594-018-0116-7",
        "resolution": 2.92,
        "distance": 4.34,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4BVN",
        "ligands": [
            {
                "name": "(S)-Cyanopindolol",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2014-04-02",
        "family": "001_001_003_007",
        "preferred_chain": "A",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1371/JOURNAL.PONE.0092727",
        "resolution": 2.1,
        "distance": -2.09,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5UVI",
        "ligands": [
            {
                "name": "ZM241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-05-24",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1107/S205225251700570X",
        "resolution": 3.2,
        "distance": -0.58,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3ZPR",
        "ligands": [
            {
                "name": "4-methyl-2-(piperazin-1-yl)quinoline",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2013-04-03",
        "family": "001_001_003_007",
        "preferred_chain": "B",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/JM400140Q",
        "resolution": 2.7,
        "distance": -1.11,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6IBL",
        "ligands": [
            {
                "name": "Formoterol",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2019-01-09",
        "family": "001_001_003_007",
        "preferred_chain": "A",
        "protein": "adrb1_melga",
        "state": "Active",
        "publication": None,
        "resolution": 2.7,
        "distance": 9.42,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5ZK8",
        "ligands": [
            {
                "name": "N-methyl scopolamine",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-11-21",
        "family": "001_001_002_002",
        "preferred_chain": "A",
        "protein": "acm2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41589-018-0152-Y",
        "resolution": 3,
        "distance": 1,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5N2S",
        "ligands": [
            {
                "name": "PSB36",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-07-26",
        "family": "001_006_001_001",
        "preferred_chain": "A",
        "protein": "aa1r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2017.06.012",
        "resolution": 3.3,
        "distance": -0.47,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5UIG",
        "ligands": [
            {
                "name": "J3.651.884G",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-02-08",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1073/PNAS.1621423114",
        "resolution": 3.5,
        "distance": 1.11,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4EA3",
        "ligands": [
            {
                "name": "C-24",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2012-04-25",
        "family": "001_002_022_004",
        "preferred_chain": "A",
        "protein": "oprx_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE11085",
        "resolution": 3.01,
        "distance": -1.21,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5VEX",
        "ligands": [
            {
                "name": "4-{[(4-Cyclohexylphenyl){[3-(Methylsulfonyl)phenyl]carbamoyl}amino]methyl}-N-(1h-Tetrazol-5-Yl)benzamide",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-05-17",
        "family": "002_001_003_003",
        "preferred_chain": "B",
        "protein": "glp1r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE22378",
        "resolution": 3,
        "distance": -5.05,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6FKD",
        "ligands": [
            {
                "name": "5-chloranyl-2-(2-oxidanylidene-2-spiro[1,3-benzodioxole-2,4'-piperidine]-1'-yl-ethyl)-3~{H}-pyridin-6-one",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2018-04-04",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1073/PNAS.1718084115",
        "resolution": 2.49,
        "distance": 7.92,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5EE7",
        "ligands": [
            {
                "name": "3,6,9,12,15,18,21,24-OCTAOXAHEXACOSAN-1-OL",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-04-20",
        "family": "002_001_003_005",
        "preferred_chain": "A",
        "protein": "glr_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE17414",
        "resolution": 2.5,
        "distance": -4.8,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3RFM",
        "ligands": [
            {
                "name": "caffeine",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2011-09-07",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2011.06.014",
        "resolution": 3.6,
        "distance": -0.48,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5ZKB",
        "ligands": [
            {
                "name": "AF-DX 384",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-11-21",
        "family": "001_001_002_002",
        "preferred_chain": "A",
        "protein": "acm2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41589-018-0152-Y",
        "resolution": 2.95,
        "distance": 0.97,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5X7D",
        "ligands": [
            {
                "name": "Carazolol",
                "type": "small molecule",
                "function": "Antagonist"
            },
            {
                "name": "4-carbamoyl-N-[(2R)-2-cyclohexyl-2-phenylacetyl]-L-phenylalanyl-3-bromo-N-methyl-L-phenylalaninamide",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-08-16",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE23652",
        "resolution": 2.7,
        "distance": -1.08,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5V57",
        "ligands": [
            {
                "name": "N-methyl-N-[1-[4-(2-methylpyrazol-3-yl)phthalazin-1-yl]piperidin-4-yl]-4-nitro-2-(trifluoromethyl)benzamide",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-05-24",
        "family": "005_001_001_011",
        "preferred_chain": "A",
        "protein": "smo_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NCOMMS15383",
        "resolution": 3,
        "distance": -1.67,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3KJ6",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2010-02-16",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE08650",
        "resolution": 3.4,
        "distance": -2.18,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4LDL",
        "ligands": [
            {
                "name": "hydroxybenzylisoproterenol",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2013-09-25",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE12572",
        "resolution": 3.1,
        "distance": 9.26,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5KW2",
        "ligands": [
            {
                "name": "(3~{S})-3-cyclopropyl-3-[2-[1-[2-[2,2-dimethylpropyl-(6-methylpyridin-2-yl)carbamoyl]-5-methoxy-phenyl]piperidin-4-yl]-1-benzofuran-6-yl]propanoic acid",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-05-02",
        "family": "001_004_001_001",
        "preferred_chain": "A",
        "protein": "ffar1_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/S41467-017-01240-W",
        "resolution": 2.76,
        "distance": 4.17,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5DHH",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2015-10-21",
        "family": "001_002_022_004",
        "preferred_chain": "A",
        "protein": "oprx_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2015.07.024",
        "resolution": 3,
        "distance": -1.11,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5V54",
        "ligands": [
            {
                "name": "CHEMBL428892",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-02-07",
        "family": "001_001_001_002",
        "preferred_chain": "A",
        "protein": "5ht1b_human",
        "state": "Intermediate",
        "publication": None,
        "resolution": 3.9,
        "distance": 3.69,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5UNH",
        "ligands": [
            {
                "name": "8EM",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-04-05",
        "family": "001_002_001_002",
        "preferred_chain": "B",
        "protein": "agtr2_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE22035",
        "resolution": 2.9,
        "distance": 9.17,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3AYN",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Todarodes pacificus",
        "publication_date": "2011-08-17",
        "family": "001_009_001_001",
        "preferred_chain": "A,B",
        "protein": "opsd_todpa",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.JMB.2011.08.044",
        "resolution": 2.7,
        "distance": -0.22,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4DAJ",
        "ligands": [
            {
                "name": "Tiotropium",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Rattus norvegicus",
        "publication_date": "2012-02-22",
        "family": "001_001_002_003",
        "preferred_chain": "A",
        "protein": "acm3_rat",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE10867",
        "resolution": 3.4,
        "distance": 0.22,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2YCZ",
        "ligands": [
            {
                "name": "timolol",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2011-06-01",
        "family": "001_001_003_007",
        "preferred_chain": "B",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1073/PNAS.1100185108",
        "resolution": 3.65,
        "distance": -1.72,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2Y01",
        "ligands": [
            {
                "name": "Dobutamine",
                "type": "small molecule",
                "function": "Agonist (partial)"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2011-03-30",
        "family": "001_001_003_007",
        "preferred_chain": "A",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE09746",
        "resolution": 2.6,
        "distance": -1.07,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6DS0",
        "ligands": [
            {
                "name": "LY266097",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-08-29",
        "family": "001_001_001_007",
        "preferred_chain": "A",
        "protein": "5ht2b_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/S41594-018-0116-7",
        "resolution": 3.19,
        "distance": 3.21,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4A4M",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2012-01-25",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1073/PNAS.1114089108",
        "resolution": 3.3,
        "distance": 8.2,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6A93",
        "ligands": [
            {
                "name": "Risperidone",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2019-02-13",
        "family": "001_001_001_006",
        "preferred_chain": "A",
        "protein": "5ht2a_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41594-018-0180-Z",
        "resolution": 3,
        "distance": -0.48,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6DDE",
        "ligands": [
            {
                "name": "DAMGO",
                "type": "peptide-like",
                "function": "Agonist"
            }
        ],
        "species": "Mus musculus",
        "publication_date": "2018-06-13",
        "family": "001_002_022_003",
        "preferred_chain": "R",
        "protein": "oprm_mouse",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/S41586-018-0219-7",
        "resolution": 3.5,
        "distance": 7.19,
        "type": "Electron microscopy"
    },
    {
        "pdb_code": "3C9M",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2008-08-05",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1107/S0907444908017162",
        "resolution": 3.4,
        "distance": -0.2,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3OE6",
        "ligands": [
            {
                "name": "IT1t",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2010-10-27",
        "family": "001_003_002_014",
        "preferred_chain": "A",
        "protein": "cxcr4_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1194396",
        "resolution": 3.2,
        "distance": -1.33,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4GPO",
        "ligands": [],
        "species": "Meleagris gallopavo",
        "publication_date": "2013-02-27",
        "family": "001_001_003_007",
        "preferred_chain": "A,B",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NSMB.2504",
        "resolution": 3.5,
        "distance": -1.36,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2R4S",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2007-11-06",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE06325",
        "resolution": 3.4,
        "distance": -2.89,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3NY9",
        "ligands": [
            {
                "name": "CHEMBL1233771",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2010-08-11",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/JA105108Q",
        "resolution": 2.84,
        "distance": -1.49,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4GBR",
        "ligands": [
            {
                "name": "(S)-Carazolol",
                "type": "small molecule",
                "function": "Inverse agonist (partial)"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2012-10-24",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1371/JOURNAL.PONE.0046039",
        "resolution": 3.99,
        "distance": -0.55,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4XEE",
        "ligands": [
            {
                "name": "CHEMBL342252",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Rattus norvegicus",
        "publication_date": "2015-07-29",
        "family": "001_002_021_001",
        "preferred_chain": "A",
        "protein": "ntr1_rat",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NCOMMS8895",
        "resolution": 2.9,
        "distance": 6.49,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3PXO",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2011-03-09",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE09789",
        "resolution": 3,
        "distance": 7.94,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5XPR",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2017-08-16",
        "family": "001_002_007_002",
        "preferred_chain": "A",
        "protein": "ednrb_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NSMB.3450",
        "resolution": 3.6,
        "distance": 0.09,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4ZJC",
        "ligands": [
            {
                "name": "SB-674042",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-03-09",
        "family": "001_002_023_001",
        "preferred_chain": "A",
        "protein": "ox1r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NSMB.3183",
        "resolution": 2.83,
        "distance": -0.54,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6FK9",
        "ligands": [
            {
                "name": "(2~{S})-3-methyl-2-phenyl-1-spiro[1,3-benzodioxole-2,4'-piperidine]-1'-yl-butan-1-one",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2018-04-04",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1073/PNAS.1718084115",
        "resolution": 2.63,
        "distance": 7.83,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4S0V",
        "ligands": [
            {
                "name": "Suvorexant",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2015-01-14",
        "family": "001_002_023_002",
        "preferred_chain": "A",
        "protein": "ox2r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE14035",
        "resolution": 2.5,
        "distance": -1.02,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4BV0",
        "ligands": [
            {
                "name": "CHEMBL342252",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Rattus norvegicus",
        "publication_date": "2014-01-29",
        "family": "001_002_021_001",
        "preferred_chain": "A",
        "protein": "ntr1_rat",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1073/PNAS.1317903111",
        "resolution": 3.1,
        "distance": 0.95,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "2I36",
        "ligands": [],
        "species": "Bos taurus",
        "publication_date": "2006-10-17",
        "family": "001_009_001_001",
        "preferred_chain": "A,B,C",
        "protein": "opsd_bovin",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1073/PNAS.0608022103",
        "resolution": 4.1,
        "distance": -0.36,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5UZ7",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2017-05-03",
        "family": "002_001_001_001",
        "preferred_chain": "R",
        "protein": "calcr_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE22327",
        "resolution": 4.1,
        "distance": 7.8,
        "type": "Electron microscopy"
    },
    {
        "pdb_code": "5NM2",
        "ligands": [
            {
                "name": "ZM241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-09-27",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41467-017-00630-4",
        "resolution": 1.95,
        "distance": -0.83,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4UG2",
        "ligands": [
            {
                "name": "Cgs 21680",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2015-04-08",
        "family": "001_006_001_002",
        "preferred_chain": "A,B",
        "protein": "aa2ar_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1124/MOL.114.097360",
        "resolution": 2.6,
        "distance": 5.86,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4QIM",
        "ligands": [
            {
                "name": "AntaXV",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2014-07-23",
        "family": "005_001_001_011",
        "preferred_chain": "A",
        "protein": "smo_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NCOMMS5355",
        "resolution": 2.61,
        "distance": -2.23,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5GLI",
        "ligands": [],
        "species": "Homo sapiens",
        "publication_date": "2016-09-07",
        "family": "001_002_007_002",
        "preferred_chain": "A",
        "protein": "ednrb_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE19319",
        "resolution": 2.5,
        "distance": -0.38,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4IAR",
        "ligands": [
            {
                "name": "ERGOTAMINE",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2013-03-13",
        "family": "001_001_001_002",
        "preferred_chain": "A",
        "protein": "5ht1b_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1232807",
        "resolution": 2.7,
        "distance": 4.22,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4U16",
        "ligands": [
            {
                "name": "methscopolamine",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Rattus norvegicus",
        "publication_date": "2014-11-26",
        "family": "001_001_002_003",
        "preferred_chain": "B",
        "protein": "acm3_rat",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2014.08.022",
        "resolution": 3.7,
        "distance": 0.2,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4QIN",
        "ligands": [
            {
                "name": "SAG1.5",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2014-07-23",
        "family": "005_001_001_011",
        "preferred_chain": "A",
        "protein": "smo_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NCOMMS5355",
        "resolution": 2.6,
        "distance": -2.38,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6FKC",
        "ligands": [
            {
                "name": "3-[1'-[(2~{S})-2-(4-chlorophenyl)-3-methyl-butanoyl]spiro[1,3-benzodioxole-2,4'-piperidine]-5-yl]propanoic acid",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2018-04-04",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1073/PNAS.1718084115",
        "resolution": 2.46,
        "distance": 7.84,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5U09",
        "ligands": [
            {
                "name": "Taranabant",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-12-07",
        "family": "001_004_005_001",
        "preferred_chain": "A",
        "protein": "cnr1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NATURE20613",
        "resolution": 2.6,
        "distance": -2.87,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5EN0",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2016-08-10",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.15252/EMBR.201642671",
        "resolution": 2.81,
        "distance": 8.4,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3C9L",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2008-08-05",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1107/S0907444908017162",
        "resolution": 2.65,
        "distance": 0.09,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3ZPQ",
        "ligands": [
            {
                "name": "4-(1-Piperazinyl)-1H-indole",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2013-04-03",
        "family": "001_001_003_007",
        "preferred_chain": "B",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/JM400140Q",
        "resolution": 2.8,
        "distance": -1.18,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5YHL",
        "ligands": [
            {
                "name": "ONO-AE3-208-Br",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-12-05",
        "family": "001_004_008_006",
        "preferred_chain": "A",
        "protein": "pe2r4_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41589-018-0131-3",
        "resolution": 4.2,
        "distance": -0.94,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4O9R",
        "ligands": [
            {
                "name": "Cyclopamine",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2014-03-05",
        "family": "005_001_001_011",
        "preferred_chain": "A",
        "protein": "smo_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NCOMMS4309",
        "resolution": 3.2,
        "distance": -2.77,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4N4W",
        "ligands": [
            {
                "name": "SANT-1",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2014-01-22",
        "family": "005_001_001_011",
        "preferred_chain": "A",
        "protein": "smo_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/NCOMMS5355",
        "resolution": 2.8,
        "distance": -1.76,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3DQB",
        "ligands": [],
        "species": "Bos taurus",
        "publication_date": "2008-09-23",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE07330",
        "resolution": 3.2,
        "distance": 8.59,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4YAY",
        "ligands": [
            {
                "name": "ZD7155",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2015-04-22",
        "family": "001_002_001_001",
        "preferred_chain": "A",
        "protein": "agtr1_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2015.04.011",
        "resolution": 2.9,
        "distance": -1.1,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5OLZ",
        "ligands": [
            {
                "name": "4-(3-amino-5-phenyl-1,2,4-triazin-6-yl)-2-chlorophenol",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-01-17",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41598-017-18570-W",
        "resolution": 1.9,
        "distance": -0.75,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5NM4",
        "ligands": [
            {
                "name": "ZM 241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2017-09-27",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41467-017-00630-4",
        "resolution": 1.7,
        "distance": -0.8,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4PXZ",
        "ligands": [
            {
                "name": "2-MeSADP",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2014-04-30",
        "family": "001_006_002_006",
        "preferred_chain": "A",
        "protein": "p2y12_human",
        "state": "Intermediate",
        "publication": "http://dx.doi.org/10.1038/NATURE13288",
        "resolution": 2.5,
        "distance": 3.91,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "1U19",
        "ligands": [
            {
                "name": "retinal",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Bos taurus",
        "publication_date": "2004-10-12",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.JMB.2004.07.044",
        "resolution": 2.2,
        "distance": -0.23,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5OM4",
        "ligands": [
            {
                "name": "4-(3-amino-5-phenyl-1,2,4-triazin-6-yl)-2-chlorophenol",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-01-17",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41598-017-18570-W",
        "resolution": 2,
        "distance": -0.66,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6AKY",
        "ligands": [
            {
                "name": "4,4-difluoro-N-[(1S)-3-{(3-exo)-3-[3-methyl-5-(propan-2-yl)-4H-1,2,4-triazol-4-yl]-8-azabicyclo[3.2.1]octan-8-yl}-1-(thiophen-3-yl)propyl]cyclohexane-1-carboxamide",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-10-24",
        "family": "001_003_002_005",
        "preferred_chain": "A",
        "protein": "ccr5_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/ACS.JMEDCHEM.8B01077",
        "resolution": 2.8,
        "distance": 0.4,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5A8E",
        "ligands": [
            {
                "name": "7-methylcyanopindolol",
                "type": "small molecule",
                "function": "Inverse agonist"
            }
        ],
        "species": "Meleagris gallopavo",
        "publication_date": "2015-09-30",
        "family": "001_001_003_007",
        "preferred_chain": "A",
        "protein": "adrb1_melga",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1124/MOL.115.101030",
        "resolution": 2.4,
        "distance": -2.23,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6GPS",
        "ligands": [
            {
                "name": "MK-0812",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2019-01-02",
        "family": "001_003_002_002",
        "preferred_chain": "A",
        "protein": "ccr2_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1016/J.STR.2018.10.027",
        "resolution": 3.3,
        "distance": 0.82,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5ZBQ",
        "ligands": [
            {
                "name": "UR-MK299",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-04-25",
        "family": "001_002_020_001",
        "preferred_chain": "A",
        "protein": "npy1r_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1038/S41586-018-0046-X",
        "resolution": 2.7,
        "distance": -1.31,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5K2D",
        "ligands": [
            {
                "name": "ZM241385",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-09-21",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIADV.1600292",
        "resolution": 1.9,
        "distance": -0.71,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4LDO",
        "ligands": [
            {
                "name": "epinephrine",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2013-09-25",
        "family": "001_001_003_008",
        "preferred_chain": "A",
        "protein": "adrb2_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE12572",
        "resolution": 3.2,
        "distance": 9.16,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6DO1",
        "ligands": [
            {
                "name": "Angiotensin-like peptide S1I8",
                "type": "peptide",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2019-01-30",
        "family": "001_002_001_001",
        "preferred_chain": "A",
        "protein": "agtr1_human",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1016/J.CELL.2018.12.006",
        "resolution": 2.9,
        "distance": 8.03,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "4RWS",
        "ligands": [
            {
                "name": "vMIP-II",
                "type": "peptide",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2015-02-11",
        "family": "001_003_002_014",
        "preferred_chain": "A",
        "protein": "cxcr4_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1126/SCIENCE.1261064",
        "resolution": 3.1,
        "distance": -0.91,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "5IU7",
        "ligands": [
            {
                "name": "2-(Furan-2-Yl)-N~5~-[2-(4-Phenylpiperidin-1-Yl)ethyl][1,2,4]triazolo[1,5-A][1,3,5]triazine-5,7-Diamine",
                "type": "small molecule",
                "function": "Agonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2016-06-29",
        "family": "001_006_001_002",
        "preferred_chain": "A",
        "protein": "aa2ar_human",
        "state": "Inactive",
        "publication": "http://dx.doi.org/10.1021/ACS.JMEDCHEM.6B00653",
        "resolution": 1.9,
        "distance": -0.68,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "6D27",
        "ligands": [
            {
                "name": "CAY10471",
                "type": "small molecule",
                "function": "Antagonist"
            }
        ],
        "species": "Homo sapiens",
        "publication_date": "2018-10-03",
        "family": "001_004_008_002",
        "preferred_chain": "A",
        "protein": "pd2r2_human",
        "state": "Inactive",
        "publication": None,
        "resolution": 2.74,
        "distance": -1.73,
        "type": "X-ray diffraction"
    },
    {
        "pdb_code": "3CAP",
        "ligands": [],
        "species": "Bos taurus",
        "publication_date": "2008-06-24",
        "family": "001_009_001_001",
        "preferred_chain": "A",
        "protein": "opsd_bovin",
        "state": "Active",
        "publication": "http://dx.doi.org/10.1038/NATURE07063",
        "resolution": 2.9,
        "distance": 7.91,
        "type": "X-ray diffraction"
    }
]
print(len(k))
# 长度为 321
