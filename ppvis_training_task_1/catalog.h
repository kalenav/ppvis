#ifndef CATALOG_H_INCLUDED
#define CATALOG_H_INCLUDED

#include <list>
#include <string>
#include "files.h"

class Catalog
{
private:
	Catalog(); // this constructor will only be used once, for the main catalog
	Catalog(Catalog& parent);

	std::string name;
	std::list<Catalog> children;
	std::list<File> contents;
	Catalog* parent;
	bool recursiveSearchByTitle(std::string title_IN, File* search_result);
	bool recursiveSearchByAuthor(Actor author_IN, File* search_result);
	bool addFile(File file);
};

#endif