'''
Created on Mar 19, 2018

@author: smckinn
@copyright: 2018 - Symas Corporation
'''

import unittest

from pyfortress import (
    # model
    User,
    Role,
    Perm,
    PermObj,
    # apis:
    review_mgr, 
    admin_mgr, 
    access_mgr,
    #exception handling:
    FortressError,
    global_ids
)

class BasicTestSuite(unittest.TestCase):
    """These tests the py-fortress review_mgr functions."""
              
                
class TestSamples(unittest.TestCase):
    """
    Basic tests for beginners
    """    

    def test_read_user(self):
        """
        Read a basic user
        """
        print('test_read_user')
        try:
            out_user = review_mgr.read_user(User(uid='foo1'))
            print_user(out_user, 'test_read_user')
        except FortressError as e:
            self.fail('test_read_user failed, exception=' + e.msg)


    def test_add_user(self):
        """
        Add a basic user
        """
        print('test_add_user')
        
        try:
            admin_mgr.add_user(User(uid='foo1', password='secret'))
            print('test_add_user success')                        
        except FortressError as e:
            self.fail('test_add_user failed, exception=' + e.msg)


    def test_delete_user(self):
        """
        Delete the simple user
        """
        print('test_delete_user')
        try:
            admin_mgr.delete_user(User(uid='foo1')) 
            print('test_delete_user success')           
        except FortressError as e:
            if e.id == global_ids.USER_NOT_FOUND:
                print('test_delete_user not found')
                pass
            else:
                self.fail('test_delete_user failed, exception=' + e.msg)


    def test_read_role(self):
        """
        Read a basic role
        """
        print('test_read_role')        
        try:
            out_role = review_mgr.read_role(Role(name='Customer'))
            print_role(out_role, 'test_read_role')                        
        except FortressError as e:
            self.fail('test_read_role failed, exception=' + e.msg)


    def test_add_role(self):
        """
        Add a basic role
        """
        print('test_add_role')        
        try:
            admin_mgr.add_role(Role(name='Customer'))
            print('test_add_role success')                        
        except FortressError as e:
            self.fail('test_add_role failed, exception=' + e.msg)


    def test_delete_role(self):
        """
        Delete a basic role
        """
        print('test_delete_role')        
        try:
            admin_mgr.delete_role(Role(name='Customer'))
            print('test_delete_role success')                        
        except FortressError as e:
            if e.id == global_ids.ROLE_NOT_FOUND:
                print('test_delete_role not found')
                pass
            else:            
                self.fail('test_delete_role failed, exception=' + e.msg)


    def test_read_obj(self):
        """
        Read a basic perm object
        """
        print('test_read_obj')        
        try:
            out_obj = review_mgr.read_object(PermObj(obj_name='ShoppingCart'))
            print_obj(out_obj, 'test_read_obj')                        
        except FortressError as e:
            self.fail('test_read_obj failed, exception=' + e.msg)


    def test_add_obj(self):
        """
        Add a basic perm object
        """
        print('test_add_obj')
        
        try:
            admin_mgr.add_object(PermObj(obj_name='ShoppingCart'))
            print('test_add_obj success')                        
        except FortressError as e:
            self.fail('test_add_obj failed, exception=' + e.msg)


    def test_delete_obj(self):
        """
        Delete a basic perm object
        """
        print('test_delete_obj')
        
        try:
            admin_mgr.delete_object(PermObj(obj_name='ShoppingCart'))
            print('test_delete_obj success')                        
        except FortressError as e:
            if e.id == global_ids.PERM_OBJ_NOT_FOUND:
                print('test_delete_obj not found')
                pass
            else:            
                self.fail('test_delete_obj failed, exception=' + e.msg)


    def test_read_perm(self):
        """
        Read a basic perm
        """
        print('test_read_perm')        
        try:
            out_perm = review_mgr.read_perm(Perm(obj_name='ShoppingCart', op_name='add'))
            print_perm(out_perm, 'test_read_perm')                        
        except FortressError as e:
            self.fail('test_read_perm failed, exception=' + e.msg)


    def test_add_perm(self):
        """
        Add a basic perm
        """
        print('test_add_perm')
        
        try:
            admin_mgr.add_perm(Perm(obj_name='ShoppingCart', op_name='add'))
            print('test_add_perm success')                        
        except FortressError as e:
            self.fail('test_add_perm failed, exception=' + e.msg)


    def test_delete_perm(self):
        """
        Delete a basic perm
        """
        print('test_delete_perm')
        try:
            admin_mgr.delete_perm(Perm(obj_name='ShoppingCart', op_name='add'))
            print('test_delete_perm success')                        
        except FortressError as e:
            if e.id == global_ids.PERM_OP_NOT_FOUND:
                print('test_delete_perm not found')
                pass
            else:            
                self.fail('test_delete_perm failed, exception=' + e.msg)


    def test_grant_perm(self):
        """
        Grant a permission to a role
        """
        print('test_grant_perm')
        
        try:
            admin_mgr.grant(Perm(obj_name='ShoppingCart', op_name='add'), Role(name="Customer"))
            print('test_grant_perm success')                        
        except FortressError as e:
            self.fail('test_grant_perm failed, exception=' + e.msg)


    def test_revoke_perm(self):
        """
        Revoke a permission from a role
        """
        print('test_revoke_perm')
        
        try:
            admin_mgr.revoke(Perm(obj_name='ShoppingCart', op_name='add'), Role(name="Customer"))
            print('test_revoke_perm success')                        
        except FortressError as e:
            if e.id == global_ids.PERM_ROLE_NOT_EXIST:
                print('test_revoke_perm not granted')
            else:
                print('test_revoke_perm error=' + e.msg)
                #self.fail('test_revoke_perm failed, exception=' + e.msg)


    def test_assign_user(self):
        """
        Assign a user to a role
        """
        print('test_assign_user')
        
        try:
            admin_mgr.assign(User(uid='foo1'), Role(name='Customer'))
            print('test_assign_user success')                        
        except FortressError as e:
            self.fail('test_assign_user failed, exception=' + e.msg)


    def test_create_session(self):
        """
        create session
        """
        print('test_create_session')
        
        try:
            session = access_mgr.create_session(User(uid='foo1', password='secret'), False)
            if not session:
                print('test_create_session fail')
                self.fail('test_create_session fail')
            else:
                print('test_create_session pass')
                pass                        
        except FortressError as e:
            self.fail('test_create_session failed, exception=' + e.msg)            
            
            
    def test_check_access(self):
        """
        create session and check perm
        """
        print('test_check_access')
        
        try:
            session = access_mgr.create_session(User(uid='foo1', password='secret'), False)
            result = access_mgr.check_access(session, Perm(obj_name='ShoppingCart', op_name='add'))
            if not result:
                print('test_check_access fail')
                self.fail('test_check_access fail')
            else:
                print('test_check_access pass')
                pass                        
        except FortressError as e:
            self.fail('test_check_access failed, exception=' + e.msg)            
            
            
    def test_session_perms(self):
        """
        create session and get perms for user
        """
        print('test_check_access')
        
        try:
            session = access_mgr.create_session(User(uid='foo1', password='secret'), False)
            perms = access_mgr.session_perms(session)
            if not perms:
                print('test_session_perms failed')
                self.fail('test_session_perms failed')
            
            for perm in perms:
                print_perm(perm, 'session_perms: ')
            pass                        
        except FortressError as e:
            self.fail('test_session_perms failed, exception=' + e.msg)
            
            
            
def print_user (entity, label):
        print(label + ' uid:' + entity.uid)

        
def print_role (entity, label):
        print(label + ' role name:' + entity.name)


def print_obj (entity, label):
        print(label + ' object name:' + entity.obj_name)


def print_perm (entity, label):
        print(label + ' object name:' + entity.obj_name + ' op name:' + entity.op_name)    
        
        
def suite():
    suite = unittest.TestSuite()
    
    # Teardown:        
    suite.addTest(TestSamples('test_delete_user'))
    suite.addTest(TestSamples('test_revoke_perm'))        
    suite.addTest(TestSamples('test_delete_perm'))        
    suite.addTest(TestSamples('test_delete_obj'))
    suite.addTest(TestSamples('test_delete_role'))
        
    # Buildup:
    suite.addTest(TestSamples('test_add_obj'))
    suite.addTest(TestSamples('test_add_perm'))
    suite.addTest(TestSamples('test_add_role'))    
    suite.addTest(TestSamples('test_grant_perm'))
    suite.addTest(TestSamples('test_add_user'))    
    suite.addTest(TestSamples('test_assign_user'))

    # Interrogate:
    suite.addTest(TestSamples('test_read_role'))    
    suite.addTest(TestSamples('test_read_obj'))
    suite.addTest(TestSamples('test_read_perm'))
    suite.addTest(TestSamples('test_read_user'))
    suite.addTest(TestSamples('test_create_session'))
    suite.addTest(TestSamples('test_check_access'))
    suite.addTest(TestSamples('test_session_perms'))
    return suite  

 
if __name__ == '__main__':
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())