# py-fortress-sample README 
 
QUICKSTART for py-fortress Role-Based Access Control.  Contains instructions to get an LDAP server up, install py-fortress
and running test program which shows how the APIs are used.
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

________________________________________________________________________________
## Clone py-fortress-sample, prepare for usage

1. Clone py-fortress-sample
    ```
    git clone https://github.com/shawnmckinney/py-fortress-sample.git
    ```

2. Change directory into root folder of project:
    ```
    cd py-fortress-sample
    ```
    _you should now be here: [py-fortress-sample](.)_

3. Now edit config file:
    ```
    vi pyfortresssample/ldap/py-fortress-cfg.json
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
    
3. Prepare the Directory Information Tree (using py-fortress installed package):
    ```
    python3 -m "pyfortress.test.test_dit_dao"
    ```
    _if you're not familiar with LDAP, you can think of this as creating tables in a RDBMS._
    
3. Change folder to where the sample program is:
    ```
    cd pyfortresssample/ldap
    ```
    _you should now be here: [py-fortress-sample/pyfortresssample/ldap](pyfortresssample/ldap)_
    
4. Run the test program:
    ```
    python3 test_samples.py 
    ```
    
5. View the output:
    ```
    ----------------------------------------------------------------------
    Ran 18 tests in 2.388s
    OK
    ```
    
6. Study the APIs in [test-sample.py](ldap/test-sample.py) module.