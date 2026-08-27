# --- openscope --- #

# earth's radius
EARTH_R = 6371000  # in meter

M_TO_KM = 0.001
NM_TO_KM = 1.852
FT_TO_KM = 0.0003048

M_TO_NM = M_TO_KM / NM_TO_KM
FT_TO_NM = FT_TO_KM / NM_TO_KM

# --- dataset --- #

HAMPEL_WINDOW_SIZE = 21

NORM_FEATURES = [
    #
    'x_nm',
    'y_nm',
    'z_nm',
    #
    # --- #
    #
    'y',
    'x',
    #
    'altitude',
    #
    'speed',
    #
    # --- #
    #
    'd1_y',
    'd1_x',
    'd1_altitude',
    #
    'd2_y',
    'd2_x',
    'd2_altitude',
    #
    # --- #
    #
    'd_y',
    'd_x',
    'd_altitude',
    #
    's_y',
    's_x',
    's_altitude',
    #
]

# match the fn. _sample_multiple_xyz_nm()
XYZ_FEATURES = ['x_nm', 'y_nm', 'z_nm']

# NOTE: This is a FIXED table; it should not be altered after the model has been trained.
# Some logic is also coupled with this table.
IN_FEATURES = [
    #
    'y',
    'x',
    #
    'altitude',
    #
    'heading-sin',
    'heading-cos',
    #
    'speed',
    #
    # --- #
    #
    'd1_y',
    'd1_x',
    'd1_altitude',
    #
    'd2_y',
    'd2_x',
    'd2_altitude',
    #
]

OUT_FEATURES = [
    #
    'y',
    'x',
    'altitude',
    #
]
OUT_SHIFT_FEATURES = [
    #
    's_y',
    's_x',
    's_altitude',
    #
]

# --- icao --- #

CALLSIGN_ICAO = [
    'ANA',  # All Nippon Airways
    'JAL',  # Japan Airlines
    'SKY',  # Skymark Airlines
    'SFJ',  # StarFlyer
    'SNJ',  # Solaseed Air
    'ADO',  # AIRDO
    'DAL',  # Delta Air Lines
    'UAL',  # United Airlines
    'AAR',  # Asiana Airlines
    'KAL',  # Korean Air
    'CES',  # China Eastern
    'AAL',  # American Airlines
    'CSN',  # China Southern Airlines
    'SIA',  # Singapore Airlines
    'HKE',  # Hong Kong Express
    'APJ',  # Peach Aviation
    'CCA',  # Air China
    'BAW',  # British Airways
    'DLH',  # Lufthansa
    'PAL',  # Philippine Airlines
    'EVA',  # EVA AIR
    'CPA',  # Cathay Pacific
    'AFR',  # Air France
    'CSH',  # Shanghai Airlines
    'THA',  # Thai Airways International
    'CAL',  # China Airlines
    'QFA',  # Qantas Airways
    'VJC',  # VietJetAir
    'UAE',  # Emirates
    'THY',  # Turkish Airlines
    'TTW',  # Tigerair Taiwan
    'ACA',  # Air Canada
    'GIA',  # Garuda Indonesia
    'ITY',  # ITA Airways
    'XAX',  # AirAsia X
    'FIN',  # Finnair
    'HVN',  # Vietnam Airlines
    'HAL',  # Hawaiian Airlines
    'CQH',  # Spring Airlines
    'GCR',  # Tianjin Airlines
    'SAS',  # Scandinavian Airlines
    'DKH',  # Juneyao Airlines
    'VOZ',  # Virgin Australia
    # 'VJT',  # VistaJet Holding SA
    # 'TBJ',  # TAG Aviation Asia
    # 'JAK',  # Masling Airlines
    # 'JTA',  # Japan Transocean Air
    #
    'SJX',  # STARLUX Airlines
    'TGW',  # Scoot
    'AMU',  # Air Macau
    'TLM',  # Thai Lion Air
    'TVJ',  # Thai Vietjet Air
    'CRK',  # Hong Kong Airlines
    'JJP',  # Jetstar Japan
    'AIQ',  # Thai AirAsia
    'JNA',  # Jin Air
    'FDX',  # FedEx Express
    'ESR',  # Eastar Jet
    'CXA',  # Xiamen Air
    'APG',  # Philippines AirAsia
    'HGB',  # Greater Bay Airlines
    'CSS',  # SF Airlines
    'CEB',  # Cebu Pacific
    'TWB',  # T'way Airlines
    'ABL',  # Air Busan
    'JJA',  # JEJU Air
    'KLM',  # KLM Royal Dutch Airlines
    'CSZ',  # Shenzhen Airlines
    'MXD',  # Batik Air Malaysia
    'MAS',  # Malaysia Airlines
    'UPS',  # UPS Airlines
    'CHH',  # Hainan Airlines
    'HKC',  # Hong Kong Air Cargo
    'UIA',  # UNI AIR
    'CKK',  # China Cargo Airlines
]
"""
The airlines sorted by the number of arrivals during the period
from July 24, 2024, to July 31, 2024, at RJTT airport.
"""

# NOTE: This is a FIXED table; it should not be altered after the model has been trained.
MODEL_ICAO = [
    'A20N',
    'A21N',
    'A320',
    'A321',
    'A332',
    'A333',
    'A339',
    'A359',
    'A35K',
    'B38M',
    'B737',
    'B738',
    'B748',
    'B763',
    'B772',
    'B773',
    'B77W',
    'B788',
    'B789',
    'B78X',
]

# --- #

AIRPORTS = {
    'RCTP': {
        'magnetic_north': -5,  # degree
        #
        'position': [25.08027, 121.23222, 108],  # N25d04m39.83 E121d13m58.16
        'MSA': 1700,  # feet
        #
        # NOTE: This is a FIXED table; it should not be altered after the model has been trained.
        'runways_order': ['05L', '23R', '05R', '23L'],
        'runways': {
            '05L': {
                'this': (25.07289, 121.21598),
                'other': (25.09449, 121.24344),
                'ils': True,
            },
            '23R': {
                'this': (25.09449, 121.24344),
                'other': (25.07289, 121.21598),
                'ils': True,
            },
            '05R': {
                'this': (25.06143, 121.22424),
                'other': (25.08120, 121.24936),
                'ils': True,
            },
            '23L': {
                'this': (25.08120, 121.24936),
                'other': (25.06143, 121.22424),
                'ils': True,
            },
        },
    },
    'RJTT': {
        'magnetic_north': -7,  # degree
        #
        'position': [35.55333, 139.78111, 0],  # N35d33m12.00 E139d46m52.00
        'MSA': 1700,  # feet
        #
        # NOTE: This is a FIXED table; it should not be altered after the model has been trained.
        'runways_order': ['04', '22', '05', '23', '16L', '34R', '16R', '34L'],
        'runways': {
            '04': {
                'this': (35.54902, 139.76128),
                'other': (35.56747, 139.77711),
                'ils': False,
            },
            '22': {
                'this': (35.56747, 139.77711),
                'other': (35.54902, 139.76128),
                'ils': True,
            },
            #
            '05': {
                'this': (35.52400, 139.80346),
                'other': (35.54060, 139.82211),
                'ils': False,
            },
            '23': {
                'this': (35.54060, 139.82211),
                'other': (35.52400, 139.80346),
                'ils': True,
            },
            #
            '16L': {
                'this': (35.56590, 139.78655),
                'other': (35.53969, 139.80514),
                'ils': True,
            },
            '34R': {
                'this': (35.53969, 139.80514),
                'other': (35.56590, 139.78655),
                'ils': True,
            },
            #
            '16R': {
                'this': (35.55999, 139.76907),
                'other': (35.53660, 139.78567),
                'ils': True,
            },
            '34L': {
                'this': (35.53660, 139.78567),
                'other': (35.55999, 139.76907),
                'ils': True,
            },
        },
    }
}
