| SCS2205 Take Home Assignment 3 |  20001061 - J P Madarasinghe |
# **Web Server**

This Simple web server is implemented using Python. in order to run this server, you should have installed **Python 3.x** and all the given files and folders should be in the same directory.
This server can handle only GET requests. It can handle multiple clients at the same time. It can handle multiple requests from a single client at the same time.
This server can not handle images, videos, and other binary files. It can only handle text, html, css and JS files.

- Python **socket** module is used to implement the server.

- Python **os** module is used to create file paths.

- Python **mimetypes** module is used to finde content types.

- **GreenShock GSAP CDN** is used to test CDN and JavaScript support.

## **How to run the server**
1. Export zip file to a folder
2. Run the following command in the terminal or command prompt
```bash
python server.py
```
3. Open a browser and go to [**localhost:2728**](http:/localhost:2728)



## **Files and folders structure**

```
Webserver
│
├── server.py ( main python file )
├── readme.md ( instructions )
└── htdocs
    ├── index.html ( main html file )
    ├── about.html ( second html file )
    ├── css
    │   ├── index.css ( contains styles for index.html file )
    │   ├── about.css ( contains styles for about.html file )
    │   ├── nav.css (contains styles for navigation bar )     
    └── js
        └── index.js ( contains js for index.js file )

```