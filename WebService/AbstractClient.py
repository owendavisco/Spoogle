from abc import ABCMeta, abstractmethod, abstractproperty


class AbstractClient:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getTrackById(self, id):
        pass

    @abstractmethod
    def getTrackByName(self, name):
        pass

    @abstractmethod
    def getAllTrack(self):
        pass

    @abstractmethod
    def getPlaylistById(self, id):
        pass

    @abstractmethod
    def getAllPlaylists(self):
        pass


