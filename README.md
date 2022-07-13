## You-Tube-Video-Downloader-Python-Telegram-Bot

__Programmer - Sunnatillo Abdivasiyev Azizovich__

### Download Python:

    https://www.python.org/

### Checking the installation of Python and Pip:

    >> python --version
    > Python 3.10.0

    >> pip --version
    > pip 22.1.2 from C:\Users\Programmer\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)

### PIP update:

    >> python -m pip install --upgrade pip
    >> pip --version
    
    > C:\Users\Programmer\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)

### Creating a virtual environment:

    >> python -m venv venv
    >> dir
    >
    13.07.2022  13:17    <DIR>          .
    13.07.2022  13:17    <DIR>          ..
    13.07.2022  13:02               152 .env.dist
    13.07.2022  13:02             1 943 .gitignore
    13.07.2022  13:02               514 app.py
    13.07.2022  13:02    <DIR>          data
    13.07.2022  13:02    <DIR>          filters
    13.07.2022  13:02    <DIR>          handlers
    13.07.2022  13:02    <DIR>          keyboards
    13.07.2022  13:02               269 loader.py
    13.07.2022  13:02    <DIR>          middlewares
    13.07.2022  13:02               195 Pipfile
    13.07.2022  13:02            30 386 Pipfile.lock
    13.07.2022  13:02                21 Procfile
    13.07.2022  13:17               710 README.md
    13.07.2022  13:16    <DIR>          readme_images
    13.07.2022  13:02                46 requirements.txt
    13.07.2022  13:02    <DIR>          states
    13.07.2022  13:02    <DIR>          utils
    13.07.2022  13:17    <DIR>          venv
               9 файлов         34 236 байт
              11 папок  407 290 744 832 байт свободно
    

    >> .\venv\Scripts\activate
    > (venv) D:\GitHub\You-Tube-Video-Downloader-Python-Telegram-Bot>

### Upload packages: 

    >> pip intall -r requirements.txt
    *********************************
    >> pip intall aiogram
    >> pip intall environs
    >> pip intall pytube

### Putting a bot token:

    Open this file and complete the information:
        .env
    
    Use this bot telegram and send the desired word:
        https://t.me/ShowJsonBot

    {
        "update_id": #update_id,
        "message": {
            "message_id": #message_id,
            "from": {
                "id": #id,
                "is_bot": false,
                "first_name": "#firstname",
                "last_name": "#lastname",
                "username": "#Username",
                "language_code": "ru"
            },
        }
    }

    Copy your ID and to be placed in the .env file
        => ADMINS=id

    Copy your Bot token to be placed in the .env file
        => BOT_TOKEN=bot_token

### Using the program:
    >> python app.py