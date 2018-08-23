# BByaWorld website

BByaWorld (https://bbyaworld.com) Minecraft server website.

# Dependencies

 - Python 3
 - Pip
 - Database (SQLite, MariaDB, MySQL, PostgreSQL, etc.)
 - NPM
 - Bower

# Setup

1. Clone this repo
2. Run `pip -r requirements.txt` to install dependencies
3. Run `npm i` to install NPM dependencies
4. Run `bower install` to install Bower components
5. Configure `secrets.json` file
6. Using proper settings module (`bbya.settings.dev` or `bbya.settings.prod`) run `python manage.py migrate` to migrate the database
7. Create superuser (if needed)
8. Run webserver
9. **Optional**: Add `python manage.py runcrons` as a Cron job to update stats and stuff automatically.

# Configuration

There are two settings modules: dev (`bbya.settings.dev`) and prod (`bbya.settings.prod`). You may specify which one is needed by setting `DJANGO_SETTINGS_MODULE` environment variable, e.g. `DJANGO_SETTINGS_MODULE=bbya.settings.prod python manage.py runserver`. Default settings module is dev.

Dev module is set to use SQLite database, prod uses MariaDB.

## `secrets.json`

`secrets.json` stores secret information like database access credentials. This file should be placed at repository root.

Example:

```json
{
	"secret_key": "django secret key",
	"db": {
		"default": {
			"name": "database",
			"user": "user",
			"password": "password"
		}
	},
	"allowed_hosts": ["1.2.3.4", "host.com"]
}
```

**Note**: Hosts as `127.0.0.1` and `bbyaworld.com` are allowed regardless of `allowed_hosts` parameter.

# License

See LICENSE file for license information