DROP TABLE IF EXISTS reports;
DROP TABLE IF EXISTS not_found;

CREATE TABLE reports (
  scan_id TEXT NOT NULL,
  resource TEXT NOT NULL,
  url TEXT NOT NULL,
  response_code INTEGER NOT NULL,
  scan_date TEXT NOT NULL,
  permalink TEXT NOT NULL,
  verbose_msg TEXT NOT NULL,
  filescan_id TEXT,
  positives TEXT NOT NULL,
  total TEXT NOT NULL
);

CREATE TABLE not_found (
    response_code TEXT NOT NULL,
    resource TEXT NOT NULL,
    verbose_msg TEXT NOT NULL
);

CREATE TABLE file_reports (
  scan_id TEXT NOT NULL,
  sha1 TEXt NOT NULL,
  resource TEXT NOT NULL,
  response_code TEXT NOT NULL,
  scan_date TEXT NOT NULL,
  permalink TEXT NOT NULL,
  verbose_msg TEXT NOT NULL,
  total TEXT NOT NULL,
  positives TEXT NOT NULL,
  sha256 TEXT NOT NULL
);

CREATE TABLE file_not_found (
    response_code TEXT NOT NULL,
    resource TEXT NOT NULL,
    verbose_msg TEXT NOT NULL
);