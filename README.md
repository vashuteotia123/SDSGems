# SDSGems [![wakatime](https://wakatime.com/badge/github/vashuteotia123/SDSGems.svg)](https://wakatime.com/badge/github/vashuteotia123/SDSGems)
Full fledge inventory management system with a ecommerce platform.


##### NOTE: This software is released under the MIT LICENSE. So please read through the information provided there before using the software.


## How to get started ?

##### Setup the virtual environment
` pip install pyenv `\
` pyenv install 3.9.6`\
` pyenv virtualenv env`\
` pyenv local env`

##### Clone the repo
On ssh: ` git clone git@github.com:vashuteotia123/SDSGems.git` \
On https: ` git clone https://github.com/vashuteotia123/SDSGems.git`

##### Install dependencies
Head to the project directory \
` python -m pip install --upgrade pip `\
` pip install -r requirements.txt `

##### Create a env file
Create .env file in SDSDiamonds directory with your credentials\
Format for .env is:\
` SECRET_KEY=<secret-key-here>` \
`DEBUG=True //only for development mode`\
`EMAIL_HOST=<gmail-mail-id>`\
`EMAIL_HOST_PASSWORD=<app-specific-password>
`
##### All done.
Run ` python manage.py runserver <port(if any)>`.

## Technologies Used.
* Python 3
* JavaScript
* Jquery
* Django3
* HTML5
* CSS3
* BootStrap
* Ion Icon
* Font Awesome
* CkEditor
* SQLite 
* Jazzmin2
* Tinymce
* Import Export
* Pillow
* Taggit 
###### In production.
* Ngnix
* Gunicorn
