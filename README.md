# py-fortress-sample README 
 
This installs py-fortress and runs a simple test program of how the RBAC API works.
______________________________________________________________________________
## Prerequisites

Minimum hardware requirements:
 * 1 Core
 * 1 GB RAM

Minimum software requirements:
 * Linux machine
 * git
 * docker engine
 * Python3 and virtualenv (venv)
________________________________________________________________________________
## Start using ApacheDS or OpenLDAP Docker Image

Follow these instructions: []()

1. Pull the docker image (pick one):

    a. apacheds
    ```
    docker pull apachedirectory/apacheds-for-apache-fortress-tests
    ```

    b. openldap
    ```
    docker pull apachedirectory/openldap-for-apache-fortress-tests
    ```

2. Run the docker container (pick one):

    a. apacheds
    ```
    export CONTAINER_ID=$(docker run -d -P apachedirectory/apacheds-for-apache-fortress-tests)
    export CONTAINER_PORT=$(docker inspect --format='{{(index (index .NetworkSettings.Ports "10389/tcp") 0).HostPort}}' $CONTAINER_ID)
    echo $CONTAINER_PORT
    ```
       
    b. openldap 
    ```
    export CONTAINER_ID=$(docker run -d -P apachedirectory/openldap-for-apache-fortress-tests)
    export CONTAINER_PORT=$(docker inspect --format='{{(index (index .NetworkSettings.Ports "389/tcp") 0).HostPort}}' $CONTAINER_ID)
    echo $CONTAINER_PORT
    ```

    * make note of the port, it's needed later
    * depending on your docker setup may need to run as root or sudo priv's.

[More Info here in py-fortress README-QUICKSTART](https://github.com/shawnmckinney/py-fortress/blob/master/pyfortress/doc/README-QUICKSTART.md)
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
    vi py-fortress-cfg.json
    ```

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
    
2. Install py-fortress:
    ```
    pip3 install py-fortress
    ```
    
3. Change folder to where the sample program is:
    ```
    cd sample/ldap
    ```
    _you should now be here: [py-fortress-sample/sample/ldap](./sample/ldap)_
    
4. Prepare the Directory Information Tree (using py-fortress installed package):
    ```
    python3 -m pyfortress.test.test_dit_dao
    ```
    _if you're not familiar with LDAP, you can think of this command as creating tables in a new database instance._

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
    
7. Study the APIs in [test_samples.py](./sample/ldap/test_samples.py) module.