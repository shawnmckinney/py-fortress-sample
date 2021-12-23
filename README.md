# py-fortress-sample README 
 
This installs py-fortress and runs a simple test program of how the RBAC API works._
______________________________________________________________________________
## Prerequisites

Minimum hardware requirements:
 * 1 Core
 * 1 GB RAM

Minimum software requirements:
 * RHEL/Debian machine
 * Python >=3.6 
 * Installed [README-LDAP-DOCKER](https://github.com/shawnmckinney/py-fortress/blob/master/pyfortress/doc/README-LDAP-DOCKER.md)
 * python-ldap dependencies installed [README-UPGRADE-PYTHON](https://github.com/shawnmckinney/py-fortress/blob/master/doc/README-UPGRADE-PYTHON.md)
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
    
3. Prepare the config:

From the project root folder, copy sample cfg file:

```bash
cp py-fortress-cfg.json.sample py-fortress-cfg.json
```

sample cfg file is here: [py-fortress-cfg.json.sample](../py-fortress-cfg.json.sample)

4. Now edit config file:
 ```
vi py-fortress-cfg.json
```

5. Set the LDAP URI
```
...
"ldap": {
...
"uri": "ldap://localhost",
...
```

* use value obtained during LDAP setup
* if in doubt use the defaults
    
6. Save and exit

________________________________________________________________________________
## Setup Python Runtime and Install py-fortress

1. Prepare your terminal for execution of python3.  From the main dir of the git repo:
```
python3 -m venv env
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

You can think of this command as creating tables in a new database instance.
```
initldap
```
*initldap is a python script, created during install of py-fortress package, that maps here: pyfortress.test.test_dit_dao*    

5. Examine the output, should finish almost instaneously (< 1 sec).
    ```
    initldap
    2018-04-06 06:02:45,895 INFO Initialize py-fortress ldap...
    2018-04-06 06:02:45,896 INFO ldap host: localhost, port:32768
    test_bootstrap
    test_bootstrap success
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.365s
    ```
    
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