"""
qjszm,lhdzk
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_auth_pro.settings')
django.setup()

from testmodel.models import Row
from django.contrib.auth.models import Group
from guardian.shortcuts import assign_perm
from django.contrib.auth.models import User


def test_auth():
    """测试权限"""
    user = User.objects.get(username='1')
    row1 = Row()
    row1.user = user
    row1.save()

    print(user.has_perm('testmodel.add_row'))  # true,付给了model级别的权限
    print(user.has_perm('add_row'))  # false

    # 分配时没有授权的情况
    print(user.has_perm('testmodel.delete_row'))  # false
    print(user.has_perm('testmodel.change_row'))  # false
    print(user.has_perm('testmodel.add_row', row1))  # false

    # 直接授权给用户，不再通过用户组
    assign_perm('add_row', user, row1)
    print(user.has_perm('add_row', row1))  # true
    print(user.has_perm('testmodel.add_row', row1))  # true


def assign_auth():
    """分配授权"""
    # 测试没有分配权限时的情况
    user = User.objects.get(username='1')
    Row.objects.create(num=0, user=user)

    user_group = Group.objects.get(name='user')
    admin_group = Group.objects.get(name='admin')
    superuser_group = Group.objects.get(name='superuser')

    # 为组分配权限
    assign_perm('testmodel.change_row', admin_group)
    assign_perm('testmodel.change_row', superuser_group)

    assign_perm('testmodel.add_row', admin_group)
    assign_perm('testmodel.add_row', user_group)

    assign_perm('testmodel.delete_row', admin_group)
    assign_perm('testmodel.delete_row', superuser_group)

    # 添加用户到组
    users = User.objects.all()
    for user in users:
        if user.username == '000':
            user.groups.add(superuser_group)
        elif user.username == '111':
            user.groups.add(admin_group)
        else:
            user.groups.add(user_group)
    pass


def add_group():
    """添加用户组"""
    Group.objects.get_or_create(name='user')
    Group.objects.get_or_create(name='admin')
    Group.objects.get_or_create(name='superuser')


def add_user():
    """添加用户"""
    # 创建超级管理员
    User.objects.get_or_create(username='000')
    # 创建管理员
    User.objects.get_or_create(username='111')
    # 创建普通用户
    for i in range(6):
        User.objects.get_or_create(username=str(i))


if __name__ == '__main__':
    # add_group()
    # add_user()
    # print(User.objects.all())
    # assign_auth()
    test_auth()
