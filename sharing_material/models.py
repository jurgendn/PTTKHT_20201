# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    idad = models.AutoField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    email = models.TextField(unique=True, blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    permission = models.TextField(blank=True, null=True)
    link_img = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comment(models.Model):
    idpost = models.AutoField(blank=True, null=True)
    idcus = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class Customer(models.Model):
    idcus = models.AutoField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    email = models.TextField(unique=True, blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    university = models.TextField(blank=True, null=True)
    level = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    date_sign_up = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Files(models.Model):
    idfile = models.AutoField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    idpost = models.IntegerField(blank=True, null=True)
    number_download = models.IntegerField(blank=True, null=True)
    display = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files'


class ManageCustomer(models.Model):
    idcus = models.IntegerField(blank=True, null=True)
    idad = models.AutoField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manage_customer'


class ManagePost(models.Model):
    idpost = models.AutoField(blank=True, null=True)
    idad = models.IntegerField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manage_post'


class Post(models.Model):
    idpost = models.AutoField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    idcus = models.IntegerField(unique=True, blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    idsubject = models.IntegerField(unique=True, blank=True, null=True)
    detail = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class Rating(models.Model):
    idpost = models.AutoField(blank=True, null=True)
    idcus = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'


class Report(models.Model):
    idpost = models.AutoField(blank=True, null=True)
    idcus = models.IntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report'


class Subject(models.Model):
    idsubject = models.AutoField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    idad = models.IntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    school = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subject'


class SubjectsManagerSubjects(models.Model):
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    idad = models.CharField(db_column='IdAd', max_length=200)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    school = models.CharField(db_column='School', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subjects_manager_subjects'
