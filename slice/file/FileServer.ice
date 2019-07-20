
#pragma once



module FileServer
{
sequence<byte> Bytes;
dictionary<string,string> ExtInfo;
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
	bool GetExInfo(string fileid,string key,int vallen,out string value);
	bool GetAllExInfo(string fileid,out ExtInfo extinfo);
	bool ReadFileInfoEx(string fileid, out FileInfo fileinfo,out ExtInfo extinfo);
	
	/* pcap stuff */
	long GenPcap(string pcapid, out string fileid);
	long ReadPcap(string fileid, long offset, long len, out Bytes buf);

	/* 测试 */
	string test1(string fileid);
};

};

