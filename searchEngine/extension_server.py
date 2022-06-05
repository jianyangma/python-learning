"""
File: extension_server.py
---------------------
"""

# This imports the SimpleServer library
import SimpleServer

# This imports the functions you defined in searchengine.py
from searchengine import create_index, search, textfiles_in_dir

from extension import find_url

# To get the json.dumps function.
import json

# the directory of files to search over
DIRECTORY = 'news'
# perhaps you want to limit to only 10 responses per search.
MAX_RESPONSES_PER_REQUEST = 10


class SearchServer:
    def __init__(self):
        """
        load the data that we need to run the search engine. This happens
        once when the server is first created.
        """
        self.html = open('extension_client.html').read()

    # this is the server request callback function.
    def handle_request(self, request):
        """
        This function gets called every time someone makes a request to our
        server. To handle a search, look for the query parameter with key "query"
        """
        # it is helpful to print out each request you receive!
        print(request)

        # if the command is empty, return the html for the search page
        if request.command == '':
            return self.html

        # if the command is search, the client wants you to perform a search!
        if request.command == 'search':
            params = request.params
            query = params['query']
            files = textfiles_in_dir(DIRECTORY)
            index = {}  # index is empty to start
            file_titles = {}  # mapping of file names to article titles is empty to start
            create_index(files, index, file_titles)
            result = search(index, query)
            output = []
            for i in range(len(result)):
                my_dict = {}
                with open(result[i], 'r') as file:
                    next(file)
                    for line in file:
                        line = line.strip()
                        temp = line.lower()
                        pos = temp.find(query.partition(" ")[0])
                        if pos != -1:
                            parts = line.split(".")
                            for part in parts:
                                temp = part.lower()
                                if query.partition(" ")[0] in temp:
                                    my_dict['snippet'] = part
                my_dict['title'] = file_titles[result[i]]
                # To link to actual original URL through beautifulsoup
                # my_dict['url'] = find_url(file_titles[result[i]])
                formatted_title = file_titles[result[i]].replace(" ", "+")
                my_dict['url'] = 'https://google.com/search?q=bccnews+' + formatted_title
                output.append(my_dict)

            return json.dumps(output, indent=2)


def main():
    # Make an instance of your Server
    handler = SearchServer()

    # Start the server to handle internet requests at http://localhost:8000
    SimpleServer.run_server(handler, 8000)


if __name__ == '__main__':
    main()
