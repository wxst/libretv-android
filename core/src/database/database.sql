CREATE TABLE IF NOT EXISTS Country(
  id_country INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50),
  code VARCHAR(5),
  flag VARCHAR(2),
  PRIMARY KEY (id_country)
);
CREATE TABLE IF NOT EXISTS Language(
  id_language INT NOT NULL AUTO_INCREMENT,
  name TINYTEXT NOT NULL,
  code VARCHAR(3) NOT NULL,
  PRIMARY KEY (id_language)
);
CREATE TABLE IF NOT EXISTS Country_Language(
  id_country INT NOT NULL,
  id_language INT NOT NULL,
  FOREIGN KEY (id_country) REFERENCES Country(id_country),
  FOREIGN KEY (id_language) REFERENCES Language(id_language),
  PRIMARY KEY (id_country, id_language)
);
CREATE TABLE IF NOT EXISTS Category(
  id_category INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_category)
);
CREATE TABLE IF NOT EXISTS Subdivision(
  id_subdivision INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  code VARCHAR(6) NOT NULL,
  PRIMARY KEY (id_subdivision)
);
CREATE TABLE IF NOT EXISTS Subdivision_Country(
  id_subdivision INT NOT NULL,
  id_country INT NOT NULL,
  FOREIGN KEY (id_subdivision) REFERENCES Subdivision(id_subdivision),
  FOREIGN KEY (id_country) REFERENCES Country(id_country),
  PRIMARY KEY (id_subdivision, id_country)
);
CREATE TABLE IF NOT EXISTS Channel(
  id_channel INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  alt_names TINYTEXT,
  network TINYTEXT,
  owners TEXT,
  id_country INT,
  id_subdivision INT,
  broadcast_area TINYTEXT,
  city VARCHAR(50),
  is_nsfw BOOLEAN NOT NULL,
  launched DATE,
  closed DATE,
  replaced_by VARCHAR(50),
  website VARCHAR(2083),
  logo VARCHAR(2083),
  FOREIGN KEY (id_subdivision) REFERENCES Subdivision(id_subdivision),
  FOREIGN KEY (id_country) REFERENCES Country(id_country),
  PRIMARY KEY (id_channel)
);
CREATE TABLE IF NOT EXISTS Channel_Language(
  id_channel INT NOT NULL,
  id_language INT NOT NULL,
  FOREIGN KEY (id_channel) REFERENCES Channel(id_channel),
  FOREIGN KEY (id_language) REFERENCES Language(id_language),
  PRIMARY KEY (id_channel, id_language)
);
CREATE TABLE IF NOT EXISTS Channel_Category(
  id_channel INT NOT NULL,
  id_category INT NOT NULL,
  FOREIGN KEY (id_channel) REFERENCES Channel(id_channel),
  FOREIGN KEY (id_category) REFERENCES Category(id_category),
  PRIMARY KEY (id_channel, id_category)
);
CREATE TABLE IF NOT EXISTS BlockList(
  id_blocklist INT NOT NULL,
  id_channel INT NOT NULL,
  ref VARCHAR(2083) NOT NULL,
  FOREIGN KEY (id_channel) REFERENCES Channel(id_channel),
  PRIMARY KEY (id_blocklist)
);
CREATE TABLE IF NOT EXISTS Stream(
  id_stream INT NOT NULL AUTO_INCREMENT,
  id_channel INT NOT NULL,
  name TINYTEXT NOT NULL,
  resolution VARCHAR(5),
  label VARCHAR(15),
  url VARCHAR(2083) NOT NULL,
  FOREIGN KEY (id_channel) REFERENCES Channel(id_channel),
  PRIMARY KEY (id_stream)
);
CREATE TABLE IF NOT EXISTS Epg(
  id_epg INT NOT NULL AUTO_INCREMENT,
  id_channel INT NOT NULL,
  source VARCHAR(50),
  id_language INT NOT NULL,
  site_id VARCHAR(50),
  channel_name VARCHAR(50),
  FOREIGN KEY (id_channel) REFERENCES Channel(id_channel),
  FOREIGN KEY (id_language) REFERENCES Language(id_language),
  PRIMARY KEY(id_epg)
);
