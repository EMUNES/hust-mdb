# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Test(models.Model):
    ϵ�� = models.TextField(blank=True, null=True)
    �ƺ� = models.TextField(blank=True, null=True)
    ������ = models.TextField(blank=True, null=True)
    ���� = models.TextField(blank=True, null=True)
    ����������д = models.TextField(blank=True, null=True)
    �������� = models.TextField(blank=True, null=True)
    ������Դ = models.TextField(blank=True, null=True)
    �ϴ��޸����� = models.TextField(blank=True, null=True)
    �������� = models.TextField(blank=True, null=True)
    ����״̬ = models.TextField(blank=True, null=True)
    ����id = models.IntegerField(db_column='����ID', blank=True, null=True)  # Field name made lowercase.
    �ȼ����� = models.TextField(blank=True, null=True)
    ��Ӧ�̴��� = models.TextField(blank=True, null=True)
    ��ά_����� = models.TextField(db_column='��ά/�����', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ģ�߱����¶� = models.FloatField(blank=True, null=True)
    �����¶� = models.FloatField(blank=True, null=True)
    ģ���¶ȷ�Χ_��Сֵ_field = models.FloatField(db_column='ģ���¶ȷ�Χ����Сֵ��', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ģ���¶ȷ�Χ_���ֵ_field = models.FloatField(db_column='ģ���¶ȷ�Χ�����ֵ��', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����¶ȷ�Χ_��Сֵ_field = models.FloatField(db_column='�����¶ȷ�Χ����Сֵ��', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����¶ȷ�Χ_���ֵ_field = models.FloatField(db_column='�����¶ȷ�Χ�����ֵ��', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ������������¶� = models.FloatField(blank=True, null=True)
    �����¶� = models.FloatField(blank=True, null=True)
    ������Ӧ�� = models.FloatField(blank=True, null=True)
    ���������� = models.FloatField(blank=True, null=True)
    �����ܶ� = models.FloatField(blank=True, null=True)
    �����ܶ� = models.FloatField(blank=True, null=True)
    pvt_b5 = models.FloatField(db_column='pvt-b5', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b6 = models.FloatField(db_column='pvt-b6', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b1m = models.FloatField(db_column='pvt-b1m', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b2m = models.FloatField(db_column='pvt-b2m', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b3m = models.FloatField(db_column='pvt-b3m', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b4m = models.FloatField(db_column='pvt-b4m', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b1s = models.FloatField(db_column='pvt-b1s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b2s = models.FloatField(db_column='pvt-b2s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b3s = models.FloatField(db_column='pvt-b3s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b4s = models.FloatField(db_column='pvt-b4s', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b7 = models.FloatField(db_column='pvt-b7', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b8 = models.FloatField(db_column='pvt-b8', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pvt_b9 = models.FloatField(db_column='pvt-b9', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ����ģ��e1 = models.FloatField(db_column='����ģ��E1', blank=True, null=True)  # Field name made lowercase.
    ����ģ��e2 = models.FloatField(db_column='����ģ��E2', blank=True, null=True)  # Field name made lowercase.
    ���ɱ�v12 = models.FloatField(blank=True, null=True)
    ���ɱ�v23 = models.FloatField(blank=True, null=True)
    ����ģ��g12 = models.FloatField(db_column='����ģ��G12', blank=True, null=True)  # Field name made lowercase.
    ���������ݺ������ͬ��ϵ��alpha1 = models.FloatField(blank=True, null=True)
    ���������ݺ������ͬ��ϵ��alpha2 = models.TextField(blank=True, null=True)
    �߲���n = models.FloatField(blank=True, null=True)
    �߲���tau_field = models.FloatField(db_column='�߲���Tau*', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �߲���d1 = models.FloatField(db_column='�߲���D1', blank=True, null=True)  # Field name made lowercase.
    �߲���d2_field = models.FloatField(db_column='�߲���D2��', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �߲���d3 = models.FloatField(db_column='�߲���D3', blank=True, null=True)  # Field name made lowercase.
    �߲���a1 = models.FloatField(db_column='�߲���A1', blank=True, null=True)  # Field name made lowercase.
    �߲���a2 = models.FloatField(db_column='�߲���A2', blank=True, null=True)  # Field name made lowercase.
    c1 = models.TextField(blank=True, null=True)
    c2 = models.TextField(blank=True, null=True)
    ת���¶� = models.TextField(blank=True, null=True)
    mfr�¶� = models.TextField(db_column='MFR�¶�', blank=True, null=True)  # Field name made lowercase.
    mfr���� = models.TextField(db_column='MFR����', blank=True, null=True)  # Field name made lowercase.
    ������mfr = models.TextField(db_column='������MFR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test'
