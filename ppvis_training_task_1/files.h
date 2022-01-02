//#ifndef FILES_H_INCLUDED
//#define FILES_H_INCLUDED

#include <string>
#include <vector>
#include "date_class.h"
#include "actors.h"

class File
{
protected:
	File();

	int type;
	std::string title;
	Date date_of_creation;
	Actor author;
public:
	virtual int getType();
};

class Document : public File
{
protected:
	Document();

	int type = 1;
	std::string text;
	std::vector<Image> referenced_images;
	void parseReferencedImages();
	void parsePath();

	// writer's methods
	Document(std::string title_IN, Date date_of_creation_IN, Writer author_IN, std::string text_IN);
	void setTitle(std::string new_title);
	void setText(std::string new_text);

	// administrator's methods
	~Document();
public:
	std::string getTitle();
	Actor getAuthor();
};

class Image : public File
{
protected:
	Image();

	int type = 2;

	// illustrator's methods
	Image(std::string title_IN, Date date_of_creation_IN, Illustrator author_IN);
	// illustraor's and administrator's methods
	~Image();
};

//#endif