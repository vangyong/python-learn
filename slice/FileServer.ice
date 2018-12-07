
#pragma once



module FileServer
{
sequence<byte> Bytes;
struct FileInfo
{
    long creattime;
	long updatetime;
	int filesize;
	byte filescore;
	string filename;
	string filetype;
	string filepath;
};

interface FileReadServer
{
    bool ReadFileInfo(string fileid, out FileInfo fileinfo);
	int  ReadFile(string fileid,out Bytes readbuffer);
	bool UpdateFileInfo(string fileid, FileInfo fileinfo);
	bool CleanFileBlock(string timefrom, string timeto,int status);
};

};

