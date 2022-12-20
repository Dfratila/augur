# MacOS Install Steps

1. Install Node 18.5.0 from their website <https://nodejs.org/en/>  

2. Npm version 18.12.1 should install automatically with Node

3. Install vue and vue cli: `npm install vue && npm i -g @vue/cli`  
    a. You might have permission errors, use the following commands to fix that
    1. `sudo chown -R $(whoami) /usr/local/lib/node\_modules`
    2. `sudo chown -R $(whoami) /usr/local/bin`
    3. `sudo chown -R $(whoami) /usr/local/share`

4. Install postgresql `brew install postgresql`  
    a. Homebrew install: <https://brew.sh/> , might need to add `eval $(/opt/homebrew/bin/brew shellenv)` to `~/.zshrc`  
    b. Create postgres user `createuser -s postgres -U <username>`

5. Install python3.9: `brew install python3.9`

6. Install redis: `brew install redis`

7. Install go  
    a. Run this command: `wget -c https://go.dev/dl/go1.19.3.linux-amd64.tar.gz -O - | sudo tar -xz -C /usr/local`  
    b. Edit your `~/.zshrc` or `~/.bashrc` and add the follwing line: `export PATH=$PATH:/usr/local/bin/go`

8. Setup postgresql database  
    a. `psql -h 127.0.0.1 -U postgres -p 5432`  
    b. Run the following SQL commands:

    ```sql
    CREATE DATABASE augur;  
    CREATE USER augur WITH ENCRYPTED PASSWORD 'password';  
    GRANT ALL PRIVILEGES ON DATABASE augur TO augur;
    ```  

    c. `\q` to quit.

9. Create python virtual environment  
    a. `python3.9 -m venv ~/.virtual_envs/augur/`  
    b. `source ~/.virtual_envs/augur/bin/activate`

10. Setup AUGUR\DB value:  
    a. Run: `export AUGUR_DB=postgresql+psycopg2://augur:password@127.0.0.1:5432/augur`  
    b. You can also set this in your `.bashrc` or `.zshrc`

11. Make a new file: `src/frontend/frontend.config.json`  
    Put the following in the file:

    ```json
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
    ```

12. Run `make install`. The `augur` command is now installed. Run augur --help to confirm this. It might ask to install something for 64-bit python3.9.

13. Run `npm install`. This installs all of the npm packages needed to run the website. After this, you can run the server.

14. Run `npm serve`, this makes a dev server on your local machine.

15. The server should be running on `localhost:8080`.
