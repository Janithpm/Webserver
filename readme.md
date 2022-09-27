| SCS2205 Take Home Assignment 3 |  20001061 - J P Madarasinghe |   

# **Web Server**

This Simple web server is implemented using Python. in order to run this server, you should have installed **Python 3.x** and all the given files and folders should be in the same directory.
This server can handle only GET requests. It can handle multiple clients at the same time. It can handle multiple requests from a single client at the same time.

This server support only html, css, js, php and images.
___

## **Python module used in the server**
- Python **socket** module is used to implement the server.

- Python **os** module is used to create file paths.

- Python **mimetypes** module is used to find content types.

___
## **How to run the server**
1. Export zip file to a folder
2. Open Command Prompt and navigate to the folder
3. Run the following command in the command prompt
```bash
python server.py
```
4. Open a browser and go to [**localhost:2728**](http:/localhost:2728)


___
## **Files and folders structure**

```
Webserver
│
├── server.py ( main python file )
├── readme.md ( instructions )
└── htdocs
    ├── favicon.ico
    ├── index.html ( first html file )
    ├── second.html ( second html file )
    ├── third
    │   └── subpage.html ( third html file )
    ├── css
    │   ├── page.css ( contains styles for pages )
    │   └── nav.css (contains styles for navigation bar )     
    ├── js
    │    └── index.js ( contains js for index.js file )
    └── images
        ├── homepage.jpg 
        ├── secondpage.jpg 
        └── subpage.jpg 

```
