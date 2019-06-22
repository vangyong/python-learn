# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.2
#
# <auto-generated>
#
# Generated from file `FileServer.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module FileServer
_M_FileServer = Ice.openModule('FileServer')
__name__ = 'FileServer'

if '_t_Bytes' not in _M_FileServer.__dict__:
    _M_FileServer._t_Bytes = IcePy.defineSequence('::FileServer::Bytes', (), IcePy._t_byte)

if 'FileInfo' not in _M_FileServer.__dict__:
    _M_FileServer.FileInfo = Ice.createTempClass()
    class FileInfo(object):
        def __init__(self, creattime=0, updatetime=0, filesize=0, filescore=0, filename='', filetype='', filepath=''):
            self.creattime = creattime
            self.updatetime = updatetime
            self.filesize = filesize
            self.filescore = filescore
            self.filename = filename
            self.filetype = filetype
            self.filepath = filepath

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.creattime)
            _h = 5 * _h + Ice.getHash(self.updatetime)
            _h = 5 * _h + Ice.getHash(self.filesize)
            _h = 5 * _h + Ice.getHash(self.filescore)
            _h = 5 * _h + Ice.getHash(self.filename)
            _h = 5 * _h + Ice.getHash(self.filetype)
            _h = 5 * _h + Ice.getHash(self.filepath)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_FileServer.FileInfo):
                return NotImplemented
            else:
                if self.creattime is None or other.creattime is None:
                    if self.creattime != other.creattime:
                        return (-1 if self.creattime is None else 1)
                else:
                    if self.creattime < other.creattime:
                        return -1
                    elif self.creattime > other.creattime:
                        return 1
                if self.updatetime is None or other.updatetime is None:
                    if self.updatetime != other.updatetime:
                        return (-1 if self.updatetime is None else 1)
                else:
                    if self.updatetime < other.updatetime:
                        return -1
                    elif self.updatetime > other.updatetime:
                        return 1
                if self.filesize is None or other.filesize is None:
                    if self.filesize != other.filesize:
                        return (-1 if self.filesize is None else 1)
                else:
                    if self.filesize < other.filesize:
                        return -1
                    elif self.filesize > other.filesize:
                        return 1
                if self.filescore is None or other.filescore is None:
                    if self.filescore != other.filescore:
                        return (-1 if self.filescore is None else 1)
                else:
                    if self.filescore < other.filescore:
                        return -1
                    elif self.filescore > other.filescore:
                        return 1
                if self.filename is None or other.filename is None:
                    if self.filename != other.filename:
                        return (-1 if self.filename is None else 1)
                else:
                    if self.filename < other.filename:
                        return -1
                    elif self.filename > other.filename:
                        return 1
                if self.filetype is None or other.filetype is None:
                    if self.filetype != other.filetype:
                        return (-1 if self.filetype is None else 1)
                else:
                    if self.filetype < other.filetype:
                        return -1
                    elif self.filetype > other.filetype:
                        return 1
                if self.filepath is None or other.filepath is None:
                    if self.filepath != other.filepath:
                        return (-1 if self.filepath is None else 1)
                else:
                    if self.filepath < other.filepath:
                        return -1
                    elif self.filepath > other.filepath:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_FileServer._t_FileInfo)

        __repr__ = __str__

    _M_FileServer._t_FileInfo = IcePy.defineStruct('::FileServer::FileInfo', FileInfo, (), (
        ('creattime', (), IcePy._t_long),
        ('updatetime', (), IcePy._t_long),
        ('filesize', (), IcePy._t_int),
        ('filescore', (), IcePy._t_byte),
        ('filename', (), IcePy._t_string),
        ('filetype', (), IcePy._t_string),
        ('filepath', (), IcePy._t_string)
    ))

    _M_FileServer.FileInfo = FileInfo
    del FileInfo

_M_FileServer._t_FileReadServer = IcePy.defineValue('::FileServer::FileReadServer', Ice.Value, -1, (), False, True, None, ())

if 'FileReadServerPrx' not in _M_FileServer.__dict__:
    _M_FileServer.FileReadServerPrx = Ice.createTempClass()
    class FileReadServerPrx(Ice.ObjectPrx):

        def ReadFileInfo(self, fileid, context=None):
            return _M_FileServer.FileReadServer._op_ReadFileInfo.invoke(self, ((fileid, ), context))

        def ReadFileInfoAsync(self, fileid, context=None):
            return _M_FileServer.FileReadServer._op_ReadFileInfo.invokeAsync(self, ((fileid, ), context))

        def begin_ReadFileInfo(self, fileid, _response=None, _ex=None, _sent=None, context=None):
            return _M_FileServer.FileReadServer._op_ReadFileInfo.begin(self, ((fileid, ), _response, _ex, _sent, context))

        def end_ReadFileInfo(self, _r):
            return _M_FileServer.FileReadServer._op_ReadFileInfo.end(self, _r)

        def ReadFile(self, fileid, context=None):
            return _M_FileServer.FileReadServer._op_ReadFile.invoke(self, ((fileid, ), context))

        def ReadFileAsync(self, fileid, context=None):
            return _M_FileServer.FileReadServer._op_ReadFile.invokeAsync(self, ((fileid, ), context))

        def begin_ReadFile(self, fileid, _response=None, _ex=None, _sent=None, context=None):
            return _M_FileServer.FileReadServer._op_ReadFile.begin(self, ((fileid, ), _response, _ex, _sent, context))

        def end_ReadFile(self, _r):
            return _M_FileServer.FileReadServer._op_ReadFile.end(self, _r)

        def UpdateFileInfo(self, fileid, fileinfo, context=None):
            return _M_FileServer.FileReadServer._op_UpdateFileInfo.invoke(self, ((fileid, fileinfo), context))

        def UpdateFileInfoAsync(self, fileid, fileinfo, context=None):
            return _M_FileServer.FileReadServer._op_UpdateFileInfo.invokeAsync(self, ((fileid, fileinfo), context))

        def begin_UpdateFileInfo(self, fileid, fileinfo, _response=None, _ex=None, _sent=None, context=None):
            return _M_FileServer.FileReadServer._op_UpdateFileInfo.begin(self, ((fileid, fileinfo), _response, _ex, _sent, context))

        def end_UpdateFileInfo(self, _r):
            return _M_FileServer.FileReadServer._op_UpdateFileInfo.end(self, _r)

        def CleanFileBlock(self, timefrom, timeto, status, context=None):
            return _M_FileServer.FileReadServer._op_CleanFileBlock.invoke(self, ((timefrom, timeto, status), context))

        def CleanFileBlockAsync(self, timefrom, timeto, status, context=None):
            return _M_FileServer.FileReadServer._op_CleanFileBlock.invokeAsync(self, ((timefrom, timeto, status), context))

        def begin_CleanFileBlock(self, timefrom, timeto, status, _response=None, _ex=None, _sent=None, context=None):
            return _M_FileServer.FileReadServer._op_CleanFileBlock.begin(self, ((timefrom, timeto, status), _response, _ex, _sent, context))

        def end_CleanFileBlock(self, _r):
            return _M_FileServer.FileReadServer._op_CleanFileBlock.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_FileServer.FileReadServerPrx.ice_checkedCast(proxy, '::FileServer::FileReadServer', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_FileServer.FileReadServerPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::FileServer::FileReadServer'
    _M_FileServer._t_FileReadServerPrx = IcePy.defineProxy('::FileServer::FileReadServer', FileReadServerPrx)

    _M_FileServer.FileReadServerPrx = FileReadServerPrx
    del FileReadServerPrx

    _M_FileServer.FileReadServer = Ice.createTempClass()
    class FileReadServer(Ice.Object):

        def ice_ids(self, current=None):
            return ('::FileServer::FileReadServer', '::Ice::Object')

        def ice_id(self, current=None):
            return '::FileServer::FileReadServer'

        @staticmethod
        def ice_staticId():
            return '::FileServer::FileReadServer'

        def ReadFileInfo(self, fileid, current=None):
            raise NotImplementedError("servant method 'ReadFileInfo' not implemented")

        def ReadFile(self, fileid, current=None):
            raise NotImplementedError("servant method 'ReadFile' not implemented")

        def UpdateFileInfo(self, fileid, fileinfo, current=None):
            raise NotImplementedError("servant method 'UpdateFileInfo' not implemented")

        def CleanFileBlock(self, timefrom, timeto, status, current=None):
            raise NotImplementedError("servant method 'CleanFileBlock' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_FileServer._t_FileReadServerDisp)

        __repr__ = __str__

    _M_FileServer._t_FileReadServerDisp = IcePy.defineClass('::FileServer::FileReadServer', FileReadServer, (), None, ())
    FileReadServer._ice_type = _M_FileServer._t_FileReadServerDisp

    FileReadServer._op_ReadFileInfo = IcePy.Operation('ReadFileInfo', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (((), _M_FileServer._t_FileInfo, False, 0),), ((), IcePy._t_bool, False, 0), ())
    FileReadServer._op_ReadFile = IcePy.Operation('ReadFile', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (((), _M_FileServer._t_Bytes, False, 0),), ((), IcePy._t_int, False, 0), ())
    FileReadServer._op_UpdateFileInfo = IcePy.Operation('UpdateFileInfo', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), _M_FileServer._t_FileInfo, False, 0)), (), ((), IcePy._t_bool, False, 0), ())
    FileReadServer._op_CleanFileBlock = IcePy.Operation('CleanFileBlock', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_int, False, 0)), (), ((), IcePy._t_bool, False, 0), ())

    _M_FileServer.FileReadServer = FileReadServer
    del FileReadServer

# End of module FileServer