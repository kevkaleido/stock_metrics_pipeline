# ============================================================
# BENCHMARKS — Used to compare all stock performance against
# ============================================================
BENCHMARKS = [
    "^GSPC",   # S&P 500
    "^NDX",    # NASDAQ 100
    "^DJI",    # Dow Jones Industrial Average
    "URTH",    # MSCI World ETF
]


# ============================================================
# INDICES
# ============================================================

# --- US Broad Market ---
US_BROAD = [
    "^GSPC",   # S&P 500
    "^IXIC",   # NASDAQ Composite
    "^NDX",    # NASDAQ 100
    "^DJI",    # Dow Jones Industrial Average
    "^RUT",    # Russell 2000
    "^RUI",    # Russell 1000
    "^MID",    # S&P 400 Mid-Cap
    "^SML",    # S&P 600 Small-Cap
    "^W5000",  # Wilshire 5000
    "^NYA",    # NYSE Composite
]

# --- US Sector ETF-Indices ---
US_SECTORS = [
    "XLK",   # Technology
    "XLF",   # Financials
    "XLE",   # Energy
    "XLV",   # Health Care
    "XLI",   # Industrials
    "XLY",   # Consumer Discretionary
    "XLP",   # Consumer Staples
    "XLU",   # Utilities
    "XLRE",  # Real Estate
    "XLB",   # Materials
    "XLC",   # Communication Services
]

# --- Europe ---
EUROPE_INDICES = [
    "^FTSE",    # UK FTSE 100
    "^FTMC",    # UK FTSE 250
    "^FTAS",    # UK FTSE All-Share
    "^GDAXI",   # Germany DAX 40
    "^MDAXI",   # Germany MDAX
    "^TECDAX",  # Germany TecDAX
    "^SDAXI",   # Germany SDAX
    "^FCHI",    # France CAC 40
    "^SSMI",    # Switzerland SMI
    "^AEX",     # Netherlands AEX
    "^BFX",     # Belgium BEL 20
    "^IBEX",    # Spain IBEX 35
    "^OMX",     # Sweden OMX Stockholm 30
    "^OMXC25",  # Denmark OMX Copenhagen 25
    "^OMXH25",  # Finland OMX Helsinki 25
    "^OBX",     # Norway Oslo OBX
    "^ATX",     # Austria ATX
    "^WIG20",   # Poland WIG 20
    "^BUX",     # Hungary BUX
    "^ATG",     # Greece Athens General
    "^ISEQ",    # Ireland ISEQ
    "^XU100",   # Turkey BIST 100
]

# --- Asia-Pacific ---
ASIA_PACIFIC_INDICES = [
    "^N225",      # Japan Nikkei 225
    "^TOPX",      # Japan TOPIX
    "^HSI",       # Hong Kong Hang Seng
    "^HSCE",      # Hong Kong Hang Seng China Enterprises
    "^HSTECH",    # Hong Kong Hang Seng Tech
    "000001.SS",  # China Shanghai Composite
    "000300.SS",  # China CSI 300
    "399001.SZ",  # China Shenzhen Component
    "^BSESN",     # India BSE Sensex
    "^NSEI",      # India Nifty 50
    "^NSEBANK",   # India Nifty Bank
    "^KS11",      # South Korea KOSPI
    "^KQ11",      # South Korea KOSDAQ
    "^TWII",      # Taiwan Weighted
    "^STI",       # Singapore STI
    "^KLSE",      # Malaysia KLCI
    "^JKSE",      # Indonesia IDX Composite
    "^SET.BK",    # Thailand SET
    "^AXJO",      # Australia ASX 200
    "^AORD",      # Australia All Ordinaries
    "^NZ50",      # New Zealand NZX 50
]

# --- Americas ---
AMERICAS_INDICES = [
    "^BVSP",    # Brazil Bovespa
    "^MXX",     # Mexico IPC
    "^MERV",    # Argentina MERVAL
    "^IPSA",    # Chile S&P/CLX IPSA
    "^GSPTSE",  # Canada S&P/TSX Composite
]

# --- Middle East & Africa ---
MEA_INDICES = [
    "^TASI.SR",  # Saudi Arabia Tadawul
    "^DFMGI",    # UAE Dubai DFM General
    "^TA35.TA",  # Israel TA-35
    "^CASE30",   # Egypt EGX 30
    "^J203.JO",  # South Africa JSE All-Share
    "^J200.JO",  # South Africa JSE Top 40
]

# --- Global Equity ETF-Indices ---
GLOBAL_ETF_INDICES = [
    "EEM",   # MSCI Emerging Markets
    "EFA",   # MSCI EAFE (Developed ex-US)
    "VT",    # FTSE All-World
    "FM",    # MSCI Frontier Markets
    "AFK",   # MSCI Africa
    "VNQI",  # Global Real Estate
    "IGF",   # Global Infrastructure
    "ICLN",  # Global Clean Energy
    "IXN",   # Global Tech
    "IXJ",   # Global Healthcare
    "IXG",   # Global Financials
]

# --- Alternative Assets (for diversification comparison) ---
ALTERNATIVE_ASSETS = [
    "GLD",  # Gold
    "SLV",  # Silver
    "AGG",  # US Bonds Aggregate
    "TLT",  # US Treasury 20yr+
    "DBC",  # Bloomberg Commodity
]

# --- All Indices Combined ---
ALL_INDICES = (
    US_BROAD +
    US_SECTORS +
    EUROPE_INDICES +
    ASIA_PACIFIC_INDICES +
    AMERICAS_INDICES +
    MEA_INDICES +
    GLOBAL_ETF_INDICES +
    ALTERNATIVE_ASSETS
)


# ============================================================
# STOCKS
# ============================================================

# --- US Tech ---
US_TECH = [
    "AAPL", "MSFT", "NVDA", "GOOGL", "GOOG", "META", "AMZN", "TSLA",
    "AMD", "INTC", "AVGO", "ORCL", "CRM", "ADBE", "QCOM", "TXN",
    "IBM", "UBER", "SNOW", "PLTR", "NOW", "NFLX", "MRVL", "MU",
    "AMAT", "LRCX", "PANW", "ZS", "CRWD", "NET", "DDOG", "SHOP",
    "SQ", "PYPL", "ANET", "FTNT", "OKTA", "TEAM", "WDAY", "VEEV",
    "ZM", "DOCU", "MDB", "HUBS", "PATH", "APP", "TTD", "ROKU",
    "SNAP", "PINS", "TWLO", "U", "RBLX", "COIN", "HOOD", "IOT",
    "ENPH", "FSLR", "ON", "SWKS", "MPWR", "ENTG", "ILMN",
    "DKNG", "CELH",
]

# --- US Finance ---
US_FINANCE = [
    "JPM", "BAC", "WFC", "GS", "MS", "C", "BLK", "AXP", "V", "MA",
    "SCHW", "BRK-B", "PGR", "MET", "PRU", "CB", "ICE", "CME",
    "SPGI", "MCO", "USB", "TFC", "PNC", "COF", "DFS", "SYF",
    "ALLY", "RF", "FITB", "HBAN", "KEY", "CFG", "MTB", "NTRS",
    "STT", "BK", "TROW", "IVZ", "AMG", "FDS", "FIS", "FISV",
    "GPN", "WEX", "PAYO", "FOUR", "LMND", "RKT", "PFSI", "COOP",
]

# --- US Healthcare ---
US_HEALTHCARE = [
    "JNJ", "UNH", "PFE", "MRK", "ABBV", "TMO", "ABT", "LLY",
    "MDT", "CVS", "ISRG", "REGN", "GILD", "VRTX", "BMY", "ZTS",
    "DXCM", "SYK", "BSX", "EW", "BDX", "BAX", "CAH", "MCK",
    "CNC", "HUM", "CI", "HCA", "THC", "UHS", "DVA", "IQV",
    "CRL", "ICLR", "MEDP", "INCY", "ALNY", "BIIB", "SRPT",
    "BMRN", "RARE", "BEAM", "EDIT", "EXAS", "NTRA", "ILMN",
]

# --- US Energy ---
US_ENERGY = [
    "XOM", "CVX", "COP", "EOG", "SLB", "PSX", "VLO", "OXY",
    "MPC", "KMI", "WMB", "DVN", "HAL", "BKR", "HES", "MRO",
    "APA", "CTRA", "EQT", "RRC", "AR", "LNG", "ET",
]

# --- US Consumer Discretionary ---
US_CONSUMER_DISC = [
    "WMT", "HD", "MCD", "NKE", "SBUX", "TGT", "COST", "LULU",
    "F", "GM", "TJX", "ROST", "BKNG", "ABNB", "EXPE", "MAR",
    "HLT", "CCL", "RCL", "NCLH", "DRI", "YUM", "CMG", "DPZ",
    "ORLY", "AZO", "KMX", "AN", "LAD", "ETSY", "CHWY",
    "CVNA", "LYFT", "DASH",
]

# --- US Consumer Staples ---
US_CONSUMER_STAPLES = [
    "PG", "KO", "PEP", "PM", "MO", "MDLZ", "GIS", "K", "CPB",
    "CAG", "SJM", "HRL", "TSN", "MKC", "CLX", "CHD", "EL",
    "CL", "KMB", "STZ",
]

# --- US Industrials ---
US_INDUSTRIALS = [
    "BA", "CAT", "GE", "HON", "RTX", "LMT", "UPS", "FDX",
    "AMT", "MMM", "DE", "EMR", "ETN", "WM", "CARR", "OTIS",
    "GD", "NOC", "LHX", "TDG", "AXON", "CTAS", "RSG", "VRSK",
    "FAST", "GWW", "IR", "XYL", "PCAR",
]

# --- US Real Estate ---
US_REAL_ESTATE = [
    "PLD", "SPG", "EQIX", "O", "PSA", "CCI", "SBAC", "DLR",
    "EXR", "AVB", "EQR", "MAA", "UDR", "NNN",
]

# --- US Materials ---
US_MATERIALS = [
    "LIN", "APD", "SHW", "ECL", "PPG", "NEM", "FCX", "NUE",
    "STLD", "RS", "ALB", "MOS", "CF", "VMC", "MLM",
]

# --- US Utilities ---
US_UTILITIES = [
    "NEE", "DUK", "SO", "D", "AEP", "EXC", "SRE", "PEG",
    "XEL", "ES", "WEC", "ETR", "FE", "PPL", "CMS",
]

# --- UK ---
UK_STOCKS = [
    "SHEL.L",  # Shell
    "BP.L",    # BP
    "HSBC.L",  # HSBC
    "AZN.L",   # AstraZeneca
    "GSK.L",   # GSK
    "ULVR.L",  # Unilever
    "RIO.L",   # Rio Tinto
    "AAL.L",   # Anglo American
    "VOD.L",   # Vodafone
    "LLOY.L",  # Lloyds Banking
    "BARC.L",  # Barclays
    "AAF.L",   # Airtel Africa
    "BATS.L",  # British American Tobacco
    "DGE.L",   # Diageo
    "EXPN.L",  # Experian
    "LSEG.L",  # London Stock Exchange Group
    "NG.L",    # National Grid
    "SSE.L",   # SSE
    "PRU.L",   # Prudential
    "STAN.L",  # Standard Chartered
    "GLEN.L",  # Glencore
    "BT-A.L",  # BT Group
    "IMB.L",   # Imperial Brands
    "REL.L",   # RELX
    "WPP.L",   # WPP
]

# --- Europe (ex-UK) ---
EUROPE_STOCKS = [
    "ASML.AS",    # ASML — Netherlands
    "INGA.AS",    # ING Group — Netherlands
    "PHIA.AS",    # Philips — Netherlands
    "ABN.AS",     # ABN AMRO — Netherlands
    "MC.PA",      # LVMH — France
    "TTE.PA",     # TotalEnergies — France
    "SAN.PA",     # Sanofi — France
    "OR.PA",      # L'Oreal — France
    "BNP.PA",     # BNP Paribas — France
    "CS.PA",      # AXA — France
    "RMS.PA",     # Hermes — France
    "KER.PA",     # Kering — France
    "SGO.PA",     # Saint-Gobain — France
    "VIE.PA",     # Veolia — France
    "SAP.DE",     # SAP — Germany
    "SIE.DE",     # Siemens — Germany
    "ALV.DE",     # Allianz — Germany
    "ADS.DE",     # Adidas — Germany
    "BAS.DE",     # BASF — Germany
    "MBG.DE",     # Mercedes-Benz — Germany
    "BMW.DE",     # BMW — Germany
    "DTE.DE",     # Deutsche Telekom — Germany
    "MUV2.DE",    # Munich Re — Germany
    "DBK.DE",     # Deutsche Bank — Germany
    "VOW3.DE",    # Volkswagen — Germany
    "LHA.DE",     # Lufthansa — Germany
    "NESN.SW",    # Nestle — Switzerland
    "NOVN.SW",    # Novartis — Switzerland
    "ROG.SW",     # Roche — Switzerland
    "AIR.PA",     # Airbus — France/EU
    "ABI.BR",     # AB InBev — Belgium
    "NOVO-B.CO",  # Novo Nordisk — Denmark
    "ENI.MI",     # Eni — Italy
    "ENEL.MI",    # Enel — Italy
    "ISP.MI",     # Intesa Sanpaolo — Italy
    "UCG.MI",     # UniCredit — Italy
    "SKG.L",      # Smurfit Kappa — Ireland
]

# --- Japan ---
JAPAN_STOCKS = [
    "7203.T",  # Toyota
    "9984.T",  # SoftBank
    "6758.T",  # Sony
    "6861.T",  # Keyence
    "7974.T",  # Nintendo
    "8306.T",  # Mitsubishi UFJ
    "8316.T",  # Sumitomo Mitsui
    "8411.T",  # Mizuho
    "6501.T",  # Hitachi
    "6702.T",  # Fujitsu
    "6752.T",  # Panasonic
    "6902.T",  # Denso
    "7267.T",  # Honda
    "7751.T",  # Canon
    "8035.T",  # Tokyo Electron
    "9432.T",  # NTT
    "9433.T",  # KDDI
    "9437.T",  # NTT Docomo
    "4063.T",  # Shin-Etsu Chemical
    "4502.T",  # Takeda Pharma
    "4503.T",  # Astellas Pharma
    "6594.T",  # Nidec
    "6981.T",  # Murata Manufacturing
]

# --- South Korea ---
KOREA_STOCKS = [
    "005930.KS",  # Samsung Electronics
    "000660.KS",  # SK Hynix
    "051910.KS",  # LG Chem
    "005380.KS",  # Hyundai Motor
    "005490.KS",  # POSCO
    "012330.KS",  # Hyundai Mobis
    "028260.KS",  # Samsung C&T
    "035420.KS",  # NAVER
    "035720.KS",  # Kakao
    "068270.KS",  # Celltrion
    "105560.KS",  # KB Financial
    "207940.KS",  # Samsung Biologics
    "373220.KS",  # LG Energy Solution
]

# --- Hong Kong ---
HK_STOCKS = [
    "9988.HK",  # Alibaba
    "0700.HK",  # Tencent
    "1299.HK",  # AIA Group
    "2318.HK",  # Ping An Insurance
    "3690.HK",  # Meituan
    "0941.HK",  # China Mobile
    "1810.HK",  # Xiaomi
    "0005.HK",  # HSBC Holdings
    "0011.HK",  # Hang Seng Bank
    "0016.HK",  # Sun Hung Kai Properties
    "0027.HK",  # Galaxy Entertainment
    "0066.HK",  # MTR Corporation
    "0388.HK",  # HK Exchanges
    "0762.HK",  # China Unicom
    "1038.HK",  # CK Infrastructure
    "1093.HK",  # CSPC Pharma
    "2388.HK",  # BOC Hong Kong
]

# --- China (US-listed ADRs) ---
CHINA_ADR = [
    "BABA",  # Alibaba
    "JD",    # JD.com
    "PDD",   # PDD Holdings
    "NIO",   # NIO
    "BIDU",  # Baidu
    "2330.TW",  # TSMC Taiwan
]

# --- Taiwan ---
TAIWAN_STOCKS = [
    "TSM",     # TSMC (US-listed)
    "2330.TW", # TSMC (Taiwan-listed)
]

# --- Australia ---
AUSTRALIA_STOCKS = [
    "BHP.AX",  # BHP Group
    "CBA.AX",  # Commonwealth Bank
    "CSL.AX",  # CSL Limited
    "NAB.AX",  # National Australia Bank
    "WBC.AX",  # Westpac
    "ANZ.AX",  # ANZ Bank
    "WES.AX",  # Wesfarmers
    "MQG.AX",  # Macquarie Group
    "RIO.AX",  # Rio Tinto
    "FMG.AX",  # Fortescue Metals
    "WOW.AX",  # Woolworths
    "TCL.AX",  # Transurban
    "TLS.AX",  # Telstra
    "STO.AX",  # Santos
    "ORG.AX",  # Origin Energy
    "AMC.AX",  # Amcor
    "ALL.AX",  # Aristocrat Leisure
    "COL.AX",  # Coles Group
    "QBE.AX",  # QBE Insurance
    "SHL.AX",  # Sonic Healthcare
]

# --- Singapore ---
SINGAPORE_STOCKS = [
    "D05.SI",   # DBS Bank
    "O39.SI",   # OCBC Bank
    "U11.SI",   # UOB Bank
    "Z74.SI",   # Singapore Telecom
    "V03.SI",   # Venture Corporation
    "BN4.SI",   # Keppel Corp
    "C6L.SI",   # Singapore Airlines
    "G13.SI",   # Genting Singapore
    "H78.SI",   # Hongkong Land
    "C38U.SI",  # CapitaLand Integrated Commercial Trust
]

# --- India ---
INDIA_STOCKS = [
    "RELIANCE.NS",    # Reliance Industries
    "TCS.NS",         # Tata Consultancy Services
    "HDFCBANK.NS",    # HDFC Bank
    "INFY.NS",        # Infosys
    "ICICIBANK.NS",   # ICICI Bank
    "HINDUNILVR.NS",  # Hindustan Unilever
    "SBIN.NS",        # State Bank of India
    "BHARTIARTL.NS",  # Bharti Airtel
    "KOTAKBANK.NS",   # Kotak Mahindra Bank
    "WIPRO.NS",       # Wipro
    "AXISBANK.NS",    # Axis Bank
    "MARUTI.NS",      # Maruti Suzuki
    "SUNPHARMA.NS",   # Sun Pharmaceutical
    "TATAMOTORS.NS",  # Tata Motors
    "TATASTEEL.NS",   # Tata Steel
    "BAJFINANCE.NS",  # Bajaj Finance
    "NESTLEIND.NS",   # Nestle India
    "ULTRACEMCO.NS",  # UltraTech Cement
    "POWERGRID.NS",   # Power Grid Corp
    "NTPC.NS",        # NTPC
    "ONGC.NS",        # Oil & Natural Gas Corp
    "COALINDIA.NS",   # Coal India
    "DIVISLAB.NS",    # Divi's Laboratories
    "DRREDDY.NS",     # Dr. Reddy's Laboratories
    "CIPLA.NS",       # Cipla
]

# --- Latin America ---
LATAM_STOCKS = [
    "ITUB",      # Itau Unibanco — Brazil ADR
    "VALE",      # Vale — Brazil ADR
    "PBR",       # Petrobras — Brazil ADR
    "ABEV",      # Ambev — Brazil ADR
    "SID",       # CSN — Brazil ADR
    "GGB",       # Gerdau — Brazil ADR
    "CIB",       # Bancolombia — Colombia ADR
    "EC",        # Ecopetrol — Colombia ADR
    "MELI",      # MercadoLibre — Argentina/LatAm
    "GLOB",      # Globant — Argentina ADR
    "DESP",      # Despegar — Argentina ADR
    "PETR4.SA",  # Petrobras — Brazil
    "WEGE3.SA",  # WEG — Brazil
    "LREN3.SA",  # Lojas Renner — Brazil
]

# --- Africa (JSE & US-listed) ---
AFRICA_STOCKS = [
    "NPN.JO",  # Naspers — South Africa
    "MTN.JO",  # MTN Group — South Africa
    "SOL.JO",  # Sasol — South Africa
    "ANG.JO",  # AngloGold Ashanti — South Africa
    "FSR.JO",  # Firstrand — South Africa
    "MFC.JO",  # Old Mutual — South Africa
    "GOLD",    # Barrick Gold — US-listed, Africa ops
    "HMY",     # Harmony Gold — US-listed
]


# ============================================================
# ALL STOCKS COMBINED
# ============================================================
ALL_STOCKS = (
    US_TECH +
    US_FINANCE +
    US_HEALTHCARE +
    US_ENERGY +
    US_CONSUMER_DISC +
    US_CONSUMER_STAPLES +
    US_INDUSTRIALS +
    US_REAL_ESTATE +
    US_MATERIALS +
    US_UTILITIES +
    UK_STOCKS +
    EUROPE_STOCKS +
    JAPAN_STOCKS +
    KOREA_STOCKS +
    HK_STOCKS +
    CHINA_ADR +
    TAIWAN_STOCKS +
    AUSTRALIA_STOCKS +
    SINGAPORE_STOCKS +
    INDIA_STOCKS +
    LATAM_STOCKS +
    AFRICA_STOCKS
)


# ============================================================
# QUICK SUMMARY
# ============================================================
if __name__ == "__main__":
    print(f"Benchmarks      : {len(BENCHMARKS)}")
    print(f"Total Indices   : {len(ALL_INDICES)}")
    print(f"Total Stocks    : {len(ALL_STOCKS)}")
    print(f"Grand Total     : {len(ALL_INDICES) + len(ALL_STOCKS)}")