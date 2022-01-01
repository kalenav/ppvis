#include <string>
#include <vector>
#include "date_class.h"
#include "actors.h"

class File
{
private:
	std::string title;
	Date date_of_creation;
	Actor author;
public:
	int getType();
};

class Document : public File
{
private:
	Document();

	int type = 1;
	std::string text;
	std::vector<Image> referenced_images;
	void parseReferencedImages();

	friend class Writer;
	Document(std::string title_IN, Date date_of_creation_IN, Writer author_IN, std::string text_IN);
	void setTitle();
	void setText();

	friend class Administrator;
	~Document();
public:
	std::string getTitle();
	Writer getAuthor();
};

class Image : public File
{
private:
	int type = 2;

	friend class Illustrator;
	Image();
	Image(std::string title_IN, Date date_of_creation_IN, Illustrator author_IN);
	friend class Administartor;
	~Image();
};