#ifndef ACTORS_H_INCLUDED
#define ACTORS_H_INCLUDED

#include <string>
#include "catalog.h"

// the task description didn't specify how actors with identical roles should be distinguished from one another; an std::string with the actor's name will be used

// concerning friend methods: the use of interfaces would fit better here due to the privacy requirements of the task,
// however I didn't find a way to use interfaces with constructors and destructors, since they can't be virtual

class Actor
{
private:
	std::string name;
public:
	Actor();
	Actor(std::string name);
};

class Secretary : public Actor
{
private:
	friend bool Catalog::recursiveSearchByTitle(std::string title_IN, File* search_result);
	friend bool Catalog::recursiveSearchByAuthor(Actor author_IN, File* search_result);
	friend bool Catalog::addFile(File file);
public:
	using Actor::Actor;
	bool searchByTitle(std::string title_IN, File* search_result);
	bool searchByAuthor(std::string title_IN, File* search_result);
	bool addFileToCatalog(File file, Catalog catalog);
};

class Writer : public Actor
{
private:
	friend Document::Document(std::string title_IN, Date date_of_creation_IN, Writer author_IN, std::string text_IN);
	friend void Document::setTitle(std::string new_title);
	friend void Document::setText(std::string new_text);
public:
	using Actor::Actor;
	Document createDocument(std::string title_IN, Date date_of_creation_IN, Writer author_IN, std::string text_IN);
	void setDocumentTitle(Document document, std::string new_title);
	void setDocumentText(Document document, std::string new_text);
	// the image link/unlink methods are not present here;
	// these are implicitly defined by Document::parseReferencedImages()
	// each time the document's text is changed, the document's linked images list will be updated as a part of it
};

class Illustrator : public Actor
{
private:
	friend Image::Image(std::string title_IN, Date date_of_creation_IN, Illustrator author_IN);
	friend Image::~Image();
public:
	using Actor::Actor;
	Image createImage(std::string title_IN, Date date_of_creation_IN, Illustrator author_IN) {};
	void deleteImage(Image img);
	bool addImageToCatalog(Image img, Catalog catalog);
};

class Administrator : public Actor
{
private:
	friend Catalog::Catalog(std::string name, Catalog& parent);
	friend Document::~Document();
	friend Image::~Image();
public:
	using Actor::Actor;
	void createCatalog(Catalog& parent);
	void deleteDocument(Document document);
	void deleteImage(Image img);
};

#endif

