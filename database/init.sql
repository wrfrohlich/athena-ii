CREATE TABLE raw_data (
    NAME TEXT,
    SURNAME TEXT,
    ECG REAL,
    EDA REAL,
    EMG REAL,
    TIME TEXT
);

CREATE TABLE heart_rate (
    NAME TEXT,
    SURNAME TEXT,
    HEART_RATE REAL,
    HEART_RATE_TS REAL
);

CREATE TABLE ecg (
    NAME TEXT,
    SURNAME TEXT,
    ECG REAL,
    ECG_TS REAL
);

CREATE TABLE eda (
    NAME TEXT,
    SURNAME TEXT,
    EDA REAL,
    EDA_TS REAL
);

CREATE TABLE emg (
    NAME TEXT,
    SURNAME TEXT,
    EMG REAL,
    EMG_TS REAL
);