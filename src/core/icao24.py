"""
ref.
1. https://hexdb.io/
2. https://www.flightradar24.com/data/aircraft/
"""

ICAO24_DICT = {
    "872f5c": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "872F5C",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA921A",
        "Type": "787 9"
    },
    "a1863b": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "A1863B",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N198DN",
        "Type": "767 332ER/W"
    },
    "8515c4": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8515C4",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA329J",
        "Type": "737NG 846/W"
    },
    "7583a0": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "7583A0",
        "OperatorFlagCode": "PAL",
        "RegisteredOwners": "Philippine Airlines",
        "Registration": "RP-C9917",
        "Type": "A321 231SL"
    },
    "71bf93": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "71BF93",
        "OperatorFlagCode": "AAR",
        "RegisteredOwners": "Asiana Airlines",
        "Registration": "HL7793",
        "Type": "A330 323E"
    },
    "861ef8": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861EF8",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA615A",
        "Type": "767 381ER"
    },
    "867904": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "867904",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA717A",
        "Type": "777 281ER"
    },
    "86e79a": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E79A",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA872A",
        "Type": "787 9"
    },
    "862226": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "862226",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA622A",
        "Type": "767 381ER/W"
    },
    "86960c": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86960C",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA79AN",
        "Type": "737NG 881/W"
    },
    "85d098": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "85D098",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA54AN",
        "Type": "737NG 881/W"
    },
    "86d2cc": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D2CC",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA817A",
        "Type": "787 8"
    },
    "78164c": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "78164C",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-307J",
        "Type": "A320 251NSL"
    },
    "789228": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "789228",
        "OperatorFlagCode": "HKE",
        "RegisteredOwners": "Hong Kong Express Airways",
        "Registration": "B-LEK",
        "Type": "A321 231SL"
    },
    "861f00": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861F00",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA615J",
        "Type": "767 346ER"
    },
    "7c531e": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "7C531E",
        "OperatorFlagCode": "QFA",
        "RegisteredOwners": "Qantas",
        "Registration": "VH-QPC",
        "Type": "A330 303"
    },
    "872fc2": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "872FC2",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA924A",
        "Type": "787 9"
    },
    "85db54": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "85DB54",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA57AN",
        "Type": "737NG 881/W"
    },
    "8514f8": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8514F8",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA323J",
        "Type": "737NG 846/W"
    },
    "868012": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "868012",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA736J",
        "Type": "777 346ER"
    },
    "71c371": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "71C371",
        "OperatorFlagCode": "AAR",
        "RegisteredOwners": "Asiana Airlines",
        "Registration": "HL8371",
        "Type": "A321 251NXSL"
    },
    "781364": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "781364",
        "OperatorFlagCode": "CSN",
        "RegisteredOwners": "China Southern Airlines",
        "Registration": "B-1065",
        "Type": "A330 343E"
    },
    "780a5b": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "780A5B",
        "OperatorFlagCode": "CPA",
        "RegisteredOwners": "Cathay Pacific Airways",
        "Registration": "B-KQK",
        "Type": "777 367ER"
    },
    "87304a": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "87304A",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA928A",
        "Type": "787 9"
    },
    "781666": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "781666",
        "OperatorFlagCode": "CSN",
        "RegisteredOwners": "China Southern Airlines",
        "Registration": "B-209X",
        "Type": "787 9"
    },
    "aa99b7": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "AA99B7",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N782UA",
        "Type": "777 222ER"
    },
    "872742": {
        "ICAOTypeCode": "B78X",
        "Manufacturer": "Boeing",
        "ModeS": "872742",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA901A",
        "Type": "787 10"
    },
    "86d259": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86D259",
        "OperatorFlagCode": "SNJ",
        "RegisteredOwners": "Solaseed Air",
        "Registration": "JA813X",
        "Type": "737NG 800/W"
    },
    "3965b1": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "3965B1",
        "OperatorFlagCode": "AFR",
        "RegisteredOwners": "Air France",
        "Registration": "F-GZNR",
        "Type": "777 328ER"
    },
    "758582": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "758582",
        "OperatorFlagCode": "PAL",
        "RegisteredOwners": "Philippine Airlines",
        "Registration": "RP-C9936",
        "Type": "A321 271NSL"
    },
    "862d94": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "862D94",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA657J",
        "Type": "767 346ER"
    },
    "86eaf2": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86EAF2",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA880J",
        "Type": "787 9"
    },
    "aa6b9d": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "AA6B9D",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N77012",
        "Type": "777 224ER"
    },
    "abfdd1": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "ABFDD1",
        "OperatorFlagCode": "AAL",
        "RegisteredOwners": "American Airlines",
        "Registration": "N872AN",
        "Type": "787 8"
    },
    "841f65": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "841F65",
        "OperatorFlagCode": "JTA",
        "RegisteredOwners": "Japan TransOcean Air",
        "Registration": "JA08RK",
        "Type": "737NG 800/W"
    },
    "aa9300": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "AA9300",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N78009",
        "Type": "777 224ER"
    },
    "86e780": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E780",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA871J",
        "Type": "787 9"
    },
    "84b7b6": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B7B6",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA214A",
        "Type": "A320 271NSL"
    },
    "851ca8": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851CA8",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA347J",
        "Type": "737NG 846/W"
    },
    "86cf7c": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86CF7C",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA809A",
        "Type": "787 8"
    },
    "8621ea": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "8621EA",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA620J",
        "Type": "767 346ER/W"
    },
    "8514b4": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8514B4",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA321J",
        "Type": "737NG 846/W"
    },
    "7cad43": {
        "ICAOTypeCode": "B38M",
        "Manufacturer": "Boeing",
        "ModeS": "7CAD43",
        "OperatorFlagCode": "VOZ",
        "RegisteredOwners": "Virgin Australia",
        "Registration": "VH-8ID",
        "Type": "737MAX 8"
    },
    "845daa": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "845DAA",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA112A",
        "Type": "A321 211SL"
    },
    "71c003": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "71C003",
        "OperatorFlagCode": "KAL",
        "RegisteredOwners": "Korean Air",
        "Registration": "HL8003",
        "Type": "A330 323E"
    },
    "851848": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851848",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA331J",
        "Type": "737NG 846/W"
    },
    "782002": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "782002",
        "OperatorFlagCode": "CSN",
        "RegisteredOwners": "China Southern Airlines",
        "Registration": "B-32FT",
        "Type": "A321 253NXSL"
    },
    "78090f": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "78090F",
        "OperatorFlagCode": "CCA",
        "RegisteredOwners": "Air China",
        "Registration": "B-5906",
        "Type": "A330 343E"
    },
    "8a0479": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "8A0479",
        "OperatorFlagCode": "GIA",
        "RegisteredOwners": "Garuda Indonesia",
        "Registration": "PK-GPU",
        "Type": "A330 343E"
    },
    "86d9f4": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86D9F4",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA837A",
        "Type": "787 9"
    },
    "7c5321": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "7C5321",
        "OperatorFlagCode": "QFA",
        "RegisteredOwners": "Qantas",
        "Registration": "VH-QPF",
        "Type": "A330 303"
    },
    "86eb94": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86EB94",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA885A",
        "Type": "787 9"
    },
    "76ceef": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "76CEEF",
        "OperatorFlagCode": "SIA",
        "RegisteredOwners": "Singapore Airlines",
        "Registration": "9V-SWO",
        "Type": "777 312ER"
    },
    "86eee4": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86EEE4",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA893A",
        "Type": "787 9"
    },
    "3965a7": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "3965A7",
        "OperatorFlagCode": "AFR",
        "RegisteredOwners": "Air France",
        "Registration": "F-GZNH",
        "Type": "777 328ER"
    },
    "86d996": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D996",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA834J",
        "Type": "787 8"
    },
    "847294": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "847294",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA16XJ",
        "Type": "A350 941"
    },
    "86d200": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D200",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA811A",
        "Type": "787 8"
    },
    "8678e2": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "8678E2",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA716A",
        "Type": "777 281ER"
    },
    "862338": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "862338",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA62AN",
        "Type": "737NG 881/W"
    },
    "a4470e": {
        "ICAOTypeCode": "A332",
        "Manufacturer": "Airbus",
        "ModeS": "A4470E",
        "OperatorFlagCode": "HAL",
        "RegisteredOwners": "Hawaiian Airlines",
        "Registration": "N375HA",
        "Type": "A330 243"
    },
    "76cd0c": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "76CD0C",
        "OperatorFlagCode": "SIA",
        "RegisteredOwners": "Singapore Airlines",
        "Registration": "9V-SHL",
        "Type": "A350 941"
    },
    "84b3eb": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B3EB",
        "OperatorFlagCode": "APJ",
        "RegisteredOwners": "Peach Aviation",
        "Registration": "JA202P",
        "Type": "A320 251NSL"
    },
    "84b451": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B451",
        "OperatorFlagCode": "APJ",
        "RegisteredOwners": "Peach Aviation",
        "Registration": "JA205P",
        "Type": "A320 251NSL"
    },
    "86d5fa": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D5FA",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA824A",
        "Type": "787 8"
    },
    "8744f6": {
        "ICAOTypeCode": "B78X",
        "Manufacturer": "Boeing",
        "ModeS": "8744F6",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA982A",
        "Type": "787 10"
    },
    "406f74": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "406F74",
        "OperatorFlagCode": "BAW",
        "RegisteredOwners": "British Airways",
        "Registration": "G-ZBKH",
        "Type": "787 9"
    },
    "71c398": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "71C398",
        "OperatorFlagCode": "AAR",
        "RegisteredOwners": "Asiana Airlines",
        "Registration": "HL8398",
        "Type": "A321 251NXSL"
    },
    "3c4b35": {
        "ICAOTypeCode": "B748",
        "Manufacturer": "Boeing",
        "ModeS": "3C4B35",
        "OperatorFlagCode": "DLH",
        "RegisteredOwners": "Lufthansa",
        "Registration": "D-ABYU",
        "Type": "747 830"
    },
    "88516b": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "88516B",
        "OperatorFlagCode": "THA",
        "RegisteredOwners": "Thai Airways International",
        "Registration": "HS-TKK",
        "Type": "777 3ALER"
    },
    "4bb146": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "4BB146",
        "OperatorFlagCode": "THY",
        "RegisteredOwners": "Turkish Airlines",
        "Registration": "TC-LJF",
        "Type": "777 3F2ER"
    },
    "781464": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "781464",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-300R",
        "Type": "A320 251NSL"
    },
    "a4e714": {
        "ICAOTypeCode": "A339",
        "Manufacturer": "Airbus",
        "ModeS": "A4E714",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N415DX",
        "Type": "A330 941N"
    },
    "86d9b0": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D9B0",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA835A",
        "Type": "787 8"
    },
    "758404": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "758404",
        "OperatorFlagCode": "PAL",
        "RegisteredOwners": "Philippine Airlines",
        "Registration": "RP-C9929",
        "Type": "A321 231SL"
    },
    "86cfa0": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86CFA0",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA80AN",
        "Type": "737NG 881/W"
    },
    "4078dd": {
        "ICAOTypeCode": "A35K",
        "Manufacturer": "Airbus",
        "ModeS": "4078DD",
        "OperatorFlagCode": "BAW",
        "RegisteredOwners": "British Airways",
        "Registration": "G-XWBF",
        "Type": "A350 1041"
    },
    "a4c703": {
        "ICAOTypeCode": "A339",
        "Manufacturer": "Airbus",
        "ModeS": "A4C703",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N407DX",
        "Type": "A330 941N"
    },
    "781360": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "781360",
        "OperatorFlagCode": "CSN",
        "RegisteredOwners": "China Southern Airlines",
        "Registration": "B-1242",
        "Type": "787 9"
    },
    "850e14": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "850E14",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA305J",
        "Type": "737NG 846/W"
    },
    "885172": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "885172",
        "OperatorFlagCode": "THA",
        "RegisteredOwners": "Thai Airways International",
        "Registration": "HS-TKR",
        "Type": "777 3ALER"
    },
    "8990e7": {
        "ICAOTypeCode": "B78X",
        "Manufacturer": "Boeing",
        "ModeS": "8990E7",
        "OperatorFlagCode": "EVA",
        "RegisteredOwners": "EVA Air",
        "Registration": "B-17811",
        "Type": "787 10"
    },
    "780bd9": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "780BD9",
        "OperatorFlagCode": "CSN",
        "RegisteredOwners": "China Southern Airlines",
        "Registration": "B-5939",
        "Type": "A330 323X"
    },
    "8a07d3": {
        "ICAOTypeCode": "A339",
        "Manufacturer": "Airbus",
        "ModeS": "8A07D3",
        "OperatorFlagCode": "GIA",
        "RegisteredOwners": "Garuda Indonesia",
        "Registration": "PK-GHE",
        "Type": "A330 941N"
    },
    "758304": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "758304",
        "OperatorFlagCode": "PAL",
        "RegisteredOwners": "Philippine Airlines",
        "Registration": "RP-C9903",
        "Type": "A321 231SL"
    },
    "781947": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "781947",
        "OperatorFlagCode": "CSN",
        "RegisteredOwners": "China Southern Airlines",
        "Registration": "B-30F7",
        "Type": "A321 253NXSL"
    },
    "781a89": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "781A89",
        "OperatorFlagCode": "CSN",
        "RegisteredOwners": "China Southern Airlines",
        "Registration": "B-320Y",
        "Type": "A321 253NXSL"
    },
    "867fac": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "867FAC",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA733J",
        "Type": "777 346ER"
    },
    "8681b7": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681B7",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73NR",
        "Type": "737NG 8FH/W"
    },
    "8460b0": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "8460B0",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA11XJ",
        "Type": "A350 941"
    },
    "7808c8": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "7808C8",
        "OperatorFlagCode": "CCA",
        "RegisteredOwners": "Air China",
        "Registration": "B-5901",
        "Type": "A330 343E"
    },
    "8678c0": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "8678C0",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA715A",
        "Type": "777 281ER"
    },
    "71c258": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "71C258",
        "OperatorFlagCode": "AAR",
        "RegisteredOwners": "Asiana Airlines",
        "Registration": "HL8258",
        "Type": "A330 323E"
    },
    "a05646": {
        "ICAOTypeCode": "B78X",
        "Manufacturer": "Boeing",
        "ModeS": "A05646",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N12010",
        "Type": "787 10"
    },
    "885170": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "885170",
        "OperatorFlagCode": "THA",
        "RegisteredOwners": "Thai Airways International",
        "Registration": "HS-TKP",
        "Type": "777 3ALER"
    },
    "86d2fb": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "86D2FB",
        "OperatorFlagCode": "APJ",
        "RegisteredOwners": "Peach Aviation",
        "Registration": "JA818P",
        "Type": "A320 214"
    },
    "846866": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "846866",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA142A",
        "Type": "A321 272NSL"
    },
    "861e9a": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861E9A",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA612J",
        "Type": "767 346ER"
    },
    "873378": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "873378",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA935A",
        "Type": "787 9"
    },
    "84b7fa": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B7FA",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA216A",
        "Type": "A320 271NSL"
    },
    "71c557": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "71C557",
        "OperatorFlagCode": "KAL",
        "RegisteredOwners": "Korean Air",
        "Registration": "HL8557",
        "Type": "A321 272NXSL"
    },
    "85120e": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "85120E",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA318J",
        "Type": "737NG 846/W"
    },
    "8681ad": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681AD",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73NF",
        "Type": "737NG 86N/W"
    },
    "8681b4": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681B4",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73NN",
        "Type": "737NG 81D/W"
    },
    "851914": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851914",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA337J",
        "Type": "737NG 846/W"
    },
    "86cef4": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86CEF4",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA805A",
        "Type": "787 8"
    },
    "8691cc": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "8691CC",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA785A",
        "Type": "777 381ER"
    },
    "86dd2a": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86DD2A",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA844J",
        "Type": "787 8"
    },
    "a50adc": {
        "ICAOTypeCode": "A339",
        "Manufacturer": "Airbus",
        "ModeS": "A50ADC",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N424DX",
        "Type": "A330 941N"
    },
    "aa92fc": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "AA92FC",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N78005",
        "Type": "777 224ER"
    },
    "4ba949": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "4BA949",
        "OperatorFlagCode": "THY",
        "RegisteredOwners": "Turkish Airlines",
        "Registration": "TC-JJI",
        "Type": "777 3F2ER"
    },
    "8518f2": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8518F2",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA336J",
        "Type": "737NG 846/W"
    },
    "841e00": {
        "ICAOTypeCode": "B737",
        "Manufacturer": "Boeing",
        "ModeS": "841E00",
        "OperatorFlagCode": "ADO",
        "RegisteredOwners": "Air Do",
        "Registration": "JA08AN",
        "Type": "737NG 781/W"
    },
    "4aca64": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "4ACA64",
        "OperatorFlagCode": "SAS",
        "RegisteredOwners": "Scandinavian Airlines System",
        "Registration": "SE-RSD",
        "Type": "A350 941"
    },
    "780d1f": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "780D1F",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-1615",
        "Type": "A321 231SL"
    },
    "841538": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "841538",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA05XJ",
        "Type": "A350 941"
    },
    "789206": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "789206",
        "OperatorFlagCode": "HKE",
        "RegisteredOwners": "Hong Kong Express Airways",
        "Registration": "B-LEH",
        "Type": "A321 231SL"
    },
    "8406e8": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "8406E8",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA01XJ",
        "Type": "A350 941"
    },
    "8514d6": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8514D6",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA322J",
        "Type": "737NG 846/W"
    },
    "885178": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "885178",
        "OperatorFlagCode": "THA",
        "RegisteredOwners": "Thai Airways International",
        "Registration": "HS-TKX",
        "Type": "777 3D7ER"
    },
    "780de4": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "780DE4",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-1679",
        "Type": "A321 231SL"
    },
    "86803d": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86803D",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA737T",
        "Type": "737NG 8Q8/W"
    },
    "8991a8": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "8991A8",
        "OperatorFlagCode": "CAL",
        "RegisteredOwners": "China Airlines",
        "Registration": "B-18360",
        "Type": "A330 302"
    },
    "abfa24": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "ABFA24",
        "OperatorFlagCode": "AAL",
        "RegisteredOwners": "American Airlines",
        "Registration": "N871AY",
        "Type": "787 8"
    },
    "3965b2": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "3965B2",
        "OperatorFlagCode": "AFR",
        "RegisteredOwners": "Air France",
        "Registration": "F-GZNS",
        "Type": "777 328ER"
    },
    "780ab5": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "780AB5",
        "OperatorFlagCode": "HKE",
        "RegisteredOwners": "Hong Kong Express Airways",
        "Registration": "B-LEB",
        "Type": "A321 231SL"
    },
    "899059": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "899059",
        "OperatorFlagCode": "TTW",
        "RegisteredOwners": "Tigerair Taiwan",
        "Registration": "B-50023",
        "Type": "A320 271NSL"
    },
    "899029": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "899029",
        "OperatorFlagCode": "TTW",
        "RegisteredOwners": "Tigerair Taiwan",
        "Registration": "B-50011",
        "Type": "A320 232SL"
    },
    "86d607": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "86D607",
        "OperatorFlagCode": "APJ",
        "RegisteredOwners": "Peach Aviation",
        "Registration": "JA824P",
        "Type": "A320 214SL"
    },
    "873028": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "873028",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA927A",
        "Type": "787 9"
    },
    "84640c": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "84640C",
        "OperatorFlagCode": "JTA",
        "RegisteredOwners": "Japan TransOcean Air",
        "Registration": "JA12RK",
        "Type": "737NG 800/W"
    },
    "846f00": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "846F00",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA15XJ",
        "Type": "A350 941"
    },
    "781101": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "781101",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-7881",
        "Type": "777 300ER"
    },
    "845d88": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "845D88",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA111A",
        "Type": "A321 211SL"
    },
    "86803a": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86803A",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA737Q",
        "Type": "737NG 86N/W"
    },
    "8691aa": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "8691AA",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA784A",
        "Type": "777 381ER"
    },
    "a50e93": {
        "ICAOTypeCode": "A339",
        "Manufacturer": "Airbus",
        "ModeS": "A50E93",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N425DX",
        "Type": "A330 941N"
    },
    "86d6c8": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86D6C8",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA82AN",
        "Type": "737NG 881/W"
    },
    "aacc5b": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "AACC5B",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N795UA",
        "Type": "777 222ER"
    },
    "a1d8fd": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "A1D8FD",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N218UA",
        "Type": "777 222ER"
    },
    "851230": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851230",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA319J",
        "Type": "737NG 846/W"
    },
    "7813bd": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "7813BD",
        "OperatorFlagCode": "CSN",
        "RegisteredOwners": "China Southern Airlines",
        "Registration": "B-1297",
        "Type": "787 9"
    },
    "84b7a1": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B7A1",
        "OperatorFlagCode": "APJ",
        "RegisteredOwners": "Peach Aviation",
        "Registration": "JA213P",
        "Type": "A320 251NSL"
    },
    "86d59c": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D59C",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA821J",
        "Type": "787 8"
    },
    "84b7c3": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B7C3",
        "OperatorFlagCode": "APJ",
        "RegisteredOwners": "Peach Aviation",
        "Registration": "JA214P",
        "Type": "A320 251NSL"
    },
    "a641b6": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "A641B6",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N502DN",
        "Type": "A350 941"
    },
    "71c506": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "71C506",
        "OperatorFlagCode": "KAL",
        "RegisteredOwners": "Korean Air",
        "Registration": "HL8506",
        "Type": "A321 272NXSL"
    },
    "aae958": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "AAE958",
        "OperatorFlagCode": "AAL",
        "RegisteredOwners": "American Airlines",
        "Registration": "N802AN",
        "Type": "787 8"
    },
    "850e58": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "850E58",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA307J",
        "Type": "737NG 846/W"
    },
    "a07dcd": {
        "ICAOTypeCode": "B78X",
        "Manufacturer": "Boeing",
        "ModeS": "A07DCD",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N13018",
        "Type": "787 10"
    },
    "86e8ac": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86E8AC",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA87AN",
        "Type": "737NG 800/W"
    },
    "84b982": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "84B982",
        "OperatorFlagCode": "SFJ",
        "RegisteredOwners": "StarFlyer",
        "Registration": "JA21MC",
        "Type": "A320 214SL"
    },
    "8880f7": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "8880F7",
        "OperatorFlagCode": "HVN",
        "RegisteredOwners": "Vietnam Airlines",
        "Registration": "VN-A867",
        "Type": "787 9"
    },
    "86d68f": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "86D68F",
        "OperatorFlagCode": "APJ",
        "RegisteredOwners": "Peach Aviation",
        "Registration": "JA828P",
        "Type": "A320 214SL"
    },
    "85e27c": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "85E27C",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA59AN",
        "Type": "737NG 881/W"
    },
    "71c350": {
        "ICAOTypeCode": "B38M",
        "Manufacturer": "Boeing",
        "ModeS": "71C350",
        "OperatorFlagCode": "KAL",
        "RegisteredOwners": "Korean Air",
        "Registration": "HL8350",
        "Type": "737MAX 8"
    },
    "861ebc": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861EBC",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA613J",
        "Type": "767 346ER"
    },
    "86d94a": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D94A",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA832A",
        "Type": "787 8"
    },
    "861ed6": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861ED6",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA614A",
        "Type": "767 381ER"
    },
    "86efb0": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86EFB0",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA899A",
        "Type": "787 9"
    },
    "406d7b": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "406D7B",
        "OperatorFlagCode": "BAW",
        "RegisteredOwners": "British Airways",
        "Registration": "G-ZBKE",
        "Type": "787 9"
    },
    "8626cc": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8626CC",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA63AN",
        "Type": "737NG 881/W"
    },
    "861eb4": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861EB4",
        "OperatorFlagCode": "ADO",
        "RegisteredOwners": "Air Do",
        "Registration": "JA613A",
        "Type": "767 381ER"
    },
    "406f75": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "406F75",
        "OperatorFlagCode": "BAW",
        "RegisteredOwners": "British Airways",
        "Registration": "G-ZBKI",
        "Type": "787 9"
    },
    "845dee": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "845DEE",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA114A",
        "Type": "A321 211SL"
    },
    "86da1e": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86DA1E",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA838J",
        "Type": "787 8"
    },
    "845dcc": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "845DCC",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA113A",
        "Type": "A321 211SL"
    },
    "407cd2": {
        "ICAOTypeCode": "A35K",
        "Manufacturer": "Airbus",
        "ModeS": "407CD2",
        "OperatorFlagCode": "BAW",
        "RegisteredOwners": "British Airways",
        "Registration": "G-XWBM",
        "Type": "A350 1041"
    },
    "780daf": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "780DAF",
        "OperatorFlagCode": "CSN",
        "RegisteredOwners": "China Southern Airlines",
        "Registration": "B-5966",
        "Type": "A330 323E"
    },
    "851936": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851936",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA338J",
        "Type": "737NG 846/W"
    },
    "7813f9": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "7813F9",
        "OperatorFlagCode": "CSN",
        "RegisteredOwners": "China Southern Airlines",
        "Registration": "B-1128",
        "Type": "787 9"
    },
    "a05614": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "A05614",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N1200K",
        "Type": "767 332ER/W"
    },
    "780a63": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "780A63",
        "OperatorFlagCode": "CPA",
        "RegisteredOwners": "Cathay Pacific Airways",
        "Registration": "B-KQO",
        "Type": "777 367ER"
    },
    "86d1f3": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86D1F3",
        "OperatorFlagCode": "SNJ",
        "RegisteredOwners": "Solaseed Air",
        "Registration": "JA810X",
        "Type": "737NG 86N/W"
    },
    "a64cdb": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "A64CDB",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N505DN",
        "Type": "A350 941"
    },
    "86cf09": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86CF09",
        "OperatorFlagCode": "SNJ",
        "RegisteredOwners": "Solaseed Air",
        "Registration": "JA805X",
        "Type": "737NG 86N/W"
    },
    "4bb141": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "4BB141",
        "OperatorFlagCode": "THY",
        "RegisteredOwners": "Turkish Airlines",
        "Registration": "TC-LJA",
        "Type": "777 3F2ER"
    },
    "8675d8": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8675D8",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA70AN",
        "Type": "737NG 881/W"
    },
    "846250": {
        "ICAOTypeCode": "B737",
        "Manufacturer": "Boeing",
        "ModeS": "846250",
        "OperatorFlagCode": "ADO",
        "RegisteredOwners": "Air Do",
        "Registration": "JA12AN",
        "Type": "737NG 781/W"
    },
    "86d310": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D310",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA819A",
        "Type": "787 8"
    },
    "8414a9": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8414A9",
        "OperatorFlagCode": "JTA",
        "RegisteredOwners": "Japan TransOcean Air",
        "Registration": "JA05RK",
        "Type": "737NG 800/W"
    },
    "861ae4": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861AE4",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA601J",
        "Type": "767 346ER"
    },
    "8686ee": {
        "ICAOTypeCode": "B773",
        "Manufacturer": "Boeing",
        "ModeS": "8686EE",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA754A",
        "Type": "777 381"
    },
    "850e9c": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "850E9C",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA309J",
        "Type": "737NG 846/W"
    },
    "86ce81": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86CE81",
        "OperatorFlagCode": "SNJ",
        "RegisteredOwners": "Solaseed Air",
        "Registration": "JA801X",
        "Type": "737NG 81D/W"
    },
    "89909d": {
        "ICAOTypeCode": "B78X",
        "Manufacturer": "Boeing",
        "ModeS": "89909D",
        "OperatorFlagCode": "EVA",
        "RegisteredOwners": "EVA Air",
        "Registration": "B-17809",
        "Type": "787 10"
    },
    "71bf92": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "71BF92",
        "OperatorFlagCode": "AAR",
        "RegisteredOwners": "Asiana Airlines",
        "Registration": "HL7792",
        "Type": "A330 323E"
    },
    "885175": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "885175",
        "OperatorFlagCode": "THA",
        "RegisteredOwners": "Thai Airways International",
        "Registration": "HS-TKU",
        "Type": "777 3D7ER"
    },
    "394a06": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "394A06",
        "OperatorFlagCode": "AFR",
        "RegisteredOwners": "Air France",
        "Registration": "F-GSQG",
        "Type": "777 328ER"
    },
    "86e800": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E800",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA875A",
        "Type": "787 9"
    },
    "a05626": {
        "ICAOTypeCode": "B78X",
        "Manufacturer": "Boeing",
        "ModeS": "A05626",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N12003",
        "Type": "787 10"
    },
    "86da40": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86DA40",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA839J",
        "Type": "787 8"
    },
    "8638b0": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8638B0",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA68AN",
        "Type": "737NG 881/W"
    },
    "8880e0": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "8880E0",
        "OperatorFlagCode": "HVN",
        "RegisteredOwners": "Vietnam Airlines",
        "Registration": "VN-A862",
        "Type": "787 9"
    },
    "aa305f": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "AA305F",
        "OperatorFlagCode": "AAL",
        "RegisteredOwners": "American Airlines",
        "Registration": "N756AM",
        "Type": "777 223ER"
    },
    "71c531": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "71C531",
        "OperatorFlagCode": "KAL",
        "RegisteredOwners": "Korean Air",
        "Registration": "HL8531",
        "Type": "A321 272NXSL"
    },
    "861ba8": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861BA8",
        "OperatorFlagCode": "ADO",
        "RegisteredOwners": "Air Do",
        "Registration": "JA607A",
        "Type": "767 381ER"
    },
    "406d78": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "406D78",
        "OperatorFlagCode": "BAW",
        "RegisteredOwners": "British Airways",
        "Registration": "G-ZBKB",
        "Type": "787 9"
    },
    "4ba954": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "4BA954",
        "OperatorFlagCode": "THY",
        "RegisteredOwners": "Turkish Airlines",
        "Registration": "TC-JJT",
        "Type": "777 3F2ER"
    },
    "780bf9": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "780BF9",
        "OperatorFlagCode": "CCA",
        "RegisteredOwners": "Air China",
        "Registration": "B-5912",
        "Type": "A330 343E"
    },
    "71c533": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "71C533",
        "OperatorFlagCode": "AAR",
        "RegisteredOwners": "Asiana Airlines",
        "Registration": "HL8533",
        "Type": "A321 251NXSL"
    },
    "842292": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "842292",
        "OperatorFlagCode": "SFJ",
        "RegisteredOwners": "StarFlyer",
        "Registration": "JA09MC",
        "Type": "A320 214"
    },
    "71bf95": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "71BF95",
        "OperatorFlagCode": "AAR",
        "RegisteredOwners": "Asiana Airlines",
        "Registration": "HL7795",
        "Type": "A330 323E"
    },
    "780f3e": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "780F3E",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-7365",
        "Type": "777 39PER"
    },
    "8a026d": {
        "ICAOTypeCode": "A332",
        "Manufacturer": "Airbus",
        "ModeS": "8A026D",
        "OperatorFlagCode": "GIA",
        "RegisteredOwners": "Garuda Indonesia",
        "Registration": "PK-GPM",
        "Type": "A330 243"
    },
    "780d94": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "780D94",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-1640",
        "Type": "A321 231SL"
    },
    "86787c": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "86787C",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA713A",
        "Type": "777 281"
    },
    "868338": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "868338",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA743A",
        "Type": "777 281ER"
    },
    "86cf2b": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86CF2B",
        "OperatorFlagCode": "SNJ",
        "RegisteredOwners": "Solaseed Air",
        "Registration": "JA806X",
        "Type": "737NG 86N/W"
    },
    "78921d": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "78921D",
        "OperatorFlagCode": "HKE",
        "RegisteredOwners": "Hong Kong Express Airways",
        "Registration": "B-LEJ",
        "Type": "A321 231SL"
    },
    "781540": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "781540",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-303D",
        "Type": "A330 343E"
    },
    "862db6": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "862DB6",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA658J",
        "Type": "767 346ER"
    },
    "86d6a4": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D6A4",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA829A",
        "Type": "787 8"
    },
    "841ff4": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "841FF4",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA08XJ",
        "Type": "A350 941"
    },
    "a18284": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "A18284",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N197DN",
        "Type": "767 332ER/W"
    },
    "868038": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "868038",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA737N",
        "Type": "737NG 8HX"
    },
    "780ac1": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "780AC1",
        "OperatorFlagCode": "HKE",
        "RegisteredOwners": "Hong Kong Express Airways",
        "Registration": "B-LEC",
        "Type": "A321 231SL"
    },
    "851bba": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851BBA",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA340J",
        "Type": "737NG 846/W"
    },
    "86808a": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86808A",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73AC",
        "Type": "737NG 800/W"
    },
    "851cec": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851CEC",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA349J",
        "Type": "737NG 846/W"
    },
    "76cef2": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "76CEF2",
        "OperatorFlagCode": "SIA",
        "RegisteredOwners": "Singapore Airlines",
        "Registration": "9V-SWR",
        "Type": "777 312ER"
    },
    "850d8c": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "850D8C",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA301J",
        "Type": "737NG 846/W"
    },
    "88812b": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "88812B",
        "OperatorFlagCode": "HVN",
        "RegisteredOwners": "Vietnam Airlines",
        "Registration": "VN-A871",
        "Type": "787 9"
    },
    "780cc2": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "780CC2",
        "OperatorFlagCode": "DKH",
        "RegisteredOwners": "Juneyao Air",
        "Registration": "B-1857",
        "Type": "A321 211SL"
    },
    "71c530": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "71C530",
        "OperatorFlagCode": "KAL",
        "RegisteredOwners": "Korean Air",
        "Registration": "HL8530",
        "Type": "A321 272NXSL"
    },
    "869582": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "869582",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA796A",
        "Type": "777 300ER"
    },
    "851120": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851120",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA311J",
        "Type": "737NG 846/W"
    },
    "71c558": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "71C558",
        "OperatorFlagCode": "KAL",
        "RegisteredOwners": "Korean Air",
        "Registration": "HL8558",
        "Type": "A321 272NXSL"
    },
    "ab0d15": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "AB0D15",
        "OperatorFlagCode": "AAL",
        "RegisteredOwners": "American Airlines",
        "Registration": "N811AB",
        "Type": "787 8"
    },
    "86e4fc": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E4FC",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA869J",
        "Type": "787 9"
    },
    "aa944a": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "AA944A",
        "OperatorFlagCode": "AAL",
        "RegisteredOwners": "American Airlines",
        "Registration": "N781AN",
        "Type": "777 223ER"
    },
    "a4dfa6": {
        "ICAOTypeCode": "A339",
        "Manufacturer": "Airbus",
        "ModeS": "A4DFA6",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N413DX",
        "Type": "A330 941N"
    },
    "8518d0": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8518D0",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA335J",
        "Type": "737NG 846/W"
    },
    "86796c": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86796C",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA71AN",
        "Type": "737NG 881/W"
    },
    "89902b": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "89902B",
        "OperatorFlagCode": "TTW",
        "RegisteredOwners": "Tigerair Taiwan",
        "Registration": "B-50016",
        "Type": "A320 232SL"
    },
    "78175d": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "78175D",
        "OperatorFlagCode": "CQH",
        "RegisteredOwners": "Spring Airlines",
        "Registration": "B-30A3",
        "Type": "A320 251NSL"
    },
    "a0a522": {
        "ICAOTypeCode": "B78X",
        "Manufacturer": "Boeing",
        "ModeS": "A0A522",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N14001",
        "Type": "787 10"
    },
    "840e10": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "840E10",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA03XJ",
        "Type": "A350 941"
    },
    "86e430": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E430",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA863J",
        "Type": "787 9"
    },
    "86eb2e": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86EB2E",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA882A",
        "Type": "787 9"
    },
    "86d266": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D266",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA814A",
        "Type": "787 8"
    },
    "76cd13": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "76CD13",
        "OperatorFlagCode": "SIA",
        "RegisteredOwners": "Singapore Airlines",
        "Registration": "9V-SHS",
        "Type": "A350 941"
    },
    "861e4e": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861E4E",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA610A",
        "Type": "767 381ER"
    },
    "8681b0": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681B0",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73NJ",
        "Type": "737NG 86N/W"
    },
    "850df2": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "850DF2",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA304J",
        "Type": "737NG 846/W"
    },
    "7811fd": {
        "ICAOTypeCode": "A332",
        "Manufacturer": "Airbus",
        "ModeS": "7811FD",
        "OperatorFlagCode": "GCR",
        "RegisteredOwners": "Tianjin Airlines",
        "Registration": "B-8596",
        "Type": "A330 243"
    },
    "846ec8": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "846EC8",
        "OperatorFlagCode": "APJ",
        "RegisteredOwners": "Peach Aviation",
        "Registration": "JA15VA",
        "Type": "A320 214SL"
    },
    "a6657e": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "A6657E",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N511DN",
        "Type": "A350 941"
    },
    "86d2aa": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D2AA",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA816A",
        "Type": "787 8"
    },
    "7818ab": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "7818AB",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-30DR",
        "Type": "A320 251NSL"
    },
    "780db0": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "780DB0",
        "OperatorFlagCode": "CSN",
        "RegisteredOwners": "China Southern Airlines",
        "Registration": "B-5967",
        "Type": "A330 323E"
    },
    "851c86": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851C86",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA346J",
        "Type": "737NG 846/W"
    },
    "7800ff": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "7800FF",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-8971",
        "Type": "A330 343E"
    },
    "86e888": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E888",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA879A",
        "Type": "787 9"
    },
    "85d7c0": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "85D7C0",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA56AN",
        "Type": "737NG 881/W"
    },
    "851580": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851580",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA327J",
        "Type": "737NG 846/W"
    },
    "8991a9": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "8991A9",
        "OperatorFlagCode": "CAL",
        "RegisteredOwners": "China Airlines",
        "Registration": "B-18361",
        "Type": "A330 302"
    },
    "a410b3": {
        "ICAOTypeCode": "A332",
        "Manufacturer": "Airbus",
        "ModeS": "A410B3",
        "OperatorFlagCode": "HAL",
        "RegisteredOwners": "Hawaiian Airlines",
        "Registration": "N361HA",
        "Type": "A330 243"
    },
    "86cf5a": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86CF5A",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA808A",
        "Type": "787 8"
    },
    "84b7e5": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B7E5",
        "OperatorFlagCode": "APJ",
        "RegisteredOwners": "Peach Aviation",
        "Registration": "JA215P",
        "Type": "A320 251NSL"
    },
    "872fe4": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "872FE4",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA925A",
        "Type": "787 9"
    },
    "86803e": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86803E",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA737U",
        "Type": "737NG 8FZ/W"
    },
    "3965a1": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "3965A1",
        "OperatorFlagCode": "AFR",
        "RegisteredOwners": "Air France",
        "Registration": "F-GZNB",
        "Type": "777 328ER"
    },
    "86e890": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E890",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA879J",
        "Type": "787 9"
    },
    "781055": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "781055",
        "OperatorFlagCode": "DKH",
        "RegisteredOwners": "Juneyao Air",
        "Registration": "B-8457",
        "Type": "A321 231SL"
    },
    "84b81c": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B81C",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA217A",
        "Type": "A320 271NSL"
    },
    "862df4": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "862DF4",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA65AN",
        "Type": "737NG 881/W"
    },
    "8515a2": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8515A2",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA328J",
        "Type": "737NG 846/W"
    },
    "8682fc": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "8682FC",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA741J",
        "Type": "777 346ER"
    },
    "8681ae": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681AE",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73NG",
        "Type": "737NG 86N/W"
    },
    "86dd6e": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86DD6E",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA846J",
        "Type": "787 8"
    },
    "a64924": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "A64924",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N504DN",
        "Type": "A350 941"
    },
    "868688": {
        "ICAOTypeCode": "B773",
        "Manufacturer": "Boeing",
        "ModeS": "868688",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA751A",
        "Type": "777 381"
    },
    "a65bb7": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "A65BB7",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N509DN",
        "Type": "A350 941"
    },
    "aa441c": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "AA441C",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N76010",
        "Type": "777 224ER"
    },
    "86e7de": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86E7DE",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA874A",
        "Type": "787 8"
    },
    "76cd11": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "76CD11",
        "OperatorFlagCode": "SIA",
        "RegisteredOwners": "Singapore Airlines",
        "Registration": "9V-SHQ",
        "Type": "A350 941"
    },
    "84bd16": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "84BD16",
        "OperatorFlagCode": "SFJ",
        "RegisteredOwners": "StarFlyer",
        "Registration": "JA22MC",
        "Type": "A320 214SL"
    },
    "7809bd": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "7809BD",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-9903",
        "Type": "A321 231SL"
    },
    "861b28": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861B28",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA603J",
        "Type": "767 346ER"
    },
    "84b794": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B794",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA213A",
        "Type": "A320 271NSL"
    },
    "3c4b34": {
        "ICAOTypeCode": "B748",
        "Manufacturer": "Boeing",
        "ModeS": "3C4B34",
        "OperatorFlagCode": "DLH",
        "RegisteredOwners": "Lufthansa",
        "Registration": "D-ABYT",
        "Type": "747 830"
    },
    "aae1ea": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "AAE1EA",
        "OperatorFlagCode": "AAL",
        "RegisteredOwners": "American Airlines",
        "Registration": "N800AN",
        "Type": "787 8"
    },
    "850dae": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "850DAE",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA302J",
        "Type": "737NG 846/W"
    },
    "846021": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "846021",
        "OperatorFlagCode": "JTA",
        "RegisteredOwners": "Japan TransOcean Air",
        "Registration": "JA11RK",
        "Type": "737NG 800/W"
    },
    "3c4b21": {
        "ICAOTypeCode": "B748",
        "Manufacturer": "Boeing",
        "ModeS": "3C4B21",
        "OperatorFlagCode": "DLH",
        "RegisteredOwners": "Lufthansa",
        "Registration": "D-ABYA",
        "Type": "747 830"
    },
    "4ba94b": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "4BA94B",
        "OperatorFlagCode": "THY",
        "RegisteredOwners": "Turkish Airlines",
        "Registration": "TC-JJK",
        "Type": "777 3F2ER"
    },
    "8681b3": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681B3",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73NM",
        "Type": "737NG 81D/W"
    },
    "78063a": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "78063A",
        "OperatorFlagCode": "CCA",
        "RegisteredOwners": "Air China",
        "Registration": "B-6513",
        "Type": "A330 343E"
    },
    "868ee4": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "868EE4",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA77AN",
        "Type": "737NG 881/W"
    },
    "888158": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "888158",
        "OperatorFlagCode": "VJC",
        "RegisteredOwners": "VietJetAir",
        "Registration": "VN-A653",
        "Type": "A321 271NSL"
    },
    "a05629": {
        "ICAOTypeCode": "B78X",
        "Manufacturer": "Boeing",
        "ModeS": "A05629",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N12006",
        "Type": "787 10"
    },
    "863c44": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "863C44",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA69AN",
        "Type": "737NG 881/W"
    },
    "780639": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "780639",
        "OperatorFlagCode": "CCA",
        "RegisteredOwners": "Air China",
        "Registration": "B-6511",
        "Type": "A330 343E"
    },
    "861e78": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861E78",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA611J",
        "Type": "767 346ER"
    },
    "861b64": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861B64",
        "OperatorFlagCode": "ADO",
        "RegisteredOwners": "Air Do",
        "Registration": "JA605A",
        "Type": "767 381ER"
    },
    "86837c": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "86837C",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA745A",
        "Type": "777 281ER"
    },
    "86e822": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E822",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA876A",
        "Type": "787 9"
    },
    "a0f427": {
        "ICAOTypeCode": "B78X",
        "Manufacturer": "Boeing",
        "ModeS": "A0F427",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N16008",
        "Type": "787 10"
    },
    "872f7e": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "872F7E",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA922A",
        "Type": "787 9"
    },
    "86ced2": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86CED2",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA804A",
        "Type": "787 8"
    },
    "76cd0b": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "76CD0B",
        "OperatorFlagCode": "SIA",
        "RegisteredOwners": "Singapore Airlines",
        "Registration": "9V-SHK",
        "Type": "A350 941"
    },
    "781704": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "781704",
        "OperatorFlagCode": "CSN",
        "RegisteredOwners": "China Southern Airlines",
        "Registration": "B-20C6",
        "Type": "787 9"
    },
    "86e3ec": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E3EC",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA861J",
        "Type": "787 9"
    },
    "780ac6": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "780AC6",
        "OperatorFlagCode": "HKE",
        "RegisteredOwners": "Hong Kong Express Airways",
        "Registration": "B-LEF",
        "Type": "A321 231SL"
    },
    "781418": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "781418",
        "OperatorFlagCode": "CSH",
        "RegisteredOwners": "Shanghai Airlines",
        "Registration": "B-1113",
        "Type": "787 9"
    },
    "c0103e": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "C0103E",
        "OperatorFlagCode": "ACA",
        "RegisteredOwners": "Air Canada",
        "Registration": "C-FGDX",
        "Type": "787 9"
    },
    "840a64": {
        "ICAOTypeCode": "A35K",
        "Manufacturer": "Airbus",
        "ModeS": "840A64",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA02WJ",
        "Type": "A350 1041"
    },
    "89902d": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "89902D",
        "OperatorFlagCode": "TTW",
        "RegisteredOwners": "Tigerair Taiwan",
        "Registration": "B-50018",
        "Type": "A320 232SL"
    },
    "76cef3": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "76CEF3",
        "OperatorFlagCode": "SIA",
        "RegisteredOwners": "Singapore Airlines",
        "Registration": "9V-SWS",
        "Type": "777 312ER"
    },
    "8681bd": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681BD",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73NX",
        "Type": "737NG 86N/W"
    },
    "8964a8": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "8964A8",
        "OperatorFlagCode": "UAE",
        "RegisteredOwners": "Emirates Airline",
        "Registration": "A6-EQP",
        "Type": "777 300ER"
    },
    "781842": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "781842",
        "OperatorFlagCode": "CQH",
        "RegisteredOwners": "Spring Airlines",
        "Registration": "B-30CN",
        "Type": "A320 251NSL"
    },
    "88812a": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "88812A",
        "OperatorFlagCode": "HVN",
        "RegisteredOwners": "Vietnam Airlines",
        "Registration": "VN-A870",
        "Type": "787 9"
    },
    "7583e2": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "7583E2",
        "OperatorFlagCode": "PAL",
        "RegisteredOwners": "Philippine Airlines",
        "Registration": "RP-C9925",
        "Type": "A321 231SL"
    },
    "780c44": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "780C44",
        "OperatorFlagCode": "CCA",
        "RegisteredOwners": "Air China",
        "Registration": "B-5947",
        "Type": "A330 343E"
    },
    "ab2ad8": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "AB2AD8",
        "OperatorFlagCode": "AAL",
        "RegisteredOwners": "American Airlines",
        "Registration": "N819AN",
        "Type": "787 8"
    },
    "86d906": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86D906",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA830A",
        "Type": "787 9"
    },
    "86d5e0": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D5E0",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA823J",
        "Type": "787 8"
    },
    "86e7bc": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E7BC",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA873A",
        "Type": "787 9"
    },
    "a45233": {
        "ICAOTypeCode": "A332",
        "Manufacturer": "Airbus",
        "ModeS": "A45233",
        "OperatorFlagCode": "HAL",
        "RegisteredOwners": "Hawaiian Airlines",
        "Registration": "N378HA",
        "Type": "A330 243"
    },
    "861bec": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861BEC",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA609A",
        "Type": "767 381ER"
    },
    "a4fc00": {
        "ICAOTypeCode": "A339",
        "Manufacturer": "Airbus",
        "ModeS": "A4FC00",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N420DX",
        "Type": "A330 941N"
    },
    "86e86e": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E86E",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA878J",
        "Type": "787 9"
    },
    "86da38": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86DA38",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA839A",
        "Type": "787 9"
    },
    "862a60": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "862A60",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA64AN",
        "Type": "737NG 881/W"
    },
    "a0a545": {
        "ICAOTypeCode": "B78X",
        "Manufacturer": "Boeing",
        "ModeS": "A0A545",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N14011",
        "Type": "787 10"
    },
    "868b50": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "868B50",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA76AN",
        "Type": "737NG 881/W"
    },
    "780ac4": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "780AC4",
        "OperatorFlagCode": "HKE",
        "RegisteredOwners": "Hong Kong Express Airways",
        "Registration": "B-LED",
        "Type": "A321 231SL"
    },
    "a45fb1": {
        "ICAOTypeCode": "A332",
        "Manufacturer": "Airbus",
        "ModeS": "A45FB1",
        "OperatorFlagCode": "HAL",
        "RegisteredOwners": "Hawaiian Airlines",
        "Registration": "N381HA",
        "Type": "A330 243"
    },
    "868041": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "868041",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA737X",
        "Type": "737NG 8AL/W"
    },
    "394a08": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "394A08",
        "OperatorFlagCode": "AFR",
        "RegisteredOwners": "Air France",
        "Registration": "F-GSQI",
        "Type": "777 328ER"
    },
    "84b7d8": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B7D8",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA215A",
        "Type": "A320 271NSL"
    },
    "861bca": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861BCA",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA608A",
        "Type": "767 381ER"
    },
    "8695a4": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "8695A4",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA797A",
        "Type": "777 300ER"
    },
    "84b77f": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B77F",
        "OperatorFlagCode": "APJ",
        "RegisteredOwners": "Peach Aviation",
        "Registration": "JA212P",
        "Type": "A320 251NSL"
    },
    "86e75e": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E75E",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA870J",
        "Type": "787 9"
    },
    "780551": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "780551",
        "OperatorFlagCode": "CQH",
        "RegisteredOwners": "Spring Airlines",
        "Registration": "B-6561",
        "Type": "A320 214"
    },
    "86220c": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "86220C",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA621J",
        "Type": "767 346ER/W"
    },
    "863188": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "863188",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA66AN",
        "Type": "737NG 881/W"
    },
    "84b750": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B750",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA211A",
        "Type": "A320 271NSL"
    },
    "407798": {
        "ICAOTypeCode": "A35K",
        "Manufacturer": "Airbus",
        "ModeS": "407798",
        "OperatorFlagCode": "BAW",
        "RegisteredOwners": "British Airways",
        "Registration": "G-XWBB",
        "Type": "A350 1041"
    },
    "76cd04": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "76CD04",
        "OperatorFlagCode": "SIA",
        "RegisteredOwners": "Singapore Airlines",
        "Registration": "9V-SHD",
        "Type": "A350 941"
    },
    "75006f": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "75006F",
        "OperatorFlagCode": "XAX",
        "RegisteredOwners": "AirAsia X",
        "Registration": "9M-XXV",
        "Type": "A330 343E"
    },
    "86eb36": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86EB36",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA882J",
        "Type": "787 9"
    },
    "8681a8": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681A8",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73NA",
        "Type": "737NG 8HX/W"
    },
    "840df8": {
        "ICAOTypeCode": "A35K",
        "Manufacturer": "Airbus",
        "ModeS": "840DF8",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA03WJ",
        "Type": "A350 1041"
    },
    "862dd8": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "862DD8",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA659J",
        "Type": "767 346ER"
    },
    "86cf38": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86CF38",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA807A",
        "Type": "787 8"
    },
    "86d5b6": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D5B6",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA822A",
        "Type": "787 8"
    },
    "85cd04": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "85CD04",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA53AN",
        "Type": "737NG 881/W"
    },
    "8511ca": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8511CA",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA316J",
        "Type": "737NG 846/W"
    },
    "8686cc": {
        "ICAOTypeCode": "B773",
        "Manufacturer": "Boeing",
        "ModeS": "8686CC",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA753A",
        "Type": "777 381"
    },
    "862248": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "862248",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA623A",
        "Type": "767 381ER/W"
    },
    "846d0c": {
        "ICAOTypeCode": "B737",
        "Manufacturer": "Boeing",
        "ModeS": "846D0C",
        "OperatorFlagCode": "ADO",
        "RegisteredOwners": "Air Do",
        "Registration": "JA15AN",
        "Type": "737NG 781/W"
    },
    "4cad44": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "4CAD44",
        "OperatorFlagCode": "ITY",
        "RegisteredOwners": "Italia Trasporto Aereo",
        "Registration": "EI-IFA",
        "Type": "A350 941"
    },
    "86eaea": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86EAEA",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA880A",
        "Type": "787 9"
    },
    "841a6c": {
        "ICAOTypeCode": "B737",
        "Manufacturer": "Boeing",
        "ModeS": "841A6C",
        "OperatorFlagCode": "ADO",
        "RegisteredOwners": "Air Do",
        "Registration": "JA07AN",
        "Type": "737NG 781/W"
    },
    "8622ae": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "8622AE",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA626A",
        "Type": "767 381ER/W"
    },
    "c01074": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "C01074",
        "OperatorFlagCode": "ACA",
        "RegisteredOwners": "Air Canada",
        "Registration": "C-FGFZ",
        "Type": "787 9"
    },
    "a1fcc5": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "A1FCC5",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N227UA",
        "Type": "777 222ER"
    },
    "86cf16": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86CF16",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA806A",
        "Type": "787 8"
    },
    "888171": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "888171",
        "OperatorFlagCode": "VJC",
        "RegisteredOwners": "VietJetAir",
        "Registration": "VN-A525",
        "Type": "A321 271NXSL"
    },
    "8964a1": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "8964A1",
        "OperatorFlagCode": "UAE",
        "RegisteredOwners": "Emirates Airline",
        "Registration": "A6-EQI",
        "Type": "777 300ER"
    },
    "71c532": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "71C532",
        "OperatorFlagCode": "KAL",
        "RegisteredOwners": "Korean Air",
        "Registration": "HL8532",
        "Type": "A321 272NXSL"
    },
    "846b34": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "846B34",
        "OperatorFlagCode": "APJ",
        "RegisteredOwners": "Peach Aviation",
        "Registration": "JA14VA",
        "Type": "A320 214SL"
    },
    "86d222": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D222",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA812A",
        "Type": "787 8"
    },
    "8622d0": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "8622D0",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA627A",
        "Type": "767 381ER/W"
    },
    "a9d5df": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "A9D5DF",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N73270",
        "Type": "737NG 824/W"
    },
    "86226a": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "86226A",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA624A",
        "Type": "767 381ER/W"
    },
    "86dd90": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86DD90",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA847J",
        "Type": "787 8"
    },
    "7806de": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "7806DE",
        "OperatorFlagCode": "CCA",
        "RegisteredOwners": "Air China",
        "Registration": "B-6525",
        "Type": "A330 343E"
    },
    "406f78": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "406F78",
        "OperatorFlagCode": "BAW",
        "RegisteredOwners": "British Airways",
        "Registration": "G-ZBKL",
        "Type": "787 9"
    },
    "8964a4": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "8964A4",
        "OperatorFlagCode": "UAE",
        "RegisteredOwners": "Emirates Airline",
        "Registration": "A6-EQL",
        "Type": "777 300ER"
    },
    "86e518": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86E518",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA86AN",
        "Type": "737NG 881/W"
    },
    "ac0196": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "AC0196",
        "OperatorFlagCode": "AAL",
        "RegisteredOwners": "American Airlines",
        "Registration": "N873BB",
        "Type": "787 8"
    },
    "86ddd4": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86DDD4",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA849J",
        "Type": "787 8"
    },
    "86d2ee": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D2EE",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA818A",
        "Type": "787 8"
    },
    "872720": {
        "ICAOTypeCode": "B78X",
        "Manufacturer": "Boeing",
        "ModeS": "872720",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA900A",
        "Type": "787 10"
    },
    "845c8d": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "845C8D",
        "OperatorFlagCode": "JTA",
        "RegisteredOwners": "Japan TransOcean Air",
        "Registration": "JA10RK",
        "Type": "737NG 800/W"
    },
    "780ac5": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "780AC5",
        "OperatorFlagCode": "HKE",
        "RegisteredOwners": "Hong Kong Express Airways",
        "Registration": "B-LEE",
        "Type": "A321 231SL"
    },
    "8468aa": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "8468AA",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA144A",
        "Type": "A321 272NSL"
    },
    "85c970": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "85C970",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA52AN",
        "Type": "737NG 881/W"
    },
    "873006": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "873006",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA926A",
        "Type": "787 9"
    },
    "851142": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851142",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA312J",
        "Type": "737NG 846/W"
    },
    "84bac2": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84BAC2",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA220A",
        "Type": "A320 271NSL"
    },
    "7808a9": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "7808A9",
        "OperatorFlagCode": "CCA",
        "RegisteredOwners": "Air China",
        "Registration": "B-6503",
        "Type": "A330 343E"
    },
    "4cad49": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "4CAD49",
        "OperatorFlagCode": "ITY",
        "RegisteredOwners": "Italia Trasporto Aereo",
        "Registration": "EI-IFF",
        "Type": "A350 941"
    },
    "868056": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "868056",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA738J",
        "Type": "777 346ER"
    },
    "888139": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "888139",
        "OperatorFlagCode": "HVN",
        "RegisteredOwners": "Vietnam Airlines",
        "Registration": "VN-A894",
        "Type": "A350 941"
    },
    "758302": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "758302",
        "OperatorFlagCode": "PAL",
        "RegisteredOwners": "Philippine Airlines",
        "Registration": "RP-C9901",
        "Type": "A321 231SL"
    },
    "8694b6": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "8694B6",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA790A",
        "Type": "777 381ER"
    },
    "3965aa": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "3965AA",
        "OperatorFlagCode": "AFR",
        "RegisteredOwners": "Air France",
        "Registration": "F-GZNK",
        "Type": "777 328ER"
    },
    "4cad47": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "4CAD47",
        "OperatorFlagCode": "ITY",
        "RegisteredOwners": "Italia Trasporto Aereo",
        "Registration": "EI-IFD",
        "Type": "A350 941"
    },
    "86dce6": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86DCE6",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA842J",
        "Type": "787 8"
    },
    "781393": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "781393",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-1073",
        "Type": "A330 343E"
    },
    "846bb6": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "846BB6",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA150A",
        "Type": "A321 272NSL"
    },
    "780a18": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "780A18",
        "OperatorFlagCode": "CPA",
        "RegisteredOwners": "Cathay Pacific Airways",
        "Registration": "B-KPW",
        "Type": "777 367ER"
    },
    "86d6ac": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D6AC",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA829J",
        "Type": "787 8"
    },
    "867d00": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "867D00",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA72AN",
        "Type": "737NG 881/W"
    },
    "86d57f": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "86D57F",
        "OperatorFlagCode": "APJ",
        "RegisteredOwners": "Peach Aviation",
        "Registration": "JA820P",
        "Type": "A320 214"
    },
    "846b6c": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "846B6C",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA14XJ",
        "Type": "A350 941"
    },
    "867ff0": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "867FF0",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA735J",
        "Type": "777 346ER"
    },
    "8681aa": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681AA",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73NC",
        "Type": "737NG 8FZ/W"
    },
    "3c4b2f": {
        "ICAOTypeCode": "B748",
        "Manufacturer": "Boeing",
        "ModeS": "3C4B2F",
        "OperatorFlagCode": "DLH",
        "RegisteredOwners": "Lufthansa",
        "Registration": "D-ABYO",
        "Type": "747 830"
    },
    "86d9b8": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D9B8",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA835J",
        "Type": "787 8"
    },
    "3c6711": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "3C6711",
        "OperatorFlagCode": "DLH",
        "RegisteredOwners": "Lufthansa",
        "Registration": "D-AIXQ",
        "Type": "A350 941"
    },
    "780a2a": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "780A2A",
        "OperatorFlagCode": "CPA",
        "RegisteredOwners": "Cathay Pacific Airways",
        "Registration": "B-KPY",
        "Type": "777 367ER"
    },
    "782001": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "782001",
        "OperatorFlagCode": "CSN",
        "RegisteredOwners": "China Southern Airlines",
        "Registration": "B-32FS",
        "Type": "A321 253NXSL"
    },
    "a519b8": {
        "ICAOTypeCode": "A339",
        "Manufacturer": "Airbus",
        "ModeS": "A519B8",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N428DX",
        "Type": "A330 941N"
    },
    "868042": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "868042",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA737Y",
        "Type": "737NG 8FZ/W"
    },
    "780a62": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "780A62",
        "OperatorFlagCode": "CPA",
        "RegisteredOwners": "Cathay Pacific Airways",
        "Registration": "B-KQN",
        "Type": "777 367ER"
    },
    "86cee7": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86CEE7",
        "OperatorFlagCode": "SNJ",
        "RegisteredOwners": "Solaseed Air",
        "Registration": "JA804X",
        "Type": "737NG 86N/W"
    },
    "840a7c": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "840A7C",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA02XJ",
        "Type": "A350 941"
    },
    "86d98e": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D98E",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA834A",
        "Type": "787 8"
    },
    "86d9fc": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D9FC",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA837J",
        "Type": "787 8"
    },
    "84c43e": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "84C43E",
        "OperatorFlagCode": "SFJ",
        "RegisteredOwners": "StarFlyer",
        "Registration": "JA24MC",
        "Type": "A320 214SL"
    },
    "7817a2": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "7817A2",
        "OperatorFlagCode": "CSH",
        "RegisteredOwners": "Shanghai Airlines",
        "Registration": "B-20D8",
        "Type": "787 9"
    },
    "86d952": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D952",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA832J",
        "Type": "787 8"
    },
    "86ef4a": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86EF4A",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA896A",
        "Type": "787 9"
    },
    "8733bc": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "8733BC",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA937A",
        "Type": "787 9"
    },
    "7cad41": {
        "ICAOTypeCode": "B38M",
        "Manufacturer": "Boeing",
        "ModeS": "7CAD41",
        "OperatorFlagCode": "VOZ",
        "RegisteredOwners": "Virgin Australia",
        "Registration": "VH-8IB",
        "Type": "737MAX 8"
    },
    "867f68": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "867F68",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA731J",
        "Type": "777 346ER"
    },
    "85d42c": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "85D42C",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA55AN",
        "Type": "737NG 881/W"
    },
    "8681be": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681BE",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73NY",
        "Type": "737NG 86N/W"
    },
    "86dcc4": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86DCC4",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA841J",
        "Type": "787 8"
    },
    "86cea3": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86CEA3",
        "OperatorFlagCode": "SNJ",
        "RegisteredOwners": "Solaseed Air",
        "Registration": "JA802X",
        "Type": "737NG 81D/W"
    },
    "781946": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "781946",
        "OperatorFlagCode": "CSN",
        "RegisteredOwners": "China Southern Airlines",
        "Registration": "B-30F6",
        "Type": "A321 253NXSL"
    },
    "84c7d2": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "84C7D2",
        "OperatorFlagCode": "SFJ",
        "RegisteredOwners": "StarFlyer",
        "Registration": "JA25MC",
        "Type": "A320 214SL"
    },
    "87339a": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "87339A",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA936A",
        "Type": "787 9"
    },
    "87453a": {
        "ICAOTypeCode": "B78X",
        "Manufacturer": "Boeing",
        "ModeS": "87453A",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA984A",
        "Type": "787 10"
    },
    "780a3b": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "780A3B",
        "OperatorFlagCode": "CPA",
        "RegisteredOwners": "Cathay Pacific Airways",
        "Registration": "B-KQI",
        "Type": "777 367ER"
    },
    "ac1df7": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "AC1DF7",
        "OperatorFlagCode": "AAL",
        "RegisteredOwners": "American Airlines",
        "Registration": "N880BJ",
        "Type": "787 8"
    },
    "76cd0a": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "76CD0A",
        "OperatorFlagCode": "SIA",
        "RegisteredOwners": "Singapore Airlines",
        "Registration": "9V-SHJ",
        "Type": "A350 941"
    },
    "780a3c": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "780A3C",
        "OperatorFlagCode": "CPA",
        "RegisteredOwners": "Cathay Pacific Airways",
        "Registration": "B-KQJ",
        "Type": "777 367ER"
    },
    "a4ce71": {
        "ICAOTypeCode": "A339",
        "Manufacturer": "Airbus",
        "ModeS": "A4CE71",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N409DX",
        "Type": "A330 941N"
    },
    "781717": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "781717",
        "OperatorFlagCode": "CSH",
        "RegisteredOwners": "Shanghai Airlines",
        "Registration": "B-20CD",
        "Type": "787 9"
    },
    "86d61c": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D61C",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA825A",
        "Type": "787 8"
    },
    "3c670b": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "3C670B",
        "OperatorFlagCode": "DLH",
        "RegisteredOwners": "Lufthansa",
        "Registration": "D-AIXK",
        "Type": "A350 941"
    },
    "780db1": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "780DB1",
        "OperatorFlagCode": "CSN",
        "RegisteredOwners": "China Southern Airlines",
        "Registration": "B-5970",
        "Type": "A330 323E"
    },
    "86e184": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86E184",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA85AN",
        "Type": "737NG 881/W"
    },
    "872766": {
        "ICAOTypeCode": "B78X",
        "Manufacturer": "Boeing",
        "ModeS": "872766",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA902A",
        "Type": "787 10"
    },
    "86efd4": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86EFD4",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA89AN",
        "Type": "737NG 800/W"
    },
    "461f56": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "461F56",
        "OperatorFlagCode": "FIN",
        "RegisteredOwners": "Finnair",
        "Registration": "OH-LWO",
        "Type": "A350 941"
    },
    "86eb72": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86EB72",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA884A",
        "Type": "787 9"
    },
    "868078": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "868078",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA739J",
        "Type": "777 346ER"
    },
    "86d96c": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86D96C",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA833A",
        "Type": "787 9"
    },
    "86e808": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E808",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA875J",
        "Type": "787 9"
    },
    "861c10": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "861C10",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA60AN",
        "Type": "737NG 881/W"
    },
    "71c528": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "71C528",
        "OperatorFlagCode": "KAL",
        "RegisteredOwners": "Korean Air",
        "Registration": "HL8528",
        "Type": "A321 272NXSL"
    },
    "750338": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "750338",
        "OperatorFlagCode": "XAX",
        "RegisteredOwners": "AirAsia X",
        "Registration": "9M-XXR",
        "Type": "A330 343X"
    },
    "861e70": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861E70",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA611A",
        "Type": "767 381ER"
    },
    "a661c7": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "A661C7",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N510DN",
        "Type": "A350 941"
    },
    "850e7a": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "850E7A",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA308J",
        "Type": "737NG 846/W"
    },
    "840d81": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "840D81",
        "OperatorFlagCode": "JTA",
        "RegisteredOwners": "Japan TransOcean Air",
        "Registration": "JA03RK",
        "Type": "737NG 800/W"
    },
    "86dc9a": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86DC9A",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA840A",
        "Type": "787 8"
    },
    "aa9093": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "AA9093",
        "OperatorFlagCode": "AAL",
        "RegisteredOwners": "American Airlines",
        "Registration": "N780AN",
        "Type": "777 223ER"
    },
    "394a00": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "394A00",
        "OperatorFlagCode": "AFR",
        "RegisteredOwners": "Air France",
        "Registration": "F-GSQA",
        "Type": "777 328ER"
    },
    "846888": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "846888",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA143A",
        "Type": "A321 272NSL"
    },
    "76cd08": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "76CD08",
        "OperatorFlagCode": "SIA",
        "RegisteredOwners": "Singapore Airlines",
        "Registration": "9V-SHH",
        "Type": "A350 941"
    },
    "86d594": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D594",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA821A",
        "Type": "787 8"
    },
    "8964a6": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "8964A6",
        "OperatorFlagCode": "UAE",
        "RegisteredOwners": "Emirates Airline",
        "Registration": "A6-EQN",
        "Type": "777 300ER"
    },
    "86d215": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86D215",
        "OperatorFlagCode": "SNJ",
        "RegisteredOwners": "Solaseed Air",
        "Registration": "JA811X",
        "Type": "737NG 86N/W"
    },
    "86d90e": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D90E",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA830J",
        "Type": "787 8"
    },
    "780a17": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "780A17",
        "OperatorFlagCode": "CPA",
        "RegisteredOwners": "Cathay Pacific Airways",
        "Registration": "B-KPV",
        "Type": "777 367ER"
    },
    "76cd03": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "76CD03",
        "OperatorFlagCode": "SIA",
        "RegisteredOwners": "Singapore Airlines",
        "Registration": "9V-SHC",
        "Type": "A350 941"
    },
    "781392": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "781392",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-1066",
        "Type": "A330 343E"
    },
    "4076e8": {
        "ICAOTypeCode": "A35K",
        "Manufacturer": "Airbus",
        "ModeS": "4076E8",
        "OperatorFlagCode": "BAW",
        "RegisteredOwners": "British Airways",
        "Registration": "G-XWBA",
        "Type": "A350 1041"
    },
    "86ce8e": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86CE8E",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA802A",
        "Type": "787 8"
    },
    "c038a7": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "C038A7",
        "OperatorFlagCode": "ACA",
        "RegisteredOwners": "Air Canada",
        "Registration": "C-FVLU",
        "Type": "787 9"
    },
    "7c5320": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "7C5320",
        "OperatorFlagCode": "QFA",
        "RegisteredOwners": "Qantas",
        "Registration": "VH-QPE",
        "Type": "A330 303"
    },
    "86228c": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "86228C",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA625A",
        "Type": "767 381ER/W"
    },
    "867fce": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "867FCE",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA734J",
        "Type": "777 346ER"
    },
    "851c20": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851C20",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA343J",
        "Type": "737NG 846/W"
    },
    "780f3a": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "780F3A",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-7347",
        "Type": "777 39PER"
    },
    "85188c": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "85188C",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA333J",
        "Type": "737NG 846/W"
    },
    "407944": {
        "ICAOTypeCode": "A35K",
        "Manufacturer": "Airbus",
        "ModeS": "407944",
        "OperatorFlagCode": "BAW",
        "RegisteredOwners": "British Airways",
        "Registration": "G-XWBH",
        "Type": "A350 1041"
    },
    "76ceec": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "76CEEC",
        "OperatorFlagCode": "SIA",
        "RegisteredOwners": "Singapore Airlines",
        "Registration": "9V-SWL",
        "Type": "777 312ER"
    },
    "861e92": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861E92",
        "OperatorFlagCode": "ADO",
        "RegisteredOwners": "Air Do",
        "Registration": "JA612A",
        "Type": "767 381ER"
    },
    "862d50": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "862D50",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA655J",
        "Type": "767 346ER"
    },
    "851bfe": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851BFE",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA342J",
        "Type": "737NG 846/W"
    },
    "394a0c": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "394A0C",
        "OperatorFlagCode": "AFR",
        "RegisteredOwners": "Air France",
        "Registration": "F-GSQM",
        "Type": "777 328ER"
    },
    "8681b6": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681B6",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73NQ",
        "Type": "737NG 81D/W"
    },
    "a4ee82": {
        "ICAOTypeCode": "A339",
        "Manufacturer": "Airbus",
        "ModeS": "A4EE82",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N417DX",
        "Type": "A330 941N"
    },
    "8881ab": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "8881AB",
        "OperatorFlagCode": "VJC",
        "RegisteredOwners": "VietJetAir",
        "Registration": "VN-A523",
        "Type": "A321 271NXSL"
    },
    "86835a": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "86835A",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA744A",
        "Type": "777 281ER"
    },
    "851492": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851492",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA320J",
        "Type": "737NG 846/W"
    },
    "3c6704": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "3C6704",
        "OperatorFlagCode": "DLH",
        "RegisteredOwners": "Lufthansa",
        "Registration": "D-AIXD",
        "Type": "A350 941"
    },
    "84b4b7": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B4B7",
        "OperatorFlagCode": "APJ",
        "RegisteredOwners": "Peach Aviation",
        "Registration": "JA208P",
        "Type": "A320 251NSL"
    },
    "861e56": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861E56",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA610J",
        "Type": "767 346ER"
    },
    "86ef06": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86EF06",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA894A",
        "Type": "787 9"
    },
    "86ef28": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86EF28",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA895A",
        "Type": "787 9"
    },
    "8681ac": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681AC",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73NE",
        "Type": "737NG 82Y/W"
    },
    "88517a": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "88517A",
        "OperatorFlagCode": "THA",
        "RegisteredOwners": "Thai Airways International",
        "Registration": "HS-TKZ",
        "Type": "777 3D7ER"
    },
    "a4c34c": {
        "ICAOTypeCode": "A339",
        "Manufacturer": "Airbus",
        "ModeS": "A4C34C",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N406DX",
        "Type": "A330 941N"
    },
    "86222e": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "86222E",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA622J",
        "Type": "767 346ER"
    },
    "84b83e": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B83E",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA218A",
        "Type": "A320 271NSL"
    },
    "aa37ce": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "AA37CE",
        "OperatorFlagCode": "AAL",
        "RegisteredOwners": "American Airlines",
        "Registration": "N758AN",
        "Type": "777 223ER"
    },
    "a1f90e": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "A1F90E",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N226UA",
        "Type": "777 222ER"
    },
    "8681ba": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681BA",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73NU",
        "Type": "737NG 86N/W"
    },
    "394a03": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "394A03",
        "OperatorFlagCode": "AFR",
        "RegisteredOwners": "Air France",
        "Registration": "F-GSQD",
        "Type": "777 328ER"
    },
    "841b6a": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "841B6A",
        "OperatorFlagCode": "SFJ",
        "RegisteredOwners": "StarFlyer",
        "Registration": "JA07MC",
        "Type": "A320 214"
    },
    "851826": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851826",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA330J",
        "Type": "737NG 846/W"
    },
    "862d72": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "862D72",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA656J",
        "Type": "767 346ER"
    },
    "71c582": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "71C582",
        "OperatorFlagCode": "AAR",
        "RegisteredOwners": "Asiana Airlines",
        "Registration": "HL8582",
        "Type": "A321 251NXSL"
    },
    "461f4f": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "461F4F",
        "OperatorFlagCode": "FIN",
        "RegisteredOwners": "Finnair",
        "Registration": "OH-LWH",
        "Type": "A350 941"
    },
    "75856d": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "75856D",
        "OperatorFlagCode": "PAL",
        "RegisteredOwners": "Philippine Airlines",
        "Registration": "RP-C9935",
        "Type": "A321 271NSL"
    },
    "a9f502": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "A9F502",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N74007",
        "Type": "777 224ER"
    },
    "851186": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851186",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA314J",
        "Type": "737NG 846/W"
    },
    "8681b2": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681B2",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73NL",
        "Type": "737NG 8HX/W"
    },
    "861ede": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861EDE",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA614J",
        "Type": "767 346ER"
    },
    "86cf91": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86CF91",
        "OperatorFlagCode": "SNJ",
        "RegisteredOwners": "Solaseed Air",
        "Registration": "JA809X",
        "Type": "737NG 86N/W"
    },
    "4aca65": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "4ACA65",
        "OperatorFlagCode": "SAS",
        "RegisteredOwners": "Scandinavian Airlines System",
        "Registration": "SE-RSE",
        "Type": "A350 941"
    },
    "868043": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "868043",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA737Z",
        "Type": "737NG 82Y/W"
    },
    "7809a6": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "7809A6",
        "OperatorFlagCode": "CCA",
        "RegisteredOwners": "Air China",
        "Registration": "B-5919",
        "Type": "A330 343E"
    },
    "7c531d": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "7C531D",
        "OperatorFlagCode": "QFA",
        "RegisteredOwners": "Qantas",
        "Registration": "VH-QPB",
        "Type": "A330 303"
    },
    "406f76": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "406F76",
        "OperatorFlagCode": "BAW",
        "RegisteredOwners": "British Airways",
        "Registration": "G-ZBKJ",
        "Type": "787 9"
    },
    "868034": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "868034",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA737J",
        "Type": "777 346ER"
    },
    "86953e": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "86953E",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA794A",
        "Type": "777 300ER"
    },
    "8470a0": {
        "ICAOTypeCode": "B737",
        "Manufacturer": "Boeing",
        "ModeS": "8470A0",
        "OperatorFlagCode": "ADO",
        "RegisteredOwners": "Air Do",
        "Registration": "JA16AN",
        "Type": "737NG 781/W"
    },
    "8744d4": {
        "ICAOTypeCode": "B78X",
        "Manufacturer": "Boeing",
        "ModeS": "8744D4",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA981A",
        "Type": "787 10"
    },
    "86d237": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86D237",
        "OperatorFlagCode": "SNJ",
        "RegisteredOwners": "Solaseed Air",
        "Registration": "JA812X",
        "Type": "737NG 86N/W"
    },
    "84b75d": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B75D",
        "OperatorFlagCode": "APJ",
        "RegisteredOwners": "Peach Aviation",
        "Registration": "JA211P",
        "Type": "A320 251NSL"
    },
    "7810fb": {
        "ICAOTypeCode": "A332",
        "Manufacturer": "Airbus",
        "ModeS": "7810FB",
        "OperatorFlagCode": "GCR",
        "RegisteredOwners": "Tianjin Airlines",
        "Registration": "B-8959",
        "Type": "A330 243"
    },
    "4cad46": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "4CAD46",
        "OperatorFlagCode": "ITY",
        "RegisteredOwners": "Italia Trasporto Aereo",
        "Registration": "EI-IFC",
        "Type": "A350 941"
    },
    "8695c6": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "8695C6",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA798A",
        "Type": "777 300ER"
    },
    "84b807": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B807",
        "OperatorFlagCode": "APJ",
        "RegisteredOwners": "Peach Aviation",
        "Registration": "JA216P",
        "Type": "A320 251NSL"
    },
    "84d28e": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84D28E",
        "OperatorFlagCode": "SFJ",
        "RegisteredOwners": "StarFlyer",
        "Registration": "JA28MC",
        "Type": "A320 251NSL"
    },
    "861f3c": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861F3C",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA617A",
        "Type": "767 381ER"
    },
    "84b860": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B860",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA219A",
        "Type": "A320 271NSL"
    },
    "885171": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "885171",
        "OperatorFlagCode": "THA",
        "RegisteredOwners": "Thai Airways International",
        "Registration": "HS-TKQ",
        "Type": "777 3ALER"
    },
    "a4caba": {
        "ICAOTypeCode": "A339",
        "Manufacturer": "Airbus",
        "ModeS": "A4CABA",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N408DX",
        "Type": "A330 941N"
    },
    "aa73b9": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "AA73B9",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N77261",
        "Type": "737NG 824/W"
    },
    "86d334": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86D334",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA81AN",
        "Type": "737NG 881/W"
    },
    "86ef6c": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86EF6C",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA897A",
        "Type": "787 9"
    },
    "71c511": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "71C511",
        "OperatorFlagCode": "AAR",
        "RegisteredOwners": "Asiana Airlines",
        "Registration": "HL8511",
        "Type": "A321 251NXSL"
    },
    "867f8a": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "867F8A",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA732J",
        "Type": "777 346ER"
    },
    "899026": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "899026",
        "OperatorFlagCode": "TTW",
        "RegisteredOwners": "Tigerair Taiwan",
        "Registration": "B-50006",
        "Type": "A320 232SL"
    },
    "861bb0": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861BB0",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA607J",
        "Type": "767 346ER/W"
    },
    "a4b827": {
        "ICAOTypeCode": "A339",
        "Manufacturer": "Airbus",
        "ModeS": "A4B827",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N403DX",
        "Type": "A330 941N"
    },
    "846978": {
        "ICAOTypeCode": "B737",
        "Manufacturer": "Boeing",
        "ModeS": "846978",
        "OperatorFlagCode": "ADO",
        "RegisteredOwners": "Air Do",
        "Registration": "JA14AN",
        "Type": "737NG 781/W"
    },
    "84bb06": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84BB06",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA222A",
        "Type": "A320 271NSL"
    },
    "8409ed": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8409ED",
        "OperatorFlagCode": "JTA",
        "RegisteredOwners": "Japan TransOcean Air",
        "Registration": "JA02RK",
        "Type": "737NG 8Q3/W"
    },
    "86ddb2": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86DDB2",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA848J",
        "Type": "787 8"
    },
    "86e84c": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E84C",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA877J",
        "Type": "787 9"
    },
    "461f54": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "461F54",
        "OperatorFlagCode": "FIN",
        "RegisteredOwners": "Finnair",
        "Registration": "OH-LWM",
        "Type": "A350 941"
    },
    "4ba947": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "4BA947",
        "OperatorFlagCode": "THY",
        "RegisteredOwners": "Turkish Airlines",
        "Registration": "TC-JJG",
        "Type": "777 3F2ER"
    },
    "a4f239": {
        "ICAOTypeCode": "A339",
        "Manufacturer": "Airbus",
        "ModeS": "A4F239",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N418DX",
        "Type": "A330 941N"
    },
    "4cad48": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "4CAD48",
        "OperatorFlagCode": "ITY",
        "RegisteredOwners": "Italia Trasporto Aereo",
        "Registration": "EI-IFE",
        "Type": "A350 941"
    },
    "86dca2": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86DCA2",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA840J",
        "Type": "787 8"
    },
    "86e778": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E778",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA871A",
        "Type": "787 9"
    },
    "c01040": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "C01040",
        "OperatorFlagCode": "ACA",
        "RegisteredOwners": "Air Canada",
        "Registration": "C-FGDZ",
        "Type": "787 9"
    },
    "780a2b": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "780A2B",
        "OperatorFlagCode": "CPA",
        "RegisteredOwners": "Cathay Pacific Airways",
        "Registration": "B-KPZ",
        "Type": "777 367ER"
    },
    "aa6914": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "AA6914",
        "OperatorFlagCode": "AAL",
        "RegisteredOwners": "American Airlines",
        "Registration": "N770AN",
        "Type": "777 223ER"
    },
    "851c64": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851C64",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA345J",
        "Type": "737NG 846/W"
    },
    "851bdc": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851BDC",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA341J",
        "Type": "737NG 846/W"
    },
    "8682da": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "8682DA",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA740J",
        "Type": "777 346ER"
    },
    "a4960c": {
        "ICAOTypeCode": "A332",
        "Manufacturer": "Airbus",
        "ModeS": "A4960C",
        "OperatorFlagCode": "HAL",
        "RegisteredOwners": "Hawaiian Airlines",
        "Registration": "N395HA",
        "Type": "A330 243"
    },
    "8411a4": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "8411A4",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA04XJ",
        "Type": "A350 941"
    },
    "874518": {
        "ICAOTypeCode": "B78X",
        "Manufacturer": "Boeing",
        "ModeS": "874518",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA983A",
        "Type": "787 10"
    },
    "885179": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "885179",
        "OperatorFlagCode": "THA",
        "RegisteredOwners": "Thai Airways International",
        "Registration": "HS-TKY",
        "Type": "777 3D7ER"
    },
    "8681b1": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681B1",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73NK",
        "Type": "737NG 86N/W"
    },
    "a4bf95": {
        "ICAOTypeCode": "A339",
        "Manufacturer": "Airbus",
        "ModeS": "A4BF95",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N405DX",
        "Type": "A330 941N"
    },
    "869210": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "869210",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA787A",
        "Type": "777 381ER"
    },
    "780dfe": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "780DFE",
        "OperatorFlagCode": "CCA",
        "RegisteredOwners": "Air China",
        "Registration": "B-6102",
        "Type": "A330 343E"
    },
    "86351c": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86351C",
        "OperatorFlagCode": "SNJ",
        "RegisteredOwners": "Solaseed Air",
        "Registration": "JA67AN",
        "Type": "737NG 881/W"
    },
    "8880df": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "8880DF",
        "OperatorFlagCode": "HVN",
        "RegisteredOwners": "Vietnam Airlines",
        "Registration": "VN-A861",
        "Type": "787 9"
    },
    "8681b5": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681B5",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73NP",
        "Type": "737NG 8HX/W"
    },
    "aace5c": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "AACE5C",
        "OperatorFlagCode": "AAL",
        "RegisteredOwners": "American Airlines",
        "Registration": "N796AN",
        "Type": "777 223ER"
    },
    "84cb66": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "84CB66",
        "OperatorFlagCode": "SFJ",
        "RegisteredOwners": "StarFlyer",
        "Registration": "JA26MC",
        "Type": "A320 214SL"
    },
    "780d9c": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "780D9C",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-2020",
        "Type": "777 39PER"
    },
    "86cf4d": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86CF4D",
        "OperatorFlagCode": "SNJ",
        "RegisteredOwners": "Solaseed Air",
        "Registration": "JA807X",
        "Type": "737NG 81D/W"
    },
    "3c670f": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "3C670F",
        "OperatorFlagCode": "DLH",
        "RegisteredOwners": "Lufthansa",
        "Registration": "D-AIXO",
        "Type": "A350 941"
    },
    "86d244": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D244",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA813A",
        "Type": "787 8"
    },
    "84b5ee": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "84B5EE",
        "OperatorFlagCode": "SFJ",
        "RegisteredOwners": "StarFlyer",
        "Registration": "JA20MC",
        "Type": "A320 214SL"
    },
    "84cefa": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "84CEFA",
        "OperatorFlagCode": "SFJ",
        "RegisteredOwners": "StarFlyer",
        "Registration": "JA27MC",
        "Type": "A320 214SL"
    },
    "8964a3": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "8964A3",
        "OperatorFlagCode": "UAE",
        "RegisteredOwners": "Emirates Airline",
        "Registration": "A6-EQK",
        "Type": "777 300ER"
    },
    "86e7e6": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E7E6",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA874J",
        "Type": "787 9"
    },
    "7501fa": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "7501FA",
        "OperatorFlagCode": "XAX",
        "RegisteredOwners": "AirAsia X",
        "Registration": "9M-XXG",
        "Type": "A330 343E"
    },
    "4aca63": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "4ACA63",
        "OperatorFlagCode": "SAS",
        "RegisteredOwners": "Scandinavian Airlines System",
        "Registration": "SE-RSC",
        "Type": "A350 941"
    },
    "780f44": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "780F44",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-8406",
        "Type": "A321 211SL"
    },
    "750525": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "750525",
        "OperatorFlagCode": "XAX",
        "RegisteredOwners": "AirAsia X",
        "Registration": "9M-XXJ",
        "Type": "A330 343E"
    },
    "789207": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "789207",
        "OperatorFlagCode": "HKE",
        "RegisteredOwners": "Hong Kong Express Airways",
        "Registration": "B-LEI",
        "Type": "A321 231SL"
    },
    "873334": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "873334",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA933A",
        "Type": "787 9"
    },
    "85c5dc": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "85C5DC",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA51AN",
        "Type": "737NG 881/W"
    },
    "8682f4": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "8682F4",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA741A",
        "Type": "777 281ER"
    },
    "781416": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "781416",
        "OperatorFlagCode": "CSH",
        "RegisteredOwners": "Shanghai Airlines",
        "Registration": "B-1111",
        "Type": "787 9"
    },
    "aaa4dc": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "AAA4DC",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N785UA",
        "Type": "777 222ER"
    },
    "461f5a": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "461F5A",
        "OperatorFlagCode": "FIN",
        "RegisteredOwners": "Finnair",
        "Registration": "OH-LWS",
        "Type": "A350 941"
    },
    "861f5e": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861F5E",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA618A",
        "Type": "767 381ER"
    },
    "86da5c": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86DA5C",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA83AN",
        "Type": "737NG 881/W"
    },
    "8694fa": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "8694FA",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA792A",
        "Type": "777 381ER"
    },
    "8518ae": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8518AE",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA334J",
        "Type": "737NG 846/W"
    },
    "aabd7f": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "AABD7F",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N791UA",
        "Type": "777 222ER"
    },
    "84b772": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "84B772",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA212A",
        "Type": "A320 271NSL"
    },
    "758335": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "758335",
        "OperatorFlagCode": "PAL",
        "RegisteredOwners": "Philippine Airlines",
        "Registration": "RP-C9909",
        "Type": "A321 231SL"
    },
    "7501f9": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "7501F9",
        "OperatorFlagCode": "XAX",
        "RegisteredOwners": "AirAsia X",
        "Registration": "9M-XXF",
        "Type": "A330 343E"
    },
    "868089": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "868089",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73AB",
        "Type": "737NG 800/W"
    },
    "a3a0ed": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "A3A0ED",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N33294",
        "Type": "737NG 824/W"
    },
    "c023c5": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "C023C5",
        "OperatorFlagCode": "ACA",
        "RegisteredOwners": "Air Canada",
        "Registration": "C-FNOE",
        "Type": "787 9"
    },
    "84183d": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "84183D",
        "OperatorFlagCode": "JTA",
        "RegisteredOwners": "Japan TransOcean Air",
        "Registration": "JA06RK",
        "Type": "737NG 800/W"
    },
    "780f3d": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "780F3D",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-7349",
        "Type": "777 39PER"
    },
    "aac136": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "AAC136",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N792UA",
        "Type": "777 222ER"
    },
    "aaffa2": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "AAFFA2",
        "OperatorFlagCode": "AAL",
        "RegisteredOwners": "American Airlines",
        "Registration": "N808AN",
        "Type": "787 8"
    },
    "7c5325": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "7C5325",
        "OperatorFlagCode": "QFA",
        "RegisteredOwners": "Qantas",
        "Registration": "VH-QPJ",
        "Type": "A330 303"
    },
    "76cd05": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "76CD05",
        "OperatorFlagCode": "SIA",
        "RegisteredOwners": "Singapore Airlines",
        "Registration": "9V-SHE",
        "Type": "A350 941"
    },
    "8681ab": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8681AB",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73ND",
        "Type": "737NG 8FZ/W"
    },
    "86d9d2": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86D9D2",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA836A",
        "Type": "787 9"
    },
    "758558": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "758558",
        "OperatorFlagCode": "PAL",
        "RegisteredOwners": "Philippine Airlines",
        "Registration": "RP-C9934",
        "Type": "A321 271NSL"
    },
    "780f39": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "780F39",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-7343",
        "Type": "777 39PER"
    },
    "86d288": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D288",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA815A",
        "Type": "787 8"
    },
    "86e82a": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E82A",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA876J",
        "Type": "787 9"
    },
    "a4d838": {
        "ICAOTypeCode": "A339",
        "Manufacturer": "Airbus",
        "ModeS": "A4D838",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N411DX",
        "Type": "A330 941N"
    },
    "3c6707": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "3C6707",
        "OperatorFlagCode": "DLH",
        "RegisteredOwners": "Lufthansa",
        "Registration": "D-AIXG",
        "Type": "A350 941"
    },
    "a65800": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "A65800",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N508DN",
        "Type": "A350 941"
    },
    "86803b": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86803B",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA737R",
        "Type": "737NG 86N/W"
    },
    "8511a8": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "8511A8",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA315J",
        "Type": "737NG 846/W"
    },
    "86ebb6": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86EBB6",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA886A",
        "Type": "787 9"
    },
    "76cd0e": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "76CD0E",
        "OperatorFlagCode": "SIA",
        "RegisteredOwners": "Singapore Airlines",
        "Registration": "9V-SHN",
        "Type": "A350 941"
    },
    "888143": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "888143",
        "OperatorFlagCode": "VJC",
        "RegisteredOwners": "VietJetAir",
        "Registration": "VN-A646",
        "Type": "A321 271NSL"
    },
    "3965a3": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "3965A3",
        "OperatorFlagCode": "AFR",
        "RegisteredOwners": "Air France",
        "Registration": "F-GZND",
        "Type": "777 328ER"
    },
    "846444": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "846444",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA12XJ",
        "Type": "A350 941"
    },
    "8991ab": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "8991AB",
        "OperatorFlagCode": "CAL",
        "RegisteredOwners": "China Airlines",
        "Registration": "B-18359",
        "Type": "A330 302"
    },
    "861b06": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861B06",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA602J",
        "Type": "767 346ER"
    },
    "86d930": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D930",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA831J",
        "Type": "787 8"
    },
    "8686aa": {
        "ICAOTypeCode": "B773",
        "Manufacturer": "Boeing",
        "ModeS": "8686AA",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA752A",
        "Type": "777 381"
    },
    "86d1de": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D1DE",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA810A",
        "Type": "787 8"
    },
    "851c42": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851C42",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA344J",
        "Type": "737NG 846/W"
    },
    "71c399": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "71C399",
        "OperatorFlagCode": "AAR",
        "RegisteredOwners": "Asiana Airlines",
        "Registration": "HL8399",
        "Type": "A321 251NXSL"
    },
    "842388": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "842388",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA09XJ",
        "Type": "A350 941"
    },
    "a92d6d": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "A92D6D",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N69020",
        "Type": "777 224ER"
    },
    "85186a": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "85186A",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA332J",
        "Type": "737NG 846/W"
    },
    "872968": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "872968",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA90AN",
        "Type": "737NG 800/W"
    },
    "789205": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "789205",
        "OperatorFlagCode": "HKE",
        "RegisteredOwners": "Hong Kong Express Airways",
        "Registration": "B-LEG",
        "Type": "A321 231SL"
    },
    "862250": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "862250",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA623J",
        "Type": "767 346ER"
    },
    "845d1c": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "845D1C",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA10XJ",
        "Type": "A350 941"
    },
    "86ec40": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86EC40",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA88AN",
        "Type": "737NG 800/W"
    },
    "78185a": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "78185A",
        "OperatorFlagCode": "CES",
        "RegisteredOwners": "China Eastern Airlines",
        "Registration": "B-30CY",
        "Type": "A320 251NSL"
    },
    "758307": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "758307",
        "OperatorFlagCode": "PAL",
        "RegisteredOwners": "Philippine Airlines",
        "Registration": "RP-C9907",
        "Type": "A321 231SL"
    },
    "780d2e": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "780D2E",
        "OperatorFlagCode": "CSH",
        "RegisteredOwners": "Shanghai Airlines",
        "Registration": "B-1721",
        "Type": "737NG 86D/W"
    },
    "868340": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "868340",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA743J",
        "Type": "777 346ER"
    },
    "89905a": {
        "ICAOTypeCode": "A20N",
        "Manufacturer": "Airbus",
        "ModeS": "89905A",
        "OperatorFlagCode": "TTW",
        "RegisteredOwners": "Tigerair Taiwan",
        "Registration": "B-50025",
        "Type": "A320 271NSL"
    },
    "780c45": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "780C45",
        "OperatorFlagCode": "CCA",
        "RegisteredOwners": "Air China",
        "Registration": "B-5948",
        "Type": "A330 343E"
    },
    "868316": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "868316",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA742A",
        "Type": "777 281ER"
    },
    "88516d": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "88516D",
        "OperatorFlagCode": "THA",
        "RegisteredOwners": "Thai Airways International",
        "Registration": "HS-TKM",
        "Type": "777 3ALER"
    },
    "8991b9": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "8991B9",
        "OperatorFlagCode": "CAL",
        "RegisteredOwners": "China Airlines",
        "Registration": "B-18311",
        "Type": "A330 302"
    },
    "850e36": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "850E36",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA306J",
        "Type": "737NG 846/W"
    },
    "3c4b30": {
        "ICAOTypeCode": "B748",
        "Manufacturer": "Boeing",
        "ModeS": "3C4B30",
        "OperatorFlagCode": "DLH",
        "RegisteredOwners": "Lufthansa",
        "Registration": "D-ABYP",
        "Type": "747 830"
    },
    "78023d": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "78023D",
        "OperatorFlagCode": "CPA",
        "RegisteredOwners": "Cathay Pacific Airways",
        "Registration": "B-KPQ",
        "Type": "777 367ER"
    },
    "868094": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "868094",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA73AN",
        "Type": "737NG 881/W"
    },
    "869560": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "869560",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA795A",
        "Type": "777 300ER"
    },
    "a17ecd": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "A17ECD",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N196DN",
        "Type": "767 332ER/W"
    },
    "86789e": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "86789E",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA714A",
        "Type": "777 281"
    },
    "851958": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "851958",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA339J",
        "Type": "737NG 846/W"
    },
    "841c60": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "841C60",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA07XJ",
        "Type": "A350 941"
    },
    "8694d8": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "8694D8",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA791A",
        "Type": "777 381ER"
    },
    "846932": {
        "ICAOTypeCode": "A21N",
        "Manufacturer": "Airbus",
        "ModeS": "846932",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA148A",
        "Type": "A321 272NSL"
    },
    "aa92f9": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "AA92F9",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N78002",
        "Type": "777 224ER"
    },
    "86e866": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86E866",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA878A",
        "Type": "787 8"
    },
    "8964a5": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "8964A5",
        "OperatorFlagCode": "UAE",
        "RegisteredOwners": "Emirates Airline",
        "Registration": "A6-EQM",
        "Type": "777 300ER"
    },
    "86da16": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86DA16",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA838A",
        "Type": "787 8"
    },
    "868428": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "868428",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA74AN",
        "Type": "737NG 881/W"
    },
    "842194": {
        "ICAOTypeCode": "B737",
        "Manufacturer": "Boeing",
        "ModeS": "842194",
        "OperatorFlagCode": "ADO",
        "RegisteredOwners": "Air Do",
        "Registration": "JA09AN",
        "Type": "737NG 781/W"
    },
    "a65092": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "A65092",
        "OperatorFlagCode": "DAL",
        "RegisteredOwners": "Delta Air Lines",
        "Registration": "N506DN",
        "Type": "A350 941"
    },
    "86d974": {
        "ICAOTypeCode": "B788",
        "Manufacturer": "Boeing",
        "ModeS": "86D974",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA833J",
        "Type": "787 8"
    },
    "a1aa10": {
        "ICAOTypeCode": "B772",
        "Manufacturer": "Boeing",
        "ModeS": "A1AA10",
        "OperatorFlagCode": "UAL",
        "RegisteredOwners": "United Airlines",
        "Registration": "N206UA",
        "Type": "777 222ER"
    },
    "780f93": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "780F93",
        "OperatorFlagCode": "CSH",
        "RegisteredOwners": "Shanghai Airlines",
        "Registration": "B-7633",
        "Type": "737NG 89P/W"
    },
    "873356": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "873356",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA934A",
        "Type": "787 9"
    },
    "86cec5": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "86CEC5",
        "OperatorFlagCode": "SNJ",
        "RegisteredOwners": "Solaseed Air",
        "Registration": "JA803X",
        "Type": "737NG 86N/W"
    },
    "845ebc": {
        "ICAOTypeCode": "B737",
        "Manufacturer": "Boeing",
        "ModeS": "845EBC",
        "OperatorFlagCode": "ADO",
        "RegisteredOwners": "Air Do",
        "Registration": "JA11AN",
        "Type": "737NG 781/W"
    },
    "841442": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "841442",
        "OperatorFlagCode": "SFJ",
        "RegisteredOwners": "StarFlyer",
        "Registration": "JA05MC",
        "Type": "A320 214"
    },
    "3c4b23": {
        "ICAOTypeCode": "B748",
        "Manufacturer": "Boeing",
        "ModeS": "3C4B23",
        "OperatorFlagCode": "DLH",
        "RegisteredOwners": "Lufthansa",
        "Registration": "D-ABYC",
        "Type": "747 830"
    },
    "7502cd": {
        "ICAOTypeCode": "A333",
        "Manufacturer": "Airbus",
        "ModeS": "7502CD",
        "OperatorFlagCode": "XAX",
        "RegisteredOwners": "AirAsia X",
        "Registration": "9M-XXK",
        "Type": "A330 343E"
    },
    "868088": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "868088",
        "OperatorFlagCode": "SKY",
        "RegisteredOwners": "Skymark Airlines",
        "Registration": "JA73AA",
        "Type": "737NG 800/W"
    },
    "861f1a": {
        "ICAOTypeCode": "B763",
        "Manufacturer": "Boeing",
        "ModeS": "861F1A",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA616A",
        "Type": "767 381ER"
    },
    "86d31d": {
        "ICAOTypeCode": "A320",
        "Manufacturer": "Airbus",
        "ModeS": "86D31D",
        "OperatorFlagCode": "APJ",
        "RegisteredOwners": "Peach Aviation",
        "Registration": "JA819P",
        "Type": "A320 214"
    },
    "8418cc": {
        "ICAOTypeCode": "A359",
        "Manufacturer": "Airbus",
        "ModeS": "8418CC",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA06XJ",
        "Type": "A350 941"
    },
    "8406d0": {
        "ICAOTypeCode": "A35K",
        "Manufacturer": "Airbus",
        "ModeS": "8406D0",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA01WJ",
        "Type": "A350 1041"
    },
    "85dee8": {
        "ICAOTypeCode": "B738",
        "Manufacturer": "Boeing",
        "ModeS": "85DEE8",
        "OperatorFlagCode": "ANA",
        "RegisteredOwners": "All Nippon Airways",
        "Registration": "JA58AN",
        "Type": "737NG 881/W"
    },
    "86e7a2": {
        "ICAOTypeCode": "B789",
        "Manufacturer": "Boeing",
        "ModeS": "86E7A2",
        "OperatorFlagCode": "JAL",
        "RegisteredOwners": "Japan Airlines",
        "Registration": "JA872J",
        "Type": "787 9"
    },
    "a455ea": {
        "ICAOTypeCode": "A332",
        "Manufacturer": "Airbus",
        "ModeS": "A455EA",
        "OperatorFlagCode": "HAL",
        "RegisteredOwners": "Hawaiian Airlines",
        "Registration": "N379HA",
        "Type": "A330 243"
    },
    "4ba946": {
        "ICAOTypeCode": "B77W",
        "Manufacturer": "Boeing",
        "ModeS": "4BA946",
        "OperatorFlagCode": "THY",
        "RegisteredOwners": "Turkish Airlines",
        "Registration": "TC-JJF",
        "Type": "777 3F2ER"
    },
    "789229": {
        "ICAOTypeCode": "A321",
        "Manufacturer": "Airbus",
        "ModeS": "789229",
        "OperatorFlagCode": "HKE",
        "RegisteredOwners": "Hong Kong Express Airways",
        "Registration": "B-LEL",
        "Type": "A321 231SL"
    },
    "888041": {
        "ModeS": "888041",
        "Registration": "VN-A687",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "841400": {
        "ModeS": "841400",
        "Registration": "JA05JJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Jetstar Japan",
        "OperatorFlagCode": "JJP"
    },
    "780a58": {
        "ModeS": "780A58",
        "Registration": "B-LBB",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "78928c": {
        "ModeS": "78928C",
        "Registration": "B-LPR",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "71bf50": {
        "ModeS": "71BF50",
        "Registration": "HL7750",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B772",
        "Type": "777 2B5ER",
        "RegisteredOwners": "Jin Air",
        "OperatorFlagCode": "JNA"
    },
    "75864d": {
        "ModeS": "75864D",
        "Registration": "RP-C9799",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Royal Air Philippines",
        "OperatorFlagCode": "RYL"
    },
    "89906e": {
        "ModeS": "89906E",
        "Registration": "B-16222",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "71be22": {
        "ModeS": "71BE22",
        "Registration": "HL7622",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A388",
        "Type": "A380 861",
        "RegisteredOwners": "Korean Air",
        "OperatorFlagCode": "KAL"
    },
    "781109": {
        "ModeS": "781109",
        "Registration": "B-7377",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 800/W",
        "RegisteredOwners": "Hainan Airlines",
        "OperatorFlagCode": "CHH"
    },
    "899030": {
        "ModeS": "899030",
        "Registration": "B-16727",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 35EER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "8990df": {
        "ModeS": "8990DF",
        "Registration": "B-16717",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 35EER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "71c261": {
        "ModeS": "71C261",
        "Registration": "HL8261",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8BK/W",
        "RegisteredOwners": "Jeju Air",
        "OperatorFlagCode": "JJA"
    },
    "78929e": {
        "ModeS": "78929E",
        "Registration": "B-LPW",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "71c375": {
        "ModeS": "71C375",
        "Registration": "HL8375",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 86N/W",
        "RegisteredOwners": "Eastar Jet",
        "OperatorFlagCode": "ESR"
    },
    "7585ea": {
        "ModeS": "7585EA",
        "Registration": "RP-C8946",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Philippines AirAsia",
        "OperatorFlagCode": "APG"
    },
    "71bf40": {
        "ModeS": "71BF40",
        "Registration": "HL7740",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 323E",
        "RegisteredOwners": "Asiana Airlines",
        "OperatorFlagCode": "AAR"
    },
    "7801b2": {
        "ModeS": "7801B2",
        "Registration": "B-HTI",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Hong Kong Express Airways",
        "OperatorFlagCode": "HKE"
    },
    "8991bc": {
        "ModeS": "8991BC",
        "Registration": "B-18315",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "75832f": {
        "ModeS": "75832F",
        "Registration": "RP-C8971",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 216",
        "RegisteredOwners": "Philippines AirAsia",
        "OperatorFlagCode": "APG"
    },
    "899082": {
        "ModeS": "899082",
        "Registration": "B-16790",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "76bd45": {
        "ModeS": "76BD45",
        "Registration": "9V-OJE",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Scoot",
        "OperatorFlagCode": "TGW"
    },
    "780235": {
        "ModeS": "780235",
        "Registration": "B-LAJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 342",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "7808c3": {
        "ModeS": "7808C3",
        "Registration": "B-5675",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 81B/W",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "880459": {
        "ModeS": "880459",
        "Registration": "HS-ABY",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Thai AirAsia",
        "OperatorFlagCode": "AIQ"
    },
    "485785": {
        "ModeS": "485785",
        "Registration": "PH-BHN",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "KLM Royal Dutch Airlines",
        "OperatorFlagCode": "KLM"
    },
    "4bb18f": {
        "ModeS": "4BB18F",
        "Registration": "TC-LLO",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "899114": {
        "ModeS": "899114",
        "Registration": "B-18109",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "76bd49": {
        "ModeS": "76BD49",
        "Registration": "9V-OJI",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Scoot",
        "OperatorFlagCode": "TGW"
    },
    "888125": {
        "ModeS": "888125",
        "Registration": "VN-A673",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "7804e7": {
        "ModeS": "7804E7",
        "Registration": "B-6382",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 213",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "8991dd": {
        "ModeS": "8991DD",
        "Registration": "B-58302",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A339",
        "Type": "A330 941N",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "899097": {
        "ModeS": "899097",
        "Registration": "B-17807",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "71c002": {
        "ModeS": "71C002",
        "Registration": "HL8002",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 323E",
        "RegisteredOwners": "Korean Air",
        "OperatorFlagCode": "KAL"
    },
    "76cc74": {
        "ModeS": "76CC74",
        "Registration": "9V-SCT",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "Singapore Airlines",
        "OperatorFlagCode": "SIA"
    },
    "89901e": {
        "ModeS": "89901E",
        "Registration": "B-18005",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 309ER",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "781f37": {
        "ModeS": "781F37",
        "Registration": "B-32DV",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "Shenzhen Airlines",
        "OperatorFlagCode": "CSZ"
    },
    "8830ef": {
        "ModeS": "8830EF",
        "Registration": "HS-LGO",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8GP/W",
        "RegisteredOwners": "Thai Lion Air",
        "OperatorFlagCode": "TLM"
    },
    "8990a8": {
        "ModeS": "8990A8",
        "Registration": "B-18112",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "8463b5": {
        "ModeS": "8463B5",
        "Registration": "JA12VA",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Peach Aviation",
        "OperatorFlagCode": "APJ"
    },
    "75047c": {
        "ModeS": "75047C",
        "Registration": "9M-RAA",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 216SL",
        "RegisteredOwners": "AirAsia",
        "OperatorFlagCode": "AXM"
    },
    "8880af": {
        "ModeS": "8880AF",
        "Registration": "VN-A689",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "88803f": {
        "ModeS": "88803F",
        "Registration": "VN-A684",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "7500c8": {
        "ModeS": "7500C8",
        "Registration": "9M-XXW",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "AirAsia X",
        "OperatorFlagCode": "XAX"
    },
    "78924a": {
        "ModeS": "78924A",
        "Registration": "B-HPE",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "84b42f": {
        "ModeS": "84B42F",
        "Registration": "JA204P",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 251NSL",
        "RegisteredOwners": "Peach Aviation",
        "OperatorFlagCode": "APJ"
    },
    "71be38": {
        "ModeS": "71BE38",
        "Registration": "HL7638",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B748",
        "Type": "747 8B5",
        "RegisteredOwners": "Korean Air",
        "OperatorFlagCode": "KAL"
    },
    "a03f48": {
        "ModeS": "A03F48",
        "Registration": "N115FE",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 3S2F",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "89904e": {
        "ModeS": "89904E",
        "Registration": "B-16208",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "781600": {
        "ModeS": "781600",
        "Registration": "B-MCI",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Air Macau",
        "OperatorFlagCode": "AMU"
    },
    "71c596": {
        "ModeS": "71C596",
        "Registration": "HL8596",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 216",
        "RegisteredOwners": "Aero K",
        "OperatorFlagCode": "EOK"
    },
    "8881d7": {
        "ModeS": "8881D7",
        "Registration": "VN-A526",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "89912e": {
        "ModeS": "89912E",
        "Registration": "B-18910",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "8880ae": {
        "ModeS": "8880AE",
        "Registration": "VN-A603",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Vietnam Airlines",
        "OperatorFlagCode": "HVN"
    },
    "7805c2": {
        "ModeS": "7805C2",
        "Registration": "B-5476",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 85C/W",
        "RegisteredOwners": "XiamenAir",
        "OperatorFlagCode": "CXA"
    },
    "88819f": {
        "ModeS": "88819F",
        "Registration": "VN-A594",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211",
        "RegisteredOwners": "Bamboo Airways",
        "OperatorFlagCode": "BAV"
    },
    "7801b6": {
        "ModeS": "7801B6",
        "Registration": "B-HLW",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343X",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "885973": {
        "ModeS": "885973",
        "Registration": "HS-VKS",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Thai VietJetAir",
        "OperatorFlagCode": "TVJ"
    },
    "861b03": {
        "ModeS": "861B03",
        "Registration": "JA602F",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 381F",
        "RegisteredOwners": "ANA Cargo",
        "OperatorFlagCode": "ANA"
    },
    "861f22": {
        "ModeS": "861F22",
        "Registration": "JA616J",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 346ER/W",
        "RegisteredOwners": "Japan Airlines",
        "OperatorFlagCode": "JAL"
    },
    "8990d8": {
        "ModeS": "8990D8",
        "Registration": "B-16709",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 35EER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "780e49": {
        "ModeS": "780E49",
        "Registration": "B-6489",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 85C/W",
        "RegisteredOwners": "XiamenAir",
        "OperatorFlagCode": "CXA"
    },
    "899016": {
        "ModeS": "899016",
        "Registration": "B-18779",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "781045": {
        "ModeS": "781045",
        "Registration": "B-1537",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 800/W",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "862d2e": {
        "ModeS": "862D2E",
        "Registration": "JA654J",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 346ERBCF",
        "RegisteredOwners": "Japan Airlines",
        "OperatorFlagCode": "JAL"
    },
    "758706": {
        "ModeS": "758706",
        "Registration": "RP-C3904",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A339",
        "Type": "A330 941N",
        "RegisteredOwners": "Cebu Pacific Air",
        "OperatorFlagCode": "CEB"
    },
    "789235": {
        "ModeS": "789235",
        "Registration": "B-HNV",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B773",
        "Type": "777 31H",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "885966": {
        "ModeS": "885966",
        "Registration": "HS-VKF",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Thai VietJetAir",
        "OperatorFlagCode": "TVJ"
    },
    "8990a6": {
        "ModeS": "8990A6",
        "Registration": "B-18781",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "780e47": {
        "ModeS": "780E47",
        "Registration": "B-6487",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 85C/W",
        "RegisteredOwners": "XiamenAir",
        "OperatorFlagCode": "CXA"
    },
    "789271": {
        "ModeS": "789271",
        "Registration": "B-KKA",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Hong Kong Express Airways",
        "OperatorFlagCode": "HKE"
    },
    "8830e9": {
        "ModeS": "8830E9",
        "Registration": "HS-LGI",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8GP/W",
        "RegisteredOwners": "Thai Lion Air",
        "OperatorFlagCode": "TLM"
    },
    "76cc73": {
        "ModeS": "76CC73",
        "Registration": "9V-SCS",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "Singapore Airlines",
        "OperatorFlagCode": "SIA"
    },
    "781252": {
        "ModeS": "781252",
        "Registration": "B-1006",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231SL",
        "RegisteredOwners": "Juneyao Air",
        "OperatorFlagCode": "DKH"
    },
    "89901f": {
        "ModeS": "89901F",
        "Registration": "B-18006",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 309ER",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "4bb18a": {
        "ModeS": "4BB18A",
        "Registration": "TC-LLJ",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "71c587": {
        "ModeS": "71C587",
        "Registration": "HL8587",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 86N/W",
        "RegisteredOwners": "Eastar Jet",
        "OperatorFlagCode": "ESR"
    },
    "78057f": {
        "ModeS": "78057F",
        "Registration": "B-6599",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 213",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "71c700": {
        "ModeS": "71C700",
        "Registration": "HL8700",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8SH/W",
        "RegisteredOwners": "Eastar Jet",
        "OperatorFlagCode": "ESR"
    },
    "89902c": {
        "ModeS": "89902C",
        "Registration": "B-50017",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Tigerair Taiwan",
        "OperatorFlagCode": "TTW"
    },
    "8832b5": {
        "ModeS": "8832B5",
        "Registration": "HS-LUU",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8GP/W",
        "RegisteredOwners": "Thai Lion Air",
        "OperatorFlagCode": "TLM"
    },
    "780ed0": {
        "ModeS": "780ED0",
        "Registration": "B-8358",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 323E",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "71c337": {
        "ModeS": "71C337",
        "Registration": "HL8337",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 82R/W",
        "RegisteredOwners": "Jeju Air",
        "OperatorFlagCode": "JJA"
    },
    "899036": {
        "ModeS": "899036",
        "Registration": "B-16731",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "899088": {
        "ModeS": "899088",
        "Registration": "B-17801",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "8990e0": {
        "ModeS": "8990E0",
        "Registration": "B-16718",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 35EER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "a7ea7e": {
        "ModeS": "A7EA7E",
        "Registration": "N609UP",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B748",
        "Type": "747 8F",
        "RegisteredOwners": "United Parcel Service",
        "OperatorFlagCode": "UPS"
    },
    "89916c": {
        "ModeS": "89916C",
        "Registration": "B-18919",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "ac638d": {
        "ModeS": "AC638D",
        "Registration": "N898FD",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "8990d5": {
        "ModeS": "8990D5",
        "Registration": "B-16706",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 35EER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "885224": {
        "ModeS": "885224",
        "Registration": "HS-TQD",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B788",
        "Type": "787 8",
        "RegisteredOwners": "Thai Airways International",
        "OperatorFlagCode": "THA"
    },
    "8991a7": {
        "ModeS": "8991A7",
        "Registration": "B-18660",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8SH/W",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "76bd47": {
        "ModeS": "76BD47",
        "Registration": "9V-OJG",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Scoot",
        "OperatorFlagCode": "TGW"
    },
    "7809e7": {
        "ModeS": "7809E7",
        "Registration": "B-5745",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 81B/W",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "484370": {
        "ModeS": "484370",
        "Registration": "PH-BQI",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B772",
        "Type": "777 206ER",
        "RegisteredOwners": "KLM Royal Dutch Airlines",
        "OperatorFlagCode": "KLM"
    },
    "899135": {
        "ModeS": "899135",
        "Registration": "B-16789",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "780a0a": {
        "ModeS": "780A0A",
        "Registration": "B-LAM",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "885974": {
        "ModeS": "885974",
        "Registration": "HS-VKT",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Thai VietJetAir",
        "OperatorFlagCode": "TVJ"
    },
    "780bfa": {
        "ModeS": "780BFA",
        "Registration": "B-5913",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "a4009e": {
        "ModeS": "A4009E",
        "Registration": "N357UP",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 34AF/W",
        "RegisteredOwners": "United Parcel Service",
        "OperatorFlagCode": "UPS"
    },
    "899040": {
        "ModeS": "899040",
        "Registration": "B-16736",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "4d0140": {
        "ModeS": "4D0140",
        "Registration": "LX-OCV",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 4R7F",
        "RegisteredOwners": "Cargolux Airlines International",
        "OperatorFlagCode": "CLX"
    },
    "7585e1": {
        "ModeS": "7585E1",
        "Registration": "RP-C8947",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 216",
        "RegisteredOwners": "Philippines AirAsia",
        "OperatorFlagCode": "APG"
    },
    "880454": {
        "ModeS": "880454",
        "Registration": "HS-ABT",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 216",
        "RegisteredOwners": "Thai AirAsia",
        "OperatorFlagCode": "AIQ"
    },
    "899017": {
        "ModeS": "899017",
        "Registration": "B-18780",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "75041f": {
        "ModeS": "75041F",
        "Registration": "9M-LRD",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B38M",
        "Type": "737MAX 8",
        "RegisteredOwners": "Batik Air Malaysia",
        "OperatorFlagCode": "MXD"
    },
    "899139": {
        "ModeS": "899139",
        "Registration": "B-17887",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787-9 Dreamliner",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "76bd4a": {
        "ModeS": "76BD4A",
        "Registration": "9V-OJJ",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Scoot",
        "OperatorFlagCode": "TGW"
    },
    "8830f1": {
        "ModeS": "8830F1",
        "Registration": "HS-LGQ",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8GP/W",
        "RegisteredOwners": "Thai Lion Air",
        "OperatorFlagCode": "TLM"
    },
    "780aa7": {
        "ModeS": "780AA7",
        "Registration": "B-LPQ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "789291": {
        "ModeS": "789291",
        "Registration": "B-HPS",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "88530a": {
        "ModeS": "88530A",
        "Registration": "HS-TXJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Thai Airways International",
        "OperatorFlagCode": "THA"
    },
    "88516f": {
        "ModeS": "88516F",
        "Registration": "HS-TKO",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 3ALER",
        "RegisteredOwners": "Thai Airways International",
        "OperatorFlagCode": "THA"
    },
    "89902a": {
        "ModeS": "89902A",
        "Registration": "B-50015",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Tigerair Taiwan",
        "OperatorFlagCode": "TTW"
    },
    "7585b3": {
        "ModeS": "7585B3",
        "Registration": "RP-C8948",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 216SL",
        "RegisteredOwners": "Philippines AirAsia",
        "OperatorFlagCode": "APG"
    },
    "78203d": {
        "ModeS": "78203D",
        "Registration": "B-32G3",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 251NSL",
        "RegisteredOwners": "Spring Airlines",
        "OperatorFlagCode": "CQH"
    },
    "8830ed": {
        "ModeS": "8830ED",
        "Registration": "HS-LGM",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 800/W",
        "RegisteredOwners": "Thai Lion Air",
        "OperatorFlagCode": "TLM"
    },
    "780a9e": {
        "ModeS": "780A9E",
        "Registration": "B-LPO",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "781146": {
        "ModeS": "781146",
        "Registration": "B-8360",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 323E",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "781362": {
        "ModeS": "781362",
        "Registration": "B-1062",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "a76683": {
        "ModeS": "A76683",
        "Registration": "N576UP",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 44AF",
        "RegisteredOwners": "United Parcel Service",
        "OperatorFlagCode": "UPS"
    },
    "780aa0": {
        "ModeS": "780AA0",
        "Registration": "B-LCH",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Hong Kong Express Airways",
        "OperatorFlagCode": "HKE"
    },
    "782277": {
        "ModeS": "782277",
        "Registration": "B-227K",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "China Cargo Airlines",
        "OperatorFlagCode": "CKK"
    },
    "89901d": {
        "ModeS": "89901D",
        "Registration": "B-18003",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 309ER",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "7809f0": {
        "ModeS": "7809F0",
        "Registration": "B-2017",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B734",
        "Type": "737 4K5SF",
        "RegisteredOwners": "SF Airlines",
        "OperatorFlagCode": "CSS"
    },
    "78021c": {
        "ModeS": "78021C",
        "Registration": "B-LIF",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 467ERF",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "899093": {
        "ModeS": "899093",
        "Registration": "B-17802",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "899105": {
        "ModeS": "899105",
        "Registration": "B-18719",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 409F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "89909c": {
        "ModeS": "89909C",
        "Registration": "B-17808",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "71bf47": {
        "ModeS": "71BF47",
        "Registration": "HL7747",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 323E",
        "RegisteredOwners": "Asiana Airlines",
        "OperatorFlagCode": "AAR"
    },
    "71c007": {
        "ModeS": "71C007",
        "Registration": "HL8007",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 3B5ER",
        "RegisteredOwners": "Korean Air",
        "OperatorFlagCode": "KAL"
    },
    "8990e9": {
        "ModeS": "8990E9",
        "Registration": "B-18107",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "88596f": {
        "ModeS": "88596F",
        "Registration": "HS-VKO",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Thai VietJetAir",
        "OperatorFlagCode": "TVJ"
    },
    "a7b07c": {
        "ModeS": "A7B07C",
        "Registration": "N595FE",
        "Manufacturer": "McDonnell Douglas",
        "ICAOTypeCode": "MD11",
        "Type": "MD-11 F",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "7804b5": {
        "ModeS": "7804B5",
        "Registration": "B-6368",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "780a49": {
        "ModeS": "780A49",
        "Registration": "B-LAR",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "76bcc3": {
        "ModeS": "76BCC3",
        "Registration": "9V-OFC",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B788",
        "Type": "787 8",
        "RegisteredOwners": "Scoot",
        "OperatorFlagCode": "TGW"
    },
    "758368": {
        "ModeS": "758368",
        "Registration": "RP-C9912",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231SL",
        "RegisteredOwners": "Philippine Airlines",
        "OperatorFlagCode": "PAL"
    },
    "7801ca": {
        "ModeS": "7801CA",
        "Registration": "B-LAE",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 342",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "7811f4": {
        "ModeS": "7811F4",
        "Registration": "B-1493",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 800/W",
        "RegisteredOwners": "Hainan Airlines",
        "OperatorFlagCode": "CHH"
    },
    "780c75": {
        "ModeS": "780C75",
        "Registration": "B-5951",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 323E",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "896484": {
        "ModeS": "896484",
        "Registration": "A6-EUZ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A388",
        "Type": "A380 842",
        "RegisteredOwners": "Emirates Airline",
        "OperatorFlagCode": "UAE"
    },
    "8991d6": {
        "ModeS": "8991D6",
        "Registration": "B-58208",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 252NXSL",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "899037": {
        "ModeS": "899037",
        "Registration": "B-16732",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "88813c": {
        "ModeS": "88813C",
        "Registration": "VN-A633",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "781565": {
        "ModeS": "781565",
        "Registration": "B-303N",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Shenzhen Airlines",
        "OperatorFlagCode": "CSZ"
    },
    "885226": {
        "ModeS": "885226",
        "Registration": "HS-TQF",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B788",
        "Type": "787 8",
        "RegisteredOwners": "Thai Airways International",
        "OperatorFlagCode": "THA"
    },
    "780cab": {
        "ModeS": "780CAB",
        "Registration": "B-1981",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 89P/W",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "780a93": {
        "ModeS": "780A93",
        "Registration": "B-LBI",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "781463": {
        "ModeS": "781463",
        "Registration": "B-300Q",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "76bd42": {
        "ModeS": "76BD42",
        "Registration": "9V-OJB",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Scoot",
        "OperatorFlagCode": "TGW"
    },
    "8991e5": {
        "ModeS": "8991E5",
        "Registration": "B-58502",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "71c539": {
        "ModeS": "71C539",
        "Registration": "HL8539",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8AS/W",
        "RegisteredOwners": "Jeju Air",
        "OperatorFlagCode": "JJA"
    },
    "8991de": {
        "ModeS": "8991DE",
        "Registration": "B-58303",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A339",
        "Type": "A330 941N",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "780a0c": {
        "ModeS": "780A0C",
        "Registration": "B-LAO",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "781dbe": {
        "ModeS": "781DBE",
        "Registration": "B-222C",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 38AERBCF",
        "RegisteredOwners": "SF Airlines",
        "OperatorFlagCode": "CSS"
    },
    "780171": {
        "ModeS": "780171",
        "Registration": "B-HNI",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B773",
        "Type": "777 367",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "71bf43": {
        "ModeS": "71BF43",
        "Registration": "HL7743",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B772",
        "Type": "777 2B5ER",
        "RegisteredOwners": "Jin Air",
        "OperatorFlagCode": "JNA"
    },
    "899124": {
        "ModeS": "899124",
        "Registration": "B-16783",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "780a8a": {
        "ModeS": "780A8A",
        "Registration": "B-KQV",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 367ER",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "789236": {
        "ModeS": "789236",
        "Registration": "B-HNW",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B773",
        "Type": "777 31H",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "89905b": {
        "ModeS": "89905B",
        "Registration": "B-50026",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 271NSL",
        "RegisteredOwners": "Tigerair Taiwan",
        "OperatorFlagCode": "TTW"
    },
    "7801dc": {
        "ModeS": "7801DC",
        "Registration": "B-HNQ",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B773",
        "Type": "777 367",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "71c572": {
        "ModeS": "71C572",
        "Registration": "HL8572",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787-10 Dreamliner",
        "RegisteredOwners": "Korean Air",
        "OperatorFlagCode": "KAL"
    },
    "75839f": {
        "ModeS": "75839F",
        "Registration": "RP-C9916",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231SL",
        "RegisteredOwners": "Philippine Airlines",
        "OperatorFlagCode": "PAL"
    },
    "782150": {
        "ModeS": "782150",
        "Registration": "B-32HW",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 251N",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "8991e8": {
        "ModeS": "8991E8",
        "Registration": "B-58505",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "704015": {
        "ModeS": "704015",
        "Registration": "XY-ALT",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Myanmar Airways International",
        "OperatorFlagCode": "MMA"
    },
    "7502d8": {
        "ModeS": "7502D8",
        "Registration": "9M-LRU",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B38M",
        "Type": "737MAX 8",
        "RegisteredOwners": "Batik Air Malaysia",
        "OperatorFlagCode": "MXD"
    },
    "846dc8": {
        "ModeS": "846DC8",
        "Registration": "JA15JJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Jetstar Japan",
        "OperatorFlagCode": "JJP"
    },
    "780e28": {
        "ModeS": "780E28",
        "Registration": "B-6062",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 84P/W",
        "RegisteredOwners": "Hainan Airlines",
        "OperatorFlagCode": "CHH"
    },
    "a81bc4": {
        "ModeS": "A81BC4",
        "Registration": "N621UP",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B748",
        "Type": "747 8F",
        "RegisteredOwners": "United Parcel Service",
        "OperatorFlagCode": "UPS"
    },
    "78929f": {
        "ModeS": "78929F",
        "Registration": "B-LPX",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "84715c": {
        "ModeS": "84715C",
        "Registration": "JA16JJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Jetstar Japan",
        "OperatorFlagCode": "JJP"
    },
    "7803ae": {
        "ModeS": "7803AE",
        "Registration": "B-6512",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "a771a8": {
        "ModeS": "A771A8",
        "Registration": "N579UP",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 45E SCD",
        "RegisteredOwners": "United Parcel Service",
        "OperatorFlagCode": "UPS"
    },
    "861b47": {
        "ModeS": "861B47",
        "Registration": "JA604F",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 381F",
        "RegisteredOwners": "ANA Cargo",
        "OperatorFlagCode": "ANA"
    },
    "7801cb": {
        "ModeS": "7801CB",
        "Registration": "B-LAF",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 342",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "71c390": {
        "ModeS": "71C390",
        "Registration": "HL8390",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Korean Air",
        "OperatorFlagCode": "KAL"
    },
    "758539": {
        "ModeS": "758539",
        "Registration": "RP-C8964",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 216",
        "RegisteredOwners": "Philippines AirAsia",
        "OperatorFlagCode": "APG"
    },
    "8991be": {
        "ModeS": "8991BE",
        "Registration": "B-18317",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "781087": {
        "ModeS": "781087",
        "Registration": "B-8648",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "8990e2": {
        "ModeS": "8990E2",
        "Registration": "B-16720",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 36NER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "899051": {
        "ModeS": "899051",
        "Registration": "B-18666",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 800/W",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "899137": {
        "ModeS": "899137",
        "Registration": "B-16786",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "71bd62": {
        "ModeS": "71BD62",
        "Registration": "HL7562",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8B5/W",
        "RegisteredOwners": "Jin Air",
        "OperatorFlagCode": "JNA"
    },
    "71c221": {
        "ModeS": "71C221",
        "Registration": "HL8221",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B739",
        "Type": "737NG 9B5ER/W",
        "RegisteredOwners": "Korean Air",
        "OperatorFlagCode": "KAL"
    },
    "89907e": {
        "ModeS": "89907E",
        "Registration": "B-17885",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "881422": {
        "ModeS": "881422",
        "Registration": "HS-EAB",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Thai AirAsia",
        "OperatorFlagCode": "AIQ"
    },
    "71c223": {
        "ModeS": "71C223",
        "Registration": "HL8223",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B739",
        "Type": "737NG 9B5ER/W",
        "RegisteredOwners": "Korean Air",
        "OperatorFlagCode": "KAL"
    },
    "8880ca": {
        "ModeS": "8880CA",
        "Registration": "VN-A611",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Vietnam Airlines",
        "OperatorFlagCode": "HVN"
    },
    "76cc69": {
        "ModeS": "76CC69",
        "Registration": "9V-SCI",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "Singapore Airlines",
        "OperatorFlagCode": "SIA"
    },
    "71bf41": {
        "ModeS": "71BF41",
        "Registration": "HL7741",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 323E",
        "RegisteredOwners": "Asiana Airlines",
        "OperatorFlagCode": "AAR"
    },
    "861ae1": {
        "ModeS": "861AE1",
        "Registration": "JA601F",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 381F",
        "RegisteredOwners": "ANA Cargo",
        "OperatorFlagCode": "ANA"
    },
    "781307": {
        "ModeS": "781307",
        "Registration": "B-MCH",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Air Macau",
        "OperatorFlagCode": "AMU"
    },
    "781e0f": {
        "ModeS": "781E0F",
        "Registration": "B-222E",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B752",
        "Type": "757 28APCF/W",
        "RegisteredOwners": "SF Airlines",
        "OperatorFlagCode": "CSS"
    },
    "781335": {
        "ModeS": "781335",
        "Registration": "B-1041",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "4ba94d": {
        "ModeS": "4BA94D",
        "Registration": "TC-JJM",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 3F2ER",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "7585a1": {
        "ModeS": "7585A1",
        "Registration": "RP-C4118",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "Cebu Pacific Air",
        "OperatorFlagCode": "CEB"
    },
    "8991e0": {
        "ModeS": "8991E0",
        "Registration": "B-58305",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A339",
        "Type": "A330 941N",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "862d0c": {
        "ModeS": "862D0C",
        "Registration": "JA653J",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 346ERBCF",
        "RegisteredOwners": "Japan Airlines",
        "OperatorFlagCode": "JAL"
    },
    "781ed3": {
        "ModeS": "781ED3",
        "Registration": "B-222Z",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "China Cargo Airlines",
        "OperatorFlagCode": "CKK"
    },
    "899094": {
        "ModeS": "899094",
        "Registration": "B-17803",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "789251": {
        "ModeS": "789251",
        "Registration": "B-LDS",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A332",
        "Type": "A330 243F",
        "RegisteredOwners": "Air Hong Kong",
        "OperatorFlagCode": "AHK"
    },
    "a38dd8": {
        "ModeS": "A38DD8",
        "Registration": "N328UP",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 34AF/W",
        "RegisteredOwners": "United Parcel Service",
        "OperatorFlagCode": "UPS"
    },
    "71c546": {
        "ModeS": "71C546",
        "Registration": "HL8546",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8GJ/W",
        "RegisteredOwners": "Eastar Jet",
        "OperatorFlagCode": "ESR"
    },
    "78041d": {
        "ModeS": "78041D",
        "Registration": "B-MBC",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Air Macau",
        "OperatorFlagCode": "AMU"
    },
    "8991b0": {
        "ModeS": "8991B0",
        "Registration": "B-18301",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "781e51": {
        "ModeS": "781E51",
        "Registration": "B-32CF",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "Shenzhen Airlines",
        "OperatorFlagCode": "CSZ"
    },
    "ac05b3": {
        "ModeS": "AC05B3",
        "Registration": "N874FD",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "4bb183": {
        "ModeS": "4BB183",
        "Registration": "TC-LLC",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "71c374": {
        "ModeS": "71C374",
        "Registration": "HL8374",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 86N/W",
        "RegisteredOwners": "Eastar Jet",
        "OperatorFlagCode": "ESR"
    },
    "76cc62": {
        "ModeS": "76CC62",
        "Registration": "9V-SCB",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "Singapore Airlines",
        "OperatorFlagCode": "SIA"
    },
    "a4c79b": {
        "ModeS": "A4C79B",
        "Registration": "N407KZ",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 4KZF",
        "RegisteredOwners": "Atlas Air",
        "OperatorFlagCode": "GTI"
    },
    "76cc64": {
        "ModeS": "76CC64",
        "Registration": "9V-SCD",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "Singapore Airlines",
        "OperatorFlagCode": "SIA"
    },
    "780ec4": {
        "ModeS": "780EC4",
        "Registration": "B-MCF",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Air Macau",
        "OperatorFlagCode": "AMU"
    },
    "899117": {
        "ModeS": "899117",
        "Registration": "B-18118",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NX",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "780b41": {
        "ModeS": "780B41",
        "Registration": "B-5791",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 85C/W",
        "RegisteredOwners": "XiamenAir",
        "OperatorFlagCode": "CXA"
    },
    "71c220": {
        "ModeS": "71C220",
        "Registration": "HL8220",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8Q8",
        "RegisteredOwners": "T way Air",
        "OperatorFlagCode": "TWB"
    },
    "780a1e": {
        "ModeS": "780A1E",
        "Registration": "B-LNY",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A332",
        "Type": "A330 243F",
        "RegisteredOwners": "Hong Kong Air Cargo",
        "OperatorFlagCode": "HKC"
    },
    "789289": {
        "ModeS": "789289",
        "Registration": "B-KJF",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 83Z/W",
        "RegisteredOwners": "Greater Bay Airlines",
        "OperatorFlagCode": "HGB"
    },
    "847c18": {
        "ModeS": "847C18",
        "Registration": "JA19JJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Jetstar Japan",
        "OperatorFlagCode": "JJP"
    },
    "8990e4": {
        "ModeS": "8990E4",
        "Registration": "B-16722",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 36NER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "88596d": {
        "ModeS": "88596D",
        "Registration": "HS-VKM",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "Thai VietJetAir",
        "OperatorFlagCode": "TVJ"
    },
    "750484": {
        "ModeS": "750484",
        "Registration": "9M-RAE",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 216SL",
        "RegisteredOwners": "AirAsia",
        "OperatorFlagCode": "AXM"
    },
    "71bf94": {
        "ModeS": "71BF94",
        "Registration": "HL7794",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 323E",
        "RegisteredOwners": "Asiana Airlines",
        "OperatorFlagCode": "AAR"
    },
    "89911c": {
        "ModeS": "89911C",
        "Registration": "B-18723",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 409F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "78927c": {
        "ModeS": "78927C",
        "Registration": "B-LHI",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "7812a6": {
        "ModeS": "7812A6",
        "Registration": "B-1019",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "868dd7": {
        "ModeS": "868DD7",
        "Registration": "JA772F",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "ANA Cargo",
        "OperatorFlagCode": "ANA"
    },
    "8990ea": {
        "ModeS": "8990EA",
        "Registration": "B-18108",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "780cbe": {
        "ModeS": "780CBE",
        "Registration": "B-1876",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 213SL",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "89901a": {
        "ModeS": "89901A",
        "Registration": "B-18055",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 36NER",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "781128": {
        "ModeS": "781128",
        "Registration": "B-1412",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 800/W",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "89907a": {
        "ModeS": "89907A",
        "Registration": "B-16336",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "750420": {
        "ModeS": "750420",
        "Registration": "9M-LRF",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B38M",
        "Type": "737MAX 8",
        "RegisteredOwners": "Batik Air Malaysia",
        "OperatorFlagCode": "MXD"
    },
    "781462": {
        "ModeS": "781462",
        "Registration": "B-300P",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "7808d1": {
        "ModeS": "7808D1",
        "Registration": "B-5655",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 85C/W",
        "RegisteredOwners": "XiamenAir",
        "OperatorFlagCode": "CXA"
    },
    "781f00": {
        "ModeS": "781F00",
        "Registration": "B-223F",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "China Cargo Airlines",
        "OperatorFlagCode": "CKK"
    },
    "4bb153": {
        "ModeS": "4BB153",
        "Registration": "TC-LJS",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "8991aa": {
        "ModeS": "8991AA",
        "Registration": "B-18358",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "75875f": {
        "ModeS": "75875F",
        "Registration": "RP-C3907",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A339",
        "Type": "A330 941N",
        "RegisteredOwners": "Cebu Pacific Air",
        "OperatorFlagCode": "CEB"
    },
    "8990c9": {
        "ModeS": "8990C9",
        "Registration": "B-58508",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "STARLUX",
        "OperatorFlagCode": "SJX"
    },
    "71ba10": {
        "ModeS": "71BA10",
        "Registration": "HL7210",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231SL",
        "RegisteredOwners": "Air Busan",
        "OperatorFlagCode": "ABL"
    },
    "a2e014": {
        "ModeS": "A2E014",
        "Registration": "N2846U",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "United Airlines",
        "OperatorFlagCode": "UAL"
    },
    "a40e1c": {
        "ModeS": "A40E1C",
        "Registration": "N360UP",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 34AF/W",
        "RegisteredOwners": "United Parcel Service",
        "OperatorFlagCode": "UPS"
    },
    "899045": {
        "ModeS": "899045",
        "Registration": "B-18662",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8AL/W",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "780a7e": {
        "ModeS": "780A7E",
        "Registration": "B-LBD",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "780c74": {
        "ModeS": "780C74",
        "Registration": "B-2048",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 31BER",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "780a27": {
        "ModeS": "780A27",
        "Registration": "B-LNX",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A332",
        "Type": "A330 243F",
        "RegisteredOwners": "Hong Kong Air Cargo",
        "OperatorFlagCode": "HKC"
    },
    "7587f5": {
        "ModeS": "7587F5",
        "Registration": "RP-C3753",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B733",
        "Type": "737 330(QC)",
        "RegisteredOwners": "SEair International",
        "OperatorFlagCode": "SGD"
    },
    "a046b6": {
        "ModeS": "A046B6",
        "Registration": "N117FE",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 3S2F",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "8881a2": {
        "ModeS": "8881A2",
        "Registration": "VN-A597",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211",
        "RegisteredOwners": "Bamboo Airways",
        "OperatorFlagCode": "BAV"
    },
    "8991b8": {
        "ModeS": "8991B8",
        "Registration": "B-18310",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "84bcd4": {
        "ModeS": "84BCD4",
        "Registration": "JA22JJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Jetstar Japan",
        "OperatorFlagCode": "JJP"
    },
    "888095": {
        "ModeS": "888095",
        "Registration": "VN-A666",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "780a0e": {
        "ModeS": "780A0E",
        "Registration": "B-LAQ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "8990dc": {
        "ModeS": "8990DC",
        "Registration": "B-16713",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 35EER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "abf6d7": {
        "ModeS": "ABF6D7",
        "Registration": "N870FD",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "899107": {
        "ModeS": "899107",
        "Registration": "B-18721",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 409F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "758384": {
        "ModeS": "758384",
        "Registration": "RP-C9915",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231SL",
        "RegisteredOwners": "Philippine Airlines",
        "OperatorFlagCode": "PAL"
    },
    "789267": {
        "ModeS": "789267",
        "Registration": "B-HPJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "71bd79": {
        "ModeS": "71BD79",
        "Registration": "HL7579",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "Asiana Airlines",
        "OperatorFlagCode": "AAR"
    },
    "780a0b": {
        "ModeS": "780A0B",
        "Registration": "B-LAN",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "789237": {
        "ModeS": "789237",
        "Registration": "B-HNX",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B773",
        "Type": "777 31H",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "780a59": {
        "ModeS": "780A59",
        "Registration": "B-LBC",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "7503ac": {
        "ModeS": "7503AC",
        "Registration": "9M-MLV",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8H6/W",
        "RegisteredOwners": "Malaysia Airlines",
        "OperatorFlagCode": "MAS"
    },
    "780233": {
        "ModeS": "780233",
        "Registration": "B-LJC",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B748",
        "Type": "747 867F",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "71bf57": {
        "ModeS": "71BF57",
        "Registration": "HL7757",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8GQ/W",
        "RegisteredOwners": "Jin Air",
        "OperatorFlagCode": "JNA"
    },
    "899021": {
        "ModeS": "899021",
        "Registration": "B-18051",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 36NER",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "899096": {
        "ModeS": "899096",
        "Registration": "B-17806",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "885112": {
        "ModeS": "885112",
        "Registration": "HS-THR",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "Thai Airways International",
        "OperatorFlagCode": "THA"
    },
    "885971": {
        "ModeS": "885971",
        "Registration": "HS-VKQ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Thai VietJetAir",
        "OperatorFlagCode": "TVJ"
    },
    "a4080c": {
        "ModeS": "A4080C",
        "Registration": "N359UP",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 34AF/W",
        "RegisteredOwners": "United Parcel Service",
        "OperatorFlagCode": "UPS"
    },
    "78105d": {
        "ModeS": "78105D",
        "Registration": "B-1542",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 800/W",
        "RegisteredOwners": "Hainan Airlines",
        "OperatorFlagCode": "CHH"
    },
    "899085": {
        "ModeS": "899085",
        "Registration": "B-16339",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "a3a084": {
        "ModeS": "A3A084",
        "Registration": "N33264",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 824/W",
        "RegisteredOwners": "United Airlines",
        "OperatorFlagCode": "UAL"
    },
    "8880a3": {
        "ModeS": "8880A3",
        "Registration": "VN-A395",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Vietnam Airlines",
        "OperatorFlagCode": "HVN"
    },
    "88815e": {
        "ModeS": "88815E",
        "Registration": "VN-A697",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NSL",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "789260": {
        "ModeS": "789260",
        "Registration": "B-KJB",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 800/W",
        "RegisteredOwners": "Greater Bay Airlines",
        "OperatorFlagCode": "HGB"
    },
    "84b73b": {
        "ModeS": "84B73B",
        "Registration": "JA210P",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 251NSL",
        "RegisteredOwners": "Peach Aviation",
        "OperatorFlagCode": "APJ"
    },
    "789296": {
        "ModeS": "789296",
        "Registration": "B-KKM",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NX",
        "RegisteredOwners": "HK express",
        "OperatorFlagCode": "HKE"
    },
    "7817f2": {
        "ModeS": "7817F2",
        "Registration": "B-30C3",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 251NSL",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "845ce4": {
        "ModeS": "845CE4",
        "Registration": "JA10VA",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Peach Aviation",
        "OperatorFlagCode": "APJ"
    },
    "78110b": {
        "ModeS": "78110B",
        "Registration": "B-7379",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 800/W",
        "RegisteredOwners": "Hainan Airlines",
        "OperatorFlagCode": "CHH"
    },
    "78147a": {
        "ModeS": "78147A",
        "Registration": "B-300U",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "a03423": {
        "ModeS": "A03423",
        "Registration": "N112FE",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 3S2F",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "880856": {
        "ModeS": "880856",
        "Registration": "HS-BBV",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 216SL",
        "RegisteredOwners": "Thai AirAsia",
        "OperatorFlagCode": "AIQ"
    },
    "8880c5": {
        "ModeS": "8880C5",
        "Registration": "VN-A609",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Vietnam Airlines",
        "OperatorFlagCode": "HVN"
    },
    "881426": {
        "ModeS": "881426",
        "Registration": "HS-EAF",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NX",
        "RegisteredOwners": "Thai AirAsia",
        "OperatorFlagCode": "AIQ"
    },
    "ac2d32": {
        "ModeS": "AC2D32",
        "Registration": "N884FD",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 FS2",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "781cfd": {
        "ModeS": "781CFD",
        "Registration": "B-221N",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 333ERBCF/W",
        "RegisteredOwners": "SF Airlines",
        "OperatorFlagCode": "CSS"
    },
    "781225": {
        "ModeS": "781225",
        "Registration": "B-8865",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Shenzhen Airlines",
        "OperatorFlagCode": "CSZ"
    },
    "8991b7": {
        "ModeS": "8991B7",
        "Registration": "B-18309",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "8990b4": {
        "ModeS": "8990B4",
        "Registration": "B-16218",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "71bf18": {
        "ModeS": "71BF18",
        "Registration": "HL7718",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B739",
        "Type": "737NG 9B5",
        "RegisteredOwners": "Jin Air",
        "OperatorFlagCode": "JNA"
    },
    "780c43": {
        "ModeS": "780C43",
        "Registration": "B-5946",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "899080": {
        "ModeS": "899080",
        "Registration": "B-16737",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "8963ed": {
        "ModeS": "8963ED",
        "Registration": "A6-EOP",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A388",
        "Type": "A380 861",
        "RegisteredOwners": "Emirates Airline",
        "OperatorFlagCode": "UAE"
    },
    "7800e4": {
        "ModeS": "7800E4",
        "Registration": "B-6848",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 232",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "899116": {
        "ModeS": "899116",
        "Registration": "B-18117",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NX",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "8990bb": {
        "ModeS": "8990BB",
        "Registration": "B-58202",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 252NXSL",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "8990c0": {
        "ModeS": "8990C0",
        "Registration": "B-58506",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "789282": {
        "ModeS": "789282",
        "Registration": "B-LKC",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A332",
        "Type": "A330 243F",
        "RegisteredOwners": "Air Hong Kong",
        "OperatorFlagCode": "AHK"
    },
    "a1c7e4": {
        "ModeS": "A1C7E4",
        "Registration": "N2136U",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "United Airlines",
        "OperatorFlagCode": "UAL"
    },
    "789249": {
        "ModeS": "789249",
        "Registration": "B-HPD",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "789265": {
        "ModeS": "789265",
        "Registration": "B-HPO",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "89907b": {
        "ModeS": "89907B",
        "Registration": "B-17881",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "78192e": {
        "ModeS": "78192E",
        "Registration": "B-30ET",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 251NSL",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "780e59": {
        "ModeS": "780E59",
        "Registration": "B-6987",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 85N/W",
        "RegisteredOwners": "Shandong Airlines",
        "OperatorFlagCode": "CDG"
    },
    "89901b": {
        "ModeS": "89901B",
        "Registration": "B-18001",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 309ER",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "78041b": {
        "ModeS": "78041B",
        "Registration": "B-MBA",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Air Macau",
        "OperatorFlagCode": "AMU"
    },
    "780a57": {
        "ModeS": "780A57",
        "Registration": "B-LBA",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "86d5e5": {
        "ModeS": "86D5E5",
        "Registration": "JA823P",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Peach Aviation",
        "OperatorFlagCode": "APJ"
    },
    "8990de": {
        "ModeS": "8990DE",
        "Registration": "B-16716",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 35EER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "8991d4": {
        "ModeS": "8991D4",
        "Registration": "B-58206",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 252NXSL",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "780e36": {
        "ModeS": "780E36",
        "Registration": "B-MCB",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Air Macau",
        "OperatorFlagCode": "AMU"
    },
    "84d283": {
        "ModeS": "84D283",
        "Registration": "JA28LR",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Jetstar Japan",
        "OperatorFlagCode": "JJP"
    },
    "78926e": {
        "ModeS": "78926E",
        "Registration": "B-LDW",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E(P2F)",
        "RegisteredOwners": "Air Hong Kong",
        "OperatorFlagCode": "AHK"
    },
    "71c335": {
        "ModeS": "71C335",
        "Registration": "HL8335",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8JP/W",
        "RegisteredOwners": "Jeju Air",
        "OperatorFlagCode": "JJA"
    },
    "88808b": {
        "ModeS": "88808B",
        "Registration": "VN-A324",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Vietnam Airlines",
        "OperatorFlagCode": "HVN"
    },
    "89907d": {
        "ModeS": "89907D",
        "Registration": "B-17883",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "88811c": {
        "ModeS": "88811C",
        "Registration": "VN-A672",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "899095": {
        "ModeS": "899095",
        "Registration": "B-17805",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "780a7a": {
        "ModeS": "780A7A",
        "Registration": "B-LPL",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "789281": {
        "ModeS": "789281",
        "Registration": "B-LKB",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A332",
        "Type": "A330 243F",
        "RegisteredOwners": "Air Hong Kong",
        "OperatorFlagCode": "AHK"
    },
    "75041b": {
        "ModeS": "75041B",
        "Registration": "9M-LRW",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B38M",
        "Type": "737MAX 8",
        "RegisteredOwners": "Batik Air Malaysia",
        "OperatorFlagCode": "MXD"
    },
    "485344": {
        "ModeS": "485344",
        "Registration": "PH-BHL",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "KLM Royal Dutch Airlines",
        "OperatorFlagCode": "KLM"
    },
    "88808f": {
        "ModeS": "88808F",
        "Registration": "VN-A329",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Vietnam Airlines",
        "OperatorFlagCode": "HVN"
    },
    "8991dc": {
        "ModeS": "8991DC",
        "Registration": "B-58301",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A339",
        "Type": "A330 941N",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "71c063": {
        "ModeS": "71C063",
        "Registration": "HL8063",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8AS/W",
        "RegisteredOwners": "Jeju Air",
        "OperatorFlagCode": "JJA"
    },
    "78926d": {
        "ModeS": "78926D",
        "Registration": "B-LDV",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E(P2F)",
        "RegisteredOwners": "Air Hong Kong",
        "OperatorFlagCode": "AHK"
    },
    "78029c": {
        "ModeS": "78029C",
        "Registration": "B-5179",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 86NBCF/W",
        "RegisteredOwners": "China Postal Airlines",
        "OperatorFlagCode": "CYZ"
    },
    "899136": {
        "ModeS": "899136",
        "Registration": "B-17886",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9 Dreamliner",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "78016f": {
        "ModeS": "78016F",
        "Registration": "B-HNG",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B773",
        "Type": "777 367",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "7bb0c1": {
        "ModeS": "7BB0C1",
        "Registration": "B-5020",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 81B",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "abab90": {
        "ModeS": "ABAB90",
        "Registration": "N851FD",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 FS2",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "89910b": {
        "ModeS": "89910B",
        "Registration": "B-18105",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "780f41": {
        "ModeS": "780F41",
        "Registration": "B-8397",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "75025a": {
        "ModeS": "75025A",
        "Registration": "9M-MTG",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 323E",
        "RegisteredOwners": "Malaysia Airlines",
        "OperatorFlagCode": "MAS"
    },
    "71c327": {
        "ModeS": "71C327",
        "Registration": "HL8327",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8KN/W",
        "RegisteredOwners": "T way Air",
        "OperatorFlagCode": "TWB"
    },
    "71c383": {
        "ModeS": "71C383",
        "Registration": "HL8383",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "Asiana Airlines",
        "OperatorFlagCode": "AAR"
    },
    "758369": {
        "ModeS": "758369",
        "Registration": "RP-C9914",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231SL",
        "RegisteredOwners": "Philippine Airlines",
        "OperatorFlagCode": "PAL"
    },
    "84b4d9": {
        "ModeS": "84B4D9",
        "Registration": "JA209P",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 251NSL",
        "RegisteredOwners": "Peach Aviation",
        "OperatorFlagCode": "APJ"
    },
    "7807d5": {
        "ModeS": "7807D5",
        "Registration": "B-6537",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A332",
        "Type": "A330 243",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "885302": {
        "ModeS": "885302",
        "Registration": "HS-TXB",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Thai Airways International",
        "OperatorFlagCode": "THA"
    },
    "780a4a": {
        "ModeS": "780A4A",
        "Registration": "B-LAX",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "8990ec": {
        "ModeS": "8990EC",
        "Registration": "B-18917",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "8990e1": {
        "ModeS": "8990E1",
        "Registration": "B-16719",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 36NER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "899070": {
        "ModeS": "899070",
        "Registration": "B-16223",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "71bf71": {
        "ModeS": "71BF71",
        "Registration": "HL7771",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "Asiana Airlines",
        "OperatorFlagCode": "AAR"
    },
    "8991e4": {
        "ModeS": "8991E4",
        "Registration": "B-58501",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "899071": {
        "ModeS": "899071",
        "Registration": "B-16225",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "8990f3": {
        "ModeS": "8990F3",
        "Registration": "B-18906",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "8466a0": {
        "ModeS": "8466A0",
        "Registration": "JA13JJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Jetstar Japan",
        "OperatorFlagCode": "JJP"
    },
    "4ba959": {
        "ModeS": "4BA959",
        "Registration": "TC-JJY",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 3F2ER",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "8990c7": {
        "ModeS": "8990C7",
        "Registration": "B-16340",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "a762cc": {
        "ModeS": "A762CC",
        "Registration": "N575UP",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 44AF",
        "RegisteredOwners": "United Parcel Service",
        "OperatorFlagCode": "UPS"
    },
    "4ba94f": {
        "ModeS": "4BA94F",
        "Registration": "TC-JJO",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 3F2ER",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "780a44": {
        "ModeS": "780A44",
        "Registration": "B-LPC",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "780fff": {
        "ModeS": "780FFF",
        "Registration": "B-7616",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 84P/W",
        "RegisteredOwners": "Hainan Airlines",
        "OperatorFlagCode": "CHH"
    },
    "750480": {
        "ModeS": "750480",
        "Registration": "9M-RAC",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 216SL",
        "RegisteredOwners": "AirAsia",
        "OperatorFlagCode": "AXM"
    },
    "781124": {
        "ModeS": "781124",
        "Registration": "B-1406",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 800/W",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "8990a4": {
        "ModeS": "8990A4",
        "Registration": "B-18772",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "71ba13": {
        "ModeS": "71BA13",
        "Registration": "HL7213",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 86N/W",
        "RegisteredOwners": "Jeju Air",
        "OperatorFlagCode": "JJA"
    },
    "a9d626": {
        "ModeS": "A9D626",
        "Registration": "N73291",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 824/W",
        "RegisteredOwners": "United Airlines",
        "OperatorFlagCode": "UAL"
    },
    "899032": {
        "ModeS": "899032",
        "Registration": "B-16729",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "71c366": {
        "ModeS": "71C366",
        "Registration": "HL8366",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Air Busan",
        "OperatorFlagCode": "ABL"
    },
    "7583e4": {
        "ModeS": "7583E4",
        "Registration": "RP-C8975",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Philippines AirAsia",
        "OperatorFlagCode": "APG"
    },
    "8881ff": {
        "ModeS": "8881FF",
        "Registration": "VN-A500",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NX",
        "RegisteredOwners": "VietJet Air",
        "OperatorFlagCode": "VJC"
    },
    "a82e57": {
        "ModeS": "A82E57",
        "Registration": "N626UP",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B748",
        "Type": "747 8F",
        "RegisteredOwners": "United Parcel Service",
        "OperatorFlagCode": "UPS"
    },
    "7809b5": {
        "ModeS": "7809B5",
        "Registration": "B-5708",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 85C/W",
        "RegisteredOwners": "XiamenAir",
        "OperatorFlagCode": "CXA"
    },
    "71c588": {
        "ModeS": "71C588",
        "Registration": "HL8588",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8GJ/W",
        "RegisteredOwners": "Eastar Jet",
        "OperatorFlagCode": "ESR"
    },
    "a806d8": {
        "ModeS": "A806D8",
        "Registration": "N616UP",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B748",
        "Type": "747 8F",
        "RegisteredOwners": "United Parcel Service",
        "OperatorFlagCode": "UPS"
    },
    "789292": {
        "ModeS": "789292",
        "Registration": "B-HPT",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "a7a1a0": {
        "ModeS": "A7A1A0",
        "Registration": "N591FE",
        "Manufacturer": "McDonnell Douglas",
        "ICAOTypeCode": "MD11",
        "Type": "MD-11 F",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "888175": {
        "ModeS": "888175",
        "Registration": "VN-A670",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "71bf33": {
        "ModeS": "71BF33",
        "Registration": "HL7733",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B772",
        "Type": "777 2B5ER",
        "RegisteredOwners": "Jin Air",
        "OperatorFlagCode": "JNA"
    },
    "71c064": {
        "ModeS": "71C064",
        "Registration": "HL8064",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8AS/W",
        "RegisteredOwners": "Jeju Air",
        "OperatorFlagCode": "JJA"
    },
    "c8273f": {
        "ModeS": "C8273F",
        "Registration": "ZK-NZN",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Air New Zealand",
        "OperatorFlagCode": "ANZ"
    },
    "899133": {
        "ModeS": "899133",
        "Registration": "B-16788",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "7502b1": {
        "ModeS": "7502B1",
        "Registration": "9M-MLQ",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8H6/W",
        "RegisteredOwners": "Malaysia Airlines",
        "OperatorFlagCode": "MAS"
    },
    "71c597": {
        "ModeS": "71C597",
        "Registration": "HL8597",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "Korean Air",
        "OperatorFlagCode": "KAL"
    },
    "840944": {
        "ModeS": "840944",
        "Registration": "JA02JJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Jetstar Japan",
        "OperatorFlagCode": "JJP"
    },
    "7892a2": {
        "ModeS": "7892A2",
        "Registration": "B-LPU",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "899023": {
        "ModeS": "899023",
        "Registration": "B-50001",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Tigerair Taiwan",
        "OperatorFlagCode": "TTW"
    },
    "4bb154": {
        "ModeS": "4BB154",
        "Registration": "TC-LJT",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "8991d7": {
        "ModeS": "8991D7",
        "Registration": "B-58209",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 252NXSL",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "899103": {
        "ModeS": "899103",
        "Registration": "B-18717",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 409F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "7803be": {
        "ModeS": "7803BE",
        "Registration": "B-6545",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A332",
        "Type": "A330 243",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "8990ed": {
        "ModeS": "8990ED",
        "Registration": "B-18918",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "899118": {
        "ModeS": "899118",
        "Registration": "B-18120",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NX",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "7502c2": {
        "ModeS": "7502C2",
        "Registration": "9M-LRR",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B38M",
        "Type": "737MAX 8",
        "RegisteredOwners": "Batik Air Malaysia",
        "OperatorFlagCode": "MXD"
    },
    "899122": {
        "ModeS": "899122",
        "Registration": "B-58510",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "STARLUX",
        "OperatorFlagCode": "SJX"
    },
    "789248": {
        "ModeS": "789248",
        "Registration": "B-HPB",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "780aa6": {
        "ModeS": "780AA6",
        "Registration": "B-LPP",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "71c547": {
        "ModeS": "71C547",
        "Registration": "HL8547",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 81M/W",
        "RegisteredOwners": "T way Air",
        "OperatorFlagCode": "TWB"
    },
    "7bb034": {
        "ModeS": "7BB034",
        "Registration": "B-2956",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B733",
        "Type": "737 33ASF",
        "RegisteredOwners": "SF Airlines",
        "OperatorFlagCode": "CSS"
    },
    "8880a5": {
        "ModeS": "8880A5",
        "Registration": "VN-A397",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Vietnam Airlines",
        "OperatorFlagCode": "HVN"
    },
    "76bd48": {
        "ModeS": "76BD48",
        "Registration": "9V-OJH",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Scoot",
        "OperatorFlagCode": "TGW"
    },
    "899018": {
        "ModeS": "899018",
        "Registration": "B-18052",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 36NER",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "a2b8b8": {
        "ModeS": "A2B8B8",
        "Registration": "N2747U",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "United Airlines",
        "OperatorFlagCode": "UAL"
    },
    "7801c7": {
        "ModeS": "7801C7",
        "Registration": "B-LAB",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 342",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "780ec2": {
        "ModeS": "780EC2",
        "Registration": "B-MCD",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231SL",
        "RegisteredOwners": "Air Macau",
        "OperatorFlagCode": "AMU"
    },
    "8880c0": {
        "ModeS": "8880C0",
        "Registration": "VN-A608",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Vietnam Airlines",
        "OperatorFlagCode": "HVN"
    },
    "781104": {
        "ModeS": "781104",
        "Registration": "B-8968",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "780262": {
        "ModeS": "780262",
        "Registration": "B-1401",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 800/W",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "780a6e": {
        "ModeS": "780A6E",
        "Registration": "B-LJK",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B748",
        "Type": "747 867F",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "8965b8": {
        "ModeS": "8965B8",
        "Registration": "A6-EFT",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "Emirates Airline",
        "OperatorFlagCode": "UAE"
    },
    "8990a1": {
        "ModeS": "8990A1",
        "Registration": "B-18652",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8Q8/W",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "71c296": {
        "ModeS": "71C296",
        "Registration": "HL8296",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8Q8/W",
        "RegisteredOwners": "Jeju Air",
        "OperatorFlagCode": "JJA"
    },
    "a2b501": {
        "ModeS": "A2B501",
        "Registration": "N2737U",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "United Airlines",
        "OperatorFlagCode": "UAL"
    },
    "8990d7": {
        "ModeS": "8990D7",
        "Registration": "B-16708",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 35EER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "750479": {
        "ModeS": "750479",
        "Registration": "9M-XBF",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "AirAsia X",
        "OperatorFlagCode": "XAX"
    },
    "78122f": {
        "ModeS": "78122F",
        "Registration": "B-8862",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "4bb182": {
        "ModeS": "4BB182",
        "Registration": "TC-LLB",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "750259": {
        "ModeS": "750259",
        "Registration": "9M-MTF",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 323E",
        "RegisteredOwners": "Malaysia Airlines",
        "OperatorFlagCode": "MAS"
    },
    "899106": {
        "ModeS": "899106",
        "Registration": "B-18720",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 409F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "a6caa1": {
        "ModeS": "A6CAA1",
        "Registration": "N537CA",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 446F",
        "RegisteredOwners": "National Airlines",
        "OperatorFlagCode": "NCR"
    },
    "76cc6c": {
        "ModeS": "76CC6C",
        "Registration": "9V-SCL",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "Singapore Airlines",
        "OperatorFlagCode": "SIA"
    },
    "78018f": {
        "ModeS": "78018F",
        "Registration": "B-HLO",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343X",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "a28dc8": {
        "ModeS": "A28DC8",
        "Registration": "N2639U",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "United Airlines",
        "OperatorFlagCode": "UAL"
    },
    "86d5c3": {
        "ModeS": "86D5C3",
        "Registration": "JA822P",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Peach Aviation",
        "OperatorFlagCode": "APJ"
    },
    "780dec": {
        "ModeS": "780DEC",
        "Registration": "B-1509",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 85N/W",
        "RegisteredOwners": "Shandong Airlines",
        "OperatorFlagCode": "CDG"
    },
    "789278": {
        "ModeS": "789278",
        "Registration": "B-LDY",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E(P2F)",
        "RegisteredOwners": "Air Hong Kong",
        "OperatorFlagCode": "AHK"
    },
    "8881d9": {
        "ModeS": "8881D9",
        "Registration": "VN-A528",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "4bb186": {
        "ModeS": "4BB186",
        "Registration": "TC-LLF",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "88809a": {
        "ModeS": "88809A",
        "Registration": "VN-A336",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Vietnam Airlines",
        "OperatorFlagCode": "HVN"
    },
    "76cc63": {
        "ModeS": "76CC63",
        "Registration": "9V-SCC",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "Singapore Airlines",
        "OperatorFlagCode": "SIA"
    },
    "71c086": {
        "ModeS": "71C086",
        "Registration": "HL8086",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8Q8",
        "RegisteredOwners": "T way Air",
        "OperatorFlagCode": "TWB"
    },
    "780529": {
        "ModeS": "780529",
        "Registration": "B-5426",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 89L/W",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "8990b1": {
        "ModeS": "8990B1",
        "Registration": "B-16215",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "86d66d": {
        "ModeS": "86D66D",
        "Registration": "JA827P",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Peach Aviation",
        "OperatorFlagCode": "APJ"
    },
    "7801cc": {
        "ModeS": "7801CC",
        "Registration": "B-HNP",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B773",
        "Type": "777 367",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "89909f": {
        "ModeS": "89909F",
        "Registration": "B-17810",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "71c235": {
        "ModeS": "71C235",
        "Registration": "HL8235",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8KG/W",
        "RegisteredOwners": "T way Air",
        "OperatorFlagCode": "TWB"
    },
    "4ba952": {
        "ModeS": "4BA952",
        "Registration": "TC-JJR",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 3F2ER",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "8990ad": {
        "ModeS": "8990AD",
        "Registration": "B-18651",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8Q8/W",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "899022": {
        "ModeS": "899022",
        "Registration": "B-18905",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "780170": {
        "ModeS": "780170",
        "Registration": "B-HNH",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B773",
        "Type": "777 367",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "780193": {
        "ModeS": "780193",
        "Registration": "B-HLS",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343X",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "780a7f": {
        "ModeS": "780A7F",
        "Registration": "B-LBE",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "8990f4": {
        "ModeS": "8990F4",
        "Registration": "B-18907",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "7801b7": {
        "ModeS": "7801B7",
        "Registration": "B-HNO",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B773",
        "Type": "777 367",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "780d22": {
        "ModeS": "780D22",
        "Registration": "B-5961",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A332",
        "Type": "A330 243",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "78114b": {
        "ModeS": "78114B",
        "Registration": "B-8366",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "789279": {
        "ModeS": "789279",
        "Registration": "B-LDZ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343(P2F)",
        "RegisteredOwners": "Air Hong Kong",
        "OperatorFlagCode": "AHK"
    },
    "780a3e": {
        "ModeS": "780A3E",
        "Registration": "B-LJI",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B748",
        "Type": "747 867F",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "8990d9": {
        "ModeS": "8990D9",
        "Registration": "B-16710",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 35EER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "c8243a": {
        "ModeS": "C8243A",
        "Registration": "ZK-NZM",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Air New Zealand",
        "OperatorFlagCode": "ANZ"
    },
    "a05ba2": {
        "ModeS": "A05BA2",
        "Registration": "N122FE",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 3S2F",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "76bd46": {
        "ModeS": "76BD46",
        "Registration": "9V-OJF",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Scoot",
        "OperatorFlagCode": "TGW"
    },
    "71c331": {
        "ModeS": "71C331",
        "Registration": "HL8331",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8JP/W",
        "RegisteredOwners": "Jeju Air",
        "OperatorFlagCode": "JJA"
    },
    "7583a7": {
        "ModeS": "7583A7",
        "Registration": "RP-C9918",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231SL",
        "RegisteredOwners": "Philippine Airlines",
        "OperatorFlagCode": "PAL"
    },
    "780236": {
        "ModeS": "780236",
        "Registration": "B-LAK",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "7809b6": {
        "ModeS": "7809B6",
        "Registration": "B-5707",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 85C/W",
        "RegisteredOwners": "XiamenAir",
        "OperatorFlagCode": "CXA"
    },
    "7816af": {
        "ModeS": "7816AF",
        "Registration": "B-MBO",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 271NSL",
        "RegisteredOwners": "Air Macau",
        "OperatorFlagCode": "AMU"
    },
    "a3a082": {
        "ModeS": "A3A082",
        "Registration": "N33262",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 824/W",
        "RegisteredOwners": "United Airlines",
        "OperatorFlagCode": "UAL"
    },
    "a21dc4": {
        "ModeS": "A21DC4",
        "Registration": "N2352U",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "United Airlines",
        "OperatorFlagCode": "UAL"
    },
    "8830f2": {
        "ModeS": "8830F2",
        "Registration": "HS-LGR",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737 8GP",
        "RegisteredOwners": "Thai Lion Air",
        "OperatorFlagCode": "TLM"
    },
    "71c259": {
        "ModeS": "71C259",
        "Registration": "HL8259",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 323E",
        "RegisteredOwners": "Asiana Airlines",
        "OperatorFlagCode": "AAR"
    },
    "899035": {
        "ModeS": "899035",
        "Registration": "B-16730",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "78179b": {
        "ModeS": "78179B",
        "Registration": "B-20CX",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B752",
        "Type": "757 236PCF/W",
        "RegisteredOwners": "SF Airlines",
        "OperatorFlagCode": "CSS"
    },
    "758774": {
        "ModeS": "758774",
        "Registration": "RP-C3909",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A339",
        "Type": "A330 941",
        "RegisteredOwners": "Cebu Pacific",
        "OperatorFlagCode": "CEB"
    },
    "8990bc": {
        "ModeS": "8990BC",
        "Registration": "B-58203",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 252NXSL",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "abfe45": {
        "ModeS": "ABFE45",
        "Registration": "N872FD",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "71c507": {
        "ModeS": "71C507",
        "Registration": "HL8507",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 86N/W",
        "RegisteredOwners": "Eastar Jet",
        "OperatorFlagCode": "ESR"
    },
    "8881f3": {
        "ModeS": "8881F3",
        "Registration": "VN-A548",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NX",
        "RegisteredOwners": "VietJet Air",
        "OperatorFlagCode": "VJC"
    },
    "a1f622": {
        "ModeS": "A1F622",
        "Registration": "N2251U",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "United Airlines",
        "OperatorFlagCode": "UAL"
    },
    "76bd41": {
        "ModeS": "76BD41",
        "Registration": "9V-OJA",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Scoot",
        "OperatorFlagCode": "TGW"
    },
    "78122a": {
        "ModeS": "78122A",
        "Registration": "B-8857",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "780a3a": {
        "ModeS": "780A3A",
        "Registration": "B-KQH",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 367ER",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "88596e": {
        "ModeS": "88596E",
        "Registration": "HS-VKN",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Thai VietJetAir",
        "OperatorFlagCode": "TVJ"
    },
    "8990a5": {
        "ModeS": "8990A5",
        "Registration": "B-18773",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "780a4e": {
        "ModeS": "780A4E",
        "Registration": "B-LPE",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "780e29": {
        "ModeS": "780E29",
        "Registration": "B-6060",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 84P/W",
        "RegisteredOwners": "Hainan Airlines",
        "OperatorFlagCode": "CHH"
    },
    "780195": {
        "ModeS": "780195",
        "Registration": "B-HYG",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343X",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "7801c6": {
        "ModeS": "7801C6",
        "Registration": "B-LAA",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 342",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "89907c": {
        "ModeS": "89907C",
        "Registration": "B-17882",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "8832ba": {
        "ModeS": "8832BA",
        "Registration": "HS-LUZ",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8GP/W",
        "RegisteredOwners": "Thai Lion Air",
        "OperatorFlagCode": "TLM"
    },
    "880846": {
        "ModeS": "880846",
        "Registration": "HS-BBF",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 216SL",
        "RegisteredOwners": "Thai AirAsia",
        "OperatorFlagCode": "AIQ"
    },
    "781228": {
        "ModeS": "781228",
        "Registration": "B-8855",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "8991b1": {
        "ModeS": "8991B1",
        "Registration": "B-18302",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "899014": {
        "ModeS": "899014",
        "Registration": "B-18778",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "780851": {
        "ModeS": "780851",
        "Registration": "B-6546",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A332",
        "Type": "A330 243",
        "RegisteredOwners": "Shanghai Airlines",
        "OperatorFlagCode": "CSH"
    },
    "781f39": {
        "ModeS": "781F39",
        "Registration": "B-32DT",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "Shenzhen Airlines",
        "OperatorFlagCode": "CSZ"
    },
    "789288": {
        "ModeS": "789288",
        "Registration": "B-KJE",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 83Z/W",
        "RegisteredOwners": "Greater Bay Airlines",
        "OperatorFlagCode": "HGB"
    },
    "7504b5": {
        "ModeS": "7504B5",
        "Registration": "9M-RAT",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 216SL",
        "RegisteredOwners": "AirAsia",
        "OperatorFlagCode": "AXM"
    },
    "8964b0": {
        "ModeS": "8964B0",
        "Registration": "A6-EVB",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A388",
        "Type": "A380 841",
        "RegisteredOwners": "Emirates Airline",
        "OperatorFlagCode": "UAE"
    },
    "789290": {
        "ModeS": "789290",
        "Registration": "B-HPR",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "780190": {
        "ModeS": "780190",
        "Registration": "B-HLP",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343X",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "885303": {
        "ModeS": "885303",
        "Registration": "HS-TXC",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Thai Airways International",
        "OperatorFlagCode": "THA"
    },
    "aaa893": {
        "ModeS": "AAA893",
        "Registration": "N786UA",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B772",
        "Type": "777 222ER",
        "RegisteredOwners": "United Airlines",
        "OperatorFlagCode": "UAL"
    },
    "758528": {
        "ModeS": "758528",
        "Registration": "RP-C8966",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 216SL",
        "RegisteredOwners": "Philippines AirAsia",
        "OperatorFlagCode": "APG"
    },
    "780850": {
        "ModeS": "780850",
        "Registration": "B-6543",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A332",
        "Type": "A330 243",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "8990be": {
        "ModeS": "8990BE",
        "Registration": "B-58205",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 252NXSL",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "76cc71": {
        "ModeS": "76CC71",
        "Registration": "9V-SCQ",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "Singapore Airlines",
        "OperatorFlagCode": "SIA"
    },
    "841b28": {
        "ModeS": "841B28",
        "Registration": "JA07JJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Jetstar Japan",
        "OperatorFlagCode": "JJP"
    },
    "8991d8": {
        "ModeS": "8991D8",
        "Registration": "B-58210",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 252NXSL",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "4cc45a": {
        "ModeS": "4CC45A",
        "Registration": "TF-AMP",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 481BCF",
        "RegisteredOwners": "Magma Aviation",
        "OperatorFlagCode": "ABD"
    },
    "780a99": {
        "ModeS": "780A99",
        "Registration": "B-LPN",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "79a04e": {
        "ModeS": "79A04E",
        "Registration": "B-6005",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "88809c": {
        "ModeS": "88809C",
        "Registration": "VN-A339",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Vietnam Airlines",
        "OperatorFlagCode": "HVN"
    },
    "780f0a": {
        "ModeS": "780F0A",
        "Registration": "B-8317",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "Juneyao Air",
        "OperatorFlagCode": "DKH"
    },
    "84c3fc": {
        "ModeS": "84C3FC",
        "Registration": "JA24JJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Jetstar Japan",
        "OperatorFlagCode": "JJP"
    },
    "7504cd": {
        "ModeS": "7504CD",
        "Registration": "9M-XXQ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "AirAsia X",
        "OperatorFlagCode": "XAX"
    },
    "780a71": {
        "ModeS": "780A71",
        "Registration": "B-LCJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Hong Kong Express Airways",
        "OperatorFlagCode": "HKE"
    },
    "78924c": {
        "ModeS": "78924C",
        "Registration": "B-HPG",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "846a5b": {
        "ModeS": "846A5B",
        "Registration": "JA14KZ",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B748",
        "Type": "747 8KZF",
        "RegisteredOwners": "Nippon Cargo Airlines",
        "OperatorFlagCode": "NCA"
    },
    "8990cf": {
        "ModeS": "8990CF",
        "Registration": "B-16332",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302X",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "8991e6": {
        "ModeS": "8991E6",
        "Registration": "B-58503",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "888093": {
        "ModeS": "888093",
        "Registration": "VN-A332",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Vietnam Airlines",
        "OperatorFlagCode": "HVN"
    },
    "899038": {
        "ModeS": "899038",
        "Registration": "B-16733",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "8991b5": {
        "ModeS": "8991B5",
        "Registration": "B-18307",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "885964": {
        "ModeS": "885964",
        "Registration": "HS-VKD",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Thai VietJetAir",
        "OperatorFlagCode": "TVJ"
    },
    "8990e6": {
        "ModeS": "8990E6",
        "Registration": "B-16725",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 35EER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "78108d": {
        "ModeS": "78108D",
        "Registration": "B-8653",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "71bf46": {
        "ModeS": "71BF46",
        "Registration": "HL7746",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 323E",
        "RegisteredOwners": "Asiana Airlines",
        "OperatorFlagCode": "AAR"
    },
    "8960f9": {
        "ModeS": "8960F9",
        "Registration": "A6-EDX",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A388",
        "Type": "A380 861",
        "RegisteredOwners": "Emirates Airline",
        "OperatorFlagCode": "UAE"
    },
    "88530e": {
        "ModeS": "88530E",
        "Registration": "HS-TXN",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Thai Airways International",
        "OperatorFlagCode": "THA"
    },
    "899084": {
        "ModeS": "899084",
        "Registration": "B-18667",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 800/W",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "7803ea": {
        "ModeS": "7803EA",
        "Registration": "B-6335",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "899057": {
        "ModeS": "899057",
        "Registration": "B-50021",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 271NSL",
        "RegisteredOwners": "Tigerair Taiwan",
        "OperatorFlagCode": "TTW"
    },
    "899104": {
        "ModeS": "899104",
        "Registration": "B-18718",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 409F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "88815c": {
        "ModeS": "88815C",
        "Registration": "VN-A693",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NSL",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "780a6a": {
        "ModeS": "780A6A",
        "Registration": "B-LPJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "a8bf91": {
        "ModeS": "A8BF91",
        "Registration": "N663CA",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 4HAERF",
        "RegisteredOwners": "National Airlines",
        "OperatorFlagCode": "NCR"
    },
    "781149": {
        "ModeS": "781149",
        "Registration": "B-8363",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "71c540": {
        "ModeS": "71C540",
        "Registration": "HL8540",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Aero K Airlines",
        "OperatorFlagCode": "EOK"
    },
    "780bc6": {
        "ModeS": "780BC6",
        "Registration": "B-1915",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 85C/W",
        "RegisteredOwners": "XiamenAir",
        "OperatorFlagCode": "CXA"
    },
    "3c4589": {
        "ModeS": "3C4589",
        "Registration": "D-AALI",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F6N",
        "RegisteredOwners": "AeroLogic",
        "OperatorFlagCode": "BOX"
    },
    "78086a": {
        "ModeS": "78086A",
        "Registration": "B-6885",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 232",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "8990bd": {
        "ModeS": "8990BD",
        "Registration": "B-58204",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 252NXSL",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "750493": {
        "ModeS": "750493",
        "Registration": "9M-RAI",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 216SL",
        "RegisteredOwners": "AirAsia",
        "OperatorFlagCode": "AXM"
    },
    "780a8d": {
        "ModeS": "780A8D",
        "Registration": "B-KQT",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 367ER",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "71c013": {
        "ModeS": "71C013",
        "Registration": "HL8013",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8SH/W",
        "RegisteredOwners": "Jin Air",
        "OperatorFlagCode": "JNA"
    },
    "8991bd": {
        "ModeS": "8991BD",
        "Registration": "B-18316",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "885305": {
        "ModeS": "885305",
        "Registration": "HS-TXE",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Thai Airways International",
        "OperatorFlagCode": "THA"
    },
    "8990ee": {
        "ModeS": "8990EE",
        "Registration": "B-18776",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "a67811": {
        "ModeS": "A67811",
        "Registration": "N516DN",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "Delta Air Lines",
        "OperatorFlagCode": "DAL"
    },
    "899000": {
        "ModeS": "899000",
        "Registration": "B-18901",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "7805c4": {
        "ModeS": "7805C4",
        "Registration": "B-6605",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 213",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "781ff2": {
        "ModeS": "781FF2",
        "Registration": "B-223Z",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 36NERBCF",
        "RegisteredOwners": "SF Airlines",
        "OperatorFlagCode": "CSS"
    },
    "780173": {
        "ModeS": "780173",
        "Registration": "B-HNK",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B773",
        "Type": "777 367",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "7801d4": {
        "ModeS": "7801D4",
        "Registration": "B-HSN",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Hong Kong Express Airways",
        "OperatorFlagCode": "HKE"
    },
    "8991a4": {
        "ModeS": "8991A4",
        "Registration": "B-18725",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 409F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "780e4a": {
        "ModeS": "780E4A",
        "Registration": "B-6490",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 85C/W",
        "RegisteredOwners": "XiamenAir",
        "OperatorFlagCode": "CXA"
    },
    "885968": {
        "ModeS": "885968",
        "Registration": "HS-VKH",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "Thai VietJetAir",
        "OperatorFlagCode": "TVJ"
    },
    "7811d8": {
        "ModeS": "7811D8",
        "Registration": "B-MCG",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231SL",
        "RegisteredOwners": "Air Macau",
        "OperatorFlagCode": "AMU"
    },
    "7816d5": {
        "ModeS": "7816D5",
        "Registration": "B-20AW",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B752",
        "Type": "757 236PCF/W",
        "RegisteredOwners": "SF Airlines",
        "OperatorFlagCode": "CSS"
    },
    "780a7b": {
        "ModeS": "780A7B",
        "Registration": "B-LNV",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A332",
        "Type": "A330 243F",
        "RegisteredOwners": "Hong Kong Air Cargo",
        "OperatorFlagCode": "HKC"
    },
    "89906d": {
        "ModeS": "89906D",
        "Registration": "B-16221",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "861f88": {
        "ModeS": "861F88",
        "Registration": "JA619J",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 346ER/W",
        "RegisteredOwners": "Japan Airlines",
        "OperatorFlagCode": "JAL"
    },
    "780478": {
        "ModeS": "780478",
        "Registration": "B-5385",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 86N/W",
        "RegisteredOwners": "XiamenAir",
        "OperatorFlagCode": "CXA"
    },
    "abd6ed": {
        "ModeS": "ABD6ED",
        "Registration": "N862GT",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B748",
        "Type": "747 8F",
        "RegisteredOwners": "Atlas Air",
        "OperatorFlagCode": "GTI"
    },
    "780bfb": {
        "ModeS": "780BFB",
        "Registration": "B-1816",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 213",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "78929a": {
        "ModeS": "78929A",
        "Registration": "B-LPS",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "780217": {
        "ModeS": "780217",
        "Registration": "B-LIA",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 467ERF",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "4bb142": {
        "ModeS": "4BB142",
        "Registration": "TC-LJB",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 3F2ER",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "ab87c8": {
        "ModeS": "AB87C8",
        "Registration": "N842FD",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 FHT",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "a1d546": {
        "ModeS": "A1D546",
        "Registration": "N217UA",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B772",
        "Type": "777 222ER",
        "RegisteredOwners": "United Airlines",
        "OperatorFlagCode": "UAL"
    },
    "861f66": {
        "ModeS": "861F66",
        "Registration": "JA618J",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 346ER/W",
        "RegisteredOwners": "Japan Airlines",
        "OperatorFlagCode": "JAL"
    },
    "7587fa": {
        "ModeS": "7587FA",
        "Registration": "RP-C3910",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A339",
        "Type": "A330 941",
        "RegisteredOwners": "Cebu Pacific",
        "OperatorFlagCode": "CEB"
    },
    "89916d": {
        "ModeS": "89916D",
        "Registration": "B-18916",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "885222": {
        "ModeS": "885222",
        "Registration": "HS-TQB",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B788",
        "Type": "787 8",
        "RegisteredOwners": "Thai Airways International",
        "OperatorFlagCode": "THA"
    },
    "78928e": {
        "ModeS": "78928E",
        "Registration": "B-KJH",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 83Z/W",
        "RegisteredOwners": "Greater Bay Airlines",
        "OperatorFlagCode": "HGB"
    },
    "899050": {
        "ModeS": "899050",
        "Registration": "B-16337",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "881427": {
        "ModeS": "881427",
        "Registration": "HS-EAG",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NX",
        "RegisteredOwners": "Thai AirAsia",
        "OperatorFlagCode": "AIQ"
    },
    "8990f0": {
        "ModeS": "8990F0",
        "Registration": "B-18111",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "781fd6": {
        "ModeS": "781FD6",
        "Registration": "B-223W",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 36NERBCF",
        "RegisteredOwners": "SF Airlines",
        "OperatorFlagCode": "CSS"
    },
    "781123": {
        "ModeS": "781123",
        "Registration": "B-1405",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 800/W",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "a91dba": {
        "ModeS": "A91DBA",
        "Registration": "N687FE",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A306",
        "Type": "A300 F4-605R",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "79a05f": {
        "ModeS": "79A05F",
        "Registration": "B-6010",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "4851b0": {
        "ModeS": "4851B0",
        "Registration": "PH-BHE",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "KLM Royal Dutch Airlines",
        "OperatorFlagCode": "KLM"
    },
    "781363": {
        "ModeS": "781363",
        "Registration": "B-1063",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "76cc61": {
        "ModeS": "76CC61",
        "Registration": "9V-SCA",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "Singapore Airlines",
        "OperatorFlagCode": "SIA"
    },
    "899063": {
        "ModeS": "899063",
        "Registration": "B-16338",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "76bcc8": {
        "ModeS": "76BCC8",
        "Registration": "9V-OFH",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B788",
        "Type": "787 8",
        "RegisteredOwners": "Scoot",
        "OperatorFlagCode": "TGW"
    },
    "84b40d": {
        "ModeS": "84B40D",
        "Registration": "JA203P",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 251NSL",
        "RegisteredOwners": "Peach Aviation",
        "OperatorFlagCode": "APJ"
    },
    "4bb188": {
        "ModeS": "4BB188",
        "Registration": "TC-LLH",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "899081": {
        "ModeS": "899081",
        "Registration": "B-16738",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "885223": {
        "ModeS": "885223",
        "Registration": "HS-TQC",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B788",
        "Type": "787 8",
        "RegisteredOwners": "Thai Airways International",
        "OperatorFlagCode": "THA"
    },
    "a66935": {
        "ModeS": "A66935",
        "Registration": "N512DN",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "Delta Air Lines",
        "OperatorFlagCode": "DAL"
    },
    "899134": {
        "ModeS": "899134",
        "Registration": "B-16785",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "aad780": {
        "ModeS": "AAD780",
        "Registration": "N798UA",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B772",
        "Type": "777 222ER",
        "RegisteredOwners": "United Airlines",
        "OperatorFlagCode": "UAL"
    },
    "8990da": {
        "ModeS": "8990DA",
        "Registration": "B-16711",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 35EER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "841ebc": {
        "ModeS": "841EBC",
        "Registration": "JA08JJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Jetstar Japan",
        "OperatorFlagCode": "JJP"
    },
    "888126": {
        "ModeS": "888126",
        "Registration": "VN-A675",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "84106c": {
        "ModeS": "84106C",
        "Registration": "JA04JJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Jetstar Japan",
        "OperatorFlagCode": "JJP"
    },
    "76bcc5": {
        "ModeS": "76BCC5",
        "Registration": "9V-OFE",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B788",
        "Type": "787 8",
        "RegisteredOwners": "Scoot",
        "OperatorFlagCode": "TGW"
    },
    "71c067": {
        "ModeS": "71C067",
        "Registration": "HL8067",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8Q8/W",
        "RegisteredOwners": "T way Air",
        "OperatorFlagCode": "TWB"
    },
    "71c357": {
        "ModeS": "71C357",
        "Registration": "HL8357",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Air Busan",
        "OperatorFlagCode": "ABL"
    },
    "89905e": {
        "ModeS": "89905E",
        "Registration": "B-50029",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 271N",
        "RegisteredOwners": "Tigerair Taiwan",
        "OperatorFlagCode": "TTW"
    },
    "780a54": {
        "ModeS": "780A54",
        "Registration": "B-LPI",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "899019": {
        "ModeS": "899019",
        "Registration": "B-18053",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 36NER",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "781f38": {
        "ModeS": "781F38",
        "Registration": "B-32DU",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "Shenzhen Airlines",
        "OperatorFlagCode": "CSZ"
    },
    "8990b2": {
        "ModeS": "8990B2",
        "Registration": "B-16216",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "781043": {
        "ModeS": "781043",
        "Registration": "B-1535",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 800/W",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "899072": {
        "ModeS": "899072",
        "Registration": "B-16226",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "71bf19": {
        "ModeS": "71BF19",
        "Registration": "HL7719",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B739",
        "Type": "737NG 9B5",
        "RegisteredOwners": "Jin Air",
        "OperatorFlagCode": "JNA"
    },
    "845f9f": {
        "ModeS": "845F9F",
        "Registration": "JA11KZ",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B748",
        "Type": "747 8KZF",
        "RegisteredOwners": "Nippon Cargo Airlines",
        "OperatorFlagCode": "NCA"
    },
    "4ba955": {
        "ModeS": "4BA955",
        "Registration": "TC-JJU",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 3F2ER",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "8990e5": {
        "ModeS": "8990E5",
        "Registration": "B-16723",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 36NER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "780927": {
        "ModeS": "780927",
        "Registration": "B-6931",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Spring Airlines",
        "OperatorFlagCode": "CQH"
    },
    "4bb18b": {
        "ModeS": "4BB18B",
        "Registration": "TC-LLK",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "8990ef": {
        "ModeS": "8990EF",
        "Registration": "B-18777",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "881425": {
        "ModeS": "881425",
        "Registration": "HS-EAE",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NX",
        "RegisteredOwners": "Thai AirAsia",
        "OperatorFlagCode": "AIQ"
    },
    "a026a5": {
        "ModeS": "A026A5",
        "Registration": "N109FE",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 3S2F",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "789277": {
        "ModeS": "789277",
        "Registration": "B-KJD",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8FH/W",
        "RegisteredOwners": "Greater Bay Airlines",
        "OperatorFlagCode": "HGB"
    },
    "76cc6a": {
        "ModeS": "76CC6A",
        "Registration": "9V-SCJ",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "Singapore Airlines",
        "OperatorFlagCode": "SIA"
    },
    "76cc72": {
        "ModeS": "76CC72",
        "Registration": "9V-SCR",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "Singapore Airlines",
        "OperatorFlagCode": "SIA"
    },
    "780a8f": {
        "ModeS": "780A8F",
        "Registration": "B-LPM",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "71c394": {
        "ModeS": "71C394",
        "Registration": "HL8394",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Air Busan",
        "OperatorFlagCode": "ABL"
    },
    "71c578": {
        "ModeS": "71C578",
        "Registration": "HL8578",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8EH/W",
        "RegisteredOwners": "Eastar Jet",
        "OperatorFlagCode": "ESR"
    },
    "899128": {
        "ModeS": "899128",
        "Registration": "B-18909",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "8963ef": {
        "ModeS": "8963EF",
        "Registration": "A6-EOR",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A388",
        "Type": "A380 861",
        "RegisteredOwners": "Emirates Airline",
        "OperatorFlagCode": "UAE"
    },
    "88596c": {
        "ModeS": "88596C",
        "Registration": "HS-VKL",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "Thai VietJetAir",
        "OperatorFlagCode": "TVJ"
    },
    "899121": {
        "ModeS": "899121",
        "Registration": "B-16781",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "781230": {
        "ModeS": "781230",
        "Registration": "B-8863",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "8832b9": {
        "ModeS": "8832B9",
        "Registration": "HS-LUY",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8GP/W",
        "RegisteredOwners": "Thai Lion Air",
        "OperatorFlagCode": "TLM"
    },
    "89916b": {
        "ModeS": "89916B",
        "Registration": "B-18915",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "8511ec": {
        "ModeS": "8511EC",
        "Registration": "JA317J",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 846/W",
        "RegisteredOwners": "Japan Airlines",
        "OperatorFlagCode": "JAL"
    },
    "899039": {
        "ModeS": "899039",
        "Registration": "B-16735",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "71bf54": {
        "ModeS": "71BF54",
        "Registration": "HL7754",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 323E",
        "RegisteredOwners": "Asiana Airlines",
        "OperatorFlagCode": "AAR"
    },
    "781e2b": {
        "ModeS": "781E2B",
        "Registration": "B-222J",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "China Cargo Airlines",
        "OperatorFlagCode": "CKK"
    },
    "ac01fc": {
        "ModeS": "AC01FC",
        "Registration": "N873FD",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "a7ef40": {
        "ModeS": "A7EF40",
        "Registration": "N610FE",
        "Manufacturer": "McDonnell Douglas",
        "ICAOTypeCode": "MD11",
        "Type": "MD-11 F",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "769103": {
        "ModeS": "769103",
        "Registration": "9V-DHC",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "Singapore Airlines",
        "OperatorFlagCode": "SIA"
    },
    "89901c": {
        "ModeS": "89901C",
        "Registration": "B-18002",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 309ER",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "781f3a": {
        "ModeS": "781F3A",
        "Registration": "B-32DS",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "Shenzhen Airlines",
        "OperatorFlagCode": "CSZ"
    },
    "7810eb": {
        "ModeS": "7810EB",
        "Registration": "B-8957",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231SL",
        "RegisteredOwners": "Juneyao Air",
        "OperatorFlagCode": "DKH"
    },
    "71c565": {
        "ModeS": "71C565",
        "Registration": "HL8565",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 85R/W",
        "RegisteredOwners": "T way Air",
        "OperatorFlagCode": "TWB"
    },
    "89913e": {
        "ModeS": "89913E",
        "Registration": "B-17888",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787-9 Dreamliner",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "899058": {
        "ModeS": "899058",
        "Registration": "B-50022",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 271NSL",
        "RegisteredOwners": "Tigerair Taiwan",
        "OperatorFlagCode": "TTW"
    },
    "885177": {
        "ModeS": "885177",
        "Registration": "HS-TKW",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 3D7ER",
        "RegisteredOwners": "Thai Airways International",
        "OperatorFlagCode": "THA"
    },
    "76cc70": {
        "ModeS": "76CC70",
        "Registration": "9V-SCP",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "Singapore Airlines",
        "OperatorFlagCode": "SIA"
    },
    "71c329": {
        "ModeS": "71C329",
        "Registration": "HL8329",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8KN/W",
        "RegisteredOwners": "T way Air",
        "OperatorFlagCode": "TWB"
    },
    "780e3f": {
        "ModeS": "780E3F",
        "Registration": "B-8018",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "76cc67": {
        "ModeS": "76CC67",
        "Registration": "9V-SCG",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "Singapore Airlines",
        "OperatorFlagCode": "SIA"
    },
    "88516c": {
        "ModeS": "88516C",
        "Registration": "HS-TKL",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 3ALER",
        "RegisteredOwners": "Thai Airways International",
        "OperatorFlagCode": "THA"
    },
    "78927a": {
        "ModeS": "78927A",
        "Registration": "B-LKA",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E(P2F)",
        "RegisteredOwners": "Air Hong Kong",
        "OperatorFlagCode": "AHK"
    },
    "899025": {
        "ModeS": "899025",
        "Registration": "B-50005",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Tigerair Taiwan",
        "OperatorFlagCode": "TTW"
    },
    "71c055": {
        "ModeS": "71C055",
        "Registration": "HL8055",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Air Busan",
        "OperatorFlagCode": "ABL"
    },
    "7583ed": {
        "ModeS": "7583ED",
        "Registration": "RP-C9926",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231SL",
        "RegisteredOwners": "Philippine Airlines",
        "OperatorFlagCode": "PAL"
    },
    "8991e7": {
        "ModeS": "8991E7",
        "Registration": "B-58504",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "885310": {
        "ModeS": "885310",
        "Registration": "HS-TXP",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Thai Airways International",
        "OperatorFlagCode": "THA"
    },
    "8881f4": {
        "ModeS": "8881F4",
        "Registration": "VN-A549",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NX",
        "RegisteredOwners": "VietJet Air",
        "OperatorFlagCode": "VJC"
    },
    "781619": {
        "ModeS": "781619",
        "Registration": "B-306F",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 251NSL",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "780368": {
        "ModeS": "780368",
        "Registration": "B-MCA",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231SL",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "899013": {
        "ModeS": "899013",
        "Registration": "B-18903",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "71c536": {
        "ModeS": "71C536",
        "Registration": "HL8536",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "Korean Air",
        "OperatorFlagCode": "KAL"
    },
    "758707": {
        "ModeS": "758707",
        "Registration": "RP-C3905",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A339",
        "Type": "A330 941N",
        "RegisteredOwners": "Cebu Pacific Air",
        "OperatorFlagCode": "CEB"
    },
    "899125": {
        "ModeS": "899125",
        "Registration": "B-18908",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "8991df": {
        "ModeS": "8991DF",
        "Registration": "B-58304",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A339",
        "Type": "A330 941N",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "485343": {
        "ModeS": "485343",
        "Registration": "PH-BHI",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "KLM Royal Dutch Airlines",
        "OperatorFlagCode": "KLM"
    },
    "780aa1": {
        "ModeS": "780AA1",
        "Registration": "B-LCI",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Hong Kong Express Airways",
        "OperatorFlagCode": "HKE"
    },
    "781054": {
        "ModeS": "781054",
        "Registration": "B-6996",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 338ERBCF",
        "RegisteredOwners": "SF Airlines",
        "OperatorFlagCode": "CSS"
    },
    "781601": {
        "ModeS": "781601",
        "Registration": "B-MCJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Air Macau",
        "OperatorFlagCode": "AMU"
    },
    "780a6d": {
        "ModeS": "780A6D",
        "Registration": "B-LNP",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343X",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "89631d": {
        "ModeS": "89631D",
        "Registration": "A6-EFM",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F1H",
        "RegisteredOwners": "Emirates Airline",
        "OperatorFlagCode": "UAE"
    },
    "86d629": {
        "ModeS": "86D629",
        "Registration": "JA825P",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Peach Aviation",
        "OperatorFlagCode": "APJ"
    },
    "7bb057": {
        "ModeS": "7BB057",
        "Registration": "B-2988",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B733",
        "Type": "737 36RSF",
        "RegisteredOwners": "SF Airlines",
        "OperatorFlagCode": "CSS"
    },
    "8880ac": {
        "ModeS": "8880AC",
        "Registration": "VN-A601",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Vietnam Airlines",
        "OperatorFlagCode": "HVN"
    },
    "895056": {
        "ModeS": "895056",
        "Registration": "V8-RBB",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 251NSL",
        "RegisteredOwners": "Royal Brunei Airlines",
        "OperatorFlagCode": "RBA"
    },
    "7801a3": {
        "ModeS": "7801A3",
        "Registration": "B-HYI",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343X",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "8880f4": {
        "ModeS": "8880F4",
        "Registration": "VN-A663",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "8990eb": {
        "ModeS": "8990EB",
        "Registration": "B-18775",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "71bd61": {
        "ModeS": "71BD61",
        "Registration": "HL7561",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8B5/W",
        "RegisteredOwners": "Jin Air",
        "OperatorFlagCode": "JNA"
    },
    "8990dd": {
        "ModeS": "8990DD",
        "Registration": "B-16715",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 35EER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "899053": {
        "ModeS": "899053",
        "Registration": "B-16211",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "8991da": {
        "ModeS": "8991DA",
        "Registration": "B-58212",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 252NXSL",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "a5fff9": {
        "ModeS": "A5FFF9",
        "Registration": "N486MC",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B744",
        "Type": "747 45EF",
        "RegisteredOwners": "Atlas Air",
        "OperatorFlagCode": "GTI"
    },
    "7801ad": {
        "ModeS": "7801AD",
        "Registration": "B-HYJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343X",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "84cb5b": {
        "ModeS": "84CB5B",
        "Registration": "JA26LR",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Jetstar Japan",
        "OperatorFlagCode": "JJP"
    },
    "8990ca": {
        "ModeS": "8990CA",
        "Registration": "B-58509",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "STARLUX",
        "OperatorFlagCode": "SJX"
    },
    "780e5b": {
        "ModeS": "780E5B",
        "Registration": "B-6988",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 85N/W",
        "RegisteredOwners": "Shandong Airlines",
        "OperatorFlagCode": "CDG"
    },
    "888185": {
        "ModeS": "888185",
        "Registration": "VN-A507",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 272NSL",
        "RegisteredOwners": "Vietnam Airlines",
        "OperatorFlagCode": "HVN"
    },
    "780b92": {
        "ModeS": "780B92",
        "Registration": "B-2506",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B734",
        "Type": "737 429SF",
        "RegisteredOwners": "SF Airlines",
        "OperatorFlagCode": "CSS"
    },
    "781df9": {
        "ModeS": "781DF9",
        "Registration": "B-222D",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 38EERBCF/W",
        "RegisteredOwners": "SF Airlines",
        "OperatorFlagCode": "CSS"
    },
    "780869": {
        "ModeS": "780869",
        "Registration": "B-6883",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 232",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "750263": {
        "ModeS": "750263",
        "Registration": "9M-MUA",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A332",
        "Type": "A330 223F",
        "RegisteredOwners": "Malaysia Airlines",
        "OperatorFlagCode": "MAS"
    },
    "7806f4": {
        "ModeS": "7806F4",
        "Registration": "B-5576",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 86NBCF/W",
        "RegisteredOwners": "China Postal Airlines",
        "OperatorFlagCode": "CYZ"
    },
    "75833a": {
        "ModeS": "75833A",
        "Registration": "RP-C8766",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Philippine Airlines",
        "OperatorFlagCode": "PAL"
    },
    "899077": {
        "ModeS": "899077",
        "Registration": "B-16335",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "89900e": {
        "ModeS": "89900E",
        "Registration": "B-16740",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "71c246": {
        "ModeS": "71C246",
        "Registration": "HL8246",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8SH/W",
        "RegisteredOwners": "Jin Air",
        "OperatorFlagCode": "JNA"
    },
    "8830f6": {
        "ModeS": "8830F6",
        "Registration": "HS-LGV",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737 8GP",
        "RegisteredOwners": "Thai Lion Air",
        "OperatorFlagCode": "TLM"
    },
    "89905d": {
        "ModeS": "89905D",
        "Registration": "B-50028",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 271N",
        "RegisteredOwners": "Tigerair Taiwan",
        "OperatorFlagCode": "TTW"
    },
    "899020": {
        "ModeS": "899020",
        "Registration": "B-18007",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 309ER",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "861bd2": {
        "ModeS": "861BD2",
        "Registration": "JA608J",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B763",
        "Type": "767 346ER/W",
        "RegisteredOwners": "Japan Airlines",
        "OperatorFlagCode": "JAL"
    },
    "8990e3": {
        "ModeS": "8990E3",
        "Registration": "B-16721",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 35EER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "885962": {
        "ModeS": "885962",
        "Registration": "HS-VKB",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214SL",
        "RegisteredOwners": "Thai VietJetAir",
        "OperatorFlagCode": "TVJ"
    },
    "78090e": {
        "ModeS": "78090E",
        "Registration": "B-6942",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 232",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "8990d6": {
        "ModeS": "8990D6",
        "Registration": "B-16707",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 35EER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "88817d": {
        "ModeS": "88817D",
        "Registration": "VN-A536",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "780a6c": {
        "ModeS": "780A6C",
        "Registration": "B-LNO",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "a1f1a0": {
        "ModeS": "A1F1A0",
        "Registration": "N224UA",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B772",
        "Type": "777 222ER",
        "RegisteredOwners": "United Airlines",
        "OperatorFlagCode": "UAL"
    },
    "78009d": {
        "ModeS": "78009D",
        "Registration": "B-8967",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343E",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "899160": {
        "ModeS": "899160",
        "Registration": "B-18912",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "4d0117": {
        "ModeS": "4D0117",
        "Registration": "LX-VCM",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B748",
        "Type": "747 8R7F",
        "RegisteredOwners": "Cargolux Airlines International",
        "OperatorFlagCode": "CLX"
    },
    "71c260": {
        "ModeS": "71C260",
        "Registration": "HL8260",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8BK/W",
        "RegisteredOwners": "Jeju Air",
        "OperatorFlagCode": "JJA"
    },
    "71bf55": {
        "ModeS": "71BF55",
        "Registration": "HL7755",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B772",
        "Type": "777 28EER",
        "RegisteredOwners": "Asiana Airlines",
        "OperatorFlagCode": "AAR"
    },
    "789287": {
        "ModeS": "789287",
        "Registration": "B-KKH",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Hong Kong Express Airways",
        "OperatorFlagCode": "HKE"
    },
    "8991b4": {
        "ModeS": "8991B4",
        "Registration": "B-18306",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "8880ab": {
        "ModeS": "8880AB",
        "Registration": "VN-A399",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Vietnam Airlines",
        "OperatorFlagCode": "HVN"
    },
    "78929b": {
        "ModeS": "78929B",
        "Registration": "B-LHP",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "780bda": {
        "ModeS": "780BDA",
        "Registration": "B-5940",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 323X",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "885965": {
        "ModeS": "885965",
        "Registration": "HS-VKE",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Thai VietJetAir",
        "OperatorFlagCode": "TVJ"
    },
    "89902f": {
        "ModeS": "89902F",
        "Registration": "B-16726",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 35EER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "a6456d": {
        "ModeS": "A6456D",
        "Registration": "N503DN",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "Delta Air Lines",
        "OperatorFlagCode": "DAL"
    },
    "89910a": {
        "ModeS": "89910A",
        "Registration": "B-18103",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "89900d": {
        "ModeS": "89900D",
        "Registration": "B-16739",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 300ER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "71c324": {
        "ModeS": "71C324",
        "Registration": "HL8324",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8AS/W",
        "RegisteredOwners": "T way Air",
        "OperatorFlagCode": "TWB"
    },
    "899120": {
        "ModeS": "899120",
        "Registration": "B-17812",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B78X",
        "Type": "787 10",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "780490": {
        "ModeS": "780490",
        "Registration": "B-5390",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 89L/W",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "899028": {
        "ModeS": "899028",
        "Registration": "B-50008",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Tigerair Taiwan",
        "OperatorFlagCode": "TTW"
    },
    "780aa3": {
        "ModeS": "780AA3",
        "Registration": "B-LRC",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "ab8b7f": {
        "ModeS": "AB8B7F",
        "Registration": "N843FD",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 FHT",
        "RegisteredOwners": "FedEx Express",
        "OperatorFlagCode": "FDX"
    },
    "4bb14c": {
        "ModeS": "4BB14C",
        "Registration": "TC-LJL",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "789297": {
        "ModeS": "789297",
        "Registration": "B-LPT",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Hong Kong Airlines",
        "OperatorFlagCode": "CRK"
    },
    "8990e8": {
        "ModeS": "8990E8",
        "Registration": "B-18106",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "84b495": {
        "ModeS": "84B495",
        "Registration": "JA207P",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 251NSL",
        "RegisteredOwners": "Peach Aviation",
        "OperatorFlagCode": "APJ"
    },
    "84c790": {
        "ModeS": "84C790",
        "Registration": "JA25JJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Jetstar Japan",
        "OperatorFlagCode": "JJP"
    },
    "780268": {
        "ModeS": "780268",
        "Registration": "B-5157",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 81QBCF/W",
        "RegisteredOwners": "China Postal Airlines",
        "OperatorFlagCode": "CYZ"
    },
    "84b3c9": {
        "ModeS": "84B3C9",
        "Registration": "JA201P",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 251NSL",
        "RegisteredOwners": "Peach Aviation",
        "OperatorFlagCode": "APJ"
    },
    "7586cf": {
        "ModeS": "7586CF",
        "Registration": "RP-C3902",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A339",
        "Type": "A330 941N",
        "RegisteredOwners": "Cebu Pacific Air",
        "OperatorFlagCode": "CEB"
    },
    "8991d5": {
        "ModeS": "8991D5",
        "Registration": "B-58207",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 252NXSL",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "71c248": {
        "ModeS": "71C248",
        "Registration": "HL8248",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B739",
        "Type": "737NG 9B5ER/W",
        "RegisteredOwners": "Korean Air",
        "OperatorFlagCode": "KAL"
    },
    "89906b": {
        "ModeS": "89906B",
        "Registration": "B-16220",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "7801b0": {
        "ModeS": "7801B0",
        "Registration": "B-HNN",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B773",
        "Type": "777 367",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "758550": {
        "ModeS": "758550",
        "Registration": "RP-C8976",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 216",
        "RegisteredOwners": "Philippines AirAsia",
        "OperatorFlagCode": "APG"
    },
    "899031": {
        "ModeS": "899031",
        "Registration": "B-16728",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 36NER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "71c032": {
        "ModeS": "71C032",
        "Registration": "HL8032",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 8GJ/W",
        "RegisteredOwners": "Jeju Air",
        "OperatorFlagCode": "JJA"
    },
    "8990d4": {
        "ModeS": "8990D4",
        "Registration": "B-16705",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 35EER",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "8990a0": {
        "ModeS": "8990A0",
        "Registration": "B-18771",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "China Airlines",
        "OperatorFlagCode": "CAL"
    },
    "8991db": {
        "ModeS": "8991DB",
        "Registration": "B-58213",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Starlux Airlines",
        "OperatorFlagCode": "SJX"
    },
    "781e34": {
        "ModeS": "781E34",
        "Registration": "B-222K",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "China Cargo Airlines",
        "OperatorFlagCode": "CKK"
    },
    "76bd44": {
        "ModeS": "76BD44",
        "Registration": "9V-OJD",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B789",
        "Type": "787 9",
        "RegisteredOwners": "Scoot",
        "OperatorFlagCode": "TGW"
    },
    "71c328": {
        "ModeS": "71C328",
        "Registration": "HL8328",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232",
        "RegisteredOwners": "Air Busan",
        "OperatorFlagCode": "ABL"
    },
    "86d64b": {
        "ModeS": "86D64B",
        "Registration": "JA826P",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 214",
        "RegisteredOwners": "Peach Aviation",
        "OperatorFlagCode": "APJ"
    },
    "899123": {
        "ModeS": "899123",
        "Registration": "B-16782",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "758616": {
        "ModeS": "758616",
        "Registration": "RP-C4122",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "Cebu Pacific Air",
        "OperatorFlagCode": "CEB"
    },
    "789295": {
        "ModeS": "789295",
        "Registration": "B-KKL",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Hong Kong Express Airways",
        "OperatorFlagCode": "HKE"
    },
    "75025c": {
        "ModeS": "75025C",
        "Registration": "9M-MTI",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 323E",
        "RegisteredOwners": "Malaysia Airlines",
        "OperatorFlagCode": "MAS"
    },
    "881423": {
        "ModeS": "881423",
        "Registration": "HS-EAC",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Thai AirAsia",
        "OperatorFlagCode": "AIQ"
    },
    "888172": {
        "ModeS": "888172",
        "Registration": "VN-A530",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 271NXSL",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "780e22": {
        "ModeS": "780E22",
        "Registration": "B-1531",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 89L/W",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "780c26": {
        "ModeS": "780C26",
        "Registration": "B-6457",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A319",
        "Type": "A319 132SL",
        "RegisteredOwners": "China Eastern Airlines",
        "OperatorFlagCode": "CES"
    },
    "88808e": {
        "ModeS": "88808E",
        "Registration": "VN-A327",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 231",
        "RegisteredOwners": "Vietnam Airlines",
        "OperatorFlagCode": "HVN"
    },
    "88813e": {
        "ModeS": "88813E",
        "Registration": "VN-A635",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "VietJetAir",
        "OperatorFlagCode": "VJC"
    },
    "780e75": {
        "ModeS": "780E75",
        "Registration": "B-6496",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 89L/W",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "89904f": {
        "ModeS": "89904F",
        "Registration": "B-16209",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 211SL",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "789270": {
        "ModeS": "789270",
        "Registration": "B-KJC",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 800/W",
        "RegisteredOwners": "Greater Bay Airlines",
        "OperatorFlagCode": "HGB"
    },
    "8990d0": {
        "ModeS": "8990D0",
        "Registration": "B-16333",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 302X",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    },
    "8990c1": {
        "ModeS": "8990C1",
        "Registration": "B-58507",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A359",
        "Type": "A350 941",
        "RegisteredOwners": "STARLUX",
        "OperatorFlagCode": "SJX"
    },
    "7801b9": {
        "ModeS": "7801B9",
        "Registration": "B-HYQ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A333",
        "Type": "A330 343X",
        "RegisteredOwners": "Cathay Pacific Airways",
        "OperatorFlagCode": "CPA"
    },
    "71c272": {
        "ModeS": "71C272",
        "Registration": "HL8272",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B739",
        "Type": "737NG 9B5ER/W",
        "RegisteredOwners": "Korean Air",
        "OperatorFlagCode": "KAL"
    },
    "84b5ac": {
        "ModeS": "84B5AC",
        "Registration": "JA20JJ",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A320",
        "Type": "A320 232SL",
        "RegisteredOwners": "Jetstar Japan",
        "OperatorFlagCode": "JJP"
    },
    "84ceef": {
        "ModeS": "84CEEF",
        "Registration": "JA27LR",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A21N",
        "Type": "A321 251NXSL",
        "RegisteredOwners": "Jetstar Japan",
        "OperatorFlagCode": "JJP"
    },
    "780033": {
        "ModeS": "780033",
        "Registration": "B-2832",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B752",
        "Type": "757 2Z0PCF",
        "RegisteredOwners": "SF Airlines",
        "OperatorFlagCode": "CSS"
    },
    "84b473": {
        "ModeS": "84B473",
        "Registration": "JA206P",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A20N",
        "Type": "A320 251NSL",
        "RegisteredOwners": "Peach Aviation",
        "OperatorFlagCode": "APJ"
    },
    "4ba945": {
        "ModeS": "4BA945",
        "Registration": "TC-JJE",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77W",
        "Type": "777 3F2ER",
        "RegisteredOwners": "Turkish Airlines",
        "OperatorFlagCode": "THY"
    },
    "7802f3": {
        "ModeS": "7802F3",
        "Registration": "B-5193",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B738",
        "Type": "737NG 81B/W",
        "RegisteredOwners": "China Southern Airlines",
        "OperatorFlagCode": "CSN"
    },
    "780acc": {
        "ModeS": "780ACC",
        "Registration": "B-9919",
        "Manufacturer": "Airbus",
        "ICAOTypeCode": "A321",
        "Type": "A321 213",
        "RegisteredOwners": "Air China",
        "OperatorFlagCode": "CCA"
    },
    "89912d": {
        "ModeS": "89912D",
        "Registration": "B-16787",
        "Manufacturer": "Boeing",
        "ICAOTypeCode": "B77L",
        "Type": "777 F",
        "RegisteredOwners": "EVA Air",
        "OperatorFlagCode": "EVA"
    }
}
