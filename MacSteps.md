1.  Install Node 18.5.0

2.  Npm version 18.12.1

3.  Install vue and vue cli `npm install vue && npm i -g @vue/cli`
    a. You might have permission errors.
    1.  sudo chown -R $(whoami) /usr/local/lib/node\_modules
    2.  sudo chown -R $(whoami) /usr/local/bin
    3.  sudo chown -R $(whoami) /usr/local/share

4.  Install postgresql `brew install postgresql`
    a. Homebrew install: https://brew.sh/ , might need to add `eval $(/opt/homebrew/bin/brew shellenv)` to `~/.zshrc`
    b. Create postgres user `createuser -s postgres -U <username>`

5.  Install python3.9 `brew install python3.9`

6.  Install redis `brew install redis`

7.  Install go
    a. Run this command: `wget -c https://go.dev/dl/go1.19.3.linux-amd64.tar.gz -O - | sudo tar -xz -C /usr/local`
    b. Edit your `~/.zshrc` or `~/.bashrc` and add the follwing line: `export PATH=$PATH:/usr/local/bin/go`

8.  Setup postgresql database
    a. `psql -h 127.0.0.1 -U postgres -p 5432`
    b. CREATE DATABASE augur;
    c. CREATE USER augur WITH ENCRYPTED PASSWORD 'password';
    d. GRANT ALL PRIVILEGES ON DATABASE augur TO augur;
    e. \q

9.  Create python virtual environment
    a. `python3.9 -m venv ~/.virtual_envs/augur/`
    b. `source ~/.virtual_envs/augur/bin/activate`

10. Setup AUGUR\DB value: `export AUGUR_DB=postgresql+psycopg2://augur:password@127.0.0.1:5432/augur`
    a. You can also set this in your `.bashrc` or `.zshrc`

11. Make your `frontend.config.json` file:
    {
    "Frontend":
    {
    "host": "delta.osshealth.io",
    "port": 5000,
    "ssl": false
    },
    "Server":
    {
    "cache\_expire": "3600",
    "host": "0.0.0.0",
    "port": 5000,
    "workers": 6,
    "timeout": 6000,
    "ssl": false,
    "ssl\_cert\_file": null,
    "ssl\_key\_file": null
    }
    }

12. Run `make install`

13. Run `npm install`

14. Run `npm serve`

15. The server should be running on `localhost:8080`
