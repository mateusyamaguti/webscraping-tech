# webscraping-tech

```text
webscraping-tech/

│
├── venv/
│
├── src/
│   │
│   ├── config/
│   │      └── settings.py
│   │
│   ├── core/
│   │      ├── http_client.py
│   │      ├── base_scraper.py
│   │      ├── exceptions.py
│   │      └── constants.py
│   │
│   ├── models/
│   │      └── news.py
│   │
│   ├── scrapers/
│   │      ├── arstechnica_scraper.py
│   │      ├── ieee_spectrum_scraper.py
│   │      ├── olhardigital_scraper.py
│   │      └── techtudo_scraper.py
│   │
│   ├── utils/
│   │      ├── url_builder.py
│   │      ├── validators.py
│   │      └── helpers.py
│   │
│   └── main.py
│
├── tests/
│      ├── test_arstechnica.py
│      ├── test_ieee.py
│      ├── test_olhardigital.py
│      └── test_techtudo.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore

```