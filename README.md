# py-fortress-sample README 
 
This installs py-fortress and runs a simple test program of how the RBAC API works._
______________________________________________________________________________
## Prerequisites

Minimum hardware requirements:
 * 1 Core
 * 1 GB RAM

Minimum software requirements:
 * Linux machine
 * Python3 and virtualenv (venv) or system install of the ldap3 python module
 * completion of [README-LDAP-DOCKER](./README-LDAP-DOCKER)
________________________________________________________________________________
## Clone py-fortress-sample, prepare for usage

1. Clone py-fortress-sample
    ```
    git clone https://github.com/shawnmckinney/py-fortress-sample.git
    ```
    
2. Change folder into the project:
    ```
    cd py-fortress-sample
    ```
    _you should now be here: py-fortress-sample_
    
3. Now edit the config file:
    ```
    vi sample/ldap/py-fortress-cfg.json
    ```
    _cfg file is here: [py-fortress-sample/sample/ldap/py-fortress-cfg.json](sample/ldap/py-fortress-cfg.json)_

4. Set the LDAP Port
    ```
    ...
    "ldap": {
      ...
      "port": 32768,
    ...
    ```
    _use value obtained earler_
        
5. Update the connection parameters (pick one):

    a. apacheds:
    ```
    "dn": "uid=admin,ou=system",
    ```
    
    b. openldap:
    ```
    "dn": "cn=Manager,dc=example,dc=com",
    ```
    _per your earlier choice of docker image_
________________________________________________________________________________
## Setup Python Runtime and Install py-fortress

1. Prepare your terminal for execution of python3.  From the main dir of the git repo:
    ```
    pyvenv env
    . env/bin/activate
    ```
    _from the py-fortress-sample folder_
    
2. Install py-fortress:
    ```
    pip3 install py-fortress
    ```
    
3. Change folder to where the sample program is:
    ```
    cd sample/ldap
    ```
    _you're now here: [py-fortress-sample/sample/ldap](./sample/ldap)_
    
4. Prepare the Directory Information Tree:
    ```
    initldap
    ```
    *initldap is a python script, created during install of py-fortress package, that maps here: pyfortress.test.test_dit_dao*    
    *you can think of this command as creating tables in a new database instance.*

5. Example the output, should finish almost instaneously (< 1 sec).
    ```
    python3 -m pyfortress.test.test_dit_dao
    2018-04-06 06:02:45,895 INFO Initialize py-fortress ldap...
    2018-04-06 06:02:45,896 INFO ldap host: localhost, port:32768
    test_bootstrap
    test_bootstrap success
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.365s
    ```
    _If it hangs more than a second or two, ctrl-c to kill it. A bug in the ldap pool causes a hang, but it indicates something went wrong with your ldap server setup and/or ldap port wrong..._        
    
6. Run the test program:
    ```
    python3 test_samples.py 
    ```
    
7. View the output:
    ```
    ----------------------------------------------------------------------
    Ran 18 tests in 2.388s
    OK
    ```
    
8. Study the APIs in [test_samples.py](./sample/ldap/test_samples.py) module.