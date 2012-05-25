# encoding: utf-8
require 'sqlite3'

db = SQLite3::Database.new "db/bestia.db"
# db.results_as_hash = true

parishes = [
    'Malbork',
    'Morąg',
    'Orzysz',
    'Oława',
    'Pszczyna',
    'Rabka-Zdrój',
    'Ruda Śląska',
    'Rybnik',
    'Skarżysko-Kamienna',
    'Stronie Śląskie',
    'Strzegom',
    'Szczecin',
    'Wrocław'
]
results = []

parishes.each do |name|
  query  = "SELECT poviat, parish, part, subpart, paragraph, source, income "
  query += "FROM income "
  query += "WHERE (parish = '#{name}' OR poviat = '#{name}') "
  query += "AND (subpart LIKE '%%alkohol%%' OR paragraph LIKE '%%alkohol%%')"

  results << db.execute( query )
end

puts results
