
from PyQt4.QtSql import QSqlDatabase, QSqlQuery
from _csv import Error

DATABASE_NAME = "progressions.db" # Saa vaihtaa

class DatabaseManager:
    
    def __init__(self):
        """Handles all database events"""
        self.db = self.create_connection()
        self.create_table()
    
    def create_connection(self):
        """Create connection to progressions.db, Create if not exists
        @return: QSqlDatabase"""
        db = QSqlDatabase.addDatabase("QSQLITE")  # QSqlDriver = SQLITE, default connection
        db.setDatabaseName(DATABASE_NAME)
        if not db.open():
            pass  # Should raise a some kind of Error
        return db
    
    def create_table(self):
        """Create table Progression(song, pattern, key) if not exist already"""
        # Tablen nimen saa vaihtaa
        query = QSqlQuery()
        query.prepare("CREATE TABLE IF NOT EXISTS Progressions(song TEXT PRIMARY KEY, pattern TEXT, key TEXT)")
        query.exec_()
    
    def get_song(self, song_name):
        """Get chord pattern of given song
        @param song_name: name of the song in database
        @type song_name: String
        @return: pattern
        @type return: String"""
        query = QSqlQuery()
        query.prepare("SELECT pattern FROM Progressions WHERE song == :song")
        query.bindValue(":song", song_name)
        success = query.exec_()
        if not success:
            pass  # Should raise a some kind of Error
        query.next()  # Get only the first result as song name is primary key.
        return query.value(0) # pattern is the only column in result set.
    
    def get_by_key(self, key):
        """Get all chord patterns in given key
        @param key: Song key e.g. C major
        @type key: String
        @return: all patterns in key
        @type return: list"""
        query = QSqlQuery()
        query.prepare("SELECT pattern FROM Progressions WHERE key == :key")
        query.bindValue(":key", key)
        success = query.exec_()
        if not success:
            pass  # TODO
        patterns = [] 
        while query.next():
            patterns.append(query.value(0))
        return patterns
    
        
    