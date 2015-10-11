
from PyQt4.QtSql import QSqlDatabase, QSqlQuery
from PyQt4.QtGui import QStringListModel

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
    
    def get_song_pattern(self, song_name):
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
            pass  # Should raise a some kind of error
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
    
    def get_song_listmodel(self, key = None, parent = None):
        """Create and return a QStringListModel of songs in database
        By default all songs are included
        @param key: Include only songs in given key
        @param key: String
        @return: List model to be passed to QListView
        @type return: QStringListModel"""
        if key == None:
            query = QSqlQuery()
            query.prepare("SELECT song FROM Patterns")
            success = query.exec_()
            if not success:
                pass  # TODO
            songs = [], 
            while query.next():
                songs.append(query.value(0))
        else:
            songs = self.get_by_key(key)
        return QStringListModel(songs, parent)
    
    def remove_song(self, song_name):
        """Removes given song from database
        @param song_name: name of the song to be removed
        @type song_name: String"""
        query = QSqlQuery()
        query.prepare("DELETE FROM Patterns WHERE song == :song")
        query.bindValue(":song", song_name)
        success = query.exec_()
        if not success:
            return  False # TODO
        return True
    
    def add_song(self, song_name, pattern, key):
        """Add a new song to database
        @param song_name: name of the song shown in QListView
        @type song_name: String
        @param pattern: chord pattern of the song
        @type pattern: String
        @param key: key of the song. Used as filter parameter
        @type key: String"""
        query = QSqlQuery()
        query.prepare("INSERT INTO Patterns(song, pattern, key) VALUES (:song, :pattern, :key)")
        query.bindValue(":song", song_name)
        query.bindValue(":pattern", pattern)
        query.bindValue(":key", key)
        success = query.exec_()
        if not success:
            return False  # TODO
        return True
        